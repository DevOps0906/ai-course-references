# VibeCoding-main — 비개발자 직장인 대상 "AI 바이브 코딩 실전 과정(20H)" 강의 패키지 + Colab 기반 Claude 바이브코딩 실습 노트북 모음
> ℹ️ 이 문서는 자료를 처음 분석할 때 작성한 정리본입니다. 레포에 넣으면서 원본 표기·연락처·토큰·문서 ID는 정리되었으니, 6장의 "노출" 항목은 **정리 전 원본 기준** 기록입니다.

> - **원본 버전**: 커밋 `dd2ceda` 기준 (최신 여부는 `python3 tools/sync.py`로 확인)
> - **총 파일 수**: 15개 (루트 7개 + `바이브코딩_기본/` 5개 + `바이브코딩_중급/` 3개)
> - **용량(압축 해제 기준)**: 1,441,879 bytes (약 1.38 MB) — 이 중 `transformer.pdf`(628 KB)와 `AI_바이브코딩_교재.pptx`(581 KB)가 약 86%
> - **자료 성격**: ① 한국표준협회 x 서울시 일자리센터 「AI 바이브 코딩 실전 과정」 4일(20시간) 강의용 PPT 교재 100장 + Day1~4 실습 워크시트(Markdown) ② Google Colab에서 Claude에게 프롬프트를 보내 코드를 받아 붙여넣는 4시간짜리 "Claude × Colab AI 어드벤처 워크숍" 노트북 5개 ③ 중급 바이브코딩 노트북 3개(Claude API 직접 호출, 사다리 게임, 우주 시뮬레이터) ④ Transformer 아키텍처 해설 슬라이드 PDF(논문 원문 아님)
> - **실행 코드 포함 여부**: 노트북 8개 중 실습용 빈 셀이 대부분이고, 완성 코드가 들어 있는 것은 `Claude_Code_바이브코딩_실습.ipynb`, `바이브코딩_우주시뮬레이터_실습.ipynb` 2개. 모든 노트북의 실행 결과(outputs)는 비어 있음.

---

## 1. 한눈에 보기

| 항목 | 내용 |
|---|---|
| **주제** | 생성형 AI 기초 → 프롬프트 엔지니어링(CRISP 템플릿) → 자연어로 웹앱 만들기(바이브 코딩) → 결과 발표·업무 적용 전략 |
| **과정명(원문)** | "AI Vibe Coding 실전 과정 (20H)", "한국표준협회 x 서울시 일자리센터", "2026" (PPT 슬라이드 1) |
| **추정 대상 학습자** | 코딩 경험 없는 직장인·구직자("비개발자 참여 가능", 슬라이드 2). 행정/총무, 마케팅/영업, 기획/전략, IT/개발 직군별 예시 제공(Day2 실습 8). 노트북 쪽은 "AI에 관심 있는 누구나 (코딩 초보 환영!)" |
| **구성(일수/세션)** | 본과정: Day 1~4, 일 6H(10:00~17:00), 총 20H. Day 4는 "*마지막 날 법정의무교육 4H 제외" 표기 → 실제 Day 4 교육 2H(추정) / 부속 워크숍: Session 0~4, 총 4시간(세션당 60분, Session 4는 30분) / 중급 노트북: 7모듈, 9단계, 7단계 실습 3종 |
| **자료 형식** | PPTX 1(100슬라이드, 노트 비어 있음), Markdown 5(실습 워크시트), Jupyter Notebook 8(Colab 메타데이터 포함), PDF 1(17쪽 16:9 슬라이드) |
| **실습 방식** | 웹 AI 채팅(ChatGPT/Claude/Gemini)에 프롬프트 복붙 → 결과 비교·기록표 작성 / Claude Artifacts에서 HTML 앱 생성 / Colab에서 "Claude에게 프롬프트 → 코드 복사 → 빈 셀 붙여넣기 → Shift+Enter" / Anthropic API로 HTML 생성 후 `IPython.display.HTML`로 즉시 렌더링 |
| **핵심 키워드** | 생성형 AI, LLM, 할루시네이션, AI 보안 가이드라인, CRISP 템플릿, Zero-Shot/Few-Shot, Chain-of-Thought, 페르소나, 출력 형식 제어, 프롬프트 체이닝, 네거티브 프롬프트, 프롬프트 라이브러리, A/B 테스트, 바이브 코딩(Andrej Karpathy), Claude Artifacts, Cursor Composer, Chart.js, Papa Parse, localStorage, CLAUDE.md, Plan 모드, TF-IDF, 코사인 유사도, OpenCV, 스타일 트랜스퍼, KoNLPy, Prophet, Canvas 애니메이션, ipywidgets, Transformer/Self-Attention |

---

## 2. 폴더·파일 구성

### 2-1. 트리 구조

```
VibeCoding-main/
├── AI_바이브코딩_교재.pptx            # 본과정 메인 교재 (100 슬라이드)
├── Day1_실습자료.md                   # Day 1 워크시트
├── Day2_실습자료.md                   # Day 2 워크시트 (가장 상세)
├── Day3_실습자료.md                   # Day 3 워크시트
├── Day4_실습자료.md                   # Day 4 워크시트
├── 실습4_강화버전.md                  # Day 1 '실습 4'의 확장 대체본
├── transformer.pdf                    # Transformer 아키텍처 해설 슬라이드 (17쪽)
├── 바이브코딩_기본/                   # Claude × Colab AI 어드벤처 워크숍 (4시간)
│   ├── Session_0_환경설정.ipynb
│   ├── Session_1_영화추천AI.ipynb
│   ├── Session_2_AI화가.ipynb
│   ├── Session_3_감성분석AI.ipynb
│   └── Session_4_예측AI_종합정리.ipynb
└── 바이브코딩_중급/
    ├── Claude_Code_바이브코딩_실습.ipynb
    ├── 바이브코딩_우주시뮬레이터_실습.ipynb
    └── 사다리게임_바이브코딩_실습.ipynb
```

### 2-2. 파일 목록

| 파일명 | 형식 | 크기 | 역할 |
|---|---|---:|---|
| `AI_바이브코딩_교재.pptx` | PPTX (100장, 이미지 56개, 발표자 노트 비어 있음) | 595,253 B | 4일 과정 전체 강의 슬라이드. 1~66 본편, 67~99 Day별 보충 슬라이드, 100 마무리 |
| `Day1_실습자료.md` | Markdown (236줄) | 7,388 B | Day 1 실습 1~5 (계정 생성, AI 비교, 문서 작성, 업무 매핑, 보안 퀴즈) |
| `Day2_실습자료.md` | Markdown (1,053줄) | 36,438 B | Day 2 실습 1~11 (프롬프트 엔지니어링 전 기법). 교시별 개념 설명까지 포함한 "읽는 교재"형 |
| `Day3_실습자료.md` | Markdown (350줄) | 10,856 B | Day 3 실습 1~5 (Todo 앱, KPI 대시보드, 디버깅, 업무 도구 프로토타입, 코드 리뷰) |
| `Day4_실습자료.md` | Markdown (310줄) | 11,248 B | Day 4 실습 1~5 (발표 준비, 동료 평가, 전략 캔버스, 30일 플랜, 자가 진단) + 만족도 설문 |
| `실습4_강화버전.md` | Markdown (200줄) | 7,513 B | Day 1 "실습 4: 내 업무에 AI 적용하기"의 강화판 (미션 A~D) |
| `transformer.pdf` | PDF (17쪽, 720×405pt) | 642,804 B | "Transformer 모델 완전 해부" 한국어 해설 슬라이드. 다른 파일에서 참조되지 않는 독립 자료 |
| `바이브코딩_기본/Session_0_환경설정.ipynb` | ipynb (셀 7, 코드 1·빈 셀) | 3,558 B | 워크숍 소개, 핵심 워크플로우, 라이브러리 환경 테스트 |
| `바이브코딩_기본/Session_1_영화추천AI.ipynb` | ipynb (셀 20, 코드 6) | 9,654 B | TF-IDF + 코사인 유사도 영화 추천 |
| `바이브코딩_기본/Session_2_AI화가.ipynb` | ipynb (셀 21, 코드 6) | 9,957 B | OpenCV 필터 + TF Hub 스타일 트랜스퍼 |
| `바이브코딩_기본/Session_3_감성분석AI.ipynb` | ipynb (셀 19, 코드 6) | 10,046 B | KoNLPy 형태소 분석 + ML 3종 감성 분류 |
| `바이브코딩_기본/Session_4_예측AI_종합정리.ipynb` | ipynb (셀 14, 코드 4) | 8,511 B | 시계열 분석 + Prophet 예측 + 종합 대시보드 |
| `바이브코딩_중급/Claude_Code_바이브코딩_실습.ipynb` | ipynb (셀 45, 코드 22 전부 작성됨) | 28,842 B | Anthropic API로 HTML 생성·렌더링, CLAUDE.md, Plan 모드 시뮬레이션 |
| `바이브코딩_중급/바이브코딩_우주시뮬레이터_실습.ipynb` | ipynb (셀 27, 코드 9 전부 작성됨) | 45,312 B | HTML/CSS/Canvas로 우주 시뮬레이터를 7단계로 키워가는 시연형 노트북 |
| `바이브코딩_중급/사다리게임_바이브코딩_실습.ipynb` | ipynb (셀 20, 코드 9 붙여넣기용) | 14,499 B | 함수 단위 프롬프트로 사다리 게임(Python + matplotlib + ipywidgets) 구현 |

---

## 3. 파일별 상세 내용

### 3-1. `AI_바이브코딩_교재.pptx` (100 슬라이드)

- **목적**: 4일 과정 전체 이론 + 실습 안내. 실습 워크시트(Day1~4 md)와 내용이 짝을 이룸.
- **메타데이터**: 제목 "AI 바이브 코딩 실전 과정", 작성자 "디지털노마드연구소", 2026-03-15 생성/수정.

**슬라이드 흐름 (본편 1~66)**

| 구간 | 슬라이드 | 주요 제목(원문) |
|---|---|---|
| 표지·개요 | 1~2 | "AI 바이브 코딩", "과정 개요 및 학습 로드맵" (총 20시간, 실습 중심, 비개발자 참여 가능) |
| **Day 1** AI와 일하는 법 | 3~23 | "생성형 AI란 무엇인가?"(2017 Transformer ~ 2025 바이브 코딩 타임라인), "생성형 AI의 작동 원리 (쉽게 이해하기)", "생성형 AI로 할 수 있는 일", "업종별 AI 활용 실무 사례", "주요 생성형 AI 모델 비교"(ChatGPT GPT-4o / Claude 4 / Gemini 2.5 / Copilot / Cursor AI / Windsurf), "ChatGPT 심층 분석", "Claude 심층 분석"(200K 컨텍스트, Artifacts, Projects), "Gemini & Copilot 심층 분석", "상황별 AI 도구 선택 가이드", "생성형 AI 실무 적용 한계점", "AI 윤리적 고려사항", "AI 사용 보안 가이드라인", "AI 핵심 용어 정리"(LLM, 토큰, RAG, 파인튜닝 등), "실습: AI 도구 비교 체험하기", "AI 실무 적용 사례: Before & After", "AI 활용 업무 효율화 프레임워크"(Discover→Design→Deploy→Document→Develop), "AI가 특히 잘하는 일 vs 못하는 일", "무료 AI 도구 시작 가이드", "Day 1 핵심 정리 & 체크리스트" |
| **Day 2** 프롬프트 엔지니어링 | 24~38 | "프롬프트 엔지니어링이란?", "프롬프트 작성 핵심 5원칙", "만능 프롬프트 템플릿 (CRISP)", "고급 기법 1: Zero-Shot vs Few-Shot", "고급 기법 2: Chain-of-Thought (CoT)", "고급 기법 3: 역할극 & 페르소나", "고급 기법 4: 출력 형식 제어", "실습: 자료 분석 프롬프트 작성", "실습: 업무 기획 프롬프트 작성", "실습: 이메일/문서 작성 프롬프트", "프롬프트 체이닝 실전 기법", "나만의 프롬프트 라이브러리 구축", "Day 2 실습 과제 & 평가"(구체성 30%·품질 30%·창의성 20%·문서화 20%) |
| **Day 3** 바이브 코딩 실전 | 39~55 | "바이브 코딩(Vibe Coding)이란?", "바이브 코딩 워크플로우", "Cursor AI 상세 가이드", "Claude Artifacts 상세 가이드", "ChatGPT Canvas/Code 가이드", "코딩 아이디어 구체화 5단계", "바이브 코딩 프로젝트 아이디어 (초급)/(중급)", "실습: AI로 할 일 목록 앱 만들기", "실습: AI로 데이터 대시보드 만들기", "코드 생성 프롬프트 핵심 패턴"(기능 명세형/참고 사이트형/점진적 확장형/오류 수정형/리팩토링형), "비개발자를 위한 웹 기술 기초", "AI로 디버깅 & 오류 수정하기", "실전 프로젝트: 나만의 업무 도구 만들기", "바이브 코딩 Best Practices" |
| **Day 4** 결과물 공유 | 56~66 | "프로젝트 결과물 발표 가이드"(창의성 25%·실용성 30%·완성도 25%·프롬프트 활용 20%), "업무 적용 전략: AI 활용 4대 영역", "조직의 AI 거버넌스 전략"(1개월→3개월→6개월→12개월 로드맵), "AI 시대에 필요한 핵심 역량", "AI 실무 적용 30일 플랜", "추천 학습 리소스", "AI의 미래: 2026 트렌드 전망", "나의 AI 활용 액션 플랜 워크시트", "자주 묻는 질문 (FAQ)" |

**보충 슬라이드 (67~99, Day 라벨이 붙어 본편 뒤에 덧붙여짐)**

| Day | 슬라이드 | 제목(원문) |
|---|---|---|
| Day 1 | 67~71 | "AI와 효과적으로 대화하는 전략", "실습: AI 서비스 계정 생성 가이드", "실전: AI로 업무 보고서 작성하기", "실전: AI로 이메일 작성하기", "실전: AI로 데이터 정리하기" |
| Day 2 | 72~79 | "프롬프트 작성 시 주의사항"(마법의 후속 프롬프트 5선), "실습: SNS/마케팅 콘텐츠 프롬프트", "실습: AI로 회의록 정리하기", "실제 프롬프트 실수 사례 & 개선", "네거티브 프롬프트 활용법", "프롬프트 A/B 테스트 방법", "업종별 실전 프롬프트 모음 (1)/(2)" |
| Day 3 | 80~90 | "바이브 코딩으로 만들 수 있는 것들", "AI에게 요청할 때 알면 좋은 기술 용어", "실습: 데이터 시각화 웹 앱 만들기"(CSV→Chart.js+Papa Parse), "실습: AI로 간단한 게임 만들기"(숫자 맞추기 6단계), "반응형 & 디자인 개선 프롬프트", "프로젝트 발표 준비 워크시트", "Cursor AI 실습 상세 가이드"(Ctrl+I Composer, Accept All, Live Server), "Claude Artifacts 실습: 인터랙티브 도구 만들기"(계산기, 퀴즈), "바이브 코딩 프로젝트 아이디어 (고급)", "실습: 개인 프로필 웹사이트 만들기", "AI에게 코드 리뷰 요청하기" |
| Day 4 | 91~99 | "프로젝트 발표 잘하는 법", "효과적인 피드백 주고받기", "업무별 AI 활용 효과 매트릭스", "팀 단위 AI 활용 전략", "AI 활용 실제 성과 사례", "AI 실무 적용 체크리스트 (귀사 맞춤)", "AI 활용 성공을 위한 마인드셋", "교육 피드백 & 개선 사항", "수료 후 지속 학습 가이드" |
| 마무리 | 100 | "수고하셨습니다!" — "코딩을 모르는 당신도 이제 개발자입니다" |

- **실습 항목**: 슬라이드 17(AI 도구 비교), 19(내 업무 적용), 32~34(분석/기획/이메일 프롬프트), 48~49(Todo·대시보드), 53(업무 도구), 82~83·86~87·89(CSV 차트·게임·Cursor 포트폴리오·계산기/퀴즈·프로필 사이트)
- **프롬프트 예시**: 있음(매우 많음). 슬라이드에 복붙 가능한 프롬프트 원문이 직접 수록됨.
- **도구/라이브러리**: ChatGPT(GPT-4o, DALL-E 3, Code Interpreter, Canvas, GPTs), Claude(Artifacts, Projects), Gemini, Microsoft Copilot, Perplexity, Cursor AI, Windsurf, Chart.js, Papa Parse, localStorage, Python matplotlib, SVG, Live Server

---

### 3-2. `Day1_실습자료.md` — "Day 1 실습 자료: AI와 일하는 법 & AI 기초"

- **목적**: AI 계정 생성, AI별 답변 비교, 업무 문서 작성 체험, 내 업무에 AI 적용, 보안 인식.
- **학습 목표(원문 요약)**: ChatGPT·Claude·Gemini 계정 생성 / 같은 질문의 AI별 답변 비교 / 업무 적용 시나리오 도출 / AI 보안 가이드라인 이해

| 번호 | 제목(원문) | 시간 | 하는 일 |
|---|---|---|---|
| 실습 1 | AI 서비스 계정 생성 | 10:30~11:00 | ChatGPT, Claude, Gemini, Perplexity 가입 체크리스트, 첫 질문 입력 |
| 실습 2 | AI 첫 대화 체험 | 11:00~11:30 | 미션 1 기본 대화(직무 소개 → 도움 방법 3가지) 3사 비교표 / 미션 2 12개월 매출 CSV(월, 매출, 고객수, 반품률) 분석 요청 → 분석 깊이·시각화·인사이트 채점 |
| 실습 3 | AI로 업무 문서 작성하기 | 14:00~14:40 | 미션 3 이메일(상황·원인·대안·톤·길이·형식) / 미션 4 보고서 초안(역할·맥락·성과·진행·계획) |
| 실습 4 | 내 업무에 AI 적용하기 | 15:00~16:00 | 업무 5개 매핑 워크시트 → 1개 실제 테스트(Before/After 시간) → 팀 공유 |
| 실습 5 | AI 보안 점검 퀴즈 | 16:30~16:50 | 8개 상황 O/X(예: 고객 실명·전화번호 포함 요청, 인사 DB 급여 데이터, 기밀 스펙 문서 등). "정답 및 해설 (강사가 공개)" |

- **프롬프트 예시**: 있음(기본 대화, 데이터 분석, 이메일, 보고서 템플릿)
- **도구**: ChatGPT, Claude, Gemini, Perplexity
- 학습 정리(3줄 요약 빈칸) + Day 1 체크리스트 6항목

### 3-3. `실습4_강화버전.md` — "실습 4: 내 업무에 AI 적용하기 (15:00~16:00)" 강화판

- **목적**: Day 1 실습 4를 페르소나·리파이닝·로드맵까지 확장한 대체본. 핵심 메시지 "AI는 '검색창'이 아닙니다."

| 미션 | 제목(원문) | 시간 | 하는 일 |
|---|---|---|---|
| A | AI 활용 업무 매핑 워크시트 | 15:00~15:15 | 원본 실습 4의 Step 1~2와 동일 |
| B | AI에게 전문가 페르소나 부여하기 | 15:15~15:30 | "신입사원을 교육하는 방법 알려줘" vs "대기업 HR 15년 교육 전문가… 중소기업 신입 3명 2주 온보딩" 비교, 나만의 페르소나 템플릿 작성 |
| C | 프롬프트 리파이닝 챌린지 | 15:30~15:50 | "팀 워크숍 기획해줘" → 조건 추가(15명, 1박2일, 1인 15만원, 수도권) → 팀 맥락 추가 3단계 비교 |
| D | AI 브레인스토밍 — 나만의 AI 활용 로드맵 만들기 | 15:50~16:00 | 1개월 AI 도입 로드맵(하루 30분, 주차별, 도구·프롬프트 예시 포함) 요청 |
| Step 5 | 팀별 결과 공유 | 16:00~16:30 | 2~3분 발표 템플릿, 타 팀원 메모표 |

- **프롬프트 예시**: 있음 / **도구**: ChatGPT, Claude, Gemini

### 3-4. `Day2_실습자료.md` — "Day 2 실습 자료: 프롬프트 엔지니어링 마스터"

- **목적**: 좋은/나쁜 프롬프트 구분, CRISP 템플릿, 4대 고급 기법, 체이닝, 프롬프트 라이브러리 구축.
- **교시 구성**: 오전 1교시(프롬프트 기초) → 오전 2교시(CRISP) → 오후 1교시(고급 기법 4가지) → 오후 2교시(체이닝) → 오후 3교시(업종별 실전) → 오후 4교시(라이브러리 & 마무리)
- **핵심 개념**: 프롬프트 5요소(역할·맥락·지시·세부사항·출력 형식), CRISP = Context / Role / Instruction / Specifics / Preference ("최소 C + I + P"), 식당 주문 비유

| 번호 | 제목(원문) | 시간 | 하는 일 |
|---|---|---|---|
| 실습 1 | 나쁜 프롬프트 vs 좋은 프롬프트 체험 | 10:10~10:30 | 이메일("이메일 써줘" vs 납품 3일 지연 상세), 데이터 분석(6개월 매출), 보고서(월간 경영 실적) 3쌍 비교 |
| 실습 2 | CRISP 템플릿 따라하기 | 11:10~11:40 | A 마케팅 이메일("AI 바이브 코딩 실전 과정" 얼리버드 30%) / B 공공기관 주간 업무 보고서 + 후속 수정 프롬프트 / C 내 업무 CRISP 작성 |
| 실습 3 | Zero-Shot vs Few-Shot 비교 체험 | 13:10~13:30 | 고객 리뷰 5개 감성 분석, 회의록 요약(표 형식 예시 제공) |
| 실습 4 | Chain-of-Thought 따라하기 | 13:30~14:00 | A 매출 15% 하락 원인 5단계 분석(외부/내부 원인, Top3, 단·중·장기 대응, 2x2 매트릭스) / B "직장인 대상 AI 활용 교육 서비스" 6단계(시장·고객·SWOT·수익모델·리스크·Go/No-Go) |
| 실습 5 | 역할극 & 다중 관점 분석 | 14:00~14:30 | 마케팅 컨설턴트/CFO/35세 과장 고객 3관점 → CEO·CFO·CHRO·현장 팀장 4관점 원샷 평가 |
| 실습 6 | 출력 형식 제어 따라하기 | 14:15~14:30 | "2025년 AI 기술 트렌드 5가지"를 표 / MECE / 경영진 보고용으로 변환 |
| 실습 7 | 프롬프트 체이닝 풀코스 따라하기 | 14:40~15:20 | "우리 팀의 업무 효율화 프로젝트 기획" 5단계(브레인스토밍 10개 → Top3 채점 → As-Is/To-Be 구체화 → 4주 간트 → 제안서) |
| 실습 8 | 업종/직무별 프롬프트 따라하기 | 15:30~16:00 | A 행정/총무(공문, 회의록) / B 마케팅/영업(경쟁사 분석: 클래스101·패스트캠퍼스·인프런·코드잇·노마드코더, 인스타 콘텐츠 5개) / C 기획/전략(AI 리터러시 기업교육 사업계획서: 인당 30만원, 월 4회, 회당 30명) / D IT/개발(`POST /api/v1/auth/login` API 가이드 문서, curl·Python 예시) |
| 실습 9 | 네거티브 프롬프트 활용 | 16:00~16:15 | "~하지 마" 조건 유무 비교 + 상황별 네거티브 프롬프트 6종 표 |
| 실습 10 | 나만의 프롬프트 라이브러리 구축 | 16:15~16:40 | 3카테고리 × 2개 양식, 효과 등급(★), 버전 관리(v1.0→v1.1→v2.0) |
| 실습 11 | 프롬프트 A/B 테스트 | 16:40~16:50 | 같은 목적 2버전 작성·채점 후 라이브러리 등록 |

- **프롬프트 예시**: 있음(이 저장소에서 가장 풍부, 복붙 가능한 원문 30개 이상)
- **도구**: 범용 AI 채팅(특정 서비스 지정 없음), 노션/구글 독스/엑셀(라이브러리 관리)
- 마무리: 기법 8종 요약표, 체크리스트 10항목

### 3-5. `Day3_실습자료.md` — "Day 3 실습 자료: AI 기반 바이브 코딩 실전"

- **목적**: 웹앱 직접 제작, 코드 생성 프롬프트 패턴, AI 디버깅, 업무 도구 프로토타이핑.

| 번호 | 제목(원문) | 시간 | 하는 일 |
|---|---|---|---|
| 실습 1 | 첫 번째 바이브 코딩 — 할 일 목록 앱 | 10:30~11:30 | Claude Artifacts로 Todo 앱(파란 테마 `#00B4D8`) → 수정 1 우선순위 색상 바 → 수정 2 완료율 프로그레스 바 → 수정 3 전체/미완료/완료 필터 → 수정 4 다크 모드(`#1E293B`/`#334155`) |
| 실습 2 | 데이터 대시보드 만들기 | 11:30~12:30 | KPI 카드 4개 + 월별 막대·카테고리 파이·7일 방문자 꺾은선, Chart.js, 다크 테마(`#0F172A`) → 색상 통일·호버 확대·제목·랜덤 새로고침 4단계 개선 |
| 실습 3 | 디버깅 실습 | 14:00~14:30 | "간단한 계산기" HTML에 의도적 오류 3개(문자열 덧셈 "35", 0 나누기 미처리, 숫자 검증 미비)를 AI에게 수정 요청 |
| 실습 4 | 나만의 업무 도구 프로토타입 제작 | 14:30~16:00 | 기획서(문제·사용자·핵심 기능·입출력·기술) → 난이도별 아이디어 8개 중 선택 → 60분 바이브 코딩 + 개발 일지 → 발표 준비(문제 1분/시연 3분/과정 2분/적용 2분) |
| 실습 5 | 코드 개선 & 최종 점검 | 16:00~16:30 | 코드 리뷰 프롬프트(문제점, UX 3가지, 추가 기능 3가지, 모바일 확인) |

- **프롬프트 예시**: 있음(Todo, 대시보드, 디버깅, 코딩 템플릿, 리뷰)
- **도구**: Claude(claude.ai Artifacts), ChatGPT, Cursor AI(선택지), HTML/CSS/JavaScript, Chart.js, Papa Parse

### 3-6. `Day4_실습자료.md` — "Day 4 실습 자료: 결과물 공유 & 업무 활용 전략"

- **목적**: 발표·상호 평가, 업무 적용 전략 수립, 30일 액션 플랜.

| 번호 | 제목(원문) | 시간 | 하는 일 |
|---|---|---|---|
| 실습 1 | 프로젝트 최종 점검 & 발표 준비 | 10:00~10:30 | 점검 체크리스트 6항목, 8분 발표 스크립트 템플릿 |
| 실습 2 | 프로젝트 발표 & 상호 평가 | 10:30~12:00 | 동료 평가표(창의성 25 / 실용성 30 / 완성도 25 / 프롬프트 활용 20 = 100점) |
| 실습 3 | 업무 적용 전략 수립 | 12:00~12:30 | "나의 AI 활용 전략 캔버스"(즉시 자동화 업무, 주 사용 도구, 보안 주의, 이번 달 프로젝트, 팀 확산), 업무별 절감률 예측표 |
| 실습 4 | 30일 AI 활용 액션 플랜 | 12:30~13:00 | 1주 일상 도입 → 2주 라이브러리 → 3주 바이브 코딩 → 4주 팀 확산 |
| 실습 5 | 최종 자가 진단 & 학습 정리 | — | 10개 역량 전/후 1~5점, Day별 회고, "나의 AI 활용 선언문" |

- 부록: 수료 후 추천 리소스(ChatGPT, Claude, Gemini, Cursor, Perplexity / YouTube, Coursera Prompt Engineering, GeekNews, 노마드 코더), 최종 체크리스트 7항목, 교육 만족도 설문 7항목
- **프롬프트 예시**: 거의 없음(발표·계획 템플릿 위주)

### 3-7. `transformer.pdf` — "Transformer 모델 완전 해부"

- **문서 정체**: **논문 원문이 아님.** "Attention Is All You Need" (Vaswani et al., 2017)을 한국어로 해설한 **17쪽 강의 슬라이드(PDF로 내보낸 PPT)**. PDF 메타데이터: Title "Transformer 모델 완전 해부", Subject "PptxGenJS Presentation", Author "AI Education", 생성 2026-03-09, 쪽 크기 720×405pt(16:9). 부제 "모든 LLM의 기반이 되는 핵심 아키텍처 완전 해부", 푸터 "AI 교육 시리즈 | Deep Learning Fundamentals".
- **목차(원문)**: 01 Transformer 탄생 배경 / 02 전체 아키텍처 개요 / 03 입력 표현: 임베딩과 위치 인코딩 / 04 Self-Attention 메커니즘 / 05 Multi-Head Attention / 06 Feed-Forward Network & 정규화 / 07 Encoder 구조 상세 / 08 Decoder 구조 상세 / 09 학습 전략과 최적화 / 10 Transformer vs RNN/LSTM / 11 Transformer 기반 모델 계보 / 12 현대 LLM으로의 진화
- **주요 내용**:
  - 위치 인코딩 수식 `PE(pos,2i)=sin(pos/10000^(2i/d_model))`, Scaled Dot-Product `softmax(QK^T/√d_k)·V`
  - Attention Score 계산 4단계 + "나는 학교에 간다" 3×3 Attention Matrix 예시
  - 학습: Teacher Forcing, Label Smoothing(ε=0.1), LR Warmup 공식, Adam(β₁=0.9, β₂=0.98, ε=10⁻⁹)
  - RNN/LSTM 비교표(병렬성, O(n²) 복잡도 등), 모델 계보(Encoder-only BERT 계열 / Decoder-only GPT·LLaMA·Claude·PaLM·Gemini / Encoder-Decoder T5·BART)
  - 현대 LLM 개선: RoPE/ALiBi, RMSNorm + Pre-Norm, GQA/MQA, SwiGLU/GeGLU, Flash Attention, Chinchilla 스케일링 법칙
  - 원본 하이퍼파라미터 표: d_model 512, d_ff 2048, h 8, d_k=d_v 64, N 6, Dropout 0.1, Warmup 4,000, ~65M 파라미터
- **실습 항목 / 프롬프트 예시**: 없음(이론 자료). 본과정 PPT 슬라이드 4의 "2017 Transformer 아키텍처 발표" 항목의 심화 보충 자료로 활용 가능(추정).

---

### 3-8. `바이브코딩_기본/` — "Claude × Colab AI 어드벤처 워크숍" (4시간)

공통 방식: 각 Step에 "💬 Claude에게 보낼 프롬프트"가 있고, 아래 **빈 코드 셀**에 Claude가 생성한 코드를 붙여넣어 실행. 에러 시 "이 에러를 수정해줘: [에러 메시지]". Colab 한글 폰트 셀(`!apt-get -qq install fonts-nanum fonts-nanum-extra`, `plt.rcParams['font.family']='NanumGothic'`)만 직접 작성되어 있음.

#### Session 0 — "🚀 Claude × Colab AI 어드벤처 워크숍 / 환경 설정 & 워크숍 소개"
- 대상·시간(4시간)·준비물(노트북, Google 계정, Claude 계정)·난이도(★1~★3) 표, 세션 시간표
- 핵심 워크플로우: ① Claude에게 코드 요청 → ② 코드 복사 → ③ Colab 빈 셀 붙여넣기 후 Shift+Enter
- Step 0 환경 테스트 프롬프트: pandas, numpy, matplotlib, sklearn 버전 출력 + 간단 테스트 + "모든 환경이 준비되었습니다! 🚀"
- 체크포인트 4항목

#### Session 1 — "🎬 Session 1: 영화 추천 AI 만들기" (60분, ★★)
| Step | 제목(원문) | 하는 일 |
|---|---|---|
| 1 | 영화 데이터셋 생성 & 탐색 | 한국 25 + 해외 25편 DataFrame(제목·장르·평점·개봉연도·감독·키워드), `df.shape/info()/describe()` |
| 2 | 데이터 시각화 | 2x2 서브플롯: 장르별 수평 막대, 평점 히스토그램+KDE, 연도별 라인, 평점 Top10 → "🎬 영화 데이터 분석 대시보드" |
| 3 | 콘텐츠 기반 추천 시스템 | 장르·키워드·감독 결합 `features` → `TfidfVectorizer` → `cosine_similarity` → `recommend_movies(title, n=5)`; '기생충', '인터스텔라', '올드보이' 테스트 + 유사도 히트맵 |
| 4 | 도전 과제 | A 하이브리드 추천(콘텐츠 70% + 평점 30%) / B `multi_recommend(movie_list)` |

#### Session 2 — "🖼️ Session 2: AI 화가 - 이미지 마법사" (60분, ★★)
| Step | 제목(원문) | 하는 일 |
|---|---|---|
| 1 | 이미지 로딩 & OpenCV 기초 | urllib로 Wikipedia Commons/Unsplash 풍경 사진 다운로드(실패 시 numpy 그라데이션), BGR→RGB, RGB 채널 분리 |
| 2 | 인스타그램 스타일 필터 6종 | 흑백, 가우시안 블러(21), 캐니 엣지(100,200), 세피아, 밝기·대비(alpha=1.3, beta=30), 반전 → "🖼️ AI 이미지 필터 갤러리" |
| 3 | 카툰 & 유화 & 스케치 효과 | `cartoonize()`(medianBlur·adaptiveThreshold·bilateralFilter), `oil_painting()`(`cv2.xphoto.oilPainting`), `pencil_sketch()` |
| 4 | 딥러닝 스타일 트랜스퍼 | T4 GPU 활성화 → TensorFlow Hub `arbitrary-image-stylization-v1-256` + 고흐 '별이 빛나는 밤' |
| 5 | 도전 과제 | 전체 필터 3x4 대형 갤러리 + 처리 시간 표시 |

#### Session 3 — "💬 Session 3: AI 감성 분석가" (60분, ★★★)
| Step | 제목(원문) | 하는 일 |
|---|---|---|
| 1 | 한국어 NLP 환경 설정 & 워드클라우드 | `pip install konlpy`, 나눔폰트, `wordcloud`, Okt 형태소/명사/품사 → 긍정·부정 리뷰 30개 생성 → 워드클라우드 2개 + Top10 막대 |
| 2 | 리뷰 데이터 전처리 & TF-IDF | 리뷰 100개(긍정=1/부정=0), `Okt morphs(stem=True)`, 불용어 제거, `TfidfVectorizer(max_features=500)`, 80:20 분할 |
| 3 | 감성 분류 모델 3종 학습 & 비교 | `LogisticRegression`, `RandomForestClassifier(n_estimators=100)`, `SVC(kernel='linear', probability=True)` → accuracy/precision/recall/F1, Confusion Matrix, 특성 중요도 Top15 |
| 4 | 실시간 감성 예측 & 도전 과제 | `predict_sentiment(text)` — 이모지 + 텍스트 프로그레스 바 출력, 테스트 리뷰 5개 |

#### Session 4 — "🧠 Session 4: AI 예측 마스터 & 종합 정리" (30분, ★★★)
| Step | 제목(원문) | 하는 일 |
|---|---|---|
| 1 | 시계열 데이터 분석 | 서울 월별 기온 시뮬레이션(2015~2024), 2x2: 이동평균 라인, 월별 박스플롯, 연도별 막대+트렌드, `fill_between` |
| 2 | Prophet으로 미래 예측 | `pip install prophet`, ds/y 변환, `yearly_seasonality=True`, 24개월 예측, 계절성 분해, MAE·RMSE |
| 3 | 종합 대시보드 & 워크숍 회고 | 4개 세션 성과를 도넛/격자/레이더/라인 2x2로 정리 → "🚀 AI 어드벤처 워크숍 - 성과 대시보드" |

- 마지막: 세션 요약표, 다음 단계 로드맵(입문~고급), **Claude 프롬프트 치트시트**(에러 수정/기능 추가/시각화 개선/코드 설명/성능 개선), 만능 공식 `[환경] + [목적] + [구체적 요구사항] + [출력 형태]`

---

### 3-9. `바이브코딩_중급/Claude_Code_바이브코딩_실습.ipynb` — "🚀 Claude Code 바이브 코딩 실습 노트북"

- **목적**: Colab에서 Anthropic Python SDK로 Claude를 직접 호출해 HTML을 생성하고 즉시 렌더링하면서, Claude Code의 작업 방식(CLAUDE.md, Plan 모드)을 체험.
- **핵심 코드(작성 완료)**:
  - `!pip install anthropic -q`, `google.colab.userdata.get('ANTHROPIC_API_KEY')` 실패 시 `input()`으로 키 입력 → `anthropic.Anthropic()`
  - 헬퍼: `ask_claude(prompt, system='', model='claude-sonnet-4-20250514', max_tokens=4096)`, `extract_html(text)`(4단계 폴백 정규식), `show_md()`, `vibe_code(prompt)`(생성 → `display(HTML(html))`), `SYSTEM_WEB` 시스템 프롬프트

| 모듈 | 제목(원문) | 실습 |
|---|---|---|
| 1 | 환경 설정 | 1-1 패키지 설치 + API 키 설정, 1-2 헬퍼 함수 정의, 1-3 첫 대화 테스트 |
| 2 | 바이브 코딩 기초 | 2-1 프로필 카드 UI, 2-2 이모지 투표 앱(고양이 vs 강아지), 2-3 프로그래밍 언어 인기 차트 |
| 3 | 단계별 웹앱 만들기 | Todo Step 1 기본 → Step 2 체크박스·카운터(이전 코드를 컨텍스트로 전달) → Step 3 필터·보라 그라디언트 → Step 4 우선순위·더블클릭 수정·다크모드 |
| 4 | CLAUDE.md 작성 실습 | 4-1 "우리 동네 맛집 지도"(Next.js 15, TypeScript, Tailwind CSS, Supabase, Zustand) CLAUDE.md 자동 생성, 4-2 내 프로젝트용(5대 핵심: 개요/명령어/규칙/구조/주의사항) |
| 5 | 프롬프트 전략 비교 | "날씨 앱 만들어줘" vs 구체적 날씨 카드, 개선 공식표(범위·기술·디자인·데이터), 5-3 AI에게 프롬프트 개선 요청 → 개선본으로 코드 생성 |
| 6 | Plan 모드 시뮬레이션 | 6-1 "코드 절대 쓰지 마" 계획 수립 → 6-2 피드백("매출 차트는 막대, 다크 테마, 알림 빼고 인기 상품 TOP5") 반영 실행 / 실제 흐름 "Shift-Tab → Plan 선택" |
| 7 | 종합 실습 — 나만의 앱 | 아이디어 7종 중 선택(기본값 "타이핑 속도 테스트 게임") → Phase 1 CLAUDE.md → 2 계획 → 3 코드 생성 → 4 기능 추가 |

- 정리: 바이브 코딩 6원칙(작게 시작/구체적으로/컨텍스트/Plan 먼저/반복 개선/검증 필수), 실제 Claude Code 사용 예(`claude`, `/init`, "커밋하고 PR 만들어줘")
- 참고 링크: `https://code.claude.com/docs/ko/overview`, `https://github.com/revfactory/claude-code-guide`
- **프롬프트 예시**: 있음(코드 안 문자열로 내장) / **도구**: anthropic SDK, IPython.display, re, Colab Secrets

### 3-10. `바이브코딩_중급/사다리게임_바이브코딩_실습.ipynb` — "🎯 사다리 게임 만들기 — 바이브 코딩 실습"

- **목적**: 함수명·입출력·조건·테스트를 명시하는 "명세형 프롬프트"로 Python 게임을 단계적으로 조립. 코드 셀은 `# Step N — Claude 코드 붙여넣기` 주석만 있음.

| Step | 제목(원문) | 하는 일 / 요구 함수 |
|---|---|---|
| 1 | 환경 설정 | fonts-nanum 설치, NanumGothic, `axes.unicode_minus=False` |
| 2 | 사다리 데이터 구조 만들기 | `create_ladder(n_players, n_rows, rung_prob=0.4)` → 2D bool, 인접 가로선 겹침 방지 |
| 3 | 텍스트로 사다리 출력 | `print_ladder(players, results, rungs)` (열 너비 8, `|-------|`) |
| 4 | 경로 추적 알고리즘 | `trace_path(start_col, rungs)` → (최종 열, 경로 리스트) |
| 5 | matplotlib 기본 시각화 | `draw_ladder(...)` 색상 `#2C3E50`/`#3498DB`, '꽝'은 `#E74C3C`, 그 외 `#27AE60` |
| 6 | 경로 강조 시각화 | `draw_path(..., start_col)` 빨간 경로·●출발·■도착 |
| 7 | 전체 결과 공개 | `draw_all_paths(...)` `matplotlib.cm.Set1` + 텍스트 결과 요약 |
| 8 | 인터랙티브 UI | ipywidgets `IntSlider`(4~15), `Dropdown`, Button 3개("🎲 새 사다리", "🔍 경로 보기", "🏆 전체 공개"), `VBox/HBox/Output`, 전역 `state` |
| 9 | 자유 실습 | 아이디어 카드 A 경로 애니메이션(`FuncAnimation`) / B 1000회 공정성 시뮬레이션 / C CSV 저장 / D 참가자 추가 UI / E Gradio 웹앱 |

- 프롬프트 작성 팁 표(역할·함수명·입출력·조건·테스트·스타일) + 나쁜/좋은 프롬프트 예시
- **도구**: Python, matplotlib, ipywidgets, (선택) pandas, gradio

### 3-11. `바이브코딩_중급/바이브코딩_우주시뮬레이터_실습.ipynb` — "🎨 바이브 코딩 실습: 나만의 인터랙티브 우주 시뮬레이터 만들기"

- **목적**: 각 단계의 "💬 AI에게 줄 프롬프트 예시"와 그 결과 코드(완성본)를 나란히 보여주며, 숫자·색상을 바꿔보는 "✏️ 직접 바꿔보기!"로 체험. 모든 코드가 `IPython.display.HTML`로 Colab 출력에 렌더링.

| Step | 제목(원문) | 핵심 기술 |
|---|---|---|
| 1 | 화면에 뭔가 띄워보기 | HTML div, 인라인 스타일 |
| 2 | 예쁘게 꾸미기 - 그라디언트와 애니메이션 텍스트 | CSS `@keyframes glow/fadeIn`, `linear-gradient` |
| 3 | 별이 빛나는 밤하늘 만들기 | Canvas 2D, `createRadialGradient`, 별 200개 랜덤 |
| 4 | 별들을 움직여보자! (애니메이션) | 워프 효과, 원근 투영, `requestAnimationFrame`, 잔상 |
| 5 | 마우스로 조종하기! | `mousemove` 이벤트, 마우스 위치를 소실점으로 |
| 6 | 행성 궤도 추가하기 | 태양 글로우 + 수성·지구·화성 원운동(`cos/sin`) |
| 7 | 최종 완성! 컨트롤 패널 추가 | 워프 스피드·별 개수 슬라이더, 테마(🧊얼음/🔥불꽃/🌈무지개), 행성 ON/OFF, 리셋, FPS 카운터 |
| 보너스 | 나만의 기능 추가 도전! | 난이도별 프롬프트(배경 음악, 클릭 폭발 파티클, 혜성, 행성 드래그) |

- **도구**: IPython.display.HTML, HTML/CSS/JavaScript Canvas (외부 라이브러리 없음)

---

## 4. 커리큘럼 흐름

### 4-1. 본과정 (PPT + Day1~4 md, 20시간)

| 단계 | Day | 학습 내용 | 산출물 |
|---|---|---|---|
| ① AI 이해·도구 체험 | Day 1 | 생성형 AI 정의·원리·모델 비교·한계·윤리·보안 → 계정 생성, 3사 비교, 이메일/보고서 작성 | AI 계정, 비교 기록표, 업무 매핑 워크시트, 보안 O/X |
| ② 프롬프트 엔지니어링 | Day 2 | 5요소 → CRISP → Zero/Few-Shot → CoT → 페르소나 → 출력 형식 → 체이닝 → 네거티브 → 라이브러리 → A/B 테스트 | 프롬프트 라이브러리 초안(3카테고리 6개+) |
| ③ 바이브 코딩 | Day 3 | 개념(Karpathy) → 도구(Cursor/Artifacts/Canvas) → Todo 앱 → KPI 대시보드 → 디버깅 → 나만의 업무 도구 | 웹앱 프로토타입 1개, 개발 일지, 발표 원고 |
| ④ 공유·확산 | Day 4 | 8분 발표·동료 평가 → 전략 캔버스 → 거버넌스 → 30일 플랜 → 자가 진단 | 평가표, 30일 액션 플랜, AI 활용 선언문 |

### 4-2. 부속 Colab 워크숍 (바이브코딩_기본, 4시간)

Session 0 환경 테스트 → Session 1 추천(pandas·TF-IDF) → Session 2 이미지(OpenCV·TF Hub) → Session 3 NLP(KoNLPy·sklearn) → Session 4 시계열(Prophet) + 종합 대시보드

### 4-3. 중급 확장 (바이브코딩_중급)

- **시각적 체험**: 우주 시뮬레이터(완성 코드 관찰 → 값 바꿔보기) — 입문용 도입부로 적합(추정)
- **명세형 프롬프트 훈련**: 사다리 게임(함수 단위 요구사항 → 조립 → ipywidgets UI)
- **AI 개발 워크플로우**: Claude API 실습(점진적 확장 → CLAUDE.md → Plan 모드 → 종합)

권장 경로(추정): Day1 → Day2 → (Colab 기본 Session 0~4 또는 우주 시뮬레이터) → Day3 → 사다리 게임/Claude Code 실습 → Day4. 파일 안에 이 연결 순서가 명시되어 있지는 않음.

---

## 5. 사용 기술·도구·외부 서비스

| 분류 | 이름 | 사용 위치 | 비고 |
|---|---|---|---|
| AI 채팅 서비스 | ChatGPT (GPT-4o, GPT-4o mini, DALL-E 3, Code Interpreter, Canvas, GPTs) | PPT, Day1~4 | 무료/유료 |
| AI 채팅 서비스 | Claude (claude.ai, Artifacts, Projects) | PPT, Day1~4, 노트북 전체 | 노트북의 코드 생성 주체 |
| AI 채팅 서비스 | Gemini (Gemini 2.5 Pro, Google AI Studio) | PPT, Day1 | |
| AI 채팅 서비스 | Microsoft Copilot, Perplexity | PPT, Day1, Day4 | |
| AI 코드 에디터 | Cursor AI (Composer, Tab, Cmd/Ctrl+K, Cmd+L, Ctrl+I), Windsurf | PPT 42·86 | Live Server 확장 언급 |
| AI API | Anthropic API (`anthropic` SDK), 모델 `claude-sonnet-4-20250514` | Claude_Code 노트북 | console.anthropic.com에서 키 발급, 유료 과금(추정) |
| AI 개발 도구 | Claude Code (`/init`, Plan 모드 Shift-Tab, CLAUDE.md) | Claude_Code 노트북 | 개념 소개 및 시뮬레이션 |
| 실행 환경 | Google Colab (T4 GPU, 보안 비밀) | 노트북 8개 | Google 계정 필요 |
| 웹 기술 | HTML / CSS / JavaScript, Canvas 2D, `requestAnimationFrame`, localStorage | Day3, 우주 시뮬레이터, Claude_Code | |
| JS 라이브러리 | Chart.js, Papa Parse | Day3, PPT 49·82 | CDN 사용 전제(추정) |
| Python 데이터 | pandas, numpy, matplotlib(+font_manager) | Session 0~4, 사다리 | 히트맵·KDE 구현 라이브러리는 AI 생성 코드에 맡김(seaborn 등 사용 가능성, 추정) |
| Python ML | scikit-learn (`TfidfVectorizer`, `cosine_similarity`, LogisticRegression, RandomForestClassifier, SVC, classification_report) | Session 1·3 | |
| 이미지 | OpenCV (`cv2`, `cv2.xphoto`), urllib | Session 2 | xphoto는 opencv-contrib 필요 |
| 딥러닝 | TensorFlow, TensorFlow Hub `arbitrary-image-stylization-v1-256` | Session 2 | GPU 권장 |
| 한국어 NLP | KoNLPy (Okt), wordcloud, 나눔폰트(fonts-nanum) | Session 3 | |
| 시계열 | Prophet | Session 4 | `pip install prophet` |
| 노트북 UI | ipywidgets, IPython.display (HTML, Markdown) | 사다리, Claude_Code, 우주 | |
| 기타(선택) | gradio, `matplotlib.animation.FuncAnimation` | 사다리 Step 9 | 아이디어로만 제시 |
| 외부 이미지 소스 | Wikipedia Commons, Unsplash, 고흐 '별이 빛나는 밤' | Session 2 | URL은 AI 생성에 맡김 |
| 학습 리소스 | Coursera Prompt Engineering, GeekNews, 노마드 코더, AI Times, Lex Fridman Podcast 등 | PPT 62, Day4 | |

---

## 6. 특이사항

### 6-1. 중복·버전 차이

| 항목 | 내용 |
|---|---|
| **실습4_강화버전.md vs Day1 실습 4** | Day1 md의 "실습 4: 내 업무에 AI 적용하기 (15:00~16:00)"와 같은 시간대·같은 제목. 강화버전은 원본의 Step 1~2를 "미션 A"로 그대로 흡수하고 미션 B(페르소나), C(3단계 리파이닝), D(1개월 로드맵)를 추가. Day1 md 본문에는 반영되지 않아 **두 버전이 병존** → 강사가 강화버전으로 교체 사용하는 것으로 추정 |
| **PPT 본편 vs 보충 슬라이드** | 슬라이드 67~99가 Day 1~4 라벨을 달고 본편(1~66) 뒤에 덧붙여져 있어 Day 순서가 섞임(예: Day 4 FAQ(66) 다음에 Day 1 슬라이드(67)). 추후 추가분으로 추정 |
| **PPT ↔ md 내용 중복** | Todo 앱, KPI 대시보드, 이메일·보고서 프롬프트, CRISP, 체이닝, 30일 플랜, 만족도 설문이 PPT와 md에 중복. 수치가 조금씩 다름(예: PPT 34 "2주 연기" vs Day2 md "3일 지연", PPT 29 CoT "외부 원인 3가지" vs Day2 md "5가지") |
| **Todo 앱 3중 구현** | Day3 실습 1(Artifacts), PPT 48, Claude_Code 노트북 Module 3에서 동일 주제를 각기 다른 단계 구성으로 반복 |
| **노트북 2계열의 성격 차이** | 기본 5개·사다리는 "빈 셀 + 붙여넣기" 방식, 우주 시뮬레이터·Claude_Code는 완성 코드 내장 방식 |

### 6-2. 내용상 불일치·오류 가능성

- **네거티브 프롬프트 상충**: PPT 72 "피해야 할 실수 — 부정형 지시 ('~하지 마' 보다 '~해줘')" vs PPT 76·Day2 실습 9 "'~하지 마'라는 지시도 … 매우 효과적" → 한 과정 안에서 메시지가 엇갈림
- **Day2 시간표 겹침**: 실습 5(14:00~14:30)와 실습 6(14:15~14:30) 시간대 중복
- **20시간 구성 표기 불일치**: PPT "총 20시간 (일 6H)" vs 4일×6H=24H, Day4 md "*마지막 날 법정의무교육 4H 제외" → 실제 Day 4 교육은 2H로 추정되나, Day4 md 시간표는 10:00~13:00 이후 시간 미기재
- **정답 누락**: Day1 실습 5 보안 퀴즈 "정답 및 해설 (강사가 공개)" — 파일 내 정답 없음
- **연도 혼재**: 과정 표지 2026 / 실습 데이터 "2024년 12월 대시보드", "2025년 AI 기술 트렌드", 공문 기한 2025-10-15 등 → 운영 시점에 맞춘 갱신 필요
- **모델 정보 노후화 가능성**: PPT 8 "Claude 4", "Gemini 2.5", "GPT-4o"; 노트북 모델 ID `claude-sonnet-4-20250514` → 2026년 하반기 기준 구형·지원 종료 가능성(추정)
- **오탈자 추정**: PPT 62 X(트위터) "@kaborpa"는 "@karpathy"의 오기로 추정. "Toran Billups의 AI Newsletter"도 실재 여부 확인 필요(추정)
- **Session 2 파일명 연결 누락**: Step 4 프롬프트가 "이전에 다운로드한 sample.jpg 사용"을 전제하지만 Step 1 프롬프트에는 저장 파일명 지정이 없음 → AI 생성 코드에 따라 파일명이 달라 실패 가능(추정)
- **Session 0 시간표**: Session 4가 "03:30 ~ 04:00"(30분)로 다른 세션(60분)보다 짧음 — 의도된 구성

### 6-3. 누락

- 실습용 데이터 파일(CSV, 이미지 등) 없음 — 모두 프롬프트로 AI가 생성하거나 인라인 데이터 사용
- 정답 코드/예시 결과물 없음(기본 노트북은 빈 셀, 출력도 모두 비어 있음)
- `transformer.pdf`는 어느 실습·슬라이드에서도 참조되지 않음(독립 보충 자료)
- PPT 발표자 노트 100장 모두 비어 있음
- README, LICENSE 파일 없음 → 재사용·재배포 조건 불명

### 6-4. 실행 환경 요구

- **웹 실습**: 개인 이메일(Gmail 권장), 스마트폰 인증, ChatGPT/Claude/Gemini/Perplexity 계정, (선택) Cursor 설치
- **Colab 노트북**: Google 계정 + Claude 계정. 설치 명령 `!apt-get -qq install fonts-nanum fonts-nanum-extra`, `pip install konlpy wordcloud prophet anthropic`. 폰트 설치 후 런타임 재시작 필요할 수 있음
- **GPU**: Session 2 Step 4 스타일 트랜스퍼는 "런타임 → 런타임 유형 변경 → T4 GPU"
- **KoNLPy**: Okt는 Java(JVM) 의존 → Colab 기본 환경에서 추가 설정이 필요할 수 있음(추정). 설치 2~3분 소요 안내
- **`cv2.xphoto`**: opencv-contrib 패키지 필요(프롬프트에 "없으면 직접 구현" 대비책 포함)
- **Claude_Code 노트북**: Anthropic API 키 필수(유료 크레딧 필요, 추정). Colab 보안 비밀 `ANTHROPIC_API_KEY` 등록 권장
- **보안 주의**: Claude_Code·우주 시뮬레이터 노트북은 AI가 생성한 HTML/JS를 `display(HTML(...))`로 Colab 출력 iframe에서 즉시 실행 → 수업용으로는 문제없으나 검증 없이 실행하는 구조

### 6-5. API 키 등 민감정보 노출 여부

| 점검 항목 | 결과 |
|---|---|
| API 키·토큰 하드코딩 | **노출 없음.** Claude_Code 노트북은 `userdata.get('ANTHROPIC_API_KEY')` 또는 `input()`으로 런타임에 받는 안전한 구조 |
| 비밀번호 | 없음 (Day2 실습 8의 `password: string`은 API 명세 예시 필드명일 뿐) |
| 실행 출력에 남은 키 | 없음 (모든 노트북 outputs 비어 있음) |
| 개인정보 | 실습 예시의 "김철수 고객(010-1234-5678)"은 보안 퀴즈용 가상 예시. PPTX 메타데이터 `lastModifiedBy`에 작성자 개인 이름(영문)이 기록되어 있음 → 재배포 시 메타데이터 정리 권장 |

---

## 7. 활용 포인트

1. **"비개발자 AI 업무활용 20H" 기업·공공 교육 상품 패키지화** — PPT 100장 + Day별 워크시트 구조를 그대로 차용해 디지털노마드연구소 브랜드 커리큘럼(B2B 위탁교육·내일배움 과정)으로 재구성. 위 6-2의 불일치(네거티브 프롬프트, 연도, 모델명)를 정리한 "2026 개정판"으로 차별화.
2. **전자책 『CRISP 프롬프트 실전 워크북』** — Day2 md(실습 11개, 복붙 프롬프트 30+개)와 PPT 보충 슬라이드(업종별 프롬프트 모음, 실수 사례 Before/After)를 직무별 장(행정·마케팅·기획·IT)으로 재편집. 기록표·채점표를 그대로 넣으면 "쓰는 워크북" 형식이 됨.
3. **프롬프트 라이브러리 SaaS / 노션 템플릿** — Day2 실습 10~11(카테고리·효과 등급·버전 관리·A/B 테스트) 양식을 노션 DB 템플릿이나 소형 SaaS(프롬프트 저장 → 버전 → A/B 채점 → 팀 공유)로 제품화. 강의 수강생 대상 후속 판매 상품으로 연결.
4. **Colab "프롬프트 → 코드 → 실행" 노트북 템플릿 상품** — 기본 5세션·사다리 게임의 "프롬프트 셀 + 빈 셀" 포맷을 공통 틀로 삼아 주제만 바꾼 시리즈(쇼핑몰 데이터 분석, 블로그 키워드 분석, 유튜브 댓글 감성 분석 등)를 대량 제작. Claude_Code 노트북의 `vibe_code()` 헬퍼를 살리면 API 기반 자동 실습 키트로 확장 가능.
5. **수강생 프로젝트 자동 평가·피드백 도구** — Day4 동료 평가 기준(창의성 25/실용성 30/완성도 25/프롬프트 활용 20)과 Day3 코드 리뷰 프롬프트를 결합해, 수강생이 HTML 결과물·사용 프롬프트를 제출하면 LLM이 채점·피드백하는 자동화(n8n 또는 SaaS) 도구로 구현.
