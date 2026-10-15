"""정리 규칙 — 원본 자료를 이 레포용으로 바꿀 때 적용하는 치환 규칙 모음.

규칙을 고칠 때는 이 파일만 수정하면 clean.py / sync.py / check.py가 모두 같은 규칙을 씁니다.
"""
import json
import os
import posixpath
import re

HERE = os.path.dirname(os.path.abspath(__file__))
CONFIG = json.load(open(os.path.join(HERE, "sources.json"), encoding="utf-8"))
OWNER_REPO = CONFIG["owner_repo"]                      # 예: DevOps0906/ai-course-references
OWNER = OWNER_REPO.split("/")[0]
LINK_BASE = CONFIG.get("link_base", "").rstrip("/")   # 비워 두면 상대경로 링크
TARGETS = {s["name"]: s["target"] for s in CONFIG["sources"]}
BRAND = "디지털노마드연구소"
BRAND_EMAIL = "writer@nomadaifactory.com"

# 원본 저장소에 없는 별도 저장소 → 이 레포 안의 대체 파일
EXTRA_PAGES = {"stack_test": TARGETS["CLAUDE_AI"] + "/stack_visualizer.html"}

URL_RE = re.compile(
    r"(?P<scheme>https?://)?"
    r"(?P<host>imguru-mooc\.github\.io|github\.com/imguru-mooc|raw\.githubusercontent\.com/imguru-mooc)"
    r"/(?P<repo>[A-Za-z0-9_\-]+)(?P<rest>/[^\s)\"'<>\]\\|,`]*)?"
)


def _rel(from_file, repo_path):
    """repo 루트 기준 경로 repo_path를 from_file 위치에서 본 상대경로로."""
    path, _, frag = repo_path.partition("#")
    base = posixpath.dirname(from_file) or "."
    rel = posixpath.relpath(path, base)
    return rel + ("#" + frag if frag else "")


def _page_target(repo, rest):
    if repo in EXTRA_PAGES:
        return EXTRA_PAGES[repo]
    if repo not in TARGETS:
        return None
    rest = (rest or "").lstrip("/")
    return posixpath.join(TARGETS[repo], rest).rstrip("/")


def map_url(m, cur_file, display=False):
    scheme, host, repo, rest = m.group("scheme"), m.group("host"), m.group("repo"), m.group("rest") or ""
    if host.startswith("raw."):
        return "<YOUR_PUBLIC_FILE_URL>/" + posixpath.basename(rest)
    if host.endswith("github.io"):
        target = _page_target(repo, rest)
        if target is None:
            return f"{scheme or ''}{OWNER.lower()}.github.io/{repo}{rest}"
        if display or not scheme:            # 슬라이드·PDF에 보이는 글자 → 레포 경로로 표시
            return f"{LINK_BASE}/{target}" if LINK_BASE else target
        if LINK_BASE:
            return f"{LINK_BASE}/{target}"
        return _rel(cur_file, target) if cur_file else target
    # github.com 저장소 주소
    if repo in EXTRA_PAGES:
        return f"{scheme or ''}github.com/{OWNER_REPO}/blob/main/{EXTRA_PAGES[repo]}"
    if repo not in TARGETS:                  # 수업 중 만드는 예시 저장소 등
        return f"{scheme or ''}github.com/{OWNER}/{repo}{rest}"
    mm = re.match(r"/(tree|blob)/[^/]+/?(.*)", rest)
    kind, sub = (mm.group(1), mm.group(2)) if mm else ("tree", "")
    path = posixpath.join(TARGETS[repo], sub).rstrip("/")
    return f"{scheme or ''}github.com/{OWNER_REPO}/{kind}/main/{path}"


# (정규식, 치환) — 위에서부터 순서대로 적용
TEXT_RULES = [
    # 연락처·이름
    (r"jikim@imguru\.co\.kr", BRAND_EMAIL),
    (r"imguru\.co\.kr", BRAND),
    (r"(강사명\s*:\s*)김정인", r"\g<1>" + BRAND),
    (r"김정인", "홍길동"),
    (r"C:\\Users\\jikim", r"C:\\Users\\nomad"),
    (r"(?i)jungin\s?kim", BRAND),
    (r"AI Education Center", BRAND),
    # Whisper 고유명사 예문 (D7) — 오인식 예시까지 같은 단어로 맞춤.
    # 슬라이드 PDF 배치가 깨지지 않도록 원래 글자 수(4자 + 연구소)에 맞춘 '노마드랩'을 사용
    (r"아이구루</span> 교육센터", "노마드랩</span> 연구소"),
    (r"아이구루 교육센터", "노마드랩 연구소"),
    (r"아이 구로 교 유 센터", "노마 드랩 연 구 소"),
    (r"아이구로 교육 센터", "노마드렙 연구 소"),
    (r"아이 구로</span> 교육센터", "노마 드랩</span> 연구소"),
    (r"아이 구로", "노마 드랩"),
    (r"아이구로", "노마드렙"),
    (r"아이구루", "노마드랩"),
    # AI_Voice 슬라이드 하단 "온라인 자료  <주소>" → 레포 안 위치 표시로 바뀌므로 이름표도 맞춤
    (r"온라인 자료", "레포 위치"),
    # 남은 계정명
    (r"\bimguru-mooc/", OWNER + "/"),
    (r"imguru-mooc", OWNER),
    # 보안 정보 (토큰·도메인·문서 ID)
    (r"(ngrok config add-authtoken\s+)(?!<YOUR)[^\s`'\"<]+", r"\g<1><YOUR_NGROK_AUTHTOKEN>"),
    (r"[\w-]+\.ngrok-free\.app", "<YOUR-STATIC-DOMAIN>.ngrok-free.app"),
    (r"(docs\.google\.com/(?:spreadsheets|document|presentation)/d/)[\w-]{20,}", r"\g<1><YOUR_DOC_ID>"),
    (r"(drive\.google\.com/drive/folders/)[\w-]{20,}", r"\g<1><YOUR_DRIVE_FOLDER_ID>"),
    (r'("documentId"\s*:\s*\{[^{}]*?"value"\s*:\s*")[\w-]{20,}', r"\g<1><YOUR_SHEET_ID>"),
    (r'("folderId"\s*:\s*\{[^{}]*?"value"\s*:\s*")[\w-]{20,}', r"\g<1><YOUR_DRIVE_FOLDER_ID>"),
    # 노트북 실행 결과 등에 찍힌 실제 API 키
    (r"sk-(?:proj-|ant-api\d\d-)?(?![\w-]*[Xx]{8})[A-Za-z0-9_-]{32,}", "<YOUR_API_KEY>"),
    (r"\bhf_[A-Za-z0-9]{30,}", "<YOUR_HF_TOKEN>"),
    (r"\bAIza(?![\w-]*[Xx]{8})[0-9A-Za-z_-]{35}", "<YOUR_GOOGLE_API_KEY>"),
    (r"\b(?:lsv2_(?:pt|sk)_|tvly-|ghp_|github_pat_)[A-Za-z0-9_]{20,}", "<YOUR_TOKEN>"),
    # 안전망: 위 규칙에서 빠진 표기
    (r"(?i)imguru", BRAND),
]
TEXT_RULES = [(re.compile(p), r) for p, r in TEXT_RULES]

# 남아 있으면 안 되는 표기 (check.py가 사용)
FORBIDDEN = re.compile(
    r"(?i:imguru)|아이구루|아이 ?구로|김정인|\bjikim\b|(?i:jungin\s?kim)|ngrok config add-authtoken\s+(?!<)\S+"
    r"|docs\.google\.com/spreadsheets/d/(?!<)[\w-]{20,}"
    r"|sk-(?:proj-|ant-api\d\d-)?(?![\w-]*[Xx]{8})[A-Za-z0-9_-]{32,}|\bhf_[A-Za-z0-9]{30,}|\bAIza(?![\w-]*[Xx]{8})[0-9A-Za-z_-]{35}"
    r"|\b(?:lsv2_(?:pt|sk)_|tvly-|ghp_|github_pat_)[A-Za-z0-9_]{20,}"
)


def crosses(spans, text):
    """text 안의 규칙 대상이 spans(글자 조각 경계) 여러 개에 걸쳐 있는지."""
    bounds = set()
    pos = 0
    for s in spans[:-1]:
        pos += len(s)
        bounds.add(pos)
    for pat in [URL_RE] + [p for p, _ in TEXT_RULES]:
        for m in pat.finditer(text):
            if any(m.start() < b < m.end() for b in bounds):
                return True
    return False


def clean_text(text, cur_file=None, display=False):
    """문자열 하나를 정리. cur_file은 레포 루트 기준 경로(상대 링크 계산용),
    display=True는 화면에 보이는 글자(슬라이드 본문·PDF)용."""
    n = 0
    text, k = URL_RE.subn(lambda m: map_url(m, cur_file, display), text)
    n += k
    for pat, rep in TEXT_RULES:
        text, k = pat.subn(rep, text)
        n += k
    return text, n
