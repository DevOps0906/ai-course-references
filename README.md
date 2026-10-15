# ai-course-references

**디지털노마드연구소 · AI 학습 레퍼런스 저장소**

AI 업무 활용, 바이브코딩, n8n 자동화, 음성 AI, LangChain 에이전트까지 직접 공부하면서 참고하려고 모아 둔 강의 자료 9종입니다.
주제별로 폴더를 나눴고, 폴더마다 `README.md`에 무엇이 들어 있는지 정리해 두었습니다.

> 🔒 **비공개 레포로만 사용합니다.** 외부 강의 자료를 개인 학습용으로 정리한 저장소라 공개하거나 재배포하지 않습니다.

---

## 📚 구성

| 단계 | 폴더 | 주제 | 주요 형식 | 파일 |
|---|---|---|---|---|
| 1 | [`01-ai-work/ai-automation`](01-ai-work/ai-automation) | 생성형 AI + 노코드 업무 자동화 개론 (모듈 1~3) | md | 3 |
| 1 | [`01-ai-work/ai-excel`](01-ai-work/ai-excel) | ChatGPT·Gemini로 엑셀 함수·분석·정제·VBA | md, xlsx | 4 |
| 1 | [`01-ai-work/claude-for-educators`](01-ai-work/claude-for-educators) | Claude로 수업 설계 → 평가 문항 → AI 활용 교수법 (3일) | md, docx, html | 12 |
| 2 | [`02-dev-basics/git`](02-dev-basics/git) | Git·GitHub 입문 8교시 실습 | md, pptx | 2 |
| 2 | [`02-dev-basics/vibe-coding`](02-dev-basics/vibe-coding) | 비개발자 바이브코딩 20H + Colab 노트북 8개 | pptx, md, ipynb | 15 |
| 3 | [`03-n8n-automation/n8n-edu-agent`](03-n8n-automation/n8n-edu-agent) | n8n + AI로 교육 업무 자동화 (7교시, 실습 1~19) | md, json | 20 |
| 3 | [`03-n8n-automation/n8n-blog`](03-n8n-automation/n8n-blog) | 셀프호스팅 n8n + WordPress 블로그 자동 발행 | md, json | 5 |
| 4 | [`04-voice-ai`](04-voice-ai) | 음성 AI: 오디오 기초 → 주파수 → 전처리 → KWS → ASR → Whisper (Day 1~7) | pptx/pdf, ipynb, html | 37 |
| 5 | [`05-langchain-agent`](05-langchain-agent) | LangChain LCEL → RAG → Gradio 챗봇 → Whisper 음성 RAG → LangGraph (14일차) | ipynb, mp3 | 56 |

## 🧭 추천 학습 순서

```
01-ai-work (프롬프트·문서·엑셀)  →  02-dev-basics (Git → 바이브코딩)
        →  03-n8n-automation (교육 업무 → 블로그 자동화)  →  04-voice-ai (Day 1 → 7)
        →  05-langchain-agent (day01 → 14)
```

> `04-voice-ai`의 Whisper(D7)와 `05-langchain-agent`의 음성 RAG(day13)는 이어서 보면 좋습니다.

- 노트북(`.ipynb`)은 Google Colab에서 열면 됩니다. `04-voice-ai`는 **T4 GPU** 런타임을 권장합니다.
- `05-langchain-agent`는 OpenAI API 키가 필요합니다. Colab 왼쪽 🔑 **보안 비밀**에 `OPENAI_API_KEY`로 등록하세요.
- `04-voice-ai/dayNN`의 `animation.html`, `worksheet.html`은 내려받아 브라우저로 열면 바로 동작합니다. 노트북·슬라이드의 링크는 같은 폴더 파일을 가리킵니다.
- n8n 워크플로(`.json`)는 n8n에서 **Import from File**로 불러온 뒤, 아래 자리표시자를 내 값으로 바꾸세요.

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

> `05-langchain-agent`는 업로드한 zip에서 가져와 원본 저장소가 없으므로 자동 동기화 대상이 아닙니다. 새 버전 zip을 받으면 폴더에 풀고 `python3 tools/clean.py 05-langchain-agent --prefix 05-langchain-agent`로 정리하세요.
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
