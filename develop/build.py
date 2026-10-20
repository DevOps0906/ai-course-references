"""엔진 + 디자인 토큰 + 문제은행 JSON → 단독 실행 HTML, 그리고 사이트 페이지(랜딩·로그인·대시보드).

사용법:  python develop/build.py [bank.json ...]   (기본: develop/banks 아래 전부)
결과:    develop/dist/<banks 기준 같은 경로>.html  (file://로 더블클릭해도 열림)
         develop/dist/index.html                   (랜딩)
         develop/dist/login.html                   (mock 로그인)
         develop/dist/dashboard.html               (대시보드: 항상 banks 전체 기준으로 다시 생성)

빌드 전에 validate.py를 돌려 오류가 있으면 그 은행은 건너뜁니다.
"""
import datetime
import glob
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ENGINE = os.path.join(HERE, "engine", "quiz.html")
LANDING_TPL = os.path.join(HERE, "engine", "landing.html")
LOGIN_TPL = os.path.join(HERE, "engine", "login.html")
DASH_TPL = os.path.join(HERE, "engine", "dashboard.html")
DESIGN = os.path.join(ROOT, "design")
TOKENS = os.path.join(DESIGN, "tokens.css")
COMPONENTS = os.path.join(DESIGN, "components.css")
ICONS = os.path.join(DESIGN, "icons.svg")
CORE_JS = os.path.join(DESIGN, "qb-core.js")
VOICE_JS = os.path.join(DESIGN, "qb-voice.js")
PROGRESS_JS = os.path.join(DESIGN, "qb-progress.js")
LANDING_JSON = os.path.join(HERE, "landing", "landing.json")
CLAIMS_MD = os.path.join(HERE, "landing", "claims.md")
BANKS = os.path.join(HERE, "banks")
DIST = os.path.join(HERE, "dist")
INDEX_OUT = os.path.join(DIST, "index.html")   # 랜딩
LOGIN_OUT = os.path.join(DIST, "login.html")
DASH_OUT = os.path.join(DIST, "dashboard.html")

SUBJECTS = [("it", "IT"), ("korean", "국어"), ("english", "영어"), ("science", "과학"), ("music", "음악"), ("art", "미술")]
LEFTOVER = re.compile(r"Quizlet|Duolingo|LeetCode|프로그래머스", re.I)   # 벤치마킹 대상 이름은 결과물에 남기지 않는다

# 허브에 보이는 단계·과정 (레포 폴더 구조와 같은 순서). 은행이 없는 과정은 '준비 중'으로 표시
STAGES = [
    ("01", "AI 업무 활용", "01-ai-work", [
        ("ai-automation", "생성형 AI + 노코드 업무 자동화"),
        ("ai-excel", "AI 엑셀 실무"),
        ("claude-for-educators", "Claude 활용 교육"),
    ]),
    ("02", "개발 기초", "02-dev-basics", [
        ("git", "Git · GitHub 입문"),
        ("vibe-coding", "비개발자 바이브코딩"),
    ]),
    ("03", "n8n 자동화", "03-n8n-automation", [
        ("n8n-edu-agent", "n8n + AI 교육 업무 자동화"),
        ("n8n-blog", "n8n 블로그 자동 발행"),
    ]),
    ("04", "음성 AI", "04-voice-ai", [
        ("", "음성 AI 전문가 과정 Day 1~8"),
    ]),
    ("05", "LangChain · RAG · Agent", "05-langchain-agent", [
        ("", "LangChain LCEL → RAG → Gradio → 음성 RAG → LangGraph (14일)"),
    ]),
    ("06", "인텔 Physical AI · AI 비전 · OpenVINO", "06-ai-openVino", [
        ("", "리눅스 → 파이썬 → OpenCV → OpenVINO 엣지 AI"),
    ]),
    ("07", "Physical AI · 자율주행", "07-physical-ai", [   # 원본 폴더: source/07-NEPES_physicalAI_자율주행자동차
        ("", "Jetson → LLM·VLM → OpenCV·ROS → Pseudo-VLA → VLA (5일)"),
    ]),
    ("08", "임베디드 · 시스템 SW", "08-embedded-sw", [   # 원본 폴더: source/08-AI_CAMPUS-main
        ("", "Python → C → 컴퓨터 구조 → 운영체제 → 리눅스 → ESP32 MCU → 라즈베리파이 입출력"),
    ]),
    ("09", "Android 프레임워크", "09-android-framework", [   # 원본 폴더: source/09-android_framework-main
        ("", "AOSP · Binder → Native 서비스·HAL → sp/Looper/JNI → SystemUI·Automotive (4일)"),
    ]),
    ("10", "Go 언어 프로그래밍", "10-go-programming", [   # 원본 폴더: source/10-go_programming-main
        ("", "Go 기초 → 모듈·CLI → 동시성 → 테스트·도구 → 웹 서버 (5일)"),
    ]),
]
STAGE_NUM = {folder: num for num, _, folder, _ in STAGES}
STAGE_SUBJECT = {}   # 과정 번호 → 과목 (없으면 "it"). 다른 과목 과정을 추가할 때 여기에 넣는다

# 허브 첫 화면 박스에 보이는 대표 키워드 (과정마다 4~6개)
STAGE_KEYWORDS = {
    "01": ["생성형 AI", "프롬프트", "업무 자동화", "엑셀 실무", "Claude 교육 활용"],
    "02": ["Git", "GitHub 협업", "바이브코딩", "프롬프트 기법", "웹 앱 프로토타입"],
    "03": ["n8n", "워크플로우", "Google Sheets·Gmail", "Webhook", "AI 노드", "블로그 자동 발행"],
    "04": ["ASR·TTS", "STFT·MFCC", "잡음 제거·VAD", "CTC·Wav2Vec2", "Whisper"],
    "05": ["LangChain LCEL", "RAG", "Gradio", "음성 RAG", "LangGraph"],
    "06": ["리눅스", "파이썬", "OpenCV", "OpenVINO", "CPU·GPU·NPU 비교"],
    "07": ["Jetson", "LLM·VLM", "OpenCV·MediaPipe", "ROS 2", "VLA"],
    "08": ["Python", "C 언어", "컴퓨터 구조", "운영체제", "리눅스 시스템", "ESP32·GPIO"],
    "09": ["AOSP 빌드", "Binder·AIDL", "Native 서비스·HAL", "Looper·JNI", "SystemUI·Automotive"],
    "10": ["Go 기초", "모듈·Cobra CLI", "고루틴·채널", "Context·Worker Pool", "웹 서버·테스트"],
}

sys.path.insert(0, HERE)
from validate import validate  # noqa: E402


def esc_title(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def js_data(obj):
    # </script> 조기 종료 방지
    return json.dumps(obj, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")


def out_path(bank_path):
    rel = os.path.relpath(bank_path, BANKS)
    return os.path.join(DIST, os.path.splitext(rel)[0] + ".html")


def read_opt(path):
    """디자인 산출물이 아직 없어도 빌드가 죽지 않게 한다."""
    if not os.path.exists(path):
        print(f"! {os.path.relpath(path, ROOT)} 없음 — 빈 값으로 빌드합니다.")
        return ""
    return open(path, encoding="utf-8").read()


def common_pairs():
    return (
        ("/*__TOKENS__*/", read_opt(TOKENS)),
        ("/*__COMPONENTS__*/", read_opt(COMPONENTS)),
        ("<!--__ICONS__-->", read_opt(ICONS)),
        ("/*__CORE__*/", read_opt(CORE_JS)),
    )


def fill(html, pairs, name):
    for key, val in pairs:
        if key not in html:
            sys.exit(f"{name}에 자리표시자 {key}가 없습니다.")
        html = html.replace(key, val)
    return html


def build(bank_path):
    errors, _, _ = validate(bank_path)
    if errors:
        print(f"✗ {os.path.relpath(bank_path, ROOT)} — 검증 오류 {len(errors)}건, validate.py로 확인하세요.")
        return False
    bank = json.load(open(bank_path, encoding="utf-8"))
    out = out_path(bank_path)
    hub_rel = os.path.relpath(DASH_OUT, os.path.dirname(out)).replace(os.sep, "/")
    stage = os.path.relpath(bank_path, BANKS).replace(os.sep, "/").split("/")[0]
    hub_stage = f"{hub_rel}#{STAGE_NUM.get(stage, stage[:2])}"   # 문제은행 → 허브의 그 과정 페이지
    html = fill(open(ENGINE, encoding="utf-8").read(), (
        ("/*__TOKENS__*/", read_opt(TOKENS)),
        ("/*__CORE__*/", read_opt(CORE_JS)),
        ("/*__VOICE__*/", read_opt(VOICE_JS)),
        ("/*__BANK__*/null", js_data(bank)),
        ("__TITLE__", esc_title(bank["title"])),
        ("__HUBSTAGE__", hub_stage),
        ("__HUB__", hub_rel),
    ), "엔진")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write(html)
    print(f"✓ {os.path.relpath(out, ROOT)}  ({len(html) // 1024} KB)")
    return True


def collect_catalog():
    """dist에 실제로 빌드된 은행만 모아 카탈로그(단계·과목·합계)를 만든다."""
    found = {}
    for p in sorted(glob.glob(os.path.join(BANKS, "**", "*.json"), recursive=True)):
        if not os.path.exists(out_path(p)) or validate(p)[0]:
            continue
        bank = json.load(open(p, encoding="utf-8"))
        parts = os.path.relpath(p, BANKS).replace(os.sep, "/").split("/")
        stage, course = parts[0], (parts[1] if len(parts) > 2 else "")
        found.setdefault((stage, course), []).append({
            "id": bank["id"], "code": bank.get("code", ""), "title": bank["title"], "subtitle": bank.get("subtitle", ""),
            "subject": bank.get("subject", "it"),
            "href": os.path.relpath(out_path(p), DIST).replace(os.sep, "/"),
            "tabs": len(bank["tabs"]), "qs": sum(len(t["qs"]) for t in bank["tabs"]),
        })
    stages = []
    for num, title, folder, courses in STAGES:
        stages.append({"num": num, "title": title, "subject": STAGE_SUBJECT.get(num, "it"),
                       "keys": STAGE_KEYWORDS.get(num, []), "courses": [
            {"title": ctitle, "banks": found.pop((folder, cfolder), [])} for cfolder, ctitle in courses]})
    for (stage, course), banks in found.items():  # STAGES에 없는 새 폴더도 빠뜨리지 않음
        stages.append({"num": stage[:2], "title": stage, "subject": "it", "courses": [{"title": course or stage, "banks": banks}]})
    all_banks = [b for s in stages for c in s["courses"] for b in c["banks"]]
    have = {b["subject"] for b in all_banks}
    subjects = [{"id": i, "label": l, "ready": i in have} for i, l in SUBJECTS]
    totals = {"stages": sum(1 for s in stages if any(c["banks"] for c in s["courses"])), "banks": len(all_banks),
              "tabs": sum(b["tabs"] for b in all_banks), "qs": sum(b["qs"] for b in all_banks)}
    return {"stages": stages, "subjects": subjects, "totals": totals, "built": datetime.date.today().isoformat()}


def sample_demo(cat):
    """랜딩 데모 문항: 단계마다 1개, 항상 같은 문항(은행 경로 정렬 순서). game · mc/ox · lv<=2 · 짧은 문제 · 그림 없음."""
    demo = []
    for st in cat["stages"]:
        pick = None
        for href in sorted(b["href"] for c in st["courses"] for b in c["banks"]):
            bank = json.load(open(os.path.join(BANKS, os.path.splitext(href)[0] + ".json"), encoding="utf-8"))
            for t in bank["tabs"]:
                for q in t["qs"]:
                    if (q.get("game") and q.get("ty") in ("mc", "ox") and (q.get("lv") or 9) <= 2
                            and len(re.sub(r"<[^>]+>", "", q["p"])) <= 90 and not q.get("img")):
                        pick = {k: q[k] for k in ("p", "o", "a", "h", "ty") if k in q}
                        pick.update({"bank": bank["title"], "stage": st["num"], "href": href})
                        break
                if pick:
                    break
            if pick:
                break
        if pick:
            demo.append(pick)
    return demo


def lint_landing(data):
    """landing.json 규칙 검사(계획 §8). 오류 목록을 돌려준다. 표가 아직 없으면 경고 후 비교표 검사만 건너뜀."""
    errs = []
    claims = {}
    if os.path.exists(CLAIMS_MD):
        for line in open(CLAIMS_MD, encoding="utf-8"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) >= 4 and re.fullmatch(r"[A-Za-z]+-?\d+", cells[0]):
                claims[cells[0]] = cells[-1]

    def walk(o, path=""):
        if isinstance(o, dict):
            for k, v in o.items():
                if k in ("claim", "claims"):
                    for cid in ([v] if isinstance(v, str) else v if isinstance(v, list) else []):
                        if claims.get(cid) != "검증":
                            errs.append(f"{path}/{k}: 주장 {cid!r}이 claims.md에서 '검증'이 아님")
                else:
                    walk(v, f"{path}/{k}")
        elif isinstance(o, list):
            for i, v in enumerate(o):
                walk(v, f"{path}[{i}]")
        elif isinstance(o, str) and re.search(r"→\s*$", o):
            errs.append(f"{path}: 문구 끝에 '→' 금지: {o!r}")
    walk(data)
    table = data.get("table")
    if not table:
        print("! landing.json에 table이 아직 없어 비교표 검사를 건너뜁니다.")
        return errs
    ours = table.get("ours")
    marks = [(r.get("cells") or {}).get(ours) for r in table.get("rows", [])]
    marks = [m.get("v") if isinstance(m, dict) else m for m in marks]
    if not any(m in ("△", "✕") for m in marks):
        errs.append("table: 우리 칸에 △·✕가 하나도 없음 (솔직하게 표시)")
    return errs


def write_page(path, html, label):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(html)
    print(f"✓ {os.path.relpath(path, ROOT)}  ({len(html) // 1024} KB)  {label}")


def lint_responsive():
    """반응형 표준 검사: @media 폭은 767/768/1023/1024만, 글자 크기는 --text-* 단계(직접 px 금지).
    기준은 design/tokens.css 머리말 참고(모바일 ≤767 · 태블릿 768~1023 · 데스크탑 ≥1024)."""
    allowed = {"767", "768", "1023", "1024"}
    errs = []
    for p in (TOKENS, COMPONENTS, ENGINE, LANDING_TPL, LOGIN_TPL, DASH_TPL):
        text = open(p, encoding="utf-8").read()
        name = os.path.relpath(p, ROOT)
        for m in re.finditer(r"@media[^{]*", text):
            for w in re.findall(r"(?:min|max)-width:\s*(\d+)px", m.group(0)):
                if w not in allowed:
                    errs.append(f"{name}: @media 폭 {w}px (허용: 767/768/1023/1024) → {m.group(0).strip()}")
        for m in re.finditer(r"font-size:\s*[\d.]+px|font:[^;}\"]*?\b[\d.]+px", text):
            errs.append(f"{name}: 글자 크기를 px로 직접 지정 → {m.group(0)} (var(--text-*) 사용)")
    for e in errs:
        print(f"✗ responsive: {e}")
    return not errs


def build_site(cat):
    """랜딩·로그인·대시보드 생성. 린트·잔여 이름 검사 오류가 있으면 False."""
    landing = json.load(open(LANDING_JSON, encoding="utf-8"))
    errs = lint_landing(landing)
    for e in errs:
        print(f"✗ landing: {e}")
    if not lint_responsive():
        errs.append("responsive")
    title = "디지털노마드연구소 · 문제은행"
    demo = sample_demo(cat)
    write_page(INDEX_OUT, fill(open(LANDING_TPL, encoding="utf-8").read(), common_pairs() + (
        ("/*__VOICE__*/", read_opt(VOICE_JS)),
        ("/*__CATALOG__*/null", js_data(cat)),
        ("/*__DEMO__*/null", js_data(demo)),
        ("/*__LANDING__*/null", js_data(landing)),
        ("__TITLE__", esc_title(title)),
    ), "랜딩"), f"랜딩 · 데모 {len(demo)}문항")
    write_page(LOGIN_OUT, fill(open(LOGIN_TPL, encoding="utf-8").read(), common_pairs() + (
        ("__TITLE__", esc_title(title)),
    ), "로그인"), "로그인")
    write_page(DASH_OUT, fill(open(DASH_TPL, encoding="utf-8").read(), common_pairs() + (
        ("/*__PROGRESS__*/", read_opt(PROGRESS_JS)),
        ("/*__CATALOG__*/null", js_data(cat)),
    ), "대시보드"), f"대시보드 · 문제은행 {cat['totals']['banks']}개")
    for p in (INDEX_OUT, LOGIN_OUT, DASH_OUT):
        m = LEFTOVER.search(open(p, encoding="utf-8").read())
        if m:
            print(f"✗ {os.path.relpath(p, ROOT)}: 벤치마킹 대상 이름 {m.group(0)!r} 남아 있음")
            errs.append(m.group(0))
    return not errs


def main():
    paths = sys.argv[1:] or sorted(glob.glob(os.path.join(BANKS, "**", "*.json"), recursive=True))
    ok = all([build(p) for p in paths])
    ok = build_site(collect_catalog()) and ok
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
