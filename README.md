# ai-course-references

**디지털노마드연구소 · AI 학습 레퍼런스 저장소**

AI 업무 활용, 바이브코딩, n8n 자동화, 음성 AI, LangChain 에이전트까지 직접 공부하면서 참고하려고 모아 둔 강의 자료 9종입니다.
주제별로 폴더를 나눴고, 폴더마다 `README.md`에 무엇이 들어 있는지 정리해 두었습니다.
원본 과정 폴더 10개는 모두 `source/` 아래에 있고, 문제은행과 빌드 결과물은 `develop/`(`develop/dist/`)에 있습니다.

> 🔒 **비공개 레포로만 사용합니다.** 외부 강의 자료를 개인 학습용으로 정리한 저장소라 공개하거나 재배포하지 않습니다.

---

## 📚 구성

| 단계 | 폴더 | 주제 | 주요 형식 | 파일 |
|---|---|---|---|---|
| 1 | [`source/01-ai-work/ai-automation`](source/01-ai-work/ai-automation) | 생성형 AI + 노코드 업무 자동화 개론 (모듈 1~3) | md | 3 |
| 1 | [`source/01-ai-work/ai-excel`](source/01-ai-work/ai-excel) | ChatGPT·Gemini로 엑셀 함수·분석·정제·VBA | md, xlsx | 4 |
| 1 | [`source/01-ai-work/claude-for-educators`](source/01-ai-work/claude-for-educators) | Claude로 수업 설계 → 평가 문항 → AI 활용 교수법 (3일) | md, docx, html | 12 |
| 2 | [`source/02-dev-basics/git`](source/02-dev-basics/git) | Git·GitHub 입문 8교시 실습 | md, pptx | 2 |
| 2 | [`source/02-dev-basics/vibe-coding`](source/02-dev-basics/vibe-coding) | 비개발자 바이브코딩 20H + Colab 노트북 8개 | pptx, md, ipynb | 15 |
| 3 | [`source/03-n8n-automation/n8n-edu-agent`](source/03-n8n-automation/n8n-edu-agent) | n8n + AI로 교육 업무 자동화 (7교시, 실습 1~19) | md, json | 20 |
| 3 | [`source/03-n8n-automation/n8n-blog`](source/03-n8n-automation/n8n-blog) | 셀프호스팅 n8n + WordPress 블로그 자동 발행 | md, json | 5 |
| 4 | [`source/04-voice-ai`](source/04-voice-ai) | 음성 AI: 오디오 기초 → 주파수 → 전처리 → KWS → ASR → Whisper → 추론 최적화·스트리밍 (Day 1~8) | pptx/pdf, ipynb, html | 43 |
| 5 | [`source/05-langchain-agent`](source/05-langchain-agent) | LangChain LCEL → RAG → Gradio 챗봇 → Whisper 음성 RAG → LangGraph (14일차) | ipynb, mp3 | 56 |
| 6 | [`source/06-ai-openVino`](source/06-ai-openVino) | 엣지 AI 비전: 리눅스 → 파이썬 → OpenCV → OpenVINO 추론·최적화·디바이스 비교 | pdf | 8 |
| 7 | [`source/07-NEPES_physicalAI_자율주행자동차`](source/07-NEPES_physicalAI_자율주행자동차) | Physical AI 5일: Jetson → LLM·VLM → OpenCV·MediaPipe·ROS 2 → Pseudo-VLA → VLA | pdf, ipynb | 108 |

## 🧭 추천 학습 순서

```
01-ai-work (프롬프트·문서·엑셀)  →  02-dev-basics (Git → 바이브코딩)
        →  03-n8n-automation (교육 업무 → 블로그 자동화)  →  04-voice-ai (Day 1 → 7)
        →  05-langchain-agent (day01 → 14)
        →  06-ai-openVino (리눅스 → 파이썬 → OpenCV → OpenVINO)  →  07 Physical AI (Jetson → VLA)
```

> `source/04-voice-ai`의 Whisper(D7)와 `source/05-langchain-agent`의 음성 RAG(day13)는 이어서 보면 좋습니다.

- 노트북(`.ipynb`)은 Google Colab에서 열면 됩니다. `source/04-voice-ai`는 **T4 GPU** 런타임을 권장합니다.
- `source/05-langchain-agent`는 OpenAI API 키가 필요합니다. Colab 왼쪽 🔑 **보안 비밀**에 `OPENAI_API_KEY`로 등록하세요.
- `source/04-voice-ai/dayNN`의 `animation.html`, `worksheet.html`은 내려받아 브라우저로 열면 바로 동작합니다. 노트북·슬라이드의 링크는 같은 폴더 파일을 가리킵니다.
- n8n 워크플로(`.json`)는 n8n에서 **Import from File**로 불러온 뒤, 아래 자리표시자를 내 값으로 바꾸세요.

## 🎯 문제은행 플랫폼 (개발 중)

강의자료를 **문제은행**으로 바꿔 공부하는 시스템입니다. 최종 목표는 PDF·TXT·Word 문서를 넣으면 자동으로 분석해 문제은행을 만드는 것입니다.

| 폴더 | 내용 |
|---|---|
| [`plan/`](plan) | 기존 자산 분석 · 플랫폼 개념 · 기획서 · 출제 기준 |
| [`design/`](design) | 디자인 시스템 · 토큰(`tokens.css`) · 공용 컴포넌트(`components.css`, `icons.svg`) · 공용 스크립트(`qb-core/progress/voice.js`) · 와이어프레임 · 벤치마킹 메모 |
| [`develop/`](develop) | 개발서 · 수집기(`ingest.py`) · 스키마 · 출제 프롬프트 · 엔진 · 검증/빌드 스크립트 |

**진입 흐름**: [`develop/dist/index.html`](develop/dist/index.html)(랜딩) → [`login.html`](develop/dist/login.html)(체험 로그인) → [`dashboard.html`](develop/dist/dashboard.html)(과정별 목록·진행률·남은 오답·학습 기록) → 각 문제은행. 문제은행의 '과정 목록' 링크도 대시보드로 연결됩니다.

**여는 법**
- `develop/dist/index.html`을 더블클릭하면 됩니다(서버 불필요). 로그인은 이름만 받는 체험용이고 비밀번호는 저장하지 않습니다.
- 말로 보기 번호 고르기는 **Chrome·Edge + 인터넷 연결**에서만 됩니다. 오디오가 브라우저 회사의 음성 인식 서버로 전송되며, `file://`로 열면 마이크 권한을 다시 물을 수 있습니다.
- 랜딩 히어로의 예시 문항 카드 3장은 방문할 때마다 순서를 섞어 4초마다 넘어갑니다. 앞 카드는 클릭이나 숫자키로 바로 풀 수 있습니다.
- 예전 북마크 `index.html#04`는 `dashboard.html#04`로 넘어갑니다.

| 단계 | 과정 | 문제은행 | 문항 | 페이지 |
|---|---|---|---|---|
| 01 | AI 업무 자동화 | 모듈1 · AI와 업무 자동화 개론 | 6탭 · 60 | [`module1.html`](develop/dist/01-ai-work/ai-automation/module1.html) |
| 01 | AI 업무 자동화 | 모듈2 · 문서·커뮤니케이션 업무 효율화 | 5탭 · 50 | [`module2.html`](develop/dist/01-ai-work/ai-automation/module2.html) |
| 01 | AI 업무 자동화 | 모듈3 · 스프레드시트·데이터 작업 자동화 | 6탭 · 60 | [`module3.html`](develop/dist/01-ai-work/ai-automation/module3.html) |
| 01 | AI 엑셀 실무 | AI 엑셀 실무 · ChatGPT·Gemini로 하는 비즈니스 엑셀 | 8탭 · 80 | [`ai-excel.html`](develop/dist/01-ai-work/ai-excel/ai-excel.html) |
| 01 | Claude 활용 교육 | Claude 활용 교육 1일차 · 수업 목표 구조화 | 6탭 · 60 | [`day1.html`](develop/dist/01-ai-work/claude-for-educators/day1.html) |
| 01 | Claude 활용 교육 | Claude 활용 교육 2일차 · 평가 문항 설계 | 5탭 · 50 | [`day2.html`](develop/dist/01-ai-work/claude-for-educators/day2.html) |
| 01 | Claude 활용 교육 | Claude 활용 교육 3일차 · AI 활용 교수 프로토콜 | 6탭 · 60 | [`day3.html`](develop/dist/01-ai-work/claude-for-educators/day3.html) |
| 02 | Git·GitHub | Git · GitHub 입문 · 8교시 실습 | 8탭 · 80 | [`git.html`](develop/dist/02-dev-basics/git/git.html) |
| 02 | 바이브코딩 | 바이브코딩 Day 1 · AI와 일하는 법 & AI 기초 | 4탭 · 40 | [`day1.html`](develop/dist/02-dev-basics/vibe-coding/day1.html) |
| 02 | 바이브코딩 | 바이브코딩 Day 2 · 프롬프트 엔지니어링 마스터 | 7탭 · 70 | [`day2.html`](develop/dist/02-dev-basics/vibe-coding/day2.html) |
| 02 | 바이브코딩 | 바이브코딩 Day 3 · AI 기반 바이브 코딩 실전 | 5탭 · 50 | [`day3.html`](develop/dist/02-dev-basics/vibe-coding/day3.html) |
| 02 | 바이브코딩 | 바이브코딩 Day 4 · 결과물 공유 & 업무 활용 전략 | 6탭 · 60 | [`day4.html`](develop/dist/02-dev-basics/vibe-coding/day4.html) |
| 02 | 바이브코딩 | 바이브코딩 기본 노트북 · 세션 0~4 | 5탭 · 50 | [`nb-basic.html`](develop/dist/02-dev-basics/vibe-coding/nb-basic.html) |
| 02 | 바이브코딩 | 바이브코딩 중급 노트북 · Claude Code·시뮬레이터·사다리게임 | 4탭 · 40 | [`nb-intermediate.html`](develop/dist/02-dev-basics/vibe-coding/nb-intermediate.html) |
| 02 | 바이브코딩 | 바이브코딩 교재 · AI 바이브 코딩 실전 과정 20H | 7탭 · 70 | [`textbook.html`](develop/dist/02-dev-basics/vibe-coding/textbook.html) |
| 02 | 바이브코딩 | Transformer 완전 해부 | 3탭 · 30 | [`transformer.html`](develop/dist/02-dev-basics/vibe-coding/transformer.html) |
| 03 | n8n 교육 자동화 | n8n 교육 자동화 1교시 · n8n 소개와 환경 구축 | 4탭 · 40 | [`period1.html`](develop/dist/03-n8n-automation/n8n-edu-agent/period1.html) |
| 03 | n8n 교육 자동화 | n8n 교육 자동화 2교시 · 핵심 노드와 데이터 연동 | 5탭 · 50 | [`period2.html`](develop/dist/03-n8n-automation/n8n-edu-agent/period2.html) |
| 03 | n8n 교육 자동화 | n8n 교육 자동화 3교시 · 교육서비스업 자동화 ① | 4탭 · 40 | [`period3.html`](develop/dist/03-n8n-automation/n8n-edu-agent/period3.html) |
| 03 | n8n 교육 자동화 | n8n 교육 자동화 4교시 · 교육서비스업 자동화 ② | 4탭 · 40 | [`period4.html`](develop/dist/03-n8n-automation/n8n-edu-agent/period4.html) |
| 03 | n8n 교육 자동화 | n8n 교육 자동화 5교시 · AI API 연동 & 프롬프트 | 6탭 · 60 | [`period5.html`](develop/dist/03-n8n-automation/n8n-edu-agent/period5.html) |
| 03 | n8n 교육 자동화 | n8n 교육 자동화 6교시 · AI 기반 교육서비스 자동화 | 6탭 · 60 | [`period6.html`](develop/dist/03-n8n-automation/n8n-edu-agent/period6.html) |
| 03 | n8n 교육 자동화 | n8n 교육 자동화 7교시 · 멀티미디어 AI 활용 | 6탭 · 60 | [`period7.html`](develop/dist/03-n8n-automation/n8n-edu-agent/period7.html) |
| 03 | n8n 블로그 | n8n 블로그 자동 발행 · 패션 블로그 자동화 4시간 | 10탭 · 100 | [`n8n-blog.html`](develop/dist/03-n8n-automation/n8n-blog/n8n-blog.html) |
| 04 | 음성 AI | 음성 AI Day 1 · 음성 AI 첫걸음 | 1탭 · 15 | [`day01.html`](develop/dist/04-voice-ai/day01.html) |
| 04 | 음성 AI | 음성 AI Day 2 · 디지털 오디오 기초 | 4탭 · 40 | [`day02.html`](develop/dist/04-voice-ai/day02.html) |
| 04 | 음성 AI | 음성 AI Day 3 · 주파수 분석 | 4탭 · 40 | [`day03.html`](develop/dist/04-voice-ai/day03.html) |
| 04 | 음성 AI | 음성 AI Day 4 · 오디오 전처리 | 4탭 · 40 | [`day04.html`](develop/dist/04-voice-ai/day04.html) |
| 04 | 음성 AI | 음성 AI Day 5 · 딥러닝 오디오 분류 | 4탭 · 40 | [`day05.html`](develop/dist/04-voice-ai/day05.html) |
| 04 | 음성 AI | 음성 AI Day 6 · ASR 원리 | 4탭 · 40 | [`day06.html`](develop/dist/04-voice-ai/day06.html) |
| 04 | 음성 AI | 음성 AI Day 7 · Whisper 심층 분석 | 4탭 · 40 | [`day07.html`](develop/dist/04-voice-ai/day07.html) |
| 04 | 음성 AI | 음성 AI Day 8 · 추론 최적화 & 스트리밍 | 4탭 · 40 | [`day08.html`](develop/dist/04-voice-ai/day08.html) |
| 06 | AI 비전 · OpenVINO | 리눅스 실습 노트 · 우분투로 배우는 리눅스 기본 | 6탭 · 60 | [`01-linux.html`](develop/dist/06-ai-openVino/01-linux.html) |
| 06 | AI 비전 · OpenVINO | 파이썬 기초부터 이미지처리까지 | 10탭 · 100 | [`02-python.html`](develop/dist/06-ai-openVino/02-python.html) |
| 06 | AI 비전 · OpenVINO | 우분투 개발 환경 구축 · Python 3.11 · VS Code · OpenVINO | 4탭 · 40 | [`03-dev-env.html`](develop/dist/06-ai-openVino/03-dev-env.html) |
| 06 | AI 비전 · OpenVINO | OpenVINO란 무엇인가 | 3탭 · 30 | [`04-what-is-openvino.html`](develop/dist/06-ai-openVino/04-what-is-openvino.html) |
| 06 | AI 비전 · OpenVINO | OpenCV · 컴퓨터 비전 기초부터 객체 검출까지 | 9탭 · 90 | [`05-opencv.html`](develop/dist/06-ai-openVino/05-opencv.html) |
| 06 | AI 비전 · OpenVINO | OpenVINO 심화와 비전 AI 프로젝트 | 8탭 · 80 | [`06-runtime.html`](develop/dist/06-ai-openVino/06-runtime.html) |
| 06 | AI 비전 · OpenVINO | CPU · GPU · NPU 속도 비교 | 3탭 · 30 | [`07-device-benchmark.html`](develop/dist/06-ai-openVino/07-device-benchmark.html) |
| 07 | Physical AI | Physical AI 1일차 · Jetson · Ubuntu · 실습 환경 | 9탭 · 90 | [`01-jetson-ubuntu.html`](develop/dist/07-physical-ai/01-jetson-ubuntu.html) |
| 07 | Physical AI | Physical AI · Python 기초와 자료구조 | 5탭 · 50 | [`02-python.html`](develop/dist/07-physical-ai/02-python.html) |
| 07 | Physical AI | Physical AI · C++ 기초 · 메모리 · STL · CMake | 9탭 · 90 | [`03-cpp.html`](develop/dist/07-physical-ai/03-cpp.html) |
| 07 | Physical AI | Physical AI 2일차 · LLM 학습 원리 (RNN·LSTM·Seq2Seq·Transformer) | 8탭 · 80 | [`04-llm-training.html`](develop/dist/07-physical-ai/04-llm-training.html) |
| 07 | Physical AI | Physical AI 2일차 · LLM 활용 (프롬프트·Tool·RAG·에이전트) | 6탭 · 60 | [`05-llm-apps.html`](develop/dist/07-physical-ai/05-llm-apps.html) |
| 07 | Physical AI | Physical AI 2일차 · VLM (이미지 질문·카메라 기록·구조화 결과) | 5탭 · 50 | [`06-vlm.html`](develop/dist/07-physical-ai/06-vlm.html) |
| 07 | Physical AI | Physical AI 3일차 · OpenCV · MediaPipe | 7탭 · 70 | [`07-opencv-mediapipe.html`](develop/dist/07-physical-ai/07-opencv-mediapipe.html) |
| 07 | Physical AI | Physical AI 3일차 · ROS 2 (노드·토픽·turtlesim·카메라·launch) | 6탭 · 60 | [`08-ros.html`](develop/dist/07-physical-ai/08-ros.html) |
| 07 | Physical AI | Physical AI 4일차 · 좌표 기반 Pseudo-VLA | 9탭 · 90 | [`09-pseudo-vla.html`](develop/dist/07-physical-ai/09-pseudo-vla.html) |
| 07 | Physical AI | Physical AI 5일차 · 학습된 VLA 정책과 시뮬레이션 | 10탭 · 100 | [`10-vla.html`](develop/dist/07-physical-ai/10-vla.html) |

합계 **79개 · 518탭 · 5,185문항** (05·08·09·10 과정 은행은 대시보드에서 볼 수 있습니다). 04-voice-ai는 기존 워크시트 구성(Day1 15문항, Day2~8 4교시×10)을 그대로 옮겼습니다.

- **학습 모드**: 탭별 10문항 채점, 해설과 자료 위치, 종합 결과와 결과 코드.
- **게임 모드**: 탭 하나를 채점하면 열립니다. 문항마다 10~15초 타이머가 있고 콤보 점수와 순위표가 있습니다.
- **말로 고르기·문제 읽기**: 마이크 버튼으로 "2번", "오"처럼 말하면 선택됩니다(Chrome·Edge). '문제 읽기'는 브라우저 음성 합성을 씁니다.
- **오답노트·해설지**: 틀린 문항이 쌓이고, 다시 풀어 맞히면 '극복'으로 표시됩니다. 인쇄할 수 있습니다.
- 새 자료 추가: [`develop/개발서.md`](develop/개발서.md) §3 → `python develop/validate.py` → `python develop/build.py`

## 🔑 직접 채워야 하는 값

| 자리표시자 | 위치 | 넣을 값 |
|---|---|---|
| `<YOUR_SHEET_ID>`, `<YOUR_DOC_ID>` | `n8n-edu-agent/실습5·6·8*.json` | 내 Google 시트 ID (또는 노드에서 목록 선택) |
| `<YOUR_DRIVE_FOLDER_ID>` | `n8n-edu-agent/실습8_자료자동배포.json` | 내 Google Drive 폴더 |
| `<YOUR_PUBLIC_FILE_URL>` | `n8n-edu-agent/비디오분석.json` | `video_sample.mp4`를 올린 공개 주소 (Supabase Storage 등) |
| `<YOUR_NGROK_AUTHTOKEN>`, `<YOUR-STATIC-DOMAIN>` | `n8n-edu-agent/n8n_로컬호스트설정.txt` | 내 ngrok 토큰·고정 도메인 |

## 🔄 원본 업데이트 반영하기

원본 자료가 갱신되면 아래 명령으로 바뀐 파일만 받아 같은 정리 규칙을 적용합니다.

```bash
pip install pymupdf                 # 처음 한 번 (PDF 정리용)
python3 tools/sync.py               # 무엇이 바뀌었는지 확인만
python3 tools/sync.py --apply       # 반영 (바뀐 파일만 정리해서 복사, CHANGELOG 기록)
python3 tools/check.py              # 정리 누락 검사 → "✓ 남은 표기 없음"이면 커밋
git add -A && git commit -m "sync: 원본 업데이트 반영" && git push
```

| 파일 | 역할 |
|---|---|
| `tools/sources.json` | 원본 저장소 ↔ 폴더 대응표, 마지막으로 반영한 커밋 |
| `tools/manifest.json` | 원본 파일별 해시 (바뀐 파일만 골라내는 기준) |
| `tools/rules.py` | 정리 규칙 — 규칙을 바꾸려면 이 파일만 수정 |
| `tools/clean.py` | md·json·ipynb·html·pptx·docx·xlsx·pdf 정리 엔진 |
| `tools/check.py` | 원본 표기·토큰·문서 ID가 남았는지 검사 |
| `tools/sync.py` | 원본 최신본 받기 → 변경 비교 → 정리 → 반영 |

> `source/05-langchain-agent`는 업로드한 zip에서 가져와 원본 저장소가 없으므로 자동 동기화 대상이 아닙니다. 새 버전 zip을 받으면 폴더에 풀고 `python3 tools/clean.py source/05-langchain-agent --prefix source/05-langchain-agent`로 정리하세요.
>
> 폴더별 `README.md`는 이 레포에서 쓴 정리 문서라 동기화할 때 덮어쓰지 않습니다. 원본에 README가 생기면 `README_원본.md`로 저장됩니다.

## 🧹 레포에 넣으면서 정리한 내용

- 원 출처 기관명·강사명·연락처·온라인 주소 → 디지털노마드연구소 표기 또는 이 레포 안의 경로로 변경
- 슬라이드·노트북의 온라인 애니메이션/워크시트 링크 → 같은 폴더의 로컬 파일 링크
- Whisper 고유명사 예문(D7)의 기관명 → `노마드랩 연구소` (오인식 예시까지 같은 단어로 통일)
- ngrok 토큰·고정 도메인, Google 시트·드라이브 ID, 하드코딩된 이메일, 노트북 출력에 찍힌 API 키 → 자리표시자
- pptx·docx·xlsx 문서 속성(작성자·마지막 수정자) → 디지털노마드연구소
- CP949 텍스트 파일 → UTF-8

자세한 이력은 [`CHANGELOG.md`](CHANGELOG.md)를 보세요.

---

<sub>디지털노마드연구소 · writer@nomadaifactory.com</sub>
