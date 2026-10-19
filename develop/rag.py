"""문항별 자료 근거 찾기(RAG) — 2단계 힌트(① 자세한 힌트 h ② 자료 발췌 src)를 만드는 도구.

사용법:
  python develop/rag.py retrieve [bank.json ...]   문항마다 자료 대목 후보(top-k)를 찾아
                                                   develop/sources/_rag/<은행 경로>.json 에 저장 (기본: 전부)
  python develop/rag.py apply <bank.json> <결과.json>
                                                   [{"id","h","src"}...] 를 은행에 합친다.
                                                   src는 자료 원문에 그대로 있는 문장이어야 한다(검증).

- 자료 목록: develop/rag_sources.json (은행 경로 → 원본 파일 glob). 없으면 은행의 source 필드를 해석.
- 검색: 자료를 쪽(PDF)·제목(md/ipynb/html)·파일(소스코드) 단위로 자르고, 단어+한글 2글자 BM25.
  질의 = 문제 + 정답 + 해설 + 자료 위치(an). an에 적힌 쪽 번호·파일 이름과 맞는 조각은 가산점.
- 원문 추출 캐시: develop/sources/_cache (레포에 올리지 않음)
"""
import glob
import hashlib
import html as htmllib
import json
import math
import os
import re
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SRC_ROOT = os.path.join(ROOT, "source")  # 원본 과정 폴더 10개가 있는 곳 — 자료 glob·bank.source는 이 기준
BANKS = os.path.join(HERE, "banks")
CACHE = os.path.join(HERE, "sources", "_cache")
OUT = os.path.join(HERE, "sources", "_rag")
MAP = os.path.join(HERE, "rag_sources.json")
CHUNK = 900          # 조각 최대 글자 수
TOPK = 3
CODE_EXT = {".c", ".h", ".go", ".sh", ".py", ".kt", ".java", ".cpp", ".aidl", ".rc", ".bp", ".mk"}

sys.path.insert(0, HERE)
import ingest  # noqa: E402


# ---------- 자료 → 조각 ----------
def _cached_text(path, fn):
    st = os.stat(path)
    key = hashlib.md5(f"{os.path.abspath(path)}|{st.st_size}|{st.st_mtime}".encode()).hexdigest()
    cp = os.path.join(CACHE, key + ".json")
    if os.path.exists(cp):
        return json.load(open(cp, encoding="utf-8"))
    data = fn(path)
    os.makedirs(CACHE, exist_ok=True)
    json.dump(data, open(cp, "w", encoding="utf-8"), ensure_ascii=False)
    return data


def _split_long(label, text):
    text = re.sub(r"[ \t]+", " ", text).strip()
    if len(text) <= CHUNK:
        return [(label, text)] if text else []
    out, buf = [], ""
    for para in re.split(r"\n\s*\n|\n(?=[-*#•▶■□○●①-⑳0-9])", text):
        if buf and len(buf) + len(para) > CHUNK:
            out.append((label, buf.strip()))
            buf = ""
        while len(para) > CHUNK:
            out.append((label, para[:CHUNK].strip()))
            para = para[CHUNK - 150:]  # 150자 겹침
        buf += para + "\n"
    if buf.strip():
        out.append((label, buf.strip()))
    return out


def _by_headings(text):
    """마크다운 제목(#)마다 나눈다. 라벨은 가장 가까운 제목."""
    parts, label, buf = [], "", []
    for line in text.splitlines():
        m = re.match(r"^#{1,4}\s+(.*)", line)
        if m and buf:
            parts.append((label, "\n".join(buf)))
            buf = []
        if m:
            label = m.group(1).strip()[:60]
        buf.append(line)
    if buf:
        parts.append((label, "\n".join(buf)))
    return parts


def _html_text(path):
    s = ingest.read_text_file(path)
    s = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", s)
    s = re.sub(r"(?i)<h([1-4])[^>]*>", lambda m: "\n" + "#" * int(m.group(1)) + " ", s)
    s = re.sub(r"(?i)<br\s*/?>|</(p|div|li|tr|h[1-6])>", "\n", s)
    s = htmllib.unescape(re.sub(r"<[^>]+>", " ", s))
    return re.sub(r"\n\s*\n+", "\n\n", s)


def load_chunks(path):
    name = os.path.basename(path)
    ext = os.path.splitext(name)[1].lower()
    if ext == ".pdf":
        pages = _cached_text(path, ingest._pdf_pages)
        return [c for i, t in enumerate(pages, 1) for c in _split_long(f"{name} p.{i}", t or "")]
    if ext == ".pptx":
        slides = _cached_text(path, ingest._pptx_slides)
        return [c for i, t in enumerate(slides, 1) for c in _split_long(f"{name} 슬라이드 {i}", t or "")]
    if ext == ".ipynb":
        text = _cached_text(path, ingest.from_ipynb)
    elif ext in (".html", ".htm"):
        text = _cached_text(path, _html_text)
    elif ext in (".md", ".txt"):
        text = ingest.read_text_file(path)
    elif ext == ".docx":
        text = _cached_text(path, ingest.from_docx)
    elif ext in CODE_EXT or name == "Makefile":
        return _split_long(name, ingest.read_text_file(path))
    else:
        return []
    return [c for lab, body in _by_headings(text) for c in _split_long(f"{name} · {lab}" if lab else name, body)]


def resolve_sources(bank_rel, bank):
    mp = json.load(open(MAP, encoding="utf-8")) if os.path.exists(MAP) else {}
    pats = mp.get(bank_rel)
    if pats is None:  # source 필드 해석: 'a/b/x.md + y.md' → a/b/x.md, a/b/y.md
        pats, base = [], ""
        for part in bank.get("source", "").split(" + "):
            part = re.sub(r"\s*\(.*?\)\s*$", "", part.strip())
            if "/" in part:
                base = os.path.dirname(part)
            elif base:
                part = base + "/" + part
            pats.append(part)
    files = []
    for p in pats:
        for f in sorted(glob.glob(os.path.join(SRC_ROOT, p), recursive=True)):
            if os.path.isfile(f) and f not in files:
                files.append(f)
    return files


# ---------- BM25 ----------
TOKEN = re.compile(r"[A-Za-z_][A-Za-z0-9_]*|\d+(?:\.\d+)?|[가-힣]+")


def tokens(s):
    s = re.sub(r"<[^>]+>", " ", s).lower()
    out = []
    for t in TOKEN.findall(s):
        if re.match(r"[가-힣]", t):
            out += [t[i:i + 2] for i in range(len(t) - 1)] or [t]
        else:
            out.append(t)
    return out


class BM25:
    def __init__(self, docs, k1=1.4, b=0.75):
        self.tf = [Counter(tokens(d)) for d in docs]
        self.len = [sum(c.values()) for c in self.tf]
        self.avg = sum(self.len) / max(1, len(self.len))
        df = Counter(t for c in self.tf for t in c)
        n = len(docs)
        self.idf = {t: math.log(1 + (n - v + .5) / (v + .5)) for t, v in df.items()}
        self.k1, self.b = k1, b

    def scores(self, q):
        qt = Counter(tokens(q))
        out = []
        for c, L in zip(self.tf, self.len):
            s = 0.0
            for t, w in qt.items():
                f = c.get(t)
                if f:
                    s += self.idf[t] * f * (self.k1 + 1) / (f + self.k1 * (1 - self.b + self.b * L / self.avg)) * min(w, 3)
            out.append(s)
        return out


def answer_text(q):
    ty, a = q["ty"], q.get("a")
    if ty == "mc":
        return q["o"][a]
    if ty == "multi":
        return " ".join(q["o"][i] for i in a)
    if ty == "match":
        return " ".join(" ".join(p) for p in q["pairs"])
    if ty == "order":
        return " ".join(q["steps"])
    return str(a)


def retrieve(bank_path):
    bank = json.load(open(bank_path, encoding="utf-8"))
    rel = os.path.relpath(bank_path, BANKS).replace(os.sep, "/")
    files = resolve_sources(rel, bank)
    chunks = [c for f in files for c in load_chunks(f)]
    if not chunks:
        print(f"✗ {rel}: 자료를 찾지 못함 — develop/rag_sources.json에 경로를 추가하세요")
        return False
    bm = BM25([lab + "\n" + txt for lab, txt in chunks])
    items = []
    for t in bank["tabs"]:
        for q in t["qs"]:
            an = q.get("an", "")
            sc = bm.scores(" ".join([q["p"], answer_text(q), answer_text(q), q.get("w", ""), an]))
            pages = set(re.findall(r"p\.?\s?(\d+)", an))
            names = [n.lower() for n in re.findall(r"[A-Za-z0-9_\-]{4,}", an)]
            for i, (lab, _) in enumerate(chunks):
                m = re.search(r" p\.(\d+)$", lab)
                if m and m.group(1) in pages:
                    sc[i] *= 1.6
                if any(n in lab.lower() for n in names):
                    sc[i] *= 1.3
            top = sorted(range(len(chunks)), key=lambda i: -sc[i])[:TOPK]
            items.append({"id": q["id"], "ty": q["ty"], "p": q["p"], "answer": answer_text(q), "an": an,
                          "h_old": q.get("h", ""),
                          "ctx": [{"k": k, "loc": chunks[i][0], "text": chunks[i][1]} for k, i in enumerate(top)]})
    out = os.path.join(OUT, os.path.splitext(rel)[0] + ".json")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    json.dump({"bank": rel, "id": bank["id"], "files": [os.path.relpath(f, SRC_ROOT).replace(os.sep, "/") for f in files],
               "items": items}, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"✓ {rel}: 자료 {len(files)}개 · 조각 {len(chunks)}개 · 문항 {len(items)}개 → {os.path.relpath(out, ROOT)}")
    return True


# ---------- 결과 합치기 ----------
def norm(s):
    # 태그 이름 꼴만 지운다: 코드의 `a < b ... >`·`<<`가 긴 원문 구간을 통째로 삼키지 않도록
    return re.sub(r"\s+", "", htmllib.unescape(re.sub(r"</?[A-Za-z!][^<>\n]*>", "", s)))


def apply(bank_path, result_path):
    bank = json.load(open(bank_path, encoding="utf-8"))
    rel = os.path.relpath(bank_path, BANKS).replace(os.sep, "/")
    raw = "".join(t for f in resolve_sources(rel, bank) for _, t in load_chunks(f))
    corpus = norm(raw)
    # 원문(코드·PDF)에 있는 '<'·'>'를 태그로 보고 지우면 사이 본문이 통째로 사라지므로, 공백만 지운 원문과도 비교한다
    corpus_ws = re.sub(r"\s+", "", htmllib.unescape(raw))
    res = {r["id"]: r for r in json.load(open(result_path, encoding="utf-8"))}
    n_h = n_src = 0
    bad = []
    for t in bank["tabs"]:
        for q in t["qs"]:
            r = res.get(q["id"])
            if not r:
                continue
            if r.get("h"):
                q["h"] = r["h"].strip()
                n_h += 1
            src = (r.get("src") or "").strip()
            if src:
                if norm(src) in corpus or re.sub(r"\s+", "", htmllib.unescape(src)) in corpus_ws:
                    q["src"] = src
                    n_src += 1
                else:
                    bad.append(q["id"])
                    q.pop("src", None)
    json.dump(bank, open(bank_path, "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=2)
    with open(bank_path, "a", encoding="utf-8", newline="\n") as f:
        f.write("\n")
    print(f"✓ {rel}: 힌트 {n_h}개 · 발췌 {n_src}개 반영" + (f" · 원문 불일치로 발췌 제외 {len(bad)}개 {bad[:8]}" if bad else ""))
    return not bad


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    if len(sys.argv) < 2 or sys.argv[1] not in ("retrieve", "apply"):
        sys.exit(__doc__)
    if sys.argv[1] == "apply":
        sys.exit(0 if apply(sys.argv[2], sys.argv[3]) else 1)
    paths = sys.argv[2:] or sorted(glob.glob(os.path.join(BANKS, "**", "*.json"), recursive=True))
    ok = all([retrieve(p) for p in paths])
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
