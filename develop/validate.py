"""문제은행 JSON을 검사합니다. 문제가 있으면 종료 코드 1.

사용법:  python develop/validate.py [bank.json ...]   (기본: develop/banks 아래 전부)

검사 항목: 필수 필드 · 유형별 정답 형식/범위 · 탭당 10문항 · id 중복 · 금지어(tools/rules.py)
경고(통과는 함): 탭당 유형 비율 · mc 정답 위치 쏠림 · 게임 문항 길이
"""
import collections
import glob
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "tools"))
try:
    from rules import FORBIDDEN  # noqa: E402
except ImportError:
    FORBIDDEN = None

TYPES = {"mc", "multi", "ox", "match", "order", "num"}
GAME_TYPES = {"mc", "multi", "ox"}
SUBJECTS = {"it", "korean", "english", "science", "music", "art", "etc"}
PER_TAB = 10
TARGET_MIX = {"mc": 5, "ox": 2, "match": 1, "order": 1, "multi": 1}
TAG = re.compile(r"<[^>]+>")
BANK_FORBIDDEN = re.compile(r"올에이아이|ALL\.AI|(?i:nepes)|네패스|판교로 289")
HTML_TAG = re.compile(r"</?(?:code|b|i|em|strong|br|span|sub|sup|p|div|a)[^>]*>", re.I)  # <eos>·<명령어> 같은 글자는 허용


def check_q(q, where, err, warn):
    for k in ("id", "ty", "p", "w", "an"):
        if not q.get(k) and q.get(k) != 0:
            err(f"{where}: '{k}' 없음")
    ty = q.get("ty")
    if ty not in TYPES:
        err(f"{where}: 알 수 없는 유형 {ty!r}")
        return
    if not q.get("h"):
        warn(f"{where}: 힌트(h) 없음")
    elif len(TAG.sub("", q["h"])) < 40:
        warn(f"{where}: 힌트가 짧음 — 자료 내용을 담아 2~3문장으로")
    src = q.get("src")
    if src is not None:
        if not isinstance(src, str) or not src.strip():
            err(f"{where}: src는 자료 원문 발췌 문자열")
        elif HTML_TAG.search(src):
            err(f"{where}: src에 HTML 태그 — 원문 그대로의 일반 글자로")
        elif len(src) > 600:
            warn(f"{where}: src 발췌 {len(src)}자 (권장 400자 이내)")
    if q.get("lv") not in (1, 2, 3):
        warn(f"{where}: lv(1~3) 없음")
    img = q.get("img")
    if img is not None:
        if not isinstance(img, dict) or not str(img.get("src") or "").strip():
            err(f"{where}: img는 {{src, alt}} 객체 (src 필수)")
        elif not str(img.get("alt") or "").strip():
            err(f"{where}: img.alt 없음 — 그림을 말로 설명하는 대체 글자 필수")
        elif "caption" in img and not isinstance(img["caption"], str):
            err(f"{where}: img.caption은 문자열")
    audio = q.get("audio")
    if audio is not None:
        if not isinstance(audio, dict) or not str(audio.get("src") or "").strip():
            err(f"{where}: audio는 {{src, transcript}} 객체 (src 필수)")
        elif not str(audio.get("transcript") or "").strip():
            err(f"{where}: audio.transcript 없음 — 듣기 문항의 대본 필수")
    a = q.get("a")
    if ty in ("mc", "multi"):
        o = q.get("o") or []
        if len(o) < 2:
            err(f"{where}: 보기(o) 2개 미만")
        if len(set(o)) != len(o):
            err(f"{where}: 보기 중복")
        if ty == "mc":
            if not isinstance(a, int) or not 0 <= a < len(o):
                err(f"{where}: mc 정답 a={a!r} 범위 밖")
        else:
            if not isinstance(a, list) or not a or any(not isinstance(i, int) or not 0 <= i < len(o) for i in a):
                err(f"{where}: multi 정답 a={a!r} 형식/범위 오류")
            elif len(set(a)) != len(a):
                err(f"{where}: multi 정답 중복")
            elif len(a) == len(o):
                warn(f"{where}: multi 보기가 전부 정답")
    elif ty == "ox":
        if not isinstance(a, bool):
            err(f"{where}: ox 정답은 true/false")
    elif ty == "match":
        pairs = q.get("pairs") or []
        if len(pairs) < 2 or any(not isinstance(p, list) or len(p) != 2 for p in pairs):
            err(f"{where}: match pairs는 [[왼쪽, 오른쪽], ...] 2쌍 이상")
        elif len({p[1] for p in pairs}) != len(pairs) or len({p[0] for p in pairs}) != len(pairs):
            err(f"{where}: match 항목 중복")
    elif ty == "order":
        steps = q.get("steps") or []
        if len(steps) < 3:
            err(f"{where}: order steps 3개 미만")
        elif len(set(steps)) != len(steps):
            err(f"{where}: order 단계 중복")
    elif ty == "num":
        if not isinstance(a, (int, float)) or isinstance(a, bool):
            err(f"{where}: num 정답은 숫자")
    # 보기·짝·단계 글자는 화면에서 이스케이프되므로 HTML을 넣으면 태그가 그대로 보인다
    texts = list(q.get("o") or []) + list(q.get("steps") or []) + [x for pr in (q.get("pairs") or []) for x in pr]
    if any(HTML_TAG.search(str(t)) for t in texts):
        err(f"{where}: 보기·짝·단계에 HTML 태그 — 일반 글자로 쓰세요(태그는 p·w에서만 허용)")
    if q.get("game"):
        if ty not in GAME_TYPES:
            err(f"{where}: game:true는 mc/ox/multi만 가능")
        plen = len(TAG.sub("", q.get("p", "")))
        if plen > 80:
            warn(f"{where}: 게임 문항인데 문제가 {plen}자 (권장 80자 이내)")
        for opt in q.get("o") or []:
            if len(opt) > 25:
                warn(f"{where}: 게임 문항 보기 '{opt[:12]}…' {len(opt)}자 (권장 25자 이내)")
                break


def validate(path):
    errors, warnings = [], []
    err, warn = errors.append, warnings.append
    with open(path, encoding="utf-8") as f:
        try:
            bank = json.load(f)
        except json.JSONDecodeError as e:
            return [f"JSON 파싱 실패: {e}"], [], None
    for k in ("id", "title", "source", "salt", "tabs"):
        if not bank.get(k):
            err(f"은행: '{k}' 없음")
    if "subject" in bank and bank["subject"] not in SUBJECTS:
        err(f"은행: 알 수 없는 subject {bank['subject']!r} (허용: {', '.join(sorted(SUBJECTS))})")
    ids = collections.Counter()
    stats = {"tabs": 0, "qs": 0, "game": 0, "types": collections.Counter()}
    for ti, tab in enumerate(bank.get("tabs") or [], 1):
        tw = f"탭{ti}({tab.get('id')})"
        for k in ("id", "title", "qs"):
            if not tab.get(k):
                err(f"{tw}: '{k}' 없음")
        qs = tab.get("qs") or []
        if len(qs) != PER_TAB:
            # legacy: 기존 워크시트 구성을 그대로 옮긴 은행(예: voice-ai D1 15문항)은 경고만
            (warn if bank.get("legacy") else err)(f"{tw}: 문항 {len(qs)}개 (탭당 {PER_TAB}개)")
        mix = collections.Counter(q.get("ty") for q in qs)
        mix_mc = mix["mc"] + mix["num"]  # num은 mc 1개를 대체
        expect = dict(TARGET_MIX)
        got = {"mc": mix_mc, "ox": mix["ox"], "match": mix["match"], "order": mix["order"], "multi": mix["multi"]}
        if got != expect:
            warn(f"{tw}: 유형 비율 {dict(got)} (권장 {expect})")
        pos = collections.Counter(q["a"] for q in qs if q.get("ty") == "mc" and isinstance(q.get("a"), int))
        if pos and max(pos.values()) >= 3:
            warn(f"{tw}: mc 정답 위치 쏠림 {dict(pos)}")
        for qi, q in enumerate(qs, 1):
            ids[q.get("id")] += 1
            check_q(q, f"{tw} Q{qi}({q.get('id')})", err, warn)
            stats["types"][q.get("ty")] += 1
            stats["game"] += bool(q.get("game"))
        stats["tabs"] += 1
        stats["qs"] += len(qs)
    for i, n in ids.items():
        if n > 1:
            err(f"id 중복: {i} ×{n}")
    # 문제은행 전용 브랜드 규칙: 원 출처 회사·고객사 이름은 문항에 쓰지 않는다(원본 파일은 저작권 표기 때문에 그대로 둠)
    shown = {k: v for k, v in bank.items() if k != "source"}  # source는 실제 파일 경로(폴더명)라 화면에 안 보임 → 제외
    for m in BANK_FORBIDDEN.finditer(json.dumps(shown, ensure_ascii=False)):
        err(f"원 출처 명칭 발견: {m.group(0)!r} — 문항에는 쓰지 않습니다(필요하면 디지털노마드연구소)")
    if FORBIDDEN is not None:
        text = json.dumps(bank, ensure_ascii=False)
        for m in FORBIDDEN.finditer(text):
            err(f"금지어 발견: {m.group(0)!r}")
    return errors, warnings, stats


def main():
    paths = sys.argv[1:] or sorted(glob.glob(os.path.join(HERE, "banks", "**", "*.json"), recursive=True))
    failed = False
    for p in paths:
        errors, warnings, stats = validate(p)
        print(f"■ {os.path.relpath(p, ROOT)}")
        if stats:
            t = ", ".join(f"{k} {v}" for k, v in sorted(stats["types"].items()))
            print(f"  {stats['tabs']}탭 · {stats['qs']}문항 · 게임 {stats['game']}문항 · {t}")
        for w in warnings:
            print(f"  ⚠ {w}")
        for e in errors:
            print(f"  ✗ {e}")
        if errors:
            failed = True
        else:
            print("  ✓ 통과")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
