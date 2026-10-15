# Git 실습 교재 (Windows 11 환경)

> **과정 개요**
> - **대상**: Git을 처음 접하거나 기초를 다지고 싶은 학습자
> - **시간**: 총 8시간 (1교시 50분 + 휴식 10분 기준 8교시)
> - **실습 환경**: Windows 11, Git for Windows, VS Code, GitHub
> - **수업 방식**: 강의 20% + 실습 80%

---

## 📋 전체 커리큘럼

| 교시 | 주제 | 핵심 내용 | 실습 |
|:---:|:---|:---|:---|
| 1교시 | Git 소개 & 환경 구축 | Git 설치, 기본 설정, Git Bash | 환경 세팅 |
| 2교시 | 로컬 저장소 기본 | init, add, commit | 첫 커밋 만들기 |
| 3교시 | 히스토리 & 변경 추적 | log, diff, status | 변경사항 추적 실습 |
| 4교시 | 브랜치 (Branch) | branch, switch, merge | 브랜치 생성/병합 |
| 5교시 | 되돌리기 & 충돌 해결 | reset, revert, restore | 머지 충돌 실습 |
| 6교시 | 원격 저장소 (GitHub) | remote, push, pull, clone | GitHub 연동 |
| 7교시 | 협업 워크플로우 | Fork, PR, 코드 리뷰 | 팀 협업 시뮬레이션 |
| 8교시 | 실전 활용 & 미니 프로젝트 | stash, rebase, tag | 종합 실습 |

---

# 🕐 1교시. Git 소개 및 환경 구축 (50분)

## 학습 목표
- Git이 무엇이며 왜 필요한지 이해한다
- Windows 11에 Git을 설치하고 초기 설정을 완료한다
- Git Bash 기본 명령어를 사용할 수 있다

## 1.1 Git이란?

**Git**은 **분산 버전 관리 시스템(Distributed Version Control System)** 입니다.

### 버전 관리가 왜 필요한가?

```
보고서_최종.docx
보고서_최종_수정.docx
보고서_진짜최종.docx
보고서_진짜최종_v2.docx
보고서_이게진짜최종.docx
```

😱 위와 같은 파일 관리, 익숙하지 않으신가요?

### Git의 핵심 가치
- **이력 관리**: 누가, 언제, 무엇을, 왜 변경했는지 추적
- **협업**: 여러 사람이 동시에 작업 가능
- **백업**: 분산 저장으로 안전성 확보
- **브랜치**: 병렬로 다양한 시도 가능

### Git vs GitHub
| 구분 | Git | GitHub |
|:---:|:---|:---|
| 정체 | 버전 관리 **도구** (소프트웨어) | Git 저장소 **호스팅 서비스** (웹) |
| 위치 | 내 PC | 클라우드(웹) |
| 비유 | 카메라 | 인스타그램 |

---

## 1.2 Windows 11에 Git 설치하기

### [실습 1-1] Git for Windows 설치

1. **공식 사이트 접속**
   - https://git-scm.com/download/win 접속
   - "64-bit Git for Windows Setup" 다운로드

2. **설치 시 주요 옵션** (대부분 기본값 유지, 다음 항목만 확인)
   - **Default editor**: `Use Visual Studio Code as Git's default editor` 선택
   - **Adjusting your PATH environment**: `Git from the command line and also from 3rd-party software` 선택 (기본값)
   - **Choose HTTPS transport backend**: `Use the OpenSSL library` (기본값)
   - **Configuring the line ending conversions**: `Checkout Windows-style, commit Unix-style line endings` (기본값)
   - **Configuring the terminal emulator**: `Use MinTTY` (기본값)

3. **설치 확인**
   - 시작 메뉴에서 **Git Bash** 검색하여 실행
   - 다음 명령어 입력
   ```bash
   git --version
   ```
   - `git version 2.xx.x.windows.x` 형태로 출력되면 성공

### [실습 1-2] VS Code 설치 (이미 설치되어 있다면 생략)

1. https://code.visualstudio.com/ 에서 다운로드 후 설치
2. 설치 시 **"Code로 열기 동작 추가"** 모두 체크

---

## 1.3 Git 초기 설정

### [실습 1-3] 사용자 정보 설정

Git Bash를 열고 본인의 이름과 이메일을 설정합니다.

```bash
# 사용자 이름 설정 (본인 이름으로)
git config --global user.name "Hong Gildong"

# 이메일 설정 (GitHub 가입 예정 이메일로)
git config --global user.email "your_email@example.com"

# 기본 브랜치명을 main으로 설정
git config --global init.defaultBranch main

# 설정 확인
git config --list
```

> 💡 **TIP**: `--global` 옵션은 PC 전체에 적용된다는 의미입니다. 특정 프로젝트만 다른 설정을 쓰려면 옵션 없이 사용합니다.

### [실습 1-4] Git Bash 기본 명령어 익히기

Git Bash는 리눅스 명령어를 사용합니다. Windows 명령 프롬프트와 다릅니다.

```bash
# 현재 위치 확인
pwd

# 현재 디렉토리 목록
ls
ls -al    # 숨김파일 포함, 상세 정보

# 디렉토리 이동
cd Desktop
cd ..     # 상위 디렉토리로

# 디렉토리 생성
mkdir git-practice

# 파일 생성
touch hello.txt

# 화면 지우기
clear     # 또는 Ctrl + L
```

### [미니 과제 1] 실습 폴더 만들기

```bash
cd ~
cd Desktop
mkdir git-study
cd git-study
pwd
```

---

# 🕐 2교시. 로컬 저장소 기본 (50분)

## 학습 목표
- Git 저장소를 생성할 수 있다
- 작업 영역, 스테이징 영역, 저장소의 개념을 이해한다
- add, commit으로 변경 이력을 저장할 수 있다

## 2.1 Git의 3단계 영역

```
┌──────────────────┐    git add    ┌──────────────────┐   git commit   ┌──────────────────┐
│  Working Directory │ ───────────→  │  Staging Area    │ ─────────────→ │  Repository       │
│  (작업 영역)        │                │  (스테이징 영역)   │                 │  (저장소)          │
│  실제 파일 작업     │                │  커밋 후보 모음    │                 │  버전 저장소       │
└──────────────────┘                └──────────────────┘                 └──────────────────┘
```

| 영역 | 설명 | 확인 명령어 |
|:---|:---|:---|
| Working Directory | 실제 파일을 작업하는 공간 | `ls` |
| Staging Area (Index) | 커밋할 파일을 모아두는 대기실 | `git status` |
| Repository (.git) | 커밋된 버전들의 저장소 | `git log` |

---

## 2.2 저장소 생성 및 첫 커밋

### [실습 2-1] 저장소 초기화

```bash
# 작업 폴더 만들기
cd ~/Desktop
mkdir my-first-repo
cd my-first-repo

# Git 저장소 초기화
git init

# 결과: Initialized empty Git repository in ...
# 숨김 폴더 .git이 생성됨
ls -al
```

> 💡 `.git` 폴더가 모든 Git 정보를 담고 있습니다. 이 폴더가 있어야 Git 저장소!

### [실습 2-2] 파일 만들기 및 상태 확인

```bash
# README 파일 만들기
echo "# 나의 첫 Git 프로젝트" > README.md

# 상태 확인
git status
```

**예상 출력**:
```
On branch main
No commits yet
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        README.md
```

🔹 **Untracked**: Git이 추적하지 않는 새 파일 상태

### [실습 2-3] 스테이징 (git add)

```bash
# 특정 파일 스테이징
git add README.md

# 상태 확인
git status
```

**예상 출력**:
```
Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   README.md
```

🔹 **Changes to be committed**: 커밋 준비 완료 상태

### [실습 2-4] 첫 커밋 만들기

```bash
# 커밋 (메시지 포함)
git commit -m "최초 커밋: README 파일 추가"

# 커밋 이력 확인
git log
```

**예상 출력**:
```
commit a1b2c3d4e5f6... (HEAD -> main)
Author: Hong Gildong <your_email@example.com>
Date:   Mon Nov 18 10:00:00 2024 +0900

    최초 커밋: README 파일 추가
```

---

## 2.3 add와 commit 한번에 (자주 쓰는 패턴)

### [실습 2-5] 파일 수정 후 커밋

```bash
# 파일 수정
echo "이 프로젝트는 Git 학습용입니다." >> README.md

# 상태 확인
git status
# → modified: README.md  (Changes not staged for commit)

# 새 파일 추가
echo "console.log('hello');" > app.js
git status

# 모든 변경사항 스테이징 (현재 디렉토리)
git add .

# 커밋
git commit -m "README 내용 추가 및 app.js 생성"

# 이력 확인
git log --oneline
```

### 주요 add 옵션

```bash
git add 파일명          # 특정 파일만
git add .              # 현재 디렉토리 모든 변경
git add -A             # 저장소 전체 모든 변경 (삭제 포함)
git add *.js           # 패턴 매칭
```

---

## 2.4 좋은 커밋 메시지 작성법

### 좋은 커밋 메시지의 7가지 규칙
1. 제목과 본문을 빈 줄로 분리
2. 제목은 50자 이내로
3. 제목 첫 글자는 대문자로 (영어 기준)
4. 제목 끝에 마침표 X
5. 제목은 **명령문**으로 작성 ("Add" O, "Added" X)
6. 본문은 **무엇을, 왜** 변경했는지 설명
7. 한 줄 72자 제한

### 예시
```
❌ 나쁜 예: "수정함"
❌ 나쁜 예: "버그 픽스"
✅ 좋은 예: "로그인 폼 이메일 유효성 검사 추가"
✅ 좋은 예: "fix: prevent crash when user input is empty"
```

### [미니 과제 2] 3개 이상 커밋 만들기

자유롭게 파일을 만들고 수정하면서 의미있는 커밋 메시지로 3개 이상의 커밋을 만들어보세요.

```bash
git log --oneline
# 3개 이상의 커밋이 보여야 합니다
```

---

# 🕐 3교시. 히스토리 & 변경 추적 (50분)

## 학습 목표
- log 명령어로 다양한 형식의 커밋 이력을 확인할 수 있다
- diff로 변경 사항을 비교할 수 있다
- 파일 상태별로 적절한 명령을 적용할 수 있다

## 3.1 git log 활용하기

### [실습 3-1] log의 다양한 옵션

```bash
# 기본 로그
git log

# 한 줄로 보기
git log --oneline

# 최근 3개만
git log -3

# 그래프 형태로
git log --oneline --graph --all

# 누가, 언제 변경했는지 + 파일 변경량
git log --stat

# 모든 변경 내용까지
git log -p

# 특정 파일의 이력만
git log --oneline README.md

# 예쁘게 보기 (사용자 정의)
git log --pretty=format:"%h - %an, %ar : %s"
```

### log 포맷 옵션 정리

| 옵션 | 의미 |
|:---:|:---|
| `%H` | 커밋 해시 (전체) |
| `%h` | 커밋 해시 (축약) |
| `%an` | 작성자 이름 |
| `%ae` | 작성자 이메일 |
| `%ad` | 작성 날짜 |
| `%ar` | 상대 시간 (예: 3 hours ago) |
| `%s` | 커밋 메시지 |

---

## 3.2 git diff로 변경사항 비교

### [실습 3-2] 변경 사항 확인

```bash
# 파일 수정
echo "새로운 줄 추가" >> README.md

# 작업 영역 vs 스테이징 영역 비교
git diff

# 스테이징
git add README.md

# 스테이징 영역 vs 마지막 커밋 비교
git diff --staged
# 또는
git diff --cached

# 커밋 후 비교
git commit -m "README에 줄 추가"

# 두 커밋 비교 (해시는 git log에서 확인)
git log --oneline
git diff 첫번째해시 두번째해시
```

### diff 결과 읽기

```diff
diff --git a/README.md b/README.md
index abc1234..def5678 100644
--- a/README.md       ← 비교 대상 (이전)
+++ b/README.md       ← 비교 대상 (이후)
@@ -1,3 +1,4 @@      ← 변경 위치
 # 나의 첫 Git 프로젝트
 이 프로젝트는 Git 학습용입니다.
+새로운 줄 추가        ← + : 추가된 줄
-삭제된 줄            ← - : 삭제된 줄
```

---

## 3.3 파일 상태 시각화

```
파일 상태 흐름도:

┌─────────────┐  git add   ┌─────────────┐ git commit  ┌─────────────┐
│ Untracked   │ ─────────→ │ Staged      │ ──────────→ │ Committed   │
│ (추적 안됨)  │             │ (스테이징됨)  │              │ (커밋됨)     │
└─────────────┘             └─────────────┘              └─────────────┘
                                  ↑                              │
                                  │   파일 수정                    │
                                  └──────────────────────────────┘
                                          ↓
                                    ┌─────────────┐
                                    │ Modified    │
                                    │ (수정됨)     │
                                    └─────────────┘
```

### [실습 3-3] 파일 상태 변화 직접 확인

```bash
# 1. 새 파일 = Untracked
touch new-file.txt
git status

# 2. add 후 = Staged
git add new-file.txt
git status

# 3. commit 후 = Committed (clean)
git commit -m "새 파일 추가"
git status

# 4. 파일 수정 후 = Modified
echo "내용 추가" > new-file.txt
git status
```

---

## 3.4 .gitignore - 추적하지 않을 파일 지정

### [실습 3-4] .gitignore 만들기

```bash
# .gitignore 파일 생성
touch .gitignore
```

VS Code로 열어서 다음 내용 작성:

```gitignore
# 운영체제
.DS_Store
Thumbs.db

# 로그 파일
*.log

# 임시 파일
*.tmp
*.temp

# 빌드 결과물
build/
dist/
*.exe

# 환경 변수
.env
.env.local

# IDE 설정
.vscode/
.idea/

# 의존성
node_modules/
__pycache__/
*.pyc
```

```bash
# 테스트
touch test.log
git status
# → test.log는 보이지 않아야 함 (정상)

# .gitignore 커밋
git add .gitignore
git commit -m ".gitignore 추가"
```

> 💡 **주의**: 이미 추적 중인 파일은 .gitignore에 추가해도 무시되지 않습니다. `git rm --cached 파일명`으로 추적 해제 후 추가하세요.

### [미니 과제 3] 종합 실습

1. 새 프로젝트 폴더 생성 (`git-history-practice`)
2. `git init`
3. HTML, CSS, JS 파일 각각 만들기
4. `.gitignore`에 `.log` 추가
5. 각 단계마다 의미있는 커밋 5개 이상 만들기
6. `git log --oneline --graph` 결과를 확인하기

---

# 🕐 4교시. 브랜치 (Branch) (50분)

## 학습 목표
- 브랜치의 개념과 필요성을 이해한다
- 브랜치를 생성, 이동, 병합할 수 있다
- 다양한 브랜치 전략의 차이를 안다

## 4.1 브랜치란?

**브랜치(Branch)** = 독립된 작업 공간

### 왜 브랜치가 필요한가?
- 메인 코드를 건드리지 않고 새 기능 시험
- 여러 사람이 충돌 없이 동시 작업
- 버전별 관리 (예: v1.0, v2.0)

### 브랜치 시각화

```
                    feature
                    o───o───o
                   /
main:  o───o───o───o───────────o (merge)
```

---

## 4.2 브랜치 기본 명령어

### [실습 4-1] 브랜치 생성 및 확인

```bash
# 새 실습 폴더
cd ~/Desktop
mkdir branch-practice
cd branch-practice
git init

# 초기 커밋 (브랜치 작업하려면 최소 1개 커밋 필요)
echo "# Branch 실습" > README.md
git add .
git commit -m "초기 커밋"

# 현재 브랜치 확인
git branch
# → * main

# 새 브랜치 생성
git branch feature-login

# 브랜치 목록
git branch
#   feature-login
# * main      (별표는 현재 위치)
```

### [실습 4-2] 브랜치 이동

```bash
# 브랜치 이동 (최신 방식)
git switch feature-login

# 또는 (구식, 여전히 많이 쓰임)
git checkout feature-login

# 브랜치 생성과 동시에 이동 (한번에)
git switch -c feature-signup
# 또는
git checkout -b feature-signup
```

### switch vs checkout

| 명령 | 용도 |
|:---|:---|
| `git switch 브랜치` | 브랜치 이동 (Git 2.23+) |
| `git switch -c 브랜치` | 생성+이동 |
| `git checkout 브랜치` | 브랜치 이동 (구식) |
| `git checkout -b 브랜치` | 생성+이동 (구식) |

> 💡 `checkout`은 여러 용도로 쓰여 혼란스러워, `switch`와 `restore`로 분리되었습니다.

---

## 4.3 브랜치에서 작업하기

### [실습 4-3] 브랜치별 다른 작업

```bash
# main으로 이동
git switch main

# main에서 작업
echo "main 브랜치 작업" >> README.md
git add .
git commit -m "main 브랜치 수정"

# feature-login으로 이동
git switch feature-login

# 파일 확인 - main의 변경이 없음 (독립적)
cat README.md

# feature-login에서 작업
echo "로그인 기능 추가" > login.html
git add .
git commit -m "로그인 페이지 추가"

# 다시 main으로 이동
git switch main

# login.html이 사라짐 (브랜치마다 다른 파일)
ls
```

---

## 4.4 브랜치 병합 (Merge)

### [실습 4-4] Fast-Forward 병합

```bash
# 새 브랜치 만들고 작업
git switch -c feature-button
echo "<button>클릭</button>" > button.html
git add .
git commit -m "버튼 추가"

# main으로 이동
git switch main

# main에 feature-button 병합
git merge feature-button

# 그래프 확인
git log --oneline --graph --all
```

### [실습 4-5] 3-way Merge

```bash
# 새 브랜치 만들고 작업
git switch -c feature-header
echo "<header>헤더</header>" > header.html
git add .
git commit -m "헤더 추가"

# main에도 다른 작업 추가
git switch main
echo "main에서 별도 수정" >> README.md
git add .
git commit -m "main에서 README 수정"

# main에 feature-header 병합
git merge feature-header
# Vim 편집기가 뜨면: i → 메시지 수정 → ESC → :wq

# 그래프 확인 (분기와 병합이 보임)
git log --oneline --graph --all
```

> 💡 **Vim 편집기 빠져나오기**: `ESC` → `:wq` (저장 후 종료) 또는 `:q!` (저장 없이 종료)

---

## 4.5 브랜치 삭제

### [실습 4-6] 사용 끝난 브랜치 삭제

```bash
# 병합된 브랜치 삭제
git branch -d feature-button
git branch -d feature-header

# 병합 안된 브랜치 강제 삭제 (주의!)
git branch -D feature-signup

# 브랜치 목록 확인
git branch
```

---

## 4.6 브랜치 전략 (간단 소개)

### Git Flow
```
main (운영)
  └─ develop (개발)
       ├─ feature/* (기능 개발)
       ├─ release/* (배포 준비)
       └─ hotfix/* (긴급 수정)
```

### GitHub Flow (단순)
```
main
  └─ feature/* (기능별 브랜치 → PR → main 병합)
```

### [미니 과제 4] 브랜치 시나리오 실습

다음 상황을 직접 구현해보세요:
1. `main`에서 시작 (README.md 있음)
2. `feature/login` 브랜치 생성, login.html 추가 후 커밋
3. `feature/signup` 브랜치 생성 (main에서), signup.html 추가 후 커밋
4. main으로 와서 두 브랜치 차례로 병합
5. `git log --oneline --graph --all`로 그래프 확인

---

# 🕐 5교시. 되돌리기 & 충돌 해결 (50분)

## 학습 목표
- 머지 충돌을 식별하고 해결할 수 있다
- 변경 사항을 되돌리는 다양한 방법을 안다
- 상황에 맞는 되돌리기 명령을 선택할 수 있다

## 5.1 머지 충돌 (Merge Conflict)

### 충돌이 발생하는 경우
**같은 파일의 같은 줄**을 두 브랜치에서 다르게 수정했을 때

### [실습 5-1] 의도적으로 충돌 만들기

```bash
# 새 실습 폴더
cd ~/Desktop
mkdir conflict-practice
cd conflict-practice
git init

# 초기 파일
echo "Hello World" > greeting.txt
git add .
git commit -m "초기 커밋"

# 브랜치 A 생성
git switch -c feature-a
echo "Hello from A" > greeting.txt
git add .
git commit -m "A 브랜치: 인사말 변경"

# main으로 이동
git switch main

# main에서도 같은 파일 같은 줄 수정
echo "Hello from Main" > greeting.txt
git add .
git commit -m "main: 인사말 변경"

# 충돌 발생!
git merge feature-a
```

**오류 메시지**:
```
Auto-merging greeting.txt
CONFLICT (content): Merge conflict in greeting.txt
Automatic merge failed; fix conflicts and then commit the result.
```

### [실습 5-2] 충돌 해결

```bash
# 충돌 파일 확인
git status

# 파일 열기
cat greeting.txt
```

**충돌 표시**:
```
<<<<<<< HEAD
Hello from Main
=======
Hello from A
>>>>>>> feature-a
```

**의미**:
- `<<<<<<< HEAD` ~ `=======` : 현재 브랜치(main)의 내용
- `=======` ~ `>>>>>>> feature-a` : 병합하려는 브랜치의 내용

**해결 방법**:

VS Code로 파일 열기:
```bash
code greeting.txt
```

VS Code에서는 친절하게 버튼이 표시됩니다:
- **Accept Current Change**: 현재 브랜치 내용 선택
- **Accept Incoming Change**: 병합 브랜치 내용 선택
- **Accept Both Changes**: 둘 다 유지
- **Compare Changes**: 비교

또는 직접 편집:
```
Hello from Main and A
```

저장 후:
```bash
# 충돌 해결 후 스테이징
git add greeting.txt

# 커밋 (자동 메시지 사용)
git commit
# Vim에서 :wq

# 결과 확인
git log --oneline --graph --all
```

---

## 5.2 되돌리기 명령어 비교

| 명령어 | 용도 | 영향 범위 |
|:---|:---|:---|
| `git restore` | 작업 영역 변경 되돌리기 | Working Directory |
| `git restore --staged` | 스테이징 취소 | Staging Area |
| `git reset` | 커밋 되돌리기 | 이력 자체 변경 |
| `git revert` | 새 커밋으로 되돌리기 | 이력 보존 |

---

## 5.3 git restore - 변경 사항 취소

### [실습 5-3] 작업 영역 되돌리기

```bash
# 새 폴더
cd ~/Desktop
mkdir restore-practice
cd restore-practice
git init

# 초기 파일과 커밋
echo "원본 내용" > sample.txt
git add .
git commit -m "초기 커밋"

# 파일 수정
echo "수정된 내용" > sample.txt
cat sample.txt

# 수정 사항 취소 (작업 영역)
git restore sample.txt
cat sample.txt
# → "원본 내용" 으로 복구됨
```

### [실습 5-4] 스테이징 취소

```bash
# 파일 수정 후 스테이징
echo "수정 내용" > sample.txt
git add sample.txt
git status

# 스테이징만 취소 (파일은 그대로)
git restore --staged sample.txt
git status
# → 수정은 남아있지만 unstaged 상태
```

---

## 5.4 git reset - 커밋 되돌리기

### reset의 3가지 모드

| 모드 | 작업 영역 | 스테이징 | 커밋 |
|:---:|:---:|:---:|:---:|
| `--soft` | 유지 | 유지 | 되돌림 |
| `--mixed` (기본) | 유지 | 되돌림 | 되돌림 |
| `--hard` | 되돌림 | 되돌림 | 되돌림 ⚠️ |

### [실습 5-5] reset 실습

```bash
# 여러 커밋 만들기
echo "v1" > version.txt
git add .
git commit -m "v1 추가"

echo "v2" >> version.txt
git add .
git commit -m "v2 추가"

echo "v3" >> version.txt
git add .
git commit -m "v3 추가"

# 이력 확인
git log --oneline

# 가장 최근 커밋만 되돌리기 (--mixed, 기본)
git reset HEAD~1
git log --oneline
git status
# → v3 변경은 작업 영역에 남아있음

# --soft로 되돌리기 (스테이징 유지)
git add .
git commit -m "v3 다시 추가"
git reset --soft HEAD~1
git status
# → v3 변경이 스테이징된 상태

# --hard로 되돌리기 (완전 삭제, 위험!)
git commit -m "v3 또 추가"
git reset --hard HEAD~1
git log --oneline
cat version.txt
# → v3가 완전히 사라짐
```

> ⚠️ **경고**: `--hard`는 변경 내용이 완전히 사라집니다. **공유된 브랜치에서는 절대 사용 금지!**

---

## 5.5 git revert - 안전한 되돌리기

`reset`은 이력을 **삭제**하지만 `revert`는 새 커밋으로 **취소**합니다.

### [실습 5-6] revert 실습

```bash
# 새 폴더
cd ~/Desktop
mkdir revert-practice
cd revert-practice
git init

# 커밋 여러 개 만들기
echo "v1" > file.txt
git add . && git commit -m "v1"
echo "v2" >> file.txt
git add . && git commit -m "v2"
echo "v3" >> file.txt
git add . && git commit -m "v3"

# 이력 확인
git log --oneline

# v2 커밋을 되돌리기 (해시 복사)
git revert HEAD~1
# 에디터 열림 → :wq

# 이력 확인
git log --oneline
# → 기존 커밋들 + "Revert v2" 커밋 추가됨

cat file.txt
```

### reset vs revert 선택 기준

| 상황 | 추천 |
|:---|:---:|
| 혼자 작업 중인 로컬 브랜치 | `reset` |
| 이미 push한 커밋 | `revert` |
| 협업 중인 브랜치 | **반드시 `revert`** |

### [미니 과제 5] 충돌 시뮬레이션

1. 새 폴더에서 git init
2. `index.html`에 `<h1>제목</h1>` 작성, 커밋
3. `feature` 브랜치 만들고 `<h1>새 제목</h1>`으로 변경, 커밋
4. main으로 돌아와서 `<h1>메인 제목</h1>`으로 변경, 커밋
5. main에 feature 병합 시도 → 충돌 발생 확인
6. 충돌 해결 후 커밋
7. `git log --oneline --graph --all`로 확인

---

# 🕐 6교시. 원격 저장소 (GitHub) (50분)

## 학습 목표
- GitHub 계정을 만들고 저장소를 생성할 수 있다
- 로컬 저장소를 원격 저장소와 연동할 수 있다
- push, pull, clone을 사용할 수 있다

## 6.1 GitHub 가입 및 저장소 생성

### [실습 6-1] GitHub 가입

1. https://github.com 접속
2. **Sign up** 클릭
3. 이메일, 비밀번호, 사용자명 입력
4. 이메일 인증 완료

> 💡 **사용자명 팁**: 나중에 변경 어려우니 신중하게! 보통 영어 이름이나 닉네임을 추천합니다.

### [실습 6-2] 원격 저장소 생성

1. GitHub 로그인 후 우측 상단 **+** → **New repository**
2. 설정:
   - **Repository name**: `my-first-github-repo`
   - **Description**: (선택) 간단한 설명
   - **Public** 선택 (Private도 무료)
   - **Add a README file** **체크 해제** (로컬에 이미 있음)
   - **.gitignore** : None
   - **License**: None
3. **Create repository** 클릭
4. 다음 화면에 표시되는 URL 복사 (HTTPS 또는 SSH)
   - 예: `https://github.com/사용자명/my-first-github-repo.git`

---

## 6.2 원격 저장소 연결

### [실습 6-3] 로컬 ↔ 원격 연결

```bash
# 로컬 폴더 준비
cd ~/Desktop
mkdir github-practice
cd github-practice
git init

# 첫 파일 만들기
echo "# GitHub 연동 실습" > README.md
git add .
git commit -m "최초 커밋"

# 원격 저장소 연결 (URL은 본인 것으로!)
git remote add origin https://github.com/사용자명/my-first-github-repo.git

# 연결 확인
git remote -v
# → origin  https://github.com/.../...git (fetch)
# → origin  https://github.com/.../...git (push)

# 기본 브랜치 확인 후 main으로
git branch -M main

# 원격으로 푸시
git push -u origin main
```

### Personal Access Token 인증

최근 GitHub은 **비밀번호 인증을 폐지**했습니다. 대신 **Personal Access Token (PAT)** 사용:

1. GitHub → 우측 상단 프로필 → **Settings**
2. 좌측 메뉴 최하단 → **Developer settings**
3. **Personal access tokens** → **Tokens (classic)**
4. **Generate new token (classic)**
5. 설정:
   - **Note**: `Git 실습용`
   - **Expiration**: 30 days
   - **Select scopes**: `repo` 체크
6. **Generate token** → 토큰 복사 (한 번만 표시되니 주의!)
7. push 시 비밀번호 자리에 토큰 붙여넣기

### Windows Credential Manager 확인

Windows에서는 자격증명 관리자에 저장됩니다.
- `제어판 → 사용자 계정 → 자격 증명 관리자 → Windows 자격 증명`
- `git:https://github.com` 항목이 있으면 GitHub 로그인 정보 저장됨

---

## 6.3 원격 저장소 명령어

### [실습 6-4] push, pull, fetch

```bash
# 로컬 변경 → 원격으로 (push)
echo "내용 추가" >> README.md
git add .
git commit -m "README 수정"
git push
# (이미 -u origin main 했으므로 git push만 해도 됨)

# 원격 변경 → 로컬로 (pull)
# GitHub 웹에서 직접 README.md 수정 후 commit
# 로컬에서:
git pull

# fetch vs pull
# fetch: 원격 내용 가져오기만 (병합 X)
git fetch

# 가져온 후 직접 병합
git merge origin/main
```

### push, pull, fetch, clone 정리

| 명령어 | 의미 |
|:---|:---|
| `git clone URL` | 원격 저장소를 복제 (처음 한번) |
| `git push` | 로컬 커밋을 원격으로 전송 |
| `git pull` | 원격 변경 가져와서 자동 병합 (fetch + merge) |
| `git fetch` | 원격 변경 가져오기만 (병합 안함) |

---

## 6.4 git clone - 원격 저장소 복제

### [실습 6-5] 다른 저장소 클론

```bash
# 새 위치로 이동
cd ~/Desktop

# GitHub의 어떤 공개 저장소든 클론 가능
# 예시: 본인이 만든 저장소를 새 폴더에 클론
git clone https://github.com/사용자명/my-first-github-repo.git cloned-repo

# 폴더 이동
cd cloned-repo

# 이력 확인 (원격의 모든 커밋이 그대로!)
git log --oneline

# remote 자동 설정됨
git remote -v
```

> 💡 `init` + `remote add`를 한번에 처리하는 것이 `clone`

---

## 6.5 README.md 작성하기

GitHub의 README.md는 저장소의 **얼굴**입니다.

### [실습 6-6] 멋진 README 만들기

```markdown
# 프로젝트 이름

## 📖 소개
프로젝트에 대한 간단한 설명을 적습니다.

## 🚀 시작하기

### 설치 방법
```bash
git clone https://github.com/사용자명/프로젝트.git
cd 프로젝트
npm install
```

### 실행
```bash
npm start
```

## 🛠 기술 스택
- HTML / CSS / JavaScript
- React 18

## 📝 라이선스
MIT License

## 👤 작성자
- 이름: 홍길동
- GitHub: [@username](https://github.com/username)
```

```bash
# 커밋 후 푸시
git add README.md
git commit -m "README 작성"
git push
```

---

### [미니 과제 6] 포트폴리오 시작하기

1. GitHub에 `portfolio` 저장소 생성
2. 로컬에 `portfolio` 폴더 만들고 git init
3. README.md에 본인 소개 작성 (마크다운 활용)
4. `about.md`, `projects.md` 등 추가 페이지 작성
5. 원격에 연결하고 push
6. GitHub 웹에서 확인

---

# 🕐 7교시. 협업 워크플로우 (50분)

## 학습 목표
- Fork와 Pull Request의 차이를 이해한다
- 협업 시나리오를 실습할 수 있다
- 코드 리뷰 문화를 경험한다

## 7.1 협업 방식 비교

### 방법 1: 공동 작업자 (Collaborator)
- 같은 팀, 같은 회사 등 신뢰 관계
- 저장소에 직접 push 권한 부여
- 빠르지만 사고 위험 ↑

### 방법 2: Fork & Pull Request
- 오픈소스, 외부 기여
- 원본을 **복사**해서 작업 → 본인 저장소에 push → 원본에 PR 요청
- 안전하지만 단계 많음

---

## 7.2 공동 작업자 추가 방식

### [실습 7-1] 협업자 초대

**시나리오**: 2명씩 짝을 지어 실습 (강사가 짝 지정)

**A 학생 (저장소 소유자)**:
1. 본인 GitHub 저장소 → **Settings** → **Collaborators**
2. **Add people** → B의 GitHub 사용자명 입력 → 초대
3. B의 이메일/알림으로 초대장 전송됨

**B 학생 (초대받은 협업자)**:
1. 초대 수락 (이메일 링크 또는 알림)
2. A의 저장소 클론
```bash
cd ~/Desktop
git clone https://github.com/A사용자명/저장소.git collab-test
cd collab-test
```
3. 파일 수정, 커밋, 푸시
```bash
echo "B가 추가한 내용" >> README.md
git add .
git commit -m "B 학생 기여"
git push
```

**A 학생**:
```bash
# B의 변경 사항 받아오기
git pull
cat README.md
# → B의 내용 확인
```

---

## 7.3 Fork & Pull Request 방식

### [실습 7-2] Fork 실습

**시나리오**: 짝 바꿔서 다른 친구의 저장소에 PR 보내기

**1단계: Fork**
1. 다른 친구의 GitHub 저장소 페이지로 이동
2. 우측 상단 **Fork** 클릭
3. 본인 계정으로 복사됨

**2단계: Clone (본인 Fork)**
```bash
cd ~/Desktop
git clone https://github.com/본인사용자명/저장소.git fork-test
cd fork-test
```

**3단계: 브랜치 생성 및 작업**
```bash
git switch -c feature/my-contribution

# 파일 수정
echo "친구의 프로젝트에 기여합니다!" >> CONTRIBUTORS.md
git add .
git commit -m "CONTRIBUTORS 파일 추가"

# 본인 Fork에 푸시
git push -u origin feature/my-contribution
```

**4단계: Pull Request 생성**
1. 본인 GitHub Fork 페이지로 이동
2. 노란색 배너의 **Compare & pull request** 클릭
   (또는 **Pull requests** 탭 → **New pull request**)
3. PR 작성:
   - **Title**: `CONTRIBUTORS 파일 추가`
   - **Description**: 
     ```
     ## 변경 내용
     - CONTRIBUTORS.md 파일 추가
     
     ## 변경 이유
     기여자 명단을 관리하기 위함
     ```
4. **Create pull request** 클릭

**5단계: 원본 저장소 소유자가 리뷰 & 머지**
1. 원본 저장소 소유자(친구)는 **Pull requests** 탭 확인
2. PR 내용 검토
3. **Files changed**에서 코드 리뷰
4. 의견이 있으면 **Comment** 또는 **Request changes**
5. 이상 없으면 **Merge pull request** → **Confirm merge**

---

## 7.4 협업 시 자주 쓰는 명령

### [실습 7-3] 최신 상태 유지

```bash
# 원격의 최신 변경 가져오기
git pull origin main

# 또는 단계별로
git fetch origin
git merge origin/main

# 본인 브랜치를 main 기준으로 최신화 (rebase 방식)
git switch feature/my-work
git rebase main
```

### upstream 설정 (Fork 후 원본 추적)

```bash
# 원본 저장소를 upstream으로 추가
git remote add upstream https://github.com/원본소유자/저장소.git

# 확인
git remote -v
# origin    https://github.com/내계정/저장소.git (fetch, push)
# upstream  https://github.com/원본소유자/저장소.git (fetch, push)

# 원본의 최신 변경 가져오기
git fetch upstream
git merge upstream/main

# 본인 Fork에도 반영
git push origin main
```

---

## 7.5 코드 리뷰 문화

### 좋은 리뷰 코멘트
- ❌ "이 코드 별로네"
- ✅ "여기서 변수명을 더 명확하게 하면 가독성이 좋아질 것 같아요. 예: `data` → `userList`"

### PR 작성 시 체크리스트
- [ ] 제목이 명확한가?
- [ ] 변경 내용을 설명했는가?
- [ ] 관련 이슈를 링크했는가? (`#123` 형식)
- [ ] 테스트했는가?
- [ ] 스크린샷이 필요한가? (UI 변경 시)

### GitHub PR 단축 기능
- `Fixes #123`: PR 머지 시 이슈 #123 자동 종료
- `Co-authored-by`: 공동 작성자 표시
- 리뷰어 지정 (Reviewers)
- 라벨 추가 (bug, feature, docs 등)

---

## 7.6 충돌이 생긴 PR 해결

### [실습 7-4] PR 충돌 시나리오

**상황**: PR을 보낸 사이 main에 다른 변경이 생겨 충돌 발생

```bash
# 본인 브랜치
git switch feature/my-work

# main 최신 가져오기
git fetch origin

# main의 변경을 본인 브랜치에 병합
git merge origin/main

# 충돌 발생 시 해결 → add → commit
# (5교시 충돌 해결 방법과 동일)

# 다시 push
git push
```

### [미니 과제 7] 협업 시뮬레이션

짝과 함께 다음을 수행:
1. A가 저장소 만들고 README.md 작성
2. B를 협업자로 초대
3. A와 B가 각각 다른 브랜치에서 작업
4. 둘 다 PR 생성
5. 서로의 PR 리뷰 후 머지
6. 충돌 발생 시 해결

---

# 🕐 8교시. 실전 활용 & 미니 프로젝트 (50분)

## 학습 목표
- stash, rebase, tag를 활용할 수 있다
- 자주 발생하는 문제를 해결할 수 있다
- 종합 미니 프로젝트를 완수한다

## 8.1 git stash - 임시 저장

### 상황
지금 작업 중인데 갑자기 다른 브랜치에서 급한 수정을 해야 할 때

### [실습 8-1] stash 사용하기

```bash
# 새 실습 폴더
cd ~/Desktop
mkdir stash-practice
cd stash-practice
git init

# 초기 파일과 커밋
echo "원본" > work.txt
git add .
git commit -m "초기 커밋"

# 작업 중 (커밋 안 함)
echo "작업 중인 내용" >> work.txt
git status
# → modified: work.txt

# stash로 임시 저장
git stash
git status
# → clean (작업 사라짐)

cat work.txt
# → 원본만 남음

# stash 목록
git stash list
# → stash@{0}: WIP on main: ...

# 다른 작업 수행 (예시)
echo "급한 작업" > urgent.txt
git add .
git commit -m "급한 수정"

# 다시 stash 꺼내기
git stash pop
# → 작업 내용 복구됨

cat work.txt
git status
```

### stash 주요 명령어

```bash
git stash                  # 임시 저장
git stash save "메시지"     # 메시지와 함께 저장
git stash list             # 목록 보기
git stash show stash@{0}   # 내용 보기
git stash pop              # 가장 최근 stash 꺼내기 (목록에서 삭제)
git stash apply stash@{0}  # 적용만 (목록 유지)
git stash drop stash@{0}   # 특정 stash 삭제
git stash clear            # 전체 삭제
```

---

## 8.2 git tag - 버전 표시

### 태그란?
특정 커밋에 **버전 라벨**을 붙이는 기능 (예: v1.0.0)

### [실습 8-2] 태그 활용

```bash
# 커밋 몇 개 만들기
echo "v1" > version.md
git add . && git commit -m "feat: 초기 기능"

echo "v1.1 fix" >> version.md
git add . && git commit -m "fix: 버그 수정"

# 가벼운 태그 (lightweight tag)
git tag v1.0.0

# 주석 태그 (annotated tag, 권장)
git tag -a v1.1.0 -m "버전 1.1.0 릴리스"

# 태그 목록
git tag

# 특정 태그 정보
git show v1.1.0

# 원격에 태그 푸시
git push origin v1.1.0

# 모든 태그 푸시
git push origin --tags

# 태그 삭제
git tag -d v1.0.0
git push origin --delete v1.0.0
```

### Semantic Versioning (시맨틱 버저닝)

```
v 1 . 2 . 3
  │   │   └─ PATCH: 버그 수정
  │   └───── MINOR: 기능 추가 (호환 유지)
  └───────── MAJOR: 큰 변경 (호환 깨짐)
```

---

## 8.3 git rebase - 이력 정리

### merge vs rebase

```
[원본]
A---B---C  (main)
     \
      D---E  (feature)

[merge 결과]
A---B---C---F  (main)
     \     /
      D---E

[rebase 결과]
A---B---C---D'---E'  (main)
```

| 방식 | 장점 | 단점 |
|:---|:---|:---|
| merge | 이력 그대로 보존, 안전 | 그래프 복잡 |
| rebase | 깔끔한 직선 이력 | 이력 변경 (위험) |

### [실습 8-3] rebase 시도

```bash
# 새 폴더
cd ~/Desktop
mkdir rebase-practice
cd rebase-practice
git init

echo "main 1" > file.txt
git add . && git commit -m "main: v1"
echo "main 2" >> file.txt
git add . && git commit -m "main: v2"

# feature 브랜치
git switch -c feature
echo "feature 1" >> file.txt
git add . && git commit -m "feature: f1"
echo "feature 2" >> file.txt
git add . && git commit -m "feature: f2"

# main에 추가 커밋
git switch main
echo "main 3" >> file.txt
git add . && git commit -m "main: v3"

# 현재 그래프 확인
git log --oneline --all --graph

# feature를 main 기준으로 rebase
git switch feature
git rebase main
# 충돌 시: 해결 후 git add → git rebase --continue

# 그래프 확인 - 직선이 됨
git log --oneline --all --graph
```

> ⚠️ **rebase 황금률**: 이미 push해서 다른 사람이 받아간 커밋은 절대 rebase하지 말 것!

---

## 8.4 자주 발생하는 문제와 해결

### 문제 1: 커밋 메시지 잘못 작성
```bash
# 가장 최근 커밋 메시지 수정
git commit --amend -m "수정된 메시지"
```

### 문제 2: 커밋에 파일 빠뜨림
```bash
# 빠진 파일 추가
git add forgot-file.txt
git commit --amend --no-edit
```

### 문제 3: 잘못된 브랜치에 커밋함
```bash
# 1. 최근 커밋 해시 저장
git log --oneline  # 예: abc1234

# 2. 잘못 커밋한 브랜치에서 되돌리기
git reset --hard HEAD~1

# 3. 올바른 브랜치로 이동
git switch correct-branch

# 4. 커밋 가져오기
git cherry-pick abc1234
```

### 문제 4: push 했는데 너무 큰 파일이 있어서 거부됨
```bash
# .gitignore에 추가하고
echo "big-file.zip" >> .gitignore

# 커밋에서 파일 제거
git rm --cached big-file.zip
git commit -m "큰 파일 제외"
git push
```

### 문제 5: 원격 변경과 충돌해서 push 안 됨
```bash
# 1. 원격 변경 받아오기
git pull origin main
# 충돌 시 해결

# 2. 다시 push
git push
```

---

## 8.5 [종합 미니 프로젝트] 개인 블로그 만들기

### 프로젝트 개요
- **목표**: GitHub Pages로 정적 블로그 배포
- **시간**: 30분
- **결과물**: 인터넷에 공개되는 본인 웹페이지

### 단계별 실습

**1단계: 저장소 생성**
1. GitHub에서 새 저장소 생성
2. 이름: `사용자명.github.io` (정확히 본인 사용자명!)
3. Public 선택, README 추가
4. 로컬에 클론
```bash
cd ~/Desktop
git clone https://github.com/사용자명/사용자명.github.io.git
cd 사용자명.github.io
```

**2단계: 기본 페이지 만들기**

`index.html` 생성:
```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>나의 블로그</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <h1>안녕하세요, 홍길동입니다 👋</h1>
        <nav>
            <a href="index.html">홈</a>
            <a href="about.html">소개</a>
        </nav>
    </header>
    <main>
        <article>
            <h2>최근 글</h2>
            <p>Git 8시간 마스터하기!</p>
        </article>
    </main>
    <footer>
        <p>© 2024 홍길동</p>
    </footer>
</body>
</html>
```

`style.css` 생성:
```css
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: 'Segoe UI', sans-serif; line-height: 1.6; padding: 20px; }
header { border-bottom: 2px solid #333; padding-bottom: 20px; margin-bottom: 20px; }
h1 { color: #2c3e50; }
nav a { margin-right: 15px; color: #3498db; text-decoration: none; }
main { max-width: 800px; margin: 0 auto; }
footer { text-align: center; margin-top: 40px; color: #777; }
```

**3단계: 브랜치로 기능 추가**
```bash
# feature 브랜치 생성
git switch -c feature/about-page

# about.html 작성
```

`about.html` 생성:
```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>소개 - 나의 블로그</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <h1>나에 대하여</h1>
        <nav>
            <a href="index.html">홈</a>
            <a href="about.html">소개</a>
        </nav>
    </header>
    <main>
        <p>Git을 배우고 있는 학습자입니다.</p>
        <h2>관심사</h2>
        <ul>
            <li>웹 개발</li>
            <li>오픈소스 기여</li>
        </ul>
    </main>
</body>
</html>
```

```bash
# 커밋
git add .
git commit -m "feat: about 페이지 추가"

# main으로 병합
git switch main
git merge feature/about-page

# 푸시
git push
```

**4단계: GitHub Pages 활성화**
1. GitHub 저장소 → **Settings** → **Pages**
2. **Source**: `Deploy from a branch`
3. **Branch**: `main` / `/ (root)` 선택
4. **Save** 클릭
5. 1-2분 후 `https://사용자명.github.io` 에서 확인!

**5단계: 태그 달기**
```bash
git tag -a v1.0.0 -m "블로그 첫 배포"
git push origin v1.0.0
```

---

## 8.6 마무리: Git 명령어 치트시트

### 일상에서 가장 자주 쓰는 명령어 (Top 10)

```bash
git status                  # 상태 확인 (가장 많이 씀!)
git add .                   # 전체 스테이징
git commit -m "메시지"       # 커밋
git push                    # 원격으로 보내기
git pull                    # 원격에서 받기
git log --oneline           # 이력 한 줄로
git switch 브랜치명          # 브랜치 이동
git switch -c 브랜치명       # 브랜치 생성+이동
git merge 브랜치명           # 병합
git diff                    # 변경 사항 보기
```

### 응급 상황 대처

```bash
# 어디까지 했는지 모르겠다
git status
git log --oneline -10

# 마지막 커밋 메시지 잘못 썼다
git commit --amend -m "올바른 메시지"

# 방금 add 한 거 취소
git restore --staged 파일

# 수정한 거 취소 (주의!)
git restore 파일

# 마지막 커밋 취소 (이력 유지)
git revert HEAD

# 작업 중인 거 잠시 치워두기
git stash
```

### 협업 워크플로우 요약

```bash
# 1. 최신 상태 받기
git switch main
git pull

# 2. 작업 브랜치 만들기
git switch -c feature/내작업

# 3. 작업 & 커밋 반복
git add .
git commit -m "작업 내용"

# 4. 원격에 푸시
git push -u origin feature/내작업

# 5. GitHub에서 PR 생성

# 6. 리뷰 & 머지

# 7. 로컬 브랜치 정리
git switch main
git pull
git branch -d feature/내작업
```

---

## 🎓 수료 체크리스트

다음 항목을 모두 직접 할 수 있다면 Git 기초 마스터!

### 1단계: 로컬
- [ ] Git 설치 및 초기 설정
- [ ] 저장소 생성 (`git init`)
- [ ] 파일 스테이징 (`git add`)
- [ ] 커밋 작성 (`git commit`)
- [ ] 이력 확인 (`git log`)
- [ ] 변경 사항 확인 (`git diff`)
- [ ] .gitignore 작성

### 2단계: 브랜치
- [ ] 브랜치 생성 (`git switch -c`)
- [ ] 브랜치 이동 (`git switch`)
- [ ] 브랜치 병합 (`git merge`)
- [ ] 충돌 해결
- [ ] 브랜치 삭제 (`git branch -d`)

### 3단계: 원격
- [ ] GitHub 저장소 생성
- [ ] 원격 연결 (`git remote add`)
- [ ] 푸시 (`git push`)
- [ ] 풀 (`git pull`)
- [ ] 클론 (`git clone`)

### 4단계: 협업
- [ ] Fork & Pull Request
- [ ] 코드 리뷰
- [ ] 협업 시 충돌 해결
- [ ] PR 머지

### 5단계: 활용
- [ ] git stash 사용
- [ ] git tag 작성
- [ ] git revert / reset 적절히 사용
- [ ] GitHub Pages 배포

---

## 📚 추가 학습 자료

### 공식 문서
- [Git 공식 문서](https://git-scm.com/doc) - 한글 지원
- [Pro Git 책](https://git-scm.com/book/ko/v2) - 무료, 한글판

### 인터랙티브 학습
- [Learn Git Branching](https://learngitbranching.js.org/?locale=ko) - 시각적 학습
- [GitHub Skills](https://skills.github.com/) - GitHub 공식 튜토리얼

### 실전 팁
- [Conventional Commits](https://www.conventionalcommits.org/ko/v1.0.0/) - 커밋 메시지 규칙
- [Git Flow 전략](https://nvie.com/posts/a-successful-git-branching-model/)

### Cheat Sheet
- [GitHub Cheat Sheet (한글)](https://training.github.com/downloads/ko/github-git-cheat-sheet/)

---

## 💬 강사 노트 (실습 진행 팁)

### 시간 배분
- 각 교시: 강의 10분 + 실습 35분 + Q&A 5분 권장
- 학습자 수준에 따라 8교시 미니 프로젝트는 과제로 대체 가능

### 실습 환경 점검 (1교시 전)
- [ ] 인터넷 연결 확인
- [ ] Windows 11 환경 통일
- [ ] 관리자 권한 확인 (설치용)
- [ ] GitHub 가입 가능한 이메일 준비

### 자주 발생하는 문제
1. **Git Bash가 안 열림** → 재설치 또는 PATH 확인
2. **push 시 인증 실패** → Personal Access Token 발급 안내
3. **충돌 메시지에 당황** → VS Code 활용법 시연
4. **Vim 빠져나오기** → `ESC` → `:wq` 반복 강조

### 평가 방법 (예시)
- 실습 과제 제출 (각 교시 미니 과제) - 60%
- 최종 미니 프로젝트 (GitHub Pages 배포) - 40%

---

**🎉 8시간 Git 실습 과정 완료!**

> "Git은 머리로 외우는 것이 아니라, **손으로 익히는** 도구입니다.  
> 매일 작은 프로젝트라도 git을 사용하면서 자연스럽게 익숙해지세요." 🚀
