"""엔진 + 디자인 토큰 + 문제은행 JSON → 단독 실행 HTML, 그리고 전체 목록(허브) 페이지.

사용법:  python develop/build.py [bank.json ...]   (기본: develop/banks 아래 전부)
결과:    develop/dist/<banks 기준 같은 경로>.html  (file://로 더블클릭해도 열림)
         develop/dist/index.html                   (허브: 항상 banks 전체 기준으로 다시 생성)

빌드 전에 validate.py를 돌려 오류가 있으면 그 은행은 건너뜁니다.
"""
import datetime
import glob
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ENGINE = os.path.join(HERE, "engine", "quiz.html")
HUB_TPL = os.path.join(HERE, "engine", "hub.html")
TOKENS = os.path.join(ROOT, "design", "tokens.css")
BANKS = os.path.join(HERE, "banks")
DIST = os.path.join(HERE, "dist")
HUB_OUT = os.path.join(DIST, "index.html")

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
    ("07", "Physical AI · 자율주행", "07-physical-ai", [   # 원본 폴더: 07-NEPES_physicalAI_자율주행자동차
        ("", "Jetson → LLM·VLM → OpenCV·ROS → Pseudo-VLA → VLA (5일)"),
    ]),
    ("08", "임베디드 · 시스템 SW", "08-embedded-sw", [   # 원본 폴더: 08-AI_CAMPUS-main
        ("", "Python → C → 컴퓨터 구조 → 운영체제 → 리눅스 → ESP32 MCU → 라즈베리파이 입출력"),
    ]),
    ("09", "Android 프레임워크", "09-android-framework", [   # 원본 폴더: 09-android_framework-main
        ("", "AOSP · Binder → Native 서비스·HAL → sp/Looper/JNI → SystemUI·Automotive (4일)"),
    ]),
    ("10", "Go 언어 프로그래밍", "10-go-programming", [   # 원본 폴더: 10-go_programming-main
        ("", "Go 기초 → 모듈·CLI → 동시성 → 테스트·도구 → 웹 서버 (5일)"),
    ]),
]
STAGE_NUM = {folder: num for num, _, folder, _ in STAGES}

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
    hub_rel = os.path.relpath(HUB_OUT, os.path.dirname(out)).replace(os.sep, "/")
    stage = os.path.relpath(bank_path, BANKS).replace(os.sep, "/").split("/")[0]
    hub_stage = f"{hub_rel}#{STAGE_NUM.get(stage, stage[:2])}"   # 문제은행 → 허브의 그 과정 페이지
    html = fill(open(ENGINE, encoding="utf-8").read(), (
        ("/*__TOKENS__*/", open(TOKENS, encoding="utf-8").read()),
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


def build_hub():
    """dist에 실제로 빌드된 은행만 모아 허브를 만든다."""
    found = {}
    for p in sorted(glob.glob(os.path.join(BANKS, "**", "*.json"), recursive=True)):
        if not os.path.exists(out_path(p)) or validate(p)[0]:
            continue
        bank = json.load(open(p, encoding="utf-8"))
        parts = os.path.relpath(p, BANKS).replace(os.sep, "/").split("/")
        stage, course = parts[0], (parts[1] if len(parts) > 2 else "")
        found.setdefault((stage, course), []).append({
            "id": bank["id"], "code": bank.get("code", ""), "title": bank["title"], "subtitle": bank.get("subtitle", ""),
            "href": os.path.relpath(out_path(p), DIST).replace(os.sep, "/"),
            "tabs": len(bank["tabs"]), "qs": sum(len(t["qs"]) for t in bank["tabs"]),
        })
    stages = []
    for num, title, folder, courses in STAGES:
        stages.append({"num": num, "title": title, "keys": STAGE_KEYWORDS.get(num, []), "courses": [
            {"title": ctitle, "banks": found.pop((folder, cfolder), [])} for cfolder, ctitle in courses]})
    for (stage, course), banks in found.items():  # STAGES에 없는 새 폴더도 빠뜨리지 않음
        stages.append({"num": stage[:2], "title": stage, "courses": [{"title": course or stage, "banks": banks}]})
    cat = {"stages": stages, "built": datetime.date.today().isoformat()}
    html = fill(open(HUB_TPL, encoding="utf-8").read(), (
        ("/*__TOKENS__*/", open(TOKENS, encoding="utf-8").read()),
        ("/*__CATALOG__*/null", js_data(cat)),
    ), "허브")
    os.makedirs(DIST, exist_ok=True)
    with open(HUB_OUT, "w", encoding="utf-8", newline="\n") as f:
        f.write(html)
    n = sum(len(c["banks"]) for s in stages for c in s["courses"])
    print(f"✓ {os.path.relpath(HUB_OUT, ROOT)}  (문제은행 {n}개)")


def main():
    paths = sys.argv[1:] or sorted(glob.glob(os.path.join(BANKS, "**", "*.json"), recursive=True))
    ok = all([build(p) for p in paths])
    build_hub()
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
