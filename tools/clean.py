"""폴더 안의 자료를 rules.py 규칙대로 정리합니다 (제자리 수정).

사용법:
    python3 tools/clean.py <폴더> --prefix <레포 루트 기준 폴더 경로>
    예) python3 tools/clean.py 04-voice-ai --prefix 04-voice-ai

지원 형식: md·txt·json·ipynb·html·py·csv(텍스트), pptx·docx·xlsx(내부 XML·문서 속성), pdf(본문 글자·링크)
PDF 처리에는 PyMuPDF가 필요합니다:  pip install pymupdf
"""
import argparse
import os
import posixpath
import re
import shutil
import sys
import tempfile
import zipfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from rules import BRAND, clean_text, crosses  # noqa: E402

TEXT_EXT = {"md", "txt", "json", "ipynb", "html", "htm", "py", "csv", "yml", "yaml", "js", "css", ""}
OFFICE_EXT = {"pptx", "docx", "xlsx"}
PLACEHOLDER = re.compile(r"<(YOUR[\w-]*)>")


def _read_text(path):
    raw = open(path, "rb").read()
    for enc in ("utf-8", "cp949"):
        try:
            return raw.decode(enc), enc
        except UnicodeDecodeError:
            pass
    return None, None


def clean_textfile(path, repo_path):
    text, enc = _read_text(path)
    if text is None:
        return 0
    new, n = clean_text(text, repo_path)
    if path.lower().endswith((".html", ".htm")):
        new = PLACEHOLDER.sub(r"&lt;\1&gt;", new)
    if n or enc != "utf-8":                       # CP949 파일은 UTF-8로 통일
        open(path, "w", encoding="utf-8", newline="").write(new)
    return n


PARA = re.compile(r"<(a|w):p[ >].*?</\1:p>", re.S)
RUN_T = re.compile(r"(<(?:a|w):t(?: [^>]*)?>)(.*?)(</(?:a|w):t>)", re.S)


def _clean_paragraph(m, repo_path, counter):
    """문단 안의 글자 조각들을 정리. URL·이름이 여러 조각에 나뉘어 있으면 첫 조각으로 합침."""
    para = m.group(0)
    runs = RUN_T.findall(para)
    if not runs:
        return para
    texts = [r[1] for r in runs]
    joined = "".join(texts)
    if crosses(texts, joined):
        new, k = clean_text(joined, repo_path, display=True)
        counter[0] += k
        it = iter([new] + [""] * (len(runs) - 1))
        return RUN_T.sub(lambda r: r.group(1) + next(it) + r.group(3), para)

    def one(r):
        new, k = clean_text(r.group(2), repo_path, display=True)
        counter[0] += k
        return r.group(1) + new + r.group(3)
    return RUN_T.sub(one, para)


def clean_office(path, repo_path):
    zin = zipfile.ZipFile(path)
    out, total = [], 0
    for info in zin.infolist():
        data = zin.read(info.filename)
        if info.filename.endswith((".xml", ".rels")):
            t = data.decode("utf-8")
            counter = [0]
            new = PARA.sub(lambda m: _clean_paragraph(m, repo_path, counter), t)   # 본문 글자
            new, n = clean_text(new, repo_path)                                       # 링크·속성
            n += counter[0]
            new = PLACEHOLDER.sub(r"&lt;\1&gt;", new)
            if info.filename in ("docProps/core.xml", "docProps/app.xml"):
                for tag in ("dc:creator", "cp:lastModifiedBy", "Company", "Manager"):
                    new, k = re.subn(rf"(<{tag}>)[^<]*(</{tag}>)", rf"\g<1>{BRAND}\g<2>", new)
                    n += k if k and t != new else 0
            if new != t:
                data = new.encode("utf-8")
                total += max(n, 1)
        out.append((info, data))
    zin.close()
    if total:
        fd, tmp = tempfile.mkstemp(suffix=".zip")
        os.close(fd)
        with zipfile.ZipFile(tmp, "w") as zout:
            for info, data in out:
                zout.writestr(info, data, compress_type=info.compress_type)
        shutil.move(tmp, path)
    return total


def _insert_mixed(page, font, latin, rect, origin, text, size, color):
    """한글은 CJK 글꼴, 영문·숫자는 Helvetica로 나눠 써서 원래 폭에 맞춤."""
    runs = re.findall(r"[\x20-\x7e]+|[^\x20-\x7e]+", text)
    def width(fs):
        return sum((latin if r.isascii() else font).text_length(r, fontsize=fs) for r in runs)
    fs = size
    while fs > 4 and width(fs) > rect.width * 1.1:
        fs -= 0.25
    x, y = origin
    for r in runs:
        ascii_run = r.isascii()
        page.insert_text((x, y), r, fontname="helv" if ascii_run else "korea", fontsize=fs, color=color)
        x += (latin if ascii_run else font).text_length(r, fontsize=fs)


def clean_pdf(path, repo_path):
    try:
        import pymupdf
    except ImportError:
        print(f"  ! PyMuPDF 없음 — PDF 건너뜀: {path}  (pip install pymupdf)")
        return 0
    doc = pymupdf.open(path)
    font, latin = pymupdf.Font("korea"), pymupdf.Font("helv")
    total = 0
    for page in doc:
        for link in page.get_links():
            uri = link.get("uri")
            if uri:
                new, k = clean_text(uri, repo_path)
                if k and new != uri:
                    link["uri"] = new
                    page.update_link(link)
                    total += 1
        todo = []
        for block in page.get_text("dict")["blocks"]:
            for line in block.get("lines", []):
                for s in line["spans"]:
                    new, k = clean_text(s["text"], repo_path, display=True)
                    if k and new != s["text"]:
                        todo.append((pymupdf.Rect(s["bbox"]), s["origin"], new, s["size"], s["color"]))
        if not todo:
            continue
        # 지우는 영역에 걸친 링크는 redaction 때 사라지므로 미리 보관했다가 다시 넣음
        keep = [l for l in page.get_links()
                if any(pymupdf.Rect(l["from"]).intersects(t[0]) for t in todo)]
        for rect, *_ in todo:
            page.add_redact_annot(rect, fill=False)
        page.apply_redactions(images=pymupdf.PDF_REDACT_IMAGE_NONE,
                              graphics=pymupdf.PDF_REDACT_LINE_ART_NONE)
        for rect, origin, new, size, color in todo:
            _insert_mixed(page, font, latin, rect, origin, new, size, pymupdf.sRGB_to_pdf(color))
            total += 1
        have = {(tuple(pymupdf.Rect(l["from"])), l.get("uri") or l.get("file")) for l in page.get_links()}
        for l in keep:
            if (tuple(pymupdf.Rect(l["from"])), l.get("uri") or l.get("file")) not in have:
                page.insert_link(l)
    meta = dict(doc.metadata or {})
    for k, v in meta.items():
        if isinstance(v, str) and v:
            nv, n = clean_text(v, repo_path, display=True)
            if n and nv != v:
                meta[k] = nv
                total += 1
    if total:
        doc.set_metadata({k: v for k, v in meta.items() if k in (
            "author", "producer", "creator", "title", "format", "encryption", "creationDate", "modDate",
            "subject", "keywords", "trapped")})
        fd, tmp = tempfile.mkstemp(suffix=".pdf")
        os.close(fd)
        doc.save(tmp, garbage=3, deflate=True)
        doc.close()
        shutil.move(tmp, path)
    else:
        doc.close()
    return total


def clean_file(path, repo_path):
    ext = path.rsplit(".", 1)[-1].lower() if "." in os.path.basename(path) else ""
    if ext in OFFICE_EXT:
        return clean_office(path, repo_path)
    if ext == "pdf":
        return clean_pdf(path, repo_path)
    if ext in TEXT_EXT:
        return clean_textfile(path, repo_path)
    return 0                                       # 이미지·오디오·비디오 등은 그대로


def clean_tree(folder, prefix):
    report = {}
    for d, _, files in os.walk(folder):
        if ".git" in d.split(os.sep):
            continue
        for f in sorted(files):
            p = os.path.join(d, f)
            rel = posixpath.join(prefix, os.path.relpath(p, folder).replace(os.sep, "/"))
            n = clean_file(p, rel)
            if n:
                report[rel] = n
    return report


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("folder")
    ap.add_argument("--prefix", required=True, help="레포 루트 기준 폴더 경로 (상대 링크 계산용)")
    a = ap.parse_args()
    rep = clean_tree(a.folder, a.prefix)
    for k, v in rep.items():
        print(f"  {v:4d}  {k}")
    print(f"정리된 파일 {len(rep)}개, 치환 {sum(rep.values())}건")
