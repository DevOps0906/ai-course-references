# n8n_agent-main — 교육서비스업 업무를 n8n과 AI(OpenAI·Claude·Gemini)로 자동화하는 2일(7교시) 실습 강의 자료
> ℹ️ 이 문서는 자료를 처음 분석할 때 작성한 정리본입니다. 레포에 넣으면서 원본 표기·연락처·토큰·문서 ID는 정리되었으니, 6장의 "노출" 항목은 **정리 전 원본 기준** 기록입니다.

> - **원본 버전**: 커밋 `63d5a05` 기준 (최신 여부는 `python3 tools/sync.py`로 확인)
> - **총 파일 수**: 20개 (zip 항목 21개 = 최상위 폴더 1 + 파일 20)
> - **용량**: 압축 약 10.7MB (11,190,855 B) / 압축 해제 약 12.6MB (13,249,649 B). 용량의 대부분은 샘플 미디어 3개(PNG 7.1MB, MP4 4.8MB, M4A 0.6MB)
> - **자료 성격**: 교시별 실습 가이드 Markdown 7개가 중심입니다(1~7교시, 실습 1~19). 여기에 n8n 워크플로 JSON 4개(실습 5·6·8 + 보너스 「비디오분석」), 실습용 더미 PDF 4개, 샘플 미디어 3개(이미지·오디오·비디오), 로컬 설치·GCP 설정 메모 txt 2개가 붙어 있습니다.

---

## 1. 한눈에 보기

| 항목 | 내용 |
|---|---|
| 주제 | n8n 워크플로 자동화 기초 → Google Workspace(Sheets·Gmail·Drive) 연동 → 교육서비스업(수강신청·리마인더·피드백·자료배포) 자동화 → AI API(OpenAI·Anthropic·Gemini) 연동 → 멀티미디어 AI(OCR·이미지 생성·PDF·음성·비디오) |
| 추정 대상 학습자 | 교육기관 운영자·교육 담당 실무자, n8n 입문 비개발 직장인(추정). 1교시 준비물이 "개인 노트북, Chrome, Google 계정"뿐이고 코드는 복사·붙여넣기 방식입니다 |
| 구성 | **Day 1**: 1~4교시(각 1시간), 실습 1~8 / **Day 2**: 5~7교시(각 1시간), 실습 9-A·9-B·9-C, 10~19. 가이드 기준 실습 21개 단위(9번이 A/B/C 3개). 8교시(팀 프로젝트)는 예고만 있고 자료 없음 |
| 워크플로 JSON | 4개: 실습5, 실습6, 실습8 + 가이드에 없는 「비디오분석」 |
| 자료 형식 | Markdown 가이드(.md), n8n 워크플로 export(.json), 더미 PDF, PNG/M4A/MP4 샘플, 메모 txt(CP949 인코딩) |
| 기준 버전 | 1~4교시는 **n8n Cloud**(`app.n8n.cloud`) 기준, 5~7교시는 "**n8n 버전: 2.12.3 기준**"이라고 명시 |
| 핵심 키워드 | Manual/Schedule/Webhook Trigger, Edit Fields(Set), IF/Switch, Code(JavaScript), Google Sheets(Read/Append/Search), Gmail(HTML), Google Drive Search, Respond to Webhook, OpenAI `gpt-4o-mini`, Anthropic `claude-sonnet-4-20250514`, Google Gemini `gemini-2.0-flash`/`gemini-2.5-flash`, Imagen, OCR, STT, Publish vs Save, Luxon `toFormat()` |

---

## 2. 폴더·파일 구성

```
n8n_agent-main/
├── 실습가이드_1교시_n8n소개_환경구축.md
├── 실습가이드_2교시_핵심노드_데이터연동.md
├── 실습가이드_3교시_교육서비스업자동화1.md
├── 실습가이드_4교시_교육서비스업자동화2.md
├── 실습가이드_5교시_AI_API연동.md
├── 실습가이드_6교시_AI기반자동화.md
├── 실습가이드_7교시_멀티미디어AI활용.md
├── 실습5_수강신청자동처리.json
├── 실습6_수업리마인더.json
├── 실습8_자료자동배포.json
├── 비디오분석.json
├── AI입문_1주차_강의자료.pdf
├── AI입문_실습가이드.pdf
├── 데이터분석_1주차_강의자료.pdf
├── 데이터분석_실습가이드.pdf
├── sample.png
├── audio_sample.m4a
├── video_sample.mp4
├── n8n_로컬호스트설정.txt
└── 구글 GCP client 정보 등록.txt
```

| 파일명 | 형식 | 크기 | 역할 |
|---|---|---|---|
| 실습가이드_1교시_n8n소개_환경구축.md | Markdown | 9.4KB | n8n Cloud 가입, 편집기 UI, 실습 1(Hello World), 노드 조작, 핵심 개념, 미니 퀴즈 |
| 실습가이드_2교시_핵심노드_데이터연동.md | Markdown | 12.9KB | Google OAuth, 실습 2~4(Sheets 읽기·쓰기, IF/Switch, 상태별 Gmail), 에러 디버깅 표 |
| 실습가이드_3교시_교육서비스업자동화1.md | Markdown | 9.6KB | 실습 5(Webhook 수강신청), 실습 6(Schedule 리마인더) |
| 실습가이드_4교시_교육서비스업자동화2.md | Markdown | 9.7KB | 실습 7(피드백 수집·Code 집계), 실습 8(Drive 자료 배포), Day 1 총정리, Day 2 과제 |
| 실습가이드_5교시_AI_API연동.md | Markdown | 21.0KB | n8n 2.x 변경점, 실습 9-A/B/C(OpenAI·Claude·Gemini 호출), 3대 모델 비교, 실습 10, 비용·보안 가이드 |
| 실습가이드_6교시_AI기반자동화.md | Markdown | 23.9KB | 실습 11~14(Q&A 봇, 피드백 AI 리포트, 콘텐츠 초안, 이메일 작성기), 프롬프트 설계 팁 |
| 실습가이드_7교시_멀티미디어AI활용.md | Markdown | 23.4KB | 실습 15~19(OCR, 이미지 생성, PDF 분석, 녹음 STT, 멀티모달), 노드 참조표, 파일 크기 제한 |
| 실습5_수강신청자동처리.json | n8n JSON | 11.3KB | 실습 5 완성본(9노드) |
| 실습6_수업리마인더.json | n8n JSON | 6.4KB | 실습 6 완성본(6노드) |
| 실습8_자료자동배포.json | n8n JSON | 5.2KB | 실습 8 완성본(5노드, 가이드보다 축소된 형태) |
| 비디오분석.json | n8n JSON | 3.8KB | 가이드에 없는 보너스 예제: 비디오 → Gemini 분석 → 요약(5노드) |
| AI입문_1주차_강의자료.pdf | PDF(A4, 1쪽) | 6.6KB | 실습 8의 Drive 배포 테스트용 더미 파일. 본문은 제목 한 줄 |
| AI입문_실습가이드.pdf | PDF(A4, 1쪽) | 6.3KB | 위와 같음 |
| 데이터분석_1주차_강의자료.pdf | PDF(A4, 1쪽) | 6.8KB | 위와 같음 |
| 데이터분석_실습가이드.pdf | PDF(A4, 1쪽) | 6.3KB | 위와 같음 |
| sample.png | PNG 2816×1536 RGBA | 7.1MB | 「인공지능(AI) 입문 과정 수강 신청」 신청서 이미지. 실습 15 OCR 입력용(추정) |
| audio_sample.m4a | AAC 48kHz 스테레오 | 612KB | 약 24.5초 음성. 실습 18 STT 입력용(추정) |
| video_sample.mp4 | H.264 3840×2160 60fps + AAC | 4.8MB | 약 1분 25초 영상. 비디오분석.json이 GitHub raw URL로 내려받는 파일 |
| n8n_로컬호스트설정.txt | 텍스트(CP949) | 696B | Windows에서 Node.js·npm으로 n8n을 설치하고 ngrok으로 외부에 공개하는 명령어 메모. **ngrok 인증 토큰 평문 포함** |
| 구글 GCP client 정보 등록.txt | 텍스트(CP949) | 392B | GCP 콘솔에서 Gmail API를 켜고 OAuth 클라이언트 ID를 만드는 절차 메모. Client ID/Secret 칸은 비어 있음 |

---

## 3. 파일별 상세 내용

### 3-1. 가이드 문서 (교시별)

#### 1교시 — 「📘 1교시 실습 가이드 — n8n 소개 & 환경 구축」 (Day 1)
- **학습 목표**: "n8n Cloud 환경을 설정하고 첫 번째 워크플로우를 실행한다"
- **목차**: 실습 전 준비 체크리스트 → 실습 1(Step 1~7) → 노드 기본 조작 연습 → 핵심 개념 정리 → 미니 퀴즈 5문항 → 산출물 체크리스트

| 실습 | 제목 | 하는 일 |
|---|---|---|
| 1 | Hello World 워크플로우 | n8n Cloud 가입·이메일 인증 → 워크플로 "실습1_HelloWorld" → Manual Trigger → Edit Fields(Set)에 `message`, `name`, `timestamp`(`{{ $now.format('YYYY-MM-DD HH:mm:ss') }}`) 3개 필드 → Test workflow → Output JSON 확인 → Ctrl+S 저장 |

- 핵심 개념: 노드 3유형(트리거·액션·로직), 엣지, Execution, JSON, Expression(`$json.필드`, `$now`, `$input.all()`)
- 단축키: Tab(노드 추가), Ctrl+D(복사), Delete, 우클릭 Deactivate, Ctrl+Z

#### 2교시 — 「📘 2교시 실습 가이드 — 핵심 노드 & 데이터 연동」 (Day 1)
- **학습 목표**: "Google Sheets, Gmail 연동 및 조건 분기(IF)를 구현한다"
- **사전 준비**: Google Sheets "수강생_명단"(헤더 이름·이메일·과정·납부여부·연락처, 가상 수강생 5명)

| 실습 | 제목 | 하는 일 |
|---|---|---|
| 2 | Google Sheets 연동 | "Google Sheets OAuth2 API" Credential("My Google") 등록 → Manual → Sheets **Read Rows** → Sheets **Append Row**("테스트학생" 추가) |
| 3 | 데이터 변환 & 조건 분기 | Edit Fields로 필드명 바꾸기(수강생이름·과정명·납부상태·등록일) → **IF**(납부상태 = 완료, TRUE 3명/FALSE 2명) → **Switch**(과정명 AI입문/데이터분석 분기) |
| 4 | 수강생 상태별 이메일 자동 발송 | "Gmail OAuth2 API" Credential("My Gmail") → Sheets → IF → TRUE: 환영 HTML 메일 / FALSE: 납부 안내 HTML 메일(예시 계좌 문구 포함) |

- 부록: 오류 표(401·403·No data found·필드명 불일치·Expression 에러), 디버깅 4단계(Executions → 실패 노드 → Input/Output 비교 → Pin Data)

#### 3교시 — 「📘 3교시 실습 가이드 — 교육서비스업 업무 자동화 ①」 (Day 1)
- **학습 목표**: "Webhook 수강 신청 자동 처리 & 수업 리마인더를 구축한다"

| 실습 | 제목 | 하는 일 |
|---|---|---|
| 5 | 수강 신청 자동 처리 시스템 | 시트 "수강신청_DB" → **Webhook**(POST, path `enrollment`) → 다른 워크플로의 HTTP Request로 테스트 POST → Edit Fields(`$json.body.*` 추출, 신청일시) → Sheets Append → Sheets Search(이메일) → IF(결과 2건 이상이면 중복) → 신규: Gmail 환영 + Slack `#enrollment-alerts`(선택) + Respond to Webhook(success) / 중복: Respond to Webhook(409, duplicate) |
| 6 | 수업 리마인더 자동 발송 시스템 | 시트 "수업일정"(과정명·수업날짜·수업시간·강의실·강사) → **Schedule Trigger**(매일 9:00) → Sheets Read → IF(수업날짜 = 내일 `$now.plus(1,'day')`) → 수강생_명단 조회·과정 매칭 → Gmail 리마인더 |

- 체크리스트에 "Webhook 개념(Test URL vs Production URL)" 포함

#### 4교시 — 「📘 4교시 실습 가이드 — 교육서비스업 업무 자동화 ②」 (Day 1)
- **학습 목표**: "피드백 자동 수집·집계 & 수업 자료 자동 배포 시스템을 구축한다"

| 실습 | 제목 | 하는 일 |
|---|---|---|
| 7 | 설문 & 피드백 자동 수집 시스템 | 시트 "교육피드백_DB"(탭 "피드백"(샘플 5건), "리포트") → ① 수강생에게 Google Forms 링크 설문 메일 발송 → ② Sheets Read → **Code**(JS로 평균·최고·최저 만족도 계산) → IF(평균 < 4.0) → TRUE: 관리자 경고 메일 / FALSE: "리포트" 탭에 Append |
| 8 | 수업 자료 자동 배포 시스템 | Drive 폴더 `교육자료/AI입문`, `교육자료/데이터분석`에 PDF 업로드(zip의 PDF 4개와 파일명 동일) → Manual → 수업일정 Read → IF(내일 수업) → **Google Drive Search Files**(`'{{과정명}}' in parents`) → 수강생 명단 조회 → Gmail(`webViewLink` 링크) → "발송로그" 시트 Append |

- **Day 1 총정리**: 표에 "오늘 만든 워크플로우 7개"(1~7)만 나와 있고 실습 8은 빠져 있습니다
- **Day 2 과제**: 본인 업무 중 자동화 대상 프로세스 1개를 골라 6개 항목(프로세스명·현재 방식·주기·도구·절감 시간·트리거)으로 정리

#### 5교시 — 「📘 5교시 실습 가이드 — AI API 연동 & 프롬프트 엔지니어링」 (Day 2)
- **학습 목표**: "ChatGPT / Claude / Gemini API를 n8n에 연동하고 프롬프트를 설계한다" (**n8n 2.12.3 기준**)
- **n8n v2.x 참고**: Save = 초안, **Publish** = 운영 배포(트리거 활성화)

| 실습 | 제목 | 하는 일 |
|---|---|---|
| 9-A | n8n에서 ChatGPT API 호출하기 (OpenAI 노드) | platform.openai.com에서 키 발급 → Credential "My OpenAI" → OpenAI 노드(Message > Send, `gpt-4o-mini`) → System 프롬프트로 역할 지정 → JSON 출력 형식 강제. 참조식 `$json.message.content` |
| 9-B | n8n에서 Claude API 호출하기 (Anthropic 노드) | console.anthropic.com 키 → "My Anthropic" → Anthropic 노드(Message a Model, `claude-sonnet-4-20250514` / 빠른 응답용 `claude-haiku-4-5-20251001`) → Add Option > System Prompt. 참조식 `$json.content[0].text`. 추가 기능 표(Analyze Document/Image, File, Prompt Generate/Improve/Templatize) |
| 9-C | n8n에서 Gemini API 호출하기 (Google Gemini 노드) | aistudio.google.com/apikey → "Google Gemini(PaLM) API" Credential "My Gemini" → Message a Model `gemini-2.0-flash`. 참조식 `$json.text`. 이미지 분석(OCR)과 Transcribe(STT) 짧은 실습 |
| 10 | AI 응답 → Sheets 저장 → 이메일 발송 | Manual → OpenAI → Edit Fields(질문·응답·모델·일시) → Sheets "AI응답로그" Append → Gmail. 응용: 노드를 Anthropic/Gemini로 바꾸거나 Merge 노드로 3개 모델 비교 |

- 부록: **3대 AI 모델 비교표**(노드명·Credential·Operation·추천 모델·응답 참조식·System 위치·무료 티어·강점), 비용 절감 설정(max_tokens 500~1000, Temperature 0.3~0.5), 2026년 3월 기준 모델별 단가표, API 키 보안 4원칙, Code 노드 Task Runner 격리(`process.env` 사용 불가)
- **날짜 함수 주의**: "✅ `$now.toFormat('yyyy-MM-dd')` / ❌ `$now.format(...)` ← 에러 발생!"이라고 명시합니다(1~4교시 가이드·JSON과 상충, 6장 참고)

#### 6교시 — 「📘 6교시 실습 가이드 — AI 기반 교육서비스 자동화 실습」 (Day 2)
- **학습 목표**: "다양한 AI 활용 워크플로우를 직접 구축한다"

| 실습 | 제목(시간) | 하는 일 |
|---|---|---|
| 11 | 수강생 Q&A 자동 응답 봇 (25분, OpenAI) | 시트 "FAQ_데이터"(FAQ 8개 + "QA로그" 탭) → Webhook(POST `qa-bot`, Respond 노드 모드) → Sheets FAQ Read → Code(FAQ 텍스트 결합 + `$('Webhook').first().json.body.question`) → OpenAI(FAQ를 넣은 System 프롬프트, FAQ에 없는 질문은 담당자 연결 안내) → Edit Fields → Sheets QA로그 Append → Respond to Webhook(answer/source/timestamp) |
| 12 | 교육 피드백 AI 요약 리포트 (20분, OpenAI 또는 Claude) | 피드백 시트 Read → Code(피드백 결합 + 통계) → OpenAI `gpt-4o-mini` 또는 Anthropic `claude-sonnet-4-20250514`(5항목 분석: 요약·긍정 Top3·개선 Top3·제언·총평) → Edit Fields → "리포트" 탭 Append → Gmail HTML 리포트 |
| 13 | 교육 콘텐츠 초안 자동 생성 (10분, Gemini) | Edit Fields(주제 "Python 데이터 분석 입문", 대상, 시간) → Gemini `gemini-2.0-flash`(슬라이드 15~20장 구성안 + 시간 배분표) → Edit Fields → Sheets "콘텐츠초안_로그" |
| 14 | 수강생 이메일 AI 자동 작성기 (5분, 선택) | Edit Fields(수강생·과정·상황) → OpenAI(HTML 이메일 200자 내외 생성) → Gmail로 AI가 만든 HTML 그대로 발송. "상황"만 바꿔 환영·독촉·결석·수료·추천 메일 생성 |

- 부록: 프롬프트 설계 5원칙(역할·규칙·형식·길이·언어), 모델별 프롬프트 팁, n8n 2.12.3 주의사항 5개

#### 7교시 — 「📘 7교시 실습 가이드 — 멀티미디어 AI 활용 실습」 (Day 2)
- **학습 목표**: "이미지·문서·오디오 등 멀티미디어를 AI로 분석·생성하는 워크플로우를 구축한다"

| 실습 | 제목(시간) | 하는 일 |
|---|---|---|
| 15 | 이미지 OCR → 수강 신청 자동 접수 (15분) | Edit Fields(imageUrl) → Gemini **Analyze Image**(JSON으로 이름·연락처·이메일·희망과정·비고 추출) → Code(코드펜스 제거, JSON.parse, 실패 처리) → Sheets "이미지신청접수_DB" → Gmail 접수 확인 |
| 16 | AI 이미지 생성 → 교육 홍보물 제작 (10분) | Edit Fields(과정명·대상·키워드) → Gemini **Generate an Image**(`imagen-3.0-generate-002`, 텍스트 없는 포스터) → Gmail 첨부, Drive Upload, Slack 활용 안내. Google Cloud 결제 계정이 필요하며 없으면 강사 데모로 진행 |
| 17 | 교육 자료 PDF AI 분석·요약 (15분) | Google Drive Download 또는 HTTP Request(File) → Anthropic **Analyze Document**(Binary) 또는 Gemini Analyze Document → 요약·학습목표·키워드·난이도·학습시간·선수지식·**복습 퀴즈 3문항** → Sheets "자료분석_로그" |
| 18 | 수업 녹음 자동 텍스트 변환 & 요약 (10분) | Drive/HTTP로 오디오 → Gemini **Transcribe a Recording** → OpenAI `gpt-4o-mini`(학습 노트 5항목) → Sheets "수업녹취_로그" → Gmail(접이식 `<details>` 원본 녹취록 포함) |
| 19 | 멀티모달 종합 파이프라인 (10분) | Edit Fields(과정명·차시·판서 이미지 URL·강사 메모) → Gemini Analyze Image(판서 텍스트 추출) → Code(판서 + 메모 결합) → OpenAI(학습 자료 6항목) → Edit Fields → Sheets → Gmail |

- 부록: Gemini·Anthropic·OpenAI 노드 Resource/Operation/출력 참조 빠른 참조표, 작업별 모델 선택 가이드, 파일 크기 제한(Gemini 인라인 20MB·File API 2GB, Claude 32MB, Whisper 25MB), 지원 포맷, 바이너리 저장 방식

### 3-2. 워크플로 JSON

공통 사항: 4개 모두 `active: false`, `settings.executionOrder: v1`, `binaryMode: separate`, 같은 n8n 인스턴스(`meta.instanceId` 동일)에서 export했고 `pinData`는 비어 있습니다. Credential은 **이름만 참조**하고 실제 키 값은 들어 있지 않습니다.

#### (1) 실습5_수강신청자동처리.json — 9노드
**흐름**: 트리거(Webhook) → 중복 검색 → 분기 → 저장·메일 → 웹훅 응답

```
Webhook (POST /enrollment, responseMode: responseNode)
  → Edit Fields (이름·이메일·과정명·연락처·신청일시)
  → Get row(s) in sheet (수강신청_DB, 필터: 이메일 = 입력 이메일, alwaysOutputData)
  → If (검색결과 비었나? Object.keys($json).length == 0)
       ├ TRUE (신규) → Append row in sheet → Send a message (Gmail 환영) → Respond to Webhook (success)
       └ FALSE → If1 (Webhook body.email contains 시트 이메일)
                   ├ TRUE (중복) → Respond to Webhook1 (duplicate)
                   └ FALSE → Append row in sheet (위와 합류)
```

| 노드명 | type | 핵심 설정 |
|---|---|---|
| Webhook | n8n-nodes-base.webhook v2.1 | POST, path `enrollment`, Respond 노드로 응답 |
| Edit Fields | set v3.4 | `$json.body.name/email/course/phone`, 신청일시 `$now.format('yyyy-MM-dd HH:mm:ss')` |
| Get row(s) in sheet | googleSheets v4.7 | 문서 "수강신청_DB"/시트1, 이메일 열 필터 |
| If / If1 | if v2.3 | 결과 개수 0 / 이메일 contains |
| Append row in sheet | googleSheets v4.7 | append, 매핑 defineBelow(Edit Fields 값 참조) |
| Send a message | gmail v2.2 | 제목 `[{{과정명}}] 수강 신청이 완료되었습니다`, HTML 본문 |
| Respond to Webhook / 1 | respondToWebhook v1.5 | JSON `{status: success}` / `{status: duplicate}` |

- **사용 서비스**: Webhook, Google Sheets, Gmail
- **결과물**: 신청 데이터 시트 저장, 환영 메일 발송, 호출자에게 JSON 응답
- **가이드와 다른 점**: 가이드는 "Append → Search → IF(2건 이상)" 순서인데 JSON은 "Search 먼저 → 없을 때만 Append" 구조입니다(더 합리적인 구조). Slack 노드가 없고, 중복 응답에 409 코드가 설정되어 있지 않아 기본값 200으로 응답합니다

#### (2) 실습6_수업리마인더.json — 6노드
**흐름**: 트리거(Manual) → 수업일정 조회 → 내일 수업 필터 → 수강생 매칭 → Gmail

```
When clicking 'Execute workflow' (Manual)
  → Get row(s) in sheet (수업일정)
  → If (수업날짜 == $now.plus(1,'day').format('yyyy-MM-dd'), dateTime 비교)
  → Get row(s) in sheet1 (수강생_명단)
  → If1 (수업일정.과정명 == 수강생.과정)
  → Send a message (Gmail: "[리마인더] 내일 {과정} 수업이 있습니다", 시간·강의실·강사)
```

- **사용 서비스**: Google Sheets(2개 문서), Gmail
- **결과물**: 내일 수업 수강생에게 리마인더 HTML 메일
- **가이드와 다른 점**: **Schedule Trigger가 없고** Manual Trigger만 있습니다(가이드는 매일 9시 Schedule + 테스트용 Manual 병렬). False 분기는 연결되어 있지 않습니다

#### (3) 실습8_자료자동배포.json — 5노드
**흐름**: 트리거(Manual) → 수업일정 → 내일 필터 → Drive 검색 → Gmail

```
Manual → Get row(s) in sheet (수업일정) → If (내일 수업)
  → Search files and folders (Google Drive, queryString: '<폴더ID 하드코딩>' in parents,
                              fields: id, name, webViewLink, exportLinks)
  → Send a message (Gmail, 수신자 고정 주소)
```

- **사용 서비스**: Google Sheets, Google Drive, Gmail
- **결과물**: 내일 수업 자료 링크 메일(시연용)
- **가이드와 다른 점(축소·미완성)**: ① 수강생 명단 조회 단계가 없어 수신자가 **고정 이메일 1개로 하드코딩**되어 있습니다(값 마스킹) ② 본문 인사말이 "홍길동님"으로 고정 ③ `<a href="{{ $json.webViewLink }}"></a>`로 링크 텍스트가 비어 있음 ④ 본문 중간에 `확인해주{{ $json.name }}시면`처럼 표현식이 잘못된 위치에 삽입됨 ⑤ "발송로그" Append 단계 누락 ⑥ Drive 검색이 과정명 대신 특정 폴더 ID로 고정

#### (4) 비디오분석.json — 5노드 (가이드에 대응 실습 없음)
**흐름**: 트리거(Manual) → 비디오 다운로드 → MIME 보정 → Gemini 비디오 분석 → Gemini 요약

```
Manual
  → HTTP Request (GET <YOUR_PUBLIC_FILE_URL>/video_sample.mp4)
  → Code in JavaScript (binary.data.mimeType = 'video/mp4', fileName = 'sample.mp4')
  → Analyze video (Google Gemini, resource: video / analyze, models/gemini-2.5-flash, inputType: binary,
                   프롬프트 "이 비디오에서 텍스트를 추출 해줘")
  → Message a model (Google Gemini, models/gemini-2.5-flash,
                     "아래 내용의 text를 알기 쉽게 5문장으로 요약 해줘", 입력 {{ $json.content.parts[0].text }})
```

- **사용 서비스**: GitHub raw(파일 호스팅), Google Gemini(Credential "Google Gemini(PaLM) Api account 2")
- **결과물**: 비디오 속 텍스트 추출 + 5문장 요약
- 의의: 7교시 참조표에 없는 **Video Resource**를 쓰는 추가 예제입니다. 가이드의 `gemini-2.0-flash`보다 최신인 `gemini-2.5-flash`를 사용합니다. HTTP로 받은 바이너리의 MIME 타입을 Code 노드에서 보정하는 기법이 실무에서 유용합니다

### 3-3. 기타 파일

| 파일 | 실제 내용 |
|---|---|
| PDF 4개 | 모두 A4 1쪽, 2026-03-24 생성, NotoSansCJKKR 서브셋 폰트. 텍스트는 "AI입문 1주차 강의자료 - 디지털노마드연구소"처럼 **제목 한 줄뿐**입니다. pdftoppm으로 렌더링해 보면 폰트 서브셋 문제로 상단에 글자 몇 개("의 u 강 강")만 보이고 나머지는 빈 페이지입니다. 실제 강의 내용은 없고, 실습 8(Drive 배포)·실습 17(PDF 분석)용 **더미 파일**입니다. 파일명이 4교시 Drive 폴더 구조 예시와 정확히 같습니다 |
| sample.png | 「[교육 신청서] 인공지능(AI) 입문 과정 수강 신청」 서식 이미지입니다. 1. 신청자 인적 사항(성명·생년월일·연락처·이메일·소속·주소), 2. 신청 교육 과정 정보(과정명·기간·시간·방법·수강료), 3. 신청 동기(손글씨 느낌 서체)와 사전 경험 체크, 4. 개인정보 동의, 5. 서명으로 구성됩니다. 주최는 "대한 인공지능 교육원"이고 인적사항은 모두 **가상 데이터**입니다. 우측 하단에 Gemini 생성 이미지 표식(✦)이 있습니다(추정 AI 생성 이미지). 실습 15 OCR 시나리오("손으로 작성한 신청서를 사진으로 찍어 보내면")와 일치합니다 |
| audio_sample.m4a | AAC 48kHz 2ch, 24.49초, 약 205kbps. 실습 18 STT 테스트용(추정). 가이드는 "스마트폰으로 30초 정도 녹음"을 권장합니다 |
| video_sample.mp4 | H.264 3840×2160 60fps + AAC 48kHz 2ch, 85.35초, 약 474kbps. 비디오분석.json 입력 파일(URL로 확인됨) |
| n8n_로컬호스트설정.txt | 「n8n 로컬 호스트 설정」: nodejs.org 다운로드 → `node -v`, `npm` 확인 → `npm install -g n8n` → `n8n start` → `http://localhost:5678` → ngrok 설치(Microsoft Store) → `ngrok --version`(3.24) → `ngrok config add-authtoken <YOUR_NGROK_AUTHTOKEN> → `ngrok http --url=<고정 도메인> 5678`. **실제 토큰과 고정 도메인이 평문으로 들어 있음(마스킹)** |
| 구글 GCP client 정보 등록.txt | 「구글 GCP client 정보 등록」: GCP 콘솔 → API 및 서비스 → Gmail API 사용 설정 → OAuth 클라이언트 ID 만들기(리디렉션 URI는 n8n Credential 화면에서 복사) → Client ID/Secret을 n8n에 붙여넣기. **값 칸은 비어 있어 노출 없음** |

---

## 4. 커리큘럼 흐름

### 4-1. 전체 학습 경로

| 단계 | 교시 | 핵심 역량 | 대표 산출물 |
|---|---|---|---|
| ① 환경·기본기 | 1교시 | n8n Cloud 가입, 캔버스·노드·Expression·JSON 이해 | Hello World |
| ② 데이터 연동 | 2교시 | Google OAuth, Sheets 읽기·쓰기, IF/Switch, Gmail HTML | 납부 상태별 메일 |
| ③ 이벤트·스케줄 자동화 | 3교시 | Webhook 수신·응답, 중복 체크, Schedule Trigger, 날짜 표현식 | 수강신청 처리, 수업 리마인더 |
| ④ 집계·파일 배포 | 4교시 | Code 노드 JS 집계, 임계값 알림, Google Drive 검색 | 피드백 집계, 자료 배포 |
| ⑤ LLM 연동 | 5교시 | 3사 API 키·Credential, System 프롬프트, JSON 출력, 모델별 응답 경로 | AI 응답 로그 파이프라인 |
| ⑥ AI 업무 자동화 | 6교시 | FAQ 기반 응답(간이 RAG), 피드백 분석 리포트, 콘텐츠·이메일 생성 | Q&A 봇, AI 리포트 |
| ⑦ 멀티모달 | 7교시 | OCR, 이미지 생성, PDF 분석, STT, 이미지+텍스트 결합 | 멀티모달 학습자료 파이프라인 |
| (⑧ 팀 프로젝트) | 8교시 | 예고만 있고 자료 없음 | — |

학습 흐름: **"노코드 기본기 → 구글 업무 도구 연동 → 교육업 실무 시나리오 → AI 텍스트 → AI 멀티미디어"** 순서로 난이도를 올립니다. Day 1의 시트(수강생_명단·수업일정·교육피드백_DB)를 Day 2에서 다시 쓰는 연속 구조입니다.

### 4-2. 가이드 ↔ JSON 대응표

| 실습 | 제목 | 교시 | JSON |
|---|---|---|---|
| 1 | Hello World 워크플로우 | 1 | ❌ 없음 |
| 2 | Google Sheets 연동 | 2 | ❌ 없음 |
| 3 | 데이터 변환 & 조건 분기 | 2 | ❌ 없음 |
| 4 | 수강생 상태별 이메일 자동 발송 | 2 | ❌ 없음 |
| 5 | 수강 신청 자동 처리 시스템 | 3 | ✅ `실습5_수강신청자동처리.json` (구조 개선, Slack·409 없음) |
| 6 | 수업 리마인더 자동 발송 시스템 | 3 | ✅ `실습6_수업리마인더.json` (Schedule 없음) |
| 7 | 설문 & 피드백 자동 수집 시스템 | 4 | ❌ 없음 |
| 8 | 수업 자료 자동 배포 시스템 | 4 | ✅ `실습8_자료자동배포.json` (축소·미완성) |
| 9-A | ChatGPT API 호출 | 5 | ❌ 없음 |
| 9-B | Claude API 호출 | 5 | ❌ 없음 |
| 9-C | Gemini API 호출 | 5 | ❌ 없음 |
| 10 | AI 응답 → Sheets → 이메일 | 5 | ❌ 없음 |
| 11 | 수강생 Q&A 자동 응답 봇 | 6 | ❌ 없음 |
| 12 | 교육 피드백 AI 요약 리포트 | 6 | ❌ 없음 |
| 13 | 교육 콘텐츠 초안 자동 생성 | 6 | ❌ 없음 |
| 14 | 수강생 이메일 AI 자동 작성기 | 6 | ❌ 없음 |
| 15 | 이미지 OCR → 수강 신청 자동 접수 | 7 | ❌ 없음 (샘플 `sample.png`만 있음, 추정) |
| 16 | AI 이미지 생성 → 교육 홍보물 | 7 | ❌ 없음 |
| 17 | 교육 자료 PDF AI 분석·요약 | 7 | ❌ 없음 (더미 PDF만 있음) |
| 18 | 수업 녹음 텍스트 변환 & 요약 | 7 | ❌ 없음 (샘플 `audio_sample.m4a`만 있음, 추정) |
| 19 | 멀티모달 종합 파이프라인 | 7 | ❌ 없음 |
| — | (가이드 없음) 비디오 분석 | — | ✅ `비디오분석.json` + `video_sample.mp4` |

→ 실습 21개 중 **JSON이 있는 것은 3개(14%)** 뿐이고, AI 관련 실습(9~19) JSON은 하나도 없습니다.

---

## 5. 사용 기술·도구·외부 서비스

| 구분 | 이름 | 사용처 | 비고 |
|---|---|---|---|
| 자동화 플랫폼 | n8n Cloud | 1~4교시 | `app.n8n.cloud` 가입 |
| 자동화 플랫폼 | n8n 2.12.3(셀프호스팅 가능) | 5~7교시 / txt 메모 | `npm install -g n8n`, `n8n start`, localhost:5678 |
| 런타임 | Node.js / npm | 로컬 설치 | Windows CMD 기준 |
| 터널링 | ngrok 3.24 | 로컬 n8n 외부 공개(Webhook·OAuth 리디렉션용, 추정) | 고정 도메인 사용 |
| 트리거 노드 | Manual Trigger, Schedule Trigger, Webhook | 전반 | — |
| 로직·가공 노드 | Edit Fields(Set), IF, Switch, Merge, Code(JavaScript), HTTP Request, Respond to Webhook | 전반 | Code는 Task Runner 격리 |
| Google | Google Sheets(OAuth2) | 실습 2~19 | Read Rows / Append Row / Search Rows |
| Google | Gmail(OAuth2) | 실습 4~19 | HTML 메일 |
| Google | Google Drive(OAuth2) | 실습 8·17·18 | Search Files, Download |
| Google | Google Forms | 실습 7 | 설문 링크만 사용 |
| Google | GCP 콘솔(OAuth 클라이언트, Gmail API) | txt 메모 | 셀프호스팅 시 필요 |
| 메신저 | Slack | 실습 5(선택), 16 | `#enrollment-alerts` |
| LLM | OpenAI — `gpt-4o-mini` (비교표에 GPT-4o) | 9-A, 10~14, 18, 19 | DALL-E·Whisper는 참조표만 |
| LLM | Anthropic — `claude-sonnet-4-20250514`, `claude-haiku-4-5-20251001` | 9-B, 12, 17 | Analyze Document |
| LLM | Google Gemini — `gemini-2.0-flash`(가이드), `models/gemini-2.5-flash`(비디오분석 JSON) | 9-C, 13, 15~19, 비디오분석 | Analyze Image/Document/Audio/Video, Transcribe |
| 이미지 생성 | Google Imagen — `imagen-3.0-generate-002` | 16 | Google Cloud 결제 계정 필요 |
| 파일 호스팅 | GitHub raw(정리 후 `<YOUR_PUBLIC_FILE_URL>`로 교체 — 직접 올린 공개 URL 입력) | 비디오분석.json | 샘플 비디오 배포 |
| 표현식 라이브러리 | Luxon(`$now.toFormat`, `$now.plus`) | 5교시 이후 | 1~4교시와 문법 혼재 |

---

## 6. 특이사항

### 6-1. ⚠️ 보안 경고 (민감정보 노출)
| 위치 | 노출된 것 | 심각도 | 조치 권고 |
|---|---|---|---|
| `n8n_로컬호스트설정.txt` | **ngrok authtoken(49자) 평문** — `ngrok config add-authtoken <YOUR_NGROK_AUTHTOKEN>` | 🔴 높음 | 공개 레포에 올라간 실제 토큰으로 보입니다. 제3자가 이 계정으로 터널을 열 수 있으므로 ngrok 대시보드에서 **즉시 재발급(revoke)** 해야 합니다. 재배포할 자료에서는 반드시 삭제하세요 |
| `n8n_로컬호스트설정.txt` | **ngrok 고정 도메인(`*.ngrok-free.app`) = 강사 n8n 인스턴스 공개 주소** | 🟠 중간 | Webhook 엔드포인트와 n8n 로그인 화면이 외부에 노출될 수 있습니다(마스킹) |
| `실습5/6/8.json` | Google Sheets **문서 ID와 docs.google.com URL**(수강신청_DB·수업일정·수강생_명단), Google Drive **폴더 ID**, Webhook `webhookId`, n8n `instanceId` | 🟡 낮음~중간 | 자격증명은 아니지만, 시트 공유 설정이 느슨하면 접근 경로가 됩니다. 템플릿으로 배포하기 전에 제거하세요(마스킹) |
| `실습8_자료자동배포.json` | Gmail 수신자에 **강사 도메인 실제 이메일 주소** 하드코딩 | 🟡 낮음 | 개인정보이므로 템플릿화할 때 `{{ $json.이메일 }}`로 바꾸세요(마스킹) |
| `구글 GCP client 정보 등록.txt` | Client ID / Client Secret 항목 | 🟢 노출 없음 | 값 칸이 비어 있음 |
| JSON 전체 | Credential | 🟢 노출 없음 | 이름만 참조("Gmail account", "Google Sheets account", "Google Drive account", "Google Gemini(PaLM) Api account 2") |
| 가이드 md | API 키 예시 | 🟢 노출 없음 | `sk-proj-xxxx…`, `sk-ant-api03-xxxx…`, `AIzaSyXXXX…` 등 플레이스홀더만 |
| sample.png | 인적사항 | 🟢 가상 데이터 | 실존 정보 아님(추정) |

### 6-2. 누락·불일치
- **JSON 누락**: 실습 1~4, 7, 9-A~C, 10~19(총 18개) JSON이 없습니다. 특히 AI 실습 JSON이 하나도 없어서 가이드만 보고 직접 만들어야 합니다.
- **8교시 자료 없음**: 6교시 끝에는 "7교시에서는 … 팀별 프로젝트"라고 예고하지만 실제 7교시는 멀티미디어 실습이고, 7교시 끝에서 다시 "8교시 팀 프로젝트"를 예고합니다. 8교시 가이드는 없습니다.
- **Day 1 총정리 표**: "워크플로우 7개"만 나와 있어 실습 8이 빠져 있고, 실습 7 구조를 "Schedule → …"로 적었지만 본문은 Manual Trigger로 안내합니다.
- **날짜 함수 문법 혼재**: 1~4교시 가이드는 `$now.format('YYYY-MM-DD')`, JSON 3개는 `$now.format('yyyy-MM-dd')`와 `$now.plus(1, 'day')`를 씁니다. 반면 5교시는 "`.format()`은 에러, `.toFormat()`과 `plus({ days: 1 })`를 쓰라"고 합니다. 수강생 혼란 요인입니다.
- **실습 5 JSON**: Edit Fields의 과정명·신청일시 값 앞에 **탭 문자**가 들어 있어(`=\t{{ … }}`) 시트에 공백이 섞여 저장될 수 있습니다.
- **실습 8 JSON**: 링크 텍스트 비어 있음, 본문 중간 `{{ $json.name }}` 오삽입, 수신자 고정 등 시연용 미완성 상태입니다(3-2 참고).
- **모델 버전**: 가이드는 `gemini-2.0-flash`, `claude-sonnet-4-20250514`(2026년 3월 시점), 비디오분석 JSON은 `gemini-2.5-flash`로 서로 다릅니다. 모델 지원 종료 여부를 재확인해야 합니다.

### 6-3. 실행 환경
- **이중 환경**: 가이드 1~4교시는 n8n **Cloud**를 쓰고, txt 메모는 Windows 로컬 **셀프호스팅**(npm + ngrok) 방법입니다. 5~7교시는 "n8n 2.12.3 기준"(Publish/Save 개념, Task Runner)입니다. 셀프호스팅에서는 Google OAuth에 자체 GCP OAuth 클라이언트가 필요하므로 GCP txt가 함께 들어 있는 것으로 보입니다(추정).
- JSON `settings.binaryMode: separate`, Webhook v2.1, Google Sheets v4.7, Gmail v2.2, Gemini v1.1 등 노드 버전으로 보아 n8n 2.x에서 export한 것입니다(추정).
- 모든 JSON이 `active: false`라서 가져온 뒤 Credential을 다시 연결하고 Publish해야 합니다.
- 비용 안내: 3개 모델을 실습에 모두 써도 "하루 $1 이하", Anthropic 신규 크레딧 $5, Gemini 무료 티어(가이드 기준)

### 6-4. 샘플 미디어 용도
| 파일 | 용도 | 근거 |
|---|---|---|
| PDF 4개 | 실습 8 Drive 배포, 실습 17 PDF 분석용 더미 | 파일명이 4교시 Drive 폴더 예시와 일치(확정). 실습 17에 "4교시에서 업로드한 교육 자료 PDF" 언급 |
| sample.png | 실습 15 이미지 OCR(수강신청서) | 이미지 내용과 OCR 추출 필드(이름·연락처·이메일·희망과정)가 일치(추정) |
| audio_sample.m4a | 실습 18 녹음 STT | 지원 포맷에 M4A 명시, 30초 내외 권장(추정) |
| video_sample.mp4 | 비디오분석.json | JSON의 GitHub raw URL이 이 파일을 지정(확정) |

---

## 7. 활용 포인트

1. **「교육기관 운영 자동화 템플릿 팩」 판매**: 실습 5(중복 체크 수강신청)·6(리마인더)·7(만족도 경고)·8(자료 배포)·11(FAQ 봇)·12(AI 피드백 리포트)를 정리된 JSON + Google Sheets 템플릿 + 셋업 가이드로 묶어 학원·교육센터 대상 상품으로 만듭니다. 누락된 JSON 18개를 직접 완성하는 것 자체가 차별점이 됩니다.
2. **강의 상품 리패키징 (2일 14시간 → 단계형 과정)**: 기초(1~4교시, Cloud), AI 연동(5~6교시), 멀티모달(7교시 + 비디오분석)로 나눠 VOD나 부트캠프로 구성합니다. 날짜 함수 불일치를 `toFormat()`으로 통일하고 모델명을 최신으로 바꾼 "2026 개정판"으로 내놓을 수 있습니다.
3. **「종이 신청서 OCR 접수」 미니 SaaS**: 실습 15(Gemini Analyze Image → JSON 파싱 → Sheets/Gmail)를 웹 업로드 폼과 Webhook으로 감싸서, 오프라인 신청서·영수증·명함을 사진으로 받아 자동 DB화하는 서비스로 만듭니다. sample.png 같은 가상 서식 데모 자산이 이미 있습니다.
4. **「수업 녹음·영상 → 학습노트 자동 발송」 서비스**: 실습 18(Transcribe → 요약)·19(판서 OCR + 강사 메모)·비디오분석.json(Gemini Video)을 합쳐 강사가 녹음이나 영상을 Drive에 올리면 요약·퀴즈·학습노트를 수강생에게 자동 발송하는 강사용 SaaS로 확장합니다. 실습 17의 PDF→퀴즈 생성 기능도 붙일 수 있습니다.
5. **멀티 LLM 라우팅 비교 데모**: 5교시의 3대 모델 비교표와 Merge 노드 응용을 "같은 질문을 3개 모델에 보내고 비용·품질을 비교하는 대시보드"로 만들어 강의 데모나 컨설팅 리드 수집용 무료 도구로 씁니다. 공개 전에 ngrok 토큰 같은 자격증명이 들어 있지 않은지 반드시 점검하세요.
