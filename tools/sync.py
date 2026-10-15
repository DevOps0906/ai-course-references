"""원본 저장소의 최신본을 받아 rules.py 규칙으로 정리한 뒤 이 레포에 반영합니다.

사용법 (레포 루트에서):
    python3 tools/sync.py                   # 무엇이 바뀌었는지 확인만 (기본, 파일 변경 없음)
    python3 tools/sync.py --apply           # 바뀐 내용을 정리해서 반영
    python3 tools/sync.py --only AI_Voice --apply
    python3 tools/sync.py --force --apply   # 커밋이 같아도 전체를 다시 정리 (규칙을 고친 뒤)

동작:
  1. .cache/upstream/<이름> 에 원본을 얕게 clone/fetch
  2. 원본 파일 해시를 tools/manifest.json 과 비교해 추가·변경·삭제 파일을 찾음
  3. --apply 시 바뀐 파일만 정리(clean.py)해서 대상 폴더에 복사, 삭제된 파일은 지움
  4. sources.json 의 last_commit, manifest.json, CHANGELOG.md 갱신
각 대상 폴더의 README.md(이 레포에서 쓴 정리 문서)는 건드리지 않습니다.
원본에 README.md가 생기면 README_원본.md 로 저장합니다.
"""
import argparse
import datetime
import hashlib
import json
import os
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from clean import clean_file  # noqa: E402

SRC_PATH = os.path.join(HERE, "sources.json")
MANIFEST_PATH = os.path.join(HERE, "manifest.json")
CACHE = os.path.join(ROOT, ".cache", "upstream")
OURS = {"README.md"}            # 대상 폴더에서 이 레포가 관리하는 파일


def git(*args, cwd=None):
    return subprocess.run(["git", "-c", "core.quotepath=off", *args], cwd=cwd,
                          check=True, capture_output=True, text=True).stdout.strip()


def sha1(path):
    h = hashlib.sha1()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def upstream_files(folder):
    out = {}
    for d, dirs, files in os.walk(folder):
        dirs[:] = [x for x in dirs if x != ".git"]
        for f in files:
            p = os.path.join(d, f)
            rel = os.path.relpath(p, folder).replace(os.sep, "/")
            if rel == "README.md":
                rel = "README_원본.md"
            out[rel] = (p, sha1(p))
    return out


def fetch(src):
    path = os.path.join(CACHE, src["name"])
    if os.path.isdir(os.path.join(path, ".git")):
        git("fetch", "--depth", "1", "origin", src["branch"], cwd=path)
        git("reset", "--hard", "FETCH_HEAD", cwd=path)
    else:
        os.makedirs(CACHE, exist_ok=True)
        git("clone", "--depth", "1", "--branch", src["branch"], src["upstream"], path)
    return path, git("rev-parse", "HEAD", cwd=path)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--only")
    a = ap.parse_args()

    config = json.load(open(SRC_PATH, encoding="utf-8"))
    manifest = json.load(open(MANIFEST_PATH, encoding="utf-8")) if os.path.exists(MANIFEST_PATH) else {}
    log = []

    for src in config["sources"]:
        if a.only and src["name"] != a.only:
            continue
        print(f"\n■ {src['name']} → {src['target']}")
        try:
            up, head = fetch(src)
        except subprocess.CalledProcessError as e:
            print(f"  ! 원본을 받지 못했습니다: {e.stderr.strip()[:200]}")
            continue
        old = src.get("last_commit", "")
        if head == old and not a.force:
            print(f"  최신 상태 ({head[:7]})")
            continue

        files = upstream_files(up)
        known = manifest.get(src["name"], {})
        added = sorted(k for k in files if k not in known)
        changed = sorted(k for k in files if k in known and (a.force or files[k][1] != known[k]))
        removed = sorted(k for k in known if k not in files)
        print(f"  커밋 {old[:7] or '-'} → {head[:7]}  |  추가 {len(added)} · 변경 {len(changed)} · 삭제 {len(removed)}")
        for tag, items in (("+", added), ("~", changed), ("-", removed)):
            for k in items:
                print(f"    {tag} {k}")

        if not a.apply:
            continue
        tgt = os.path.join(ROOT, src["target"])
        for k in removed:
            p = os.path.join(tgt, k)
            if os.path.exists(p) and k not in OURS:
                os.remove(p)
        for k in added + changed:
            dst = os.path.join(tgt, k)
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copy2(files[k][0], dst)
            clean_file(dst, f"{src['target']}/{k}")
        manifest[src["name"]] = {k: v[1] for k, v in files.items()}
        src["last_commit"] = head
        log.append((src["name"], old, head, added, changed, removed))

    if a.apply and log:
        json.dump(config, open(SRC_PATH, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        json.dump(manifest, open(MANIFEST_PATH, "w", encoding="utf-8"), ensure_ascii=False, indent=1, sort_keys=True)
        today = datetime.date.today().isoformat()
        lines = []
        for name, old, head, ad, ch, rm in log:
            lines.append(f"- **{name}** `{old[:7] or '-'}` → `{head[:7]}` — 추가 {len(ad)}, 변경 {len(ch)}, 삭제 {len(rm)}")
            lines += [f"  - {t} {k}" for t, ks in (("추가", ad), ("변경", ch), ("삭제", rm)) for k in ks]
        cl = os.path.join(ROOT, "CHANGELOG.md")
        body = open(cl, encoding="utf-8").read() if os.path.exists(cl) else "# CHANGELOG\n"
        head_line, _, rest = body.partition("\n")
        open(cl, "w", encoding="utf-8").write(f"{head_line}\n\n## {today} 원본 동기화\n" + "\n".join(lines) + "\n" + rest)
        print("\n반영 완료 → 이제 `python3 tools/check.py` 로 검사하고 커밋하세요.")
    elif not a.apply:
        print("\n(확인만 했습니다. 반영하려면 --apply)")


if __name__ == "__main__":
    main()
