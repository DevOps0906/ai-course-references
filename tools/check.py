"""레포 전체에 원본 표기·보안 정보가 남아 있는지 검사합니다. 남아 있으면 종료 코드 1.

사용법:  python3 tools/check.py [폴더]   (기본: 레포 루트, tools/ 폴더는 제외)
"""
import os
import re
import subprocess
import sys
import zipfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from rules import FORBIDDEN  # noqa: E402

ROOT = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP_DIRS = {".git", "tools", ".cache"}
TAG = re.compile(r"<[^>]+>")


def texts(path):
    ext = path.rsplit(".", 1)[-1].lower()
    if ext in ("pptx", "docx", "xlsx"):
        z = zipfile.ZipFile(path)
        for n in z.namelist():
            if n.endswith((".xml", ".rels")):
                raw = z.read(n).decode("utf-8", "ignore")
                yield n, raw
                yield n + "(본문)", TAG.sub("", raw)
    elif ext == "pdf":
        try:
            import pymupdf
            doc = pymupdf.open(path)
            for i, page in enumerate(doc, 1):
                yield f"p{i}", page.get_text()
                for l in page.get_links():
                    yield f"p{i}-link", l.get("uri") or ""
            yield "meta", str(doc.metadata)
        except ImportError:
            yield "pdf", subprocess.run(["pdftotext", path, "-"], capture_output=True, text=True).stdout
    elif ext in ("png", "jpg", "jpeg", "gif", "mp4", "m4a", "mp3", "wav", "zip"):
        return
    else:
        raw = open(path, "rb").read()
        for enc in ("utf-8", "cp949"):
            try:
                yield "", raw.decode(enc)
                break
            except UnicodeDecodeError:
                continue


bad = 0
for d, dirs, files in os.walk(ROOT):
    dirs[:] = [x for x in dirs if x not in SKIP_DIRS]
    for f in files:
        p = os.path.join(d, f)
        for part, t in texts(p):
            for m in FORBIDDEN.finditer(t):
                bad += 1
                s = t[max(0, m.start() - 30): m.end() + 30].replace("\n", " ")
                print(f"✗ {os.path.relpath(p, ROOT)} {part}: …{s}…")
print("✓ 남은 표기 없음" if not bad else f"남은 표기 {bad}건")
sys.exit(1 if bad else 0)
