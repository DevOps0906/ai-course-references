# git_study-main — Windows 11 환경 Git·GitHub 입문 8시간(8교시) 실습 교재 + 강사 판서(Git 내부 구조 도식) 슬라이드
> ℹ️ 이 문서는 자료를 처음 분석할 때 작성한 정리본입니다. 레포에 넣으면서 원본 표기·연락처·토큰·문서 ID는 정리되었으니, 6장의 "노출" 항목은 **정리 전 원본 기준** 기록입니다.

> - **원본 버전**: 커밋 `98973e3` 기준 (최신 여부는 `python3 tools/sync.py`로 확인)
> - **총 파일 수**: 2개 (Markdown 1, PPTX 1)
> - **용량(압축 해제 기준)**: 118,319 bytes (약 116 KB)
> - **자료 성격**: ① `Git_실습교재.md` — 1교시(설치)~8교시(stash·tag·rebase·GitHub Pages 배포)까지 명령어·예상 출력·미니 과제·강사 노트를 모두 담은 **자기완결형 실습 교재**(1,947줄, 실습 38개 + 미니 과제 7개 + 종합 프로젝트 1개) ② `git수업_판서.pptx` — 강사가 수업 중 화면에 띄워 설명하는 **판서용 도식 10장**(Working Directory / Staging Area / Repository와 blob·tree·commit 해시, 브랜치 포인터·병합 그림). 발표자 노트·이미지 없음.

---

## 1. 한눈에 보기

| 항목 | 내용 |
|---|---|
| **주제** | Git 버전 관리 기초 → 브랜치·충돌·되돌리기 → GitHub 원격 저장소 → 협업(Collaborator, Fork & PR) → stash/tag/rebase → GitHub Pages 배포 |
| **과정 개요(원문)** | "대상: Git을 처음 접하거나 기초를 다지고 싶은 학습자", "시간: 총 8시간 (1교시 50분 + 휴식 10분 기준 8교시)", "실습 환경: Windows 11, Git for Windows, VS Code, GitHub", "수업 방식: 강의 20% + 실습 80%" |
| **추정 대상 학습자** | Git 미경험 개발 입문자, 부트캠프·대학 수강생, 협업을 시작하는 비전공 개발자. 2인 1조 짝 실습이 있어 오프라인 집합교육 전제(추정) |
| **구성(일수/세션)** | 1일 8교시(교시당 50분). 강사 노트 권장 배분: 강의 10분 + 실습 35분 + Q&A 5분 |
| **자료 형식** | Markdown 교재 1(bash 코드 블록 60개), PPTX 판서 10장(텍스트 도형 기반 다이어그램) |
| **평가(예시, 원문)** | 실습 과제 제출(각 교시 미니 과제) 60% + 최종 미니 프로젝트(GitHub Pages 배포) 40% |
| **핵심 키워드** | 분산 버전 관리, Working Directory / Staging Area / Repository, `git init/add/commit`, `log/diff/status`, `.gitignore`, `branch/switch/merge`, Fast-Forward vs 3-way Merge, Merge Conflict, `restore/reset(--soft/--mixed/--hard)/revert`, `remote/push/pull/fetch/clone`, Personal Access Token, Collaborator, Fork & Pull Request, upstream, 코드 리뷰, `stash`, `tag`(Semantic Versioning), `rebase`, `cherry-pick`, `commit --amend`, GitHub Pages, Git Flow / GitHub Flow |

---

## 2. 폴더·파일 구성

### 2-1. 트리 구조

```
git_study-main/
├── Git_실습교재.md      # 8교시 전체 실습 교재 (1,947줄)
└── git수업_판서.pptx    # 강사 판서용 도식 슬라이드 (10장)
```

### 2-2. 파일 목록

| 파일명 | 형식 | 크기 | 역할 |
|---|---|---:|---|
| `Git_실습교재.md` | Markdown (1,947줄, ```bash 블록 60개) | 46,286 B | 메인 교재. 교시별 학습 목표 → 개념 → `[실습 x-y]` 명령어 → 예상 출력 → `[미니 과제 n]` → 치트시트 → 수료 체크리스트 → 추가 학습 자료 → 강사 노트 |
| `git수업_판서.pptx` | PPTX (10장, 노트 0, 이미지 0) | 72,033 B | 교재 2~4교시 실습을 Git 내부 객체(blob/tree/commit)와 브랜치 포인터 그림으로 설명하는 판서 자료. 생성 2026-05-04, 수정 2026-05-20 |

---

## 3. 파일별 상세 내용

### 3-1. `Git_실습교재.md` — "Git 실습 교재 (Windows 11 환경)"

- **목적**: Git 설치부터 GitHub 협업·배포까지 8시간 안에 손으로 익히게 하는 단계형 실습서. 마지막 문구: "Git은 머리로 외우는 것이 아니라, **손으로 익히는** 도구입니다."
- **전체 커리큘럼 표(원문)**: 1교시 Git 소개 & 환경 구축 / 2교시 로컬 저장소 기본 / 3교시 히스토리 & 변경 추적 / 4교시 브랜치 (Branch) / 5교시 되돌리기 & 충돌 해결 / 6교시 원격 저장소 (GitHub) / 7교시 협업 워크플로우 / 8교시 실전 활용 & 미니 프로젝트
- **프롬프트 예시 유무**: 없음(AI 활용 내용 없음, 순수 Git 명령어 실습)

#### 1교시. Git 소개 및 환경 구축 (50분)
- 개념: 버전 관리 필요성("보고서_진짜최종_v2.docx" 예시), Git 핵심 가치 4가지, Git vs GitHub(카메라 vs 인스타그램 비유)

| 번호 | 제목(원문) | 하는 일 / 명령어 |
|---|---|---|
| 실습 1-1 | Git for Windows 설치 | git-scm.com에서 64-bit 설치. 옵션: Default editor = VS Code, PATH 기본값, OpenSSL, "Checkout Windows-style, commit Unix-style", MinTTY → `git --version` |
| 실습 1-2 | VS Code 설치 | "Code로 열기 동작 추가" 체크 |
| 실습 1-3 | 사용자 정보 설정 | `git config --global user.name/user.email`, `init.defaultBranch main`, `git config --list` |
| 실습 1-4 | Git Bash 기본 명령어 익히기 | `pwd`, `ls -al`, `cd`, `mkdir`, `touch`, `clear` |
| 미니 과제 1 | 실습 폴더 만들기 | `~/Desktop/git-study` 생성 |

#### 2교시. 로컬 저장소 기본 (50분)
- 개념: 3단계 영역 도식(Working Directory → `git add` → Staging Area → `git commit` → Repository), 좋은 커밋 메시지 7규칙

| 번호 | 제목(원문) | 하는 일 / 명령어 |
|---|---|---|
| 실습 2-1 | 저장소 초기화 | `my-first-repo` 생성, `git init`, `.git` 확인 |
| 실습 2-2 | 파일 만들기 및 상태 확인 | `echo "# 나의 첫 Git 프로젝트" > README.md`, `git status`(Untracked) |
| 실습 2-3 | 스테이징 (git add) | `git add README.md`(Changes to be committed) |
| 실습 2-4 | 첫 커밋 만들기 | `git commit -m "최초 커밋: README 파일 추가"`, `git log` |
| 실습 2-5 | 파일 수정 후 커밋 | README 추가 + `app.js` 생성 → `git add .` → "README 내용 추가 및 app.js 생성" → `git log --oneline`. add 옵션(`.`, `-A`, `*.js`) |
| 미니 과제 2 | 3개 이상 커밋 만들기 | 의미 있는 메시지로 커밋 3개+ |

#### 3교시. 히스토리 & 변경 추적 (50분)

| 번호 | 제목(원문) | 하는 일 / 명령어 |
|---|---|---|
| 실습 3-1 | log의 다양한 옵션 | `--oneline`, `-3`, `--graph --all`, `--stat`, `-p`, 파일별, `--pretty=format:"%h - %an, %ar : %s"` + 포맷 옵션표(%H %h %an %ae %ad %ar %s) |
| 실습 3-2 | 변경 사항 확인 | `git diff`, `--staged`/`--cached`, 두 커밋 비교, diff 결과 읽는 법 |
| 실습 3-3 | 파일 상태 변화 직접 확인 | Untracked → Staged → Committed → Modified 흐름 |
| 실습 3-4 | .gitignore 만들기 | OS·로그·임시·빌드·`.env`·IDE·`node_modules/`·`__pycache__/` 패턴, `git rm --cached` 주의 |
| 미니 과제 3 | 종합 실습 | `git-history-practice`에서 HTML/CSS/JS + 커밋 5개+ |

#### 4교시. 브랜치 (Branch) (50분)

| 번호 | 제목(원문) | 하는 일 / 명령어 |
|---|---|---|
| 실습 4-1 | 브랜치 생성 및 확인 | `branch-practice`, "초기 커밋", `git branch feature-login` |
| 실습 4-2 | 브랜치 이동 | `git switch`, `git checkout`, `git switch -c feature-signup` / `checkout -b`, switch vs checkout 표 |
| 실습 4-3 | 브랜치별 다른 작업 | main 수정 / feature-login에서 `login.html` → 브랜치마다 파일이 다름 확인 |
| 실습 4-4 | Fast-Forward 병합 | `feature-button`(button.html) → `git merge feature-button` |
| 실습 4-5 | 3-way Merge | `feature-header`(header.html) + main 별도 수정 → merge(머지 커밋 메시지 편집) |
| 실습 4-6 | 사용 끝난 브랜치 삭제 | `git branch -d` / `-D` |
| 미니 과제 4 | 브랜치 시나리오 실습 | `feature/login`, `feature/signup` 생성·차례 병합 |
- 브랜치 전략 소개: Git Flow(main/develop/feature/release/hotfix), GitHub Flow

#### 5교시. 되돌리기 & 충돌 해결 (50분)

| 번호 | 제목(원문) | 하는 일 / 명령어 |
|---|---|---|
| 실습 5-1 | 의도적으로 충돌 만들기 | `conflict-practice`, greeting.txt를 feature-a·main에서 다르게 수정 → `CONFLICT (content)` |
| 실습 5-2 | 충돌 해결 | `<<<<<<< HEAD / ======= / >>>>>>>` 해석, VS Code의 Accept Current/Incoming/Both/Compare 버튼 → `git add` → `git commit` |
| 실습 5-3 | 작업 영역 되돌리기 | `git restore sample.txt` |
| 실습 5-4 | 스테이징 취소 | `git restore --staged` |
| 실습 5-5 | reset 실습 | `git reset HEAD~1`(mixed) → `--soft` → `--hard` 비교(3모드 표) |
| 실습 5-6 | revert 실습 | `revert-practice`, `git revert HEAD~1` → "Revert v2" 커밋 |
| 미니 과제 5 | 충돌 시뮬레이션 | index.html `<h1>` 충돌 → 해결 |
- reset vs revert 선택 기준표("협업 중인 브랜치 → 반드시 revert")

#### 6교시. 원격 저장소 (GitHub) (50분)

| 번호 | 제목(원문) | 하는 일 / 명령어 |
|---|---|---|
| 실습 6-1 | GitHub 가입 | Sign up, 사용자명 신중히 |
| 실습 6-2 | 원격 저장소 생성 | `my-first-github-repo`, README 체크 해제 |
| 실습 6-3 | 로컬 ↔ 원격 연결 | `git remote add origin …`, `git remote -v`, `git branch -M main`, `git push -u origin main` + **Personal Access Token(classic, repo scope, 30 days) 발급 절차**, Windows 자격 증명 관리자 확인 |
| 실습 6-4 | push, pull, fetch | 웹에서 수정 후 `git pull`, `git fetch` + `git merge origin/main` |
| 실습 6-5 | 다른 저장소 클론 | `git clone … cloned-repo` |
| 실습 6-6 | 멋진 README 만들기 | 소개/시작하기/기술 스택/라이선스/작성자 템플릿 |
| 미니 과제 6 | 포트폴리오 시작하기 | `portfolio` 저장소 + about.md, projects.md push |

#### 7교시. 협업 워크플로우 (50분)
- 개념: 공동 작업자(Collaborator) vs Fork & Pull Request 비교

| 번호 | 제목(원문) | 하는 일 / 명령어 |
|---|---|---|
| 실습 7-1 | 협업자 초대 | 2인 1조. A: Settings → Collaborators → Add people / B: 초대 수락 → clone → push / A: `git pull` |
| 실습 7-2 | Fork 실습 | Fork → clone → `git switch -c feature/my-contribution` → CONTRIBUTORS.md → push → Compare & pull request → 원본 소유자 리뷰·Merge |
| 실습 7-3 | 최신 상태 유지 | `git pull origin main`, `git rebase main`, `git remote add upstream …`, `git fetch upstream` |
| 실습 7-4 | PR 충돌 시나리오 | `git fetch origin` → `git merge origin/main` → 해결 → push |
| 미니 과제 7 | 협업 시뮬레이션 | 협업자 초대, 각자 브랜치·PR·상호 리뷰·충돌 해결 |
- 코드 리뷰 문화(좋은/나쁜 코멘트), PR 체크리스트 5항목, PR 단축 기능(`Fixes #123`, `Co-authored-by`, Reviewers, 라벨)

#### 8교시. 실전 활용 & 미니 프로젝트 (50분)

| 번호 | 제목(원문) | 하는 일 / 명령어 |
|---|---|---|
| 실습 8-1 | stash 사용하기 | `git stash` / `list` / `pop` + 주요 명령(save, show, apply, drop, clear) |
| 실습 8-2 | 태그 활용 | lightweight `git tag v1.0.0`, annotated `git tag -a v1.1.0 -m …`, `git push origin --tags`, 삭제 + Semantic Versioning(MAJOR.MINOR.PATCH) |
| 실습 8-3 | rebase 시도 | merge vs rebase 도식·장단점, `git rebase main`, `--continue`, "rebase 황금률" |
| 8.4 | 자주 발생하는 문제와 해결 | ① `commit --amend -m` ② `--amend --no-edit` ③ 잘못된 브랜치 커밋 → `reset --hard` + `cherry-pick` ④ 큰 파일 `git rm --cached` ⑤ push 거부 → `pull` 후 push |
| 8.5 | [종합 미니 프로젝트] 개인 블로그 만들기 | `사용자명.github.io` 저장소 → index.html·style.css(코드 전문 제공) → `feature/about-page` 브랜치로 about.html → merge·push → Settings → Pages(Deploy from a branch, main / root) → `git tag -a v1.0.0 -m "블로그 첫 배포"` |
| 8.6 | 마무리: Git 명령어 치트시트 | Top 10 명령어, 응급 상황 대처, 협업 워크플로우 7단계 |

- **부록**: 🎓 수료 체크리스트(로컬 7 / 브랜치 5 / 원격 5 / 협업 4 / 활용 4 = 25항목), 📚 추가 학습 자료(Git 공식 문서, Pro Git 한글판, Learn Git Branching, GitHub Skills, Conventional Commits, Git Flow 원문, GitHub Cheat Sheet 한글), 💬 강사 노트(시간 배분, 환경 점검 4항목, 자주 발생하는 문제 4가지: Git Bash 실행 불가/PAT 인증 실패/충돌 당황/Vim 탈출, 평가 방법)
- **사용 도구**: Git for Windows(Git Bash, MinTTY), VS Code(병합 충돌 UI), GitHub 웹(Collaborators, Fork, PR, Pages, Developer settings), Windows 자격 증명 관리자, Vim(기본 편집기 상황 대응)

### 3-2. `git수업_판서.pptx` — 강사 판서 슬라이드 (10장)

- **목적**: 교재의 명령어 실습이 `.git` 내부에서 어떤 객체 변화를 일으키는지 강사가 그림으로 설명. 텍스트 상자·도형만으로 구성(제목 없음, 이미지·노트 없음).
- **슬라이드 흐름**

| 슬라이드 | 내용(슬라이드 텍스트 기준) | 대응 교재 실습 |
|---|---|---|
| 1 | 저장소 URL `https://github.com/DevOps0906/ai-course-references/tree/main/02-dev-basics/git`, 강사명 표기 | 오리엔테이션 |
| 2 | Working Directory / Staging Area / Repository 3영역 + `git add` / `git commit`. README.md 내용 "# 나의 첫 Git 프로젝트"의 blob 해시 `0366cd0f039472c9ad4648ebba67709663267387`, tree, "commit : 작성자, 반영자, 메시지" | 실습 2-2 ~ 2-4 |
| 3 | `git add .` 후 두 번째 커밋: README blob `c6c85f4`, app.js blob `e92152`("console.log('hello');"), tree `febf6d`→`ccbdda`, 커밋 `450416`("최초 커밋…") → `2a6135`("README 내용 추가 및 app.js 생성")의 **parent 연결** | 실습 2-5 |
| 4 | "새로운 줄 추가" 후 스테이징에만 새 README blob `43c386`이 생긴 상태(작업 영역·스테이징·저장소 차이) | 실습 3-2 (`git diff` / `--staged`) |
| 5 | "branch 구조": `main`, `feature-login`이 같은 커밋 `450416`을 가리키고, `HEAD` → `refs/heads/feature-signup` | 실습 4-1 ~ 4-2 |
| 6 | 브랜치별 커밋 그래프: main("main 브랜치 작업"), feature-login(login.html "로그인 기능 추가"), feature-button(button.html "버튼 추가") | 실습 4-3 ~ 4-4 |
| 7 | `$ git merge feature-button` + feature-header(header.html `<header>헤더</header>`), main "main에서 별도 수정" | 실습 4-4 ~ 4-5 |
| 8 | 7과 동일 구성(병합 단계 애니메이션용 복제 슬라이드로 추정) | 실습 4-5 |
| 9 | 브랜치 정리 후 `main`, `HEAD`만 남은 그래프 | 실습 4-6 |
| 10 | 강사 연락 이메일(정리 후 `writer@nomadaifactory.com`), 실습 저장소 예시 `https://github.com/DevOps0906/my-first-github` | 6교시 원격 저장소 |

- **검증 메모**: 슬라이드의 blob 해시는 교재 `echo` 내용과 정확히 일치(직접 `git hash-object`로 계산: "# 나의 첫 Git 프로젝트\n" → `0366cd0f…`, 두 줄 README → `c6c85f4d…`, `console.log('hello');\n` → `e921523b…`). 즉 **blob 해시는 수강생 PC에서도 동일하게 재현**되고, commit 해시(`450416`, `2a6135`)는 작성자·시각에 따라 달라짐 → 이 차이를 판서로 설명하는 구성으로 추정.
- **실습 항목 / 프롬프트 예시**: 없음(설명용 도식)

---

## 4. 커리큘럼 흐름

| 단계 | 교시 | 핵심 질문 | 핵심 명령 | 산출물 |
|---|---|---|---|---|
| ① 준비 | 1교시 | Git이 왜 필요한가? | `git --version`, `git config --global` | 설치·설정 완료된 PC |
| ② 로컬 기록 | 2교시 | 변경을 어떻게 저장하나? | `init`, `add`, `commit` | 첫 저장소, 커밋 3개+ |
| ③ 이력 추적 | 3교시 | 무엇이 언제 바뀌었나? | `log`, `diff`, `status`, `.gitignore` | 커밋 5개+ 저장소 |
| ④ 병렬 작업 | 4교시 | 메인을 건드리지 않고 실험하려면? | `branch`, `switch`, `merge` | FF·3-way 병합 그래프 |
| ⑤ 복구 | 5교시 | 충돌·실수는 어떻게 되돌리나? | 충돌 해결, `restore`, `reset`, `revert` | 해결된 충돌 커밋 |
| ⑥ 원격 | 6교시 | 클라우드에 올리고 받으려면? | `remote`, `push`, `pull`, `fetch`, `clone`, PAT | GitHub 저장소, README, portfolio |
| ⑦ 협업 | 7교시 | 남과 함께 작업하려면? | Collaborator, Fork, PR, `upstream`, 리뷰 | 상호 PR 머지 |
| ⑧ 실전 | 8교시 | 실무 도구와 배포 | `stash`, `tag`, `rebase`, `amend`, `cherry-pick`, GitHub Pages | `사용자명.github.io` 블로그 + v1.0.0 태그 |

판서 PPT는 ②~④ 단계(2~4교시)의 내부 동작 설명에 집중되어 있고, ⑤~⑧ 단계에 대한 판서는 없음.

---

## 5. 사용 기술·도구·외부 서비스

| 분류 | 이름 | 사용 위치 | 비고 |
|---|---|---|---|
| 버전 관리 | Git (Git for Windows 2.x, Git Bash, MinTTY) | 전 교시 | `switch`/`restore`는 Git 2.23+ 필요 |
| 편집기 | VS Code | 1교시 설치, 5교시 충돌 해결 UI | Git 기본 편집기로 지정 |
| 편집기 | Vim | 4-5, 5-2, 5-6 머지/리버트 메시지 | `i` → `ESC` → `:wq` / `:q!` |
| 호스팅 | GitHub (Repository, Collaborators, Fork, Pull Request, Files changed 리뷰, Settings → Pages, Developer settings → PAT) | 6~8교시 | 무료 계정 |
| 인증 | Personal Access Token (classic), Windows 자격 증명 관리자 | 6교시 | 비밀번호 인증 대체 |
| 배포 | GitHub Pages (Deploy from a branch) | 8.5 | `https://사용자명.github.io` |
| 웹 | HTML, CSS | 8.5 블로그 | index.html, about.html, style.css 전문 제공 |
| 규칙·전략 | Semantic Versioning, Conventional Commits, Git Flow, GitHub Flow | 2.4, 4.6, 8.2 | |
| 학습 리소스 | git-scm.com/doc, Pro Git(한글), Learn Git Branching, GitHub Skills, GitHub Cheat Sheet(한글) | 부록 | |
| 판서 | Microsoft PowerPoint | `git수업_판서.pptx` | |

---

## 6. 특이사항

### 6-1. 중복·버전 차이

- 중복 파일·버전 분기 없음(파일 2개, 역할 분리 명확).
- 판서 슬라이드 7과 8은 텍스트 구성이 동일 → 애니메이션/단계 표시용 복제로 추정.
- 판서 슬라이드 10의 실습 저장소명 `my-first-github`와 교재 6-2의 `my-first-github-repo`가 다름(강사 시연용 실제 저장소 vs 교재 예시명으로 추정).

### 6-2. 내용상 불일치·오류 가능성

| 위치 | 내용 |
|---|---|
| 1-1 vs 4-5·5-2·5-6 | 설치 시 기본 편집기를 **VS Code**로 지정하라고 해놓고, 이후 머지·커밋 단계에서는 "Vim 편집기가 뜨면 … `:wq`"라고 안내 → 실제로는 VS Code 탭이 열려 저장 후 닫아야 함. 강사 노트의 "Vim 빠져나오기" 항목과도 연동되어 수강생 혼란 가능 |
| 실습 5-6 revert | v1→v2→v3를 같은 파일 끝에 연속 추가한 뒤 `git revert HEAD~1`(v2 되돌리기) → **교재 명령 그대로 빈 저장소에서 재현한 결과 `CONFLICT (content): Merge conflict in file.txt` / `error: could not revert … v2` 발생 확인.** 교재는 "에디터 열림 → :wq"만 안내하고 충돌 대처는 없음 → 수업 중 막히는 지점 |
| 실습 8-3 rebase | 같은 파일 끝에 main·feature가 각각 줄을 추가 → **재현 결과 첫 커밋(f1) 적용 시 충돌 발생 확인.** 교재에는 "충돌 시: 해결 후 git add → git rebase --continue" 한 줄만 있음(충돌이 '반드시' 난다는 안내 필요) |
| 2.4 커밋 규칙 | "제목 첫 글자는 대문자로" 규칙과 예시 `fix: prevent crash …`(소문자 Conventional Commits) 혼재 |
| 7.3 | `git switch feature/my-work` — 앞 실습(7-2)에서 만든 브랜치는 `feature/my-contribution`이라 이름이 연결되지 않음 |
| 8.1 | `git stash save "메시지"`는 구식 문법(현행 `git stash push -m`) |
| 6-6 README 예시 | ```markdown 블록 안에 ```bash 블록을 중첩해 **마크다운 렌더링이 깨짐**(전자책·웹 게시 시 수정 필요) |
| 예시 연도 | 예상 출력 `Date: Mon Nov 18 … 2024`, `© 2024 홍길동` 등 2024년 기준 예시(판서는 2026년 작성) |

### 6-3. 누락

- README.md, LICENSE 없음 → 저장소 소개·재사용 조건 불명
- 판서는 2~4교시만 다룸(5~8교시 도식 없음)
- 5교시 이후 명령의 예상 출력 예시가 앞부분보다 적음
- SSH 키 인증 방식은 "HTTPS 또는 SSH" 언급만 있고 설정 절차 없음
- macOS/Linux 대응 내용 없음(Windows 11 전용)

### 6-4. 실행 환경 요구

- Windows 11, 설치용 관리자 권한, 인터넷 연결(강사 노트 "실습 환경 점검")
- Git for Windows, VS Code 설치
- GitHub 계정(가입 가능한 이메일), push용 Personal Access Token(classic, `repo` scope)
- 7교시는 **2인 1조** 필요(강사가 짝 지정) → 1인 온라인 독학 시 계정 2개 또는 대체 시나리오 필요
- 8.5는 Public 저장소 `사용자명.github.io` 필요

### 6-5. API 키 등 민감정보 노출 여부

| 점검 항목 | 결과 |
|---|---|
| API 키·PAT·비밀번호 값 | **노출 없음.** PAT는 발급 절차만 안내, 실제 토큰 값 없음 |
| Git 설정 예시 | `user.name "Hong Gildong"`, `user.email "your_email@example.com"` — 플레이스홀더 |
| 해시 값 | 판서의 SHA-1 해시는 교재 예시 파일 내용의 blob/commit 해시로 민감정보 아님 |
| 개인정보 | 판서 슬라이드 1에 강사 실명, 슬라이드 10에 **강사 업무 이메일 주소 기재(정리 후 `writer@nomadaifactory.com`)**. PPTX 메타데이터 `creator`/`lastModifiedBy`에도 강사 개인 이름 기록 → 재배포 시 제거 권장 |

---

## 7. 활용 포인트

1. **"AI 바이브코더를 위한 Git 4시간" 압축 강의 상품** — 8교시 중 1~4·6교시와 8.5 GitHub Pages 배포만 뽑아 "AI로 만든 웹앱을 GitHub에 올리고 배포하기" 과정으로 재구성. 기존 바이브코딩 커리큘럼의 Day 3~4 사이에 붙이는 후속 모듈로 판매.
2. **전자책 『손으로 익히는 Git — Windows 11 실습 노트』** — 실습 38개 + 미니 과제 7개 구조가 이미 장·절 체계라 그대로 출간 원고화 가능. 위 6-2의 오류(편집기 불일치, revert 충돌, 중첩 코드 블록)를 바로잡고, 판서의 blob/tree/commit 도식을 일러스트로 다시 그려 차별화.
3. **Git 판서 도식을 인터랙티브 웹 교보재로 전환** — 판서 슬라이드 2~9(3영역, 해시, parent 연결, 브랜치 포인터, 병합)를 명령어를 누를 때마다 그림이 바뀌는 HTML 시뮬레이터로 바이브 코딩해 강의·유튜브 콘텐츠와 무료 리드 마그넷으로 활용.
4. **치트시트·체크리스트 템플릿 상품** — 8.6 "Top 10 명령어 / 응급 상황 대처 / 협업 워크플로우" + 수료 체크리스트 25항목 + PR 체크리스트를 1~2장짜리 PDF/노션 템플릿으로 만들어 강의 부록 또는 단독 저가 상품으로 판매.
5. **Git 실습 자동 채점 SaaS·자동화** — 미니 과제 기준(예: "커밋 5개 이상", "`--graph`에 분기·병합 존재", "v1.0.0 태그", "Pages 배포 URL 응답")을 GitHub API로 검사하는 자동 채점기를 만들어 강의 운영(평가 60/40 기준)에 적용하고, 다른 강사에게 화이트라벨로 제공.
