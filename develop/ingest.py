"""문서(PDF · TXT · DOCX · MD · IPYNB)를 출제용 마크다운 한 개로 바꿉니다.

파이프라인 ① 수집 단계. 결과 md를 출제 프롬프트(prompts/출제_프롬프트.md)에 넣습니다.

사용법:  python develop/ingest.py <문서> [-o 출력.md]
         (기본 출력: develop/sources/<문서이름>.md)

- PDF  : 페이지별 텍스트 추출 (`## p.N` 머리말). pymupdf → pypdf → pdftotext 중 있는 것 사용.
         글자가 거의 없으면 스캔본 경고(OCR은 이후 단계)
- DOCX : word/document.xml을 직접 읽음. 제목 스타일(Heading/제목) → #, 목록 → -, 표 → 마크다운 표
- TXT  : utf-8 → cp949 순으로 해석
- MD   : 그대로 복사
- IPYNB: 마크다운 셀은 그대로, 코드 셀은 ```python 블록
"""
import argparse
import json
import os
import re
import subprocess
import sys
import zipfile
import xml.etree.ElementTree as ET

HERE = os.path.dirname(os.path.abspath(__file__))
W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


def read_text_file(path):
    raw = open(path, "rb").read()
    for enc in ("utf-8-sig", "cp949"):
        try:
            return raw.decode(enc)
        except UnicodeDecodeError:
            continue
    return raw.decode("utf-8", "replace")


def _pdf_pages(path):
    """페이지별 텍스트. pymupdf → pypdf → pdftotext 순으로 있는 것을 씁니다."""
    try:
        import pymupdf
        return [p.get_text() for p in pymupdf.open(path)]
    except ImportError:
        pass
    try:
        from pypdf import PdfReader
        return [p.extract_text() or "" for p in PdfReader(path).pages]
    except ImportError:
        pass
    try:
        out = subprocess.run(["pdftotext", "-layout", path, "-"], capture_output=True, text=True, encoding="utf-8").stdout
        return out.split("\f")
    except FileNotFoundError:
        sys.exit("PDF 추출 도구가 없습니다:  pip install -r tools/requirements.txt")


def from_pdf(path):
    pages = _pdf_pages(path)
    parts, chars = [], 0
    for i, t in enumerate(pages, 1):
        t = t.strip()
        chars += len(t)
        if t:
            parts.append(f"## p.{i}\n\n{t}")
    if pages and chars / len(pages) < 30:
        print(f"⚠ 페이지당 평균 {chars // len(pages)}자 — 스캔 PDF일 수 있습니다(OCR 필요).", file=sys.stderr)
    return "\n\n".join(parts)


def _para_text(p):
    return "".join(t.text or "" for t in p.iter(W + "t"))


def _para_style(p):
    s = p.find(f"{W}pPr/{W}pStyle")
    return (s.get(W + "val") or "") if s is not None else ""


def from_docx(path):
    with zipfile.ZipFile(path) as z:
        root = ET.fromstring(z.read("word/document.xml"))
    body = root.find(W + "body")
    out = []
    for el in body:
        if el.tag == W + "p":
            text = _para_text(el).strip()
            if not text:
                continue
            style = _para_style(el).lower()
            m = re.search(r"(heading|제목)\s*(\d)", style)
            if m:
                out.append("#" * min(int(m.group(2)), 6) + " " + text)
            elif style == "title":
                out.append("# " + text)
            elif el.find(f"{W}pPr/{W}numPr") is not None or "list" in style:
                out.append("- " + text)
            else:
                out.append(text)
        elif el.tag == W + "tbl":
            rows = []
            for tr in el.iter(W + "tr"):
                cells = [" ".join(_para_text(p).strip() for p in tc.iter(W + "p")).replace("|", "\\|")
                         for tc in tr.iter(W + "tc")]
                rows.append("| " + " | ".join(cells) + " |")
            if rows:
                ncol = rows[0].count("|") - 1
                rows.insert(1, "|" + "---|" * ncol)
                out.append("\n".join(rows))
    return "\n\n".join(out)


def from_ipynb(path):
    nb = json.loads(read_text_file(path))
    out = []
    for cell in nb.get("cells", []):
        src = "".join(cell.get("source", []))
        if not src.strip():
            continue
        out.append(src if cell.get("cell_type") == "markdown" else f"```python\n{src}\n```")
    return "\n\n".join(out)


def ingest(path):
    ext = os.path.splitext(path)[1].lower()
    if ext == ".pdf":
        body = from_pdf(path)
    elif ext == ".docx":
        body = from_docx(path)
    elif ext == ".ipynb":
        body = from_ipynb(path)
    elif ext in (".txt", ".md", ".markdown"):
        body = read_text_file(path)
    else:
        sys.exit(f"지원하지 않는 형식: {ext} (pdf, docx, txt, md, ipynb)")
    body = re.sub(r"\n{3,}", "\n\n", body).strip()
    head = f"<!-- source: {os.path.basename(path)} · ingest.py -->\n\n"
    return head + body + "\n"


def main():
    ap = argparse.ArgumentParser(description="문서 → 출제용 마크다운")
    ap.add_argument("src")
    ap.add_argument("-o", "--out")
    args = ap.parse_args()
    text = ingest(args.src)
    out = args.out or os.path.join(HERE, "sources", os.path.splitext(os.path.basename(args.src))[0] + ".md")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"✓ {out}  ({len(text):,}자, 줄 {text.count(chr(10)):,})")


if __name__ == "__main__":
    main()
