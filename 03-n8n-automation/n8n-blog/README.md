# n8n_blog-main — Docker 셀프호스팅 n8n + WordPress로 AI 패션 블로그(아이디어→글→이미지→초안 발행)를 자동화하는 4시간 실습 과정
> ℹ️ 이 문서는 자료를 처음 분석할 때 작성한 정리본입니다. 레포에 넣으면서 원본 표기·연락처·토큰·문서 ID는 정리되었으니, 6장의 "노출" 항목은 **정리 전 원본 기준** 기록입니다.

> - **원본 버전**: 커밋 `4727b6c` 기준 (최신 여부는 `python3 tools/sync.py`로 확인)
> - **총 파일 수**: 5개 (zip 항목 6개 = 최상위 폴더 1 + 파일 5)
> - **용량**: 압축 약 53.4KB (54,675 B) / 압축 해제 약 154.4KB (158,055 B)
> - **자료 성격**: 단일 통합 가이드 Markdown 1개(「패션블로그자동화.md」, 2,738줄, 93.3KB)와 그 가이드의 실습 1~4 완성본 n8n 워크플로 JSON 4개로 구성됩니다. 가이드 말미에 "**디지털노마드연구소** | AI 교육 전문"이라고 적혀 있고, 스스로 "이미지 WordPress 반영 상세 보강판"이라고 소개합니다.

---

## 1. 한눈에 보기

| 항목 | 내용 |
|---|---|
| 주제 | 로컬 Docker로 n8n + WordPress + MariaDB를 띄우고, OpenAI(글)와 Gemini(이미지)로 **시즌 인식 → 아이디어 → SEO 글 → 품질 채점 → 룩북 이미지 → WordPress 미디어 업로드 → 초안 저장**까지 자동화 |
| 대상 학습자 | 원문: "**패션 블로거, 패션 마케터, 쇼핑몰 운영자, 스타일리스트, 패션 인플루언서**" / 전제: "기본 PC 사용 능력" |
| 구성 | 사전 준비(60~90분, 교육 전 별도) + **4교시 × 60분** / 실습 1, 2, 3-1·3-2·3-3, 4 (+ 4-2 Schedule 로테이션) / 교시마다 이론 5분 + 실습 45분 + 체크포인트 5분 + 휴식 5분 |
| 비율 | "이론 15% + 실습 85% · 모든 실습은 화면 단위로 상세 안내" |
| 워크플로 JSON | 4개(실습1~4), 가이드의 「📂 교육 산출물」 목록과 파일명이 정확히 같음 |
| 자료 형식 | Markdown 가이드 1개(코드·YAML·PHP·JS 포함) + n8n export JSON 4개 |
| 기준 버전 | "**n8n 2.12.3 + WordPress 최신 + Docker 기반**" (compose는 `n8nio/n8n:latest`, `wordpress:latest`, `mariadb:11`) |
| 핵심 키워드 | Docker Compose, 셀프호스팅, Docker 내부 통신(`http://wordpress`), OpenAI `GPT-4.1-MINI`, Gemini `models/gemini-2.5-flash-image`(Nano Banana), SEO 메타, 11항목 품질 체크, S/A/B/C 등급, Markdown→HTML, WordPress Application Password, REST API `/wp-json/wp/v2/media`, Featured Media, IF 품질 게이트, Schedule 요일 로테이션 |

---

## 2. 폴더·파일 구성

```
n8n_blog-main/
├── 패션블로그자동화.md            ← 통합 실습 가이드 (사전준비 + 1~4교시 + FAQ + 치트시트)
├── 실습1_패션트렌드아이디어.json   ← 1교시 산출물
├── 실습2_패션블로그생성기.json     ← 2교시 산출물
├── 실습3_이미지포함_패션.json      ← 3교시 산출물 (이미지 업로드 보강판)
└── 실습4_올인원파이프라인.json     ← 4교시 산출물 (불완전, 6장 참고)
```

| 파일명 | 형식 | 크기 | 역할 |
|---|---|---|---|
| 패션블로그자동화.md | Markdown(2,738줄) | 93.3KB | 과정 전체 교재. 환경 구축 → 실습 1~4 → 운영 노하우 → 수료 체크리스트 → FAQ → Docker 명령어 |
| 실습1_패션트렌드아이디어.json | n8n JSON | 6.8KB | 4노드. 시즌·인기도 정렬 아이디어 10개 생성기 |
| 실습2_패션블로그생성기.json | n8n JSON | 12.7KB | 5노드. SEO 메타 → 본문 → 11항목 품질 체크·HTML 변환 |
| 실습3_이미지포함_패션.json | n8n JSON | 21.8KB | 11노드. + 이미지 프롬프트 → Gemini 이미지 → WP Media 업로드 → 본문 삽입 → WP 초안 |
| 실습4_올인원파이프라인.json | n8n JSON | 19.6KB | 12노드. 카테고리만 입력하는 올인원 + IF 품질 게이트(가이드 대비 일부 누락) |

---

## 3. 파일별 상세 내용

### 3-1. 가이드 문서 「👗 패션 블로그 자동화 4시간 과정 (자체 호스팅 버전 · 상세 실습 가이드)」

#### 문서 전체 목차
1. 🎯 4시간 안에 달성할 목표(6개) / 💡 왜 패션 블로그에 자동화가 필요한가(수동 3~5시간 → 15분 등 비교표)
2. 🗓️ 4교시 구성 / 📚 각 교시의 학습 구조
3. 📋 사전 준비 — Docker로 n8n + WordPress 환경 구축 (Step 1~6)
4. 🕐 1교시 / 🕑 2교시 / 🕒 3교시 / 🕓 4교시
5. 🏆 최종 수료 체크리스트 / 📚 4시간 학습 핵심 정리 / 💬 자주 묻는 질문 / 📂 교육 산출물 / 🛠️ Docker 기본 명령어 치트시트 / 🎓 다음 단계 추천 학습

#### 사전 준비 — Docker 환경 구축 (60~90분)
| Step | 내용 |
|---|---|
| 1 | 시스템 요구사항(RAM 최소 8GB/권장 16GB, 저장공간 10~20GB, CPU 가상화), Windows 가상화 확인 |
| 2 | Docker Desktop 설치(Windows: **WSL 2** 체크 필수, macOS Intel/Apple Silicon), `docker --version`, `docker compose version` |
| 3 | `fashion-blog` 폴더 + **docker-compose.yml** 작성: 서비스 3개 `wordpress_db`(mariadb:11, `fashion_db`) / `wordpress`(8080:80, `fashion_wordpress`) / `n8n`(5678, `fashion_n8n`, `GENERIC_TIMEZONE=Asia/Seoul`, `N8N_SECURE_COOKIE=false`, `N8N_RUNNERS_ENABLED=true`), 볼륨 3개, 브리지 네트워크 `blog_net` |
| 4 | `docker compose up -d` → `ps` 확인 → n8n owner 계정 생성(localhost:5678) → WordPress 설치(사이트 제목 「룩북 다이어리」, 사용자 `fashionadmin`, 검색엔진 차단 체크) |
| 5 | WordPress 카테고리 5개: 트렌드(`trends`)·스타일링(`styling`)·리뷰(`reviews`)·쇼핑가이드(`shopping`)·룩북(`lookbook`) + **카테고리 ID 메모** |
| 6 | 정상 동작 체크 6개, 자주 발생하는 문제 Top 3(포트 8080 충돌, n8n 흰 화면, Docker daemon 미실행) |

#### 1교시 — n8n 기초 + AI 연동 & 트렌드 아이디어 생성 (60분)
- **학습 목표**: 셀프호스팅 n8n과 Docker 내부 통신 이해 / OpenAI·Gemini Credential 등록 / 실습 1
- **1-1 핵심 개념**: 브라우저는 `http://localhost:8080`, n8n 내부에서는 `http://wordpress`(아파트 비유). n8n 2.x 변경점(Save vs Publish, Code 노드 Task Runner, `.toFormat()`)
- **1-2 Credential**: OpenAI(`n8n-fashion` 키, 결제 $5~10 충전 권장), Gemini(무료 티어 "분당 15회, 일 1500회"), Anthropic(선택)

| 실습 | 제목 | 하는 일 |
|---|---|---|
| 1 | 패션 트렌드 아이디어 자동 생성기 (35분) | Manual Trigger → Edit Fields(스타일 「미니멀 & 모던」, 타겟독자, 카테고리, 글유형) → OpenAI `GPT-4.1-MINI`(System: "10년 경력 시니어 에디터", JSON 배열만 출력 / User: 아이디어 10개, 필드 제목·카테고리·키워드·검색의도·예상인기도·각도·썸네일, Temperature 0.7) → Code(코드펜스 제거·파싱 → **현재 월로 4계절 판별** + 시즌 무드·컬러·추천키워드 → 인기도 내림차순 정렬) |

#### 2교시 — AI 패션 콘텐츠 자동 생성 (60분)
- **학습 목표**: SEO 패션 글 생성 / 톤앤매너 반영 / 특화 품질 체크(11개 항목)
- **2-1 톤앤매너**: 좋은 패션 글 5요소(공감 후크·시각 묘사·실용 팁·트렌드 맥락·구매 가이드), 피해야 할 표현표("뚱뚱한 체형" → "볼륨감 있는 체형" 등), E-E-A-T

| 실습 | 제목 | 하는 일 |
|---|---|---|
| 2 | 패션 블로그 글 자동 생성기 (42분) | Edit Fields 6개(주제 「2026 봄 여자 트렌치코트 스타일링」, 키워드, 타겟독자, 카테고리, 톤, 목표글자수 2000) → **OpenAI #1**(SEO JSON: meta_title·meta_description·h1·hook·h2_sections 5개·related_keywords·featured_items·price_tiers, Temp 0.6) → **OpenAI #2 「OpenAI_본문작성」**(Markdown 본문 작성 규칙 10개, Temp 0.8, Max Tokens 3000) → **Code 품질 체크**(글자수·H1/H2·키워드 밀도·가격대·스타일링 팁·체형/상황 팁·이모지·CTA·체크리스트 → 100점 감점제, **S(90+)/A(80+)/B(70+)/C** 등급, 70점 이상 통과 + 정규식 기반 **Markdown→HTML** 변환) |

#### 3교시 — 룩북 이미지 생성 + WordPress 연동 (60분)
- **학습 목표**: 카테고리별 맞춤 이미지 / Application Password 연동 / 글 + 이미지 → 카테고리 매핑 → 초안 저장

| 실습 | 제목 | 하는 일 |
|---|---|---|
| 3-1 | 카테고리별 이미지 자동 생성 (20분) | 실습 2 복제 → `실습3_이미지포함_패션` → **Code_이미지프롬프트**(카테고리별 영어 프롬프트 5종: 쇼핑가이드=flat lay, 스타일링=street photo, 트렌드=mood board, 리뷰=marble 제품샷, 룩북=전신 에디토리얼 + 시즌 무드 + "16:9, NO text, NO logos…" + `categoryMap`) → **Google Gemini Generate an Image**(`models/gemini-2.5-flash-image`) |
| (3-2 준비) | WordPress Application Password 생성 (15분) | `docker exec -it fashion_wordpress bash` → nano 설치 → `wp-config.php`에 `add_filter( 'wp_is_application_passwords_available', '__return_true' );` 추가(HTTP 환경 허용) → 재시작 → 프로필에서 앱 비밀번호 `n8n` 발급 → n8n WordPress Credential(URL **`http://wordpress`**, `fashionadmin`, 앱 비밀번호) |
| 3-2 | WordPress 자동 초안 저장 (25분) | WordPress 노드(Post/Create, Title·Content `본문_HTML`·Status `draft`·Slug `fashion-{{ $now.toFormat('yyyyMMdd-HHmm') }}`·Categories) → 최종 보고 Code(글 ID, 품질, 검토_URL·미리보기_URL, 다음 단계 4개) |
| 3-3 ⭐ | 생성한 이미지를 WordPress에 실제로 반영하기 (30분, 핵심 보강) | 기본 WordPress 노드가 Media를 지원하지 않으므로 **HTTP Request `HTTP_이미지업로드`**(POST `http://wordpress/wp-json/wp/v2/media`, Basic Auth 별도 Credential, 헤더 `Content-Type: image/png` + `Content-Disposition`, Body `n8n Binary File`, 필드 `data`) → **Code_미디어병합**(`<figure class="wp-block-image">` 블록을 H1 뒤에 삽입, 미디어ID·URL 전달, 업로드 실패 방어) → WordPress 노드 수정(`본문_HTML_이미지포함` + **Featured Media ID**) → 최종 보고 수정 → WP 3중 확인(미디어 라이브러리·목록 썸네일·편집 화면/미리보기). 심화: 여러 위치 삽입 3가지 방법(`<!-- wp:image -->` 블록 주석 등) |

- 자주 발생하는 문제 9개(앱 비밀번호 섹션 안 보임, 401, 미분류 저장, HTML 노출, 400 Bad Request, `rest_upload_sideload_error`, 이미지 미반영, 썸네일 미표시, 이미지 깨짐)

#### 4교시 — 완전 자동화 파이프라인 & 운영 시스템 (60분)
- **학습 목표**: 엔드투엔드 통합 / IF 품질 게이트 / Schedule Trigger / 운영 노하우

| 실습 | 제목 | 하는 일 |
|---|---|---|
| 4 | 올인원 패션 블로그 자동화 시스템 (45분, "총 13개 노드") | 실습 3 복제 → Edit Fields(**카테고리만**) → **Code_시즌판별**(시즌·시즌키워드·시즌이벤트) → OpenAI #1(아이디어 5개 JSON) → **Code_아이디어선택**(인기도 최고 1개 + 톤·목표글자수 기본값) → OpenAI #2(SEO 구조) → OpenAI #3(본문) → Code(품질 체크) → **IF_품질게이트**(품질점수 ≥ 70) → TRUE: 이미지 프롬프트 → Gemini → HTTP 업로드 → 미디어병합 → WordPress → 최종 보고 / FALSE: **Code_재작성필요** 로그 |
| 4-2 | Schedule Trigger & 요일별 로테이션 (10분) | `실습4_스케줄_버전` 복제 → Schedule(매일 9:00) → Code로 요일→카테고리 매핑(월 트렌드 / 화 스타일링 / 수 리뷰 / 목 쇼핑가이드 / 금 룩북, 주말은 `return []`로 중단) → Active/Publish. PC가 꺼지면 동작하지 않으므로 VPS 이전 권장 |

- **4-3 운영**: 월 20~30개 글 기준 비용 "월 $5~8"(OpenAI), Gemini 이미지는 무료 티어 / **운영 5계명**(Draft 저장 필수, E-E-A-T, 시즌 1~2개월 전 발행, 포용적 체형 표현, API 비용 한도) / 일·주·월 운영 체크리스트
- **FAQ**: AI 글 구글 페널티, 시즌 자동 전환, 이미지 저작권, HTTP Request로 업로드하는 이유, 이미지 여러 장, 대표 이미지와 본문 이미지 차이, PC 종료 시 Schedule, **6시간 과정과의 차이**(RSS 트렌드 수집·콘텐츠 캘린더·다중 AI 교차 검수·이미지 SEO), n8n이 느려질 때
- **다음 단계**: 6시간 과정 / 8시간 과정(MCP 연동, Webhook, 고급 Code) / VPS·SSL·도메인·백업 / GA4·Search Console 연동

### 3-2. 워크플로 JSON

공통: 4개 모두 `active: false`, `executionOrder: v1`, `binaryMode: separate`이고 같은 인스턴스(`instanceId` 동일)에서 export했습니다. 실습3·4에는 `availableInMCP: false` 설정이 있습니다. OpenAI 노드는 `@n8n/n8n-nodes-langchain.openAi` v2.1(Resource Text, "Message a model"), 모델은 `gpt-4.1-mini`입니다. **가이드에 적힌 Temperature·Max Tokens 옵션은 JSON에 하나도 설정되어 있지 않습니다**(`options: {}`). Credential은 이름만 참조합니다.

#### (1) 실습1_패션트렌드아이디어.json — 4노드
```
When clicking 'Execute workflow' (Manual)
  → Edit Fields (스타일 / 타겟독자 / 카테고리 / 글유형)
  → Message a model (OpenAI gpt-4.1-mini, System 에디터 페르소나 + User 아이디어 10개 JSON)
  → Code in JavaScript (output[0].content[0].text 파싱 → 시즌 판별 → 메타 추가 → 인기도 정렬 → 아이템 10개)
```
- 사용 서비스: OpenAI / 결과물: 시즌 정보가 붙은 아이디어 아이템 10개(상태 "대기중")
- 가이드와의 대응: 노드 구성·프롬프트·코드 일치. Temperature 0.7만 빠짐

#### (2) 실습2_패션블로그생성기.json — 5노드
```
Manual → Edit Fields (주제·키워드·타겟독자·카테고리·톤·목표글자수)
  → Message a model (SEO 메타+구조 JSON)
  → Message a model1 (Markdown 본문, $('Edit Fields') 참조로 톤·글자수 주입)
  → Code in JavaScript (11항목 품질 체크 + 등급 + MD→HTML)
```
- 사용 서비스: OpenAI(2회 호출) / 결과물: 제목·본문_MD·본문_HTML·품질점수·등급·강점·이슈 JSON
- 가이드와의 대응: 일치. 단 `목표글자수` 타입이 가이드의 **Number가 아니라 string**이고, Temperature 0.6/0.8과 Max Tokens 3000이 없습니다. 노드명이 가이드의 "OpenAI_본문작성"이 아니라 기본명 "Message a model1"입니다

#### (3) 실습3_이미지포함_패션.json — 11노드 (3-3 보강판 반영)
```
Manual → Edit Fields → Message a model (SEO) → Message a model1 (본문)
  → Code in JavaScript (품질 체크)
  → Code (이미지 프롬프트 + 카테고리ID, categoryMap 트렌드3·스타일링4·리뷰5·쇼핑가이드6·룩북7)
  → Generate an image (Google Gemini, models/gemini-2.5-flash-image "Nano Banana")
  → HTTP_이미지업로드 (POST http://wordpress/wp-json/wp/v2/media, httpBasicAuth,
                       Content-Type image/png, Content-Disposition fashion-{yyyyMMddHHmm}.png, binary 필드 data)
  → Code_미디어병합 (figure/img 블록 H1 뒤 삽입, 미디어ID·URL)
  → Create a post (WordPress: title=제목, content=본문_HTML_이미지포함, status=draft, slug, categories=카테고리ID)
  → Code in JavaScript2 (최종 보고: 글_ID·품질·검토/미리보기 URL)
```
| 사용 서비스 | 결과물 |
|---|---|
| OpenAI, Google Gemini(이미지), WordPress REST API(Media), WordPress 노드(Post) | 본문에 AI 이미지가 들어간 WordPress **초안 글** + 미디어 라이브러리 이미지 |

- 가이드와의 차이: ① **Create a post에 `Featured Media ID` 필드가 없어** 대표 이미지(썸네일)가 설정되지 않습니다(가이드가 "⭐ 핵심"이라고 강조한 부분) ② 최종 보고 Code가 보강 전 버전이라 대표이미지_ID/URL 필드가 없습니다 ③ Content-Disposition 파일명에 카테고리가 빠짐 ④ Basic Auth Credential 이름이 "Unnamed credential"(가이드는 "My WordPress Basic Auth") ⑤ 노드명 규칙이 다름. JSON에서는 이미지 프롬프트 노드 이름이 "Code"이고 품질 체크 노드가 "Code in JavaScript"입니다(가이드 본문의 `$('Code in JavaScript1')`는 JSON에 없음). 이미지 프롬프트 Code가 `...item`으로 품질 결과를 그대로 넘기기 때문에 `$('Code')` 참조는 동작합니다(추정)

#### (4) 실습4_올인원파이프라인.json — 12노드 (가이드 대비 불완전)
```
Manual → Edit Fields (카테고리 = 스타일링)
  → Code_시즌판별
  → Message a model (아이디어 5개 JSON)
  → Code_아이디어선택 (최고 인기도 1개 선택)
  → Message a model1 (⚠ 아이디어 5개 생성 프롬프트가 그대로 복제됨 — SEO/본문 작성 아님)
  → Code in JavaScript (품질 체크)
  → Code (이미지 프롬프트)
  → IF_품질게이트 (품질점수 ≥ 70, number gte)
       ├ TRUE → Generate an image (Gemini) → Create a post (WordPress draft) → Code in JavaScript2 (최종 보고)
       └ FALSE → (연결 없음)
```
- 사용 서비스: OpenAI(2회), Google Gemini(이미지), WordPress
- 가이드(13노드)와 비교해 **빠진 노드**: OpenAI #3(본문 작성), HTTP_이미지업로드, Code_미디어병합, Code_재작성필요(FALSE 분기)
- **동작상 문제(추정)**: ① 두 번째 OpenAI가 본문 대신 아이디어 JSON을 만들기 때문에 품질 체크 대상이 짧은 JSON 문자열이 됩니다. 그러면 글자수·H2 감점으로 70점에 못 미쳐 IF FALSE(미연결)에서 멈출 가능성이 큽니다 ② Create a post의 `categories = {{ $json.catId }}`가 어떤 노드에서도 만들어지지 않는 필드라서 "미분류"로 저장될 수 있습니다 ③ Content가 `본문_HTML`(이미지 없음)이고 Featured Media도 없어 이미지가 WordPress에 반영되지 않습니다. Gemini가 이미지를 생성만 하고 끝납니다
- 노드 순서도 가이드와 다릅니다. 가이드는 품질 체크 → IF → 이미지 프롬프트 순서인데, JSON은 품질 체크 → 이미지 프롬프트 → IF 순서입니다

---

## 4. 커리큘럼 흐름

### 4-1. 전체 학습 경로

| 단계 | 시간 | 습득 역량 | 누적 파이프라인 |
|---|---|---|---|
| 사전 준비 | 60~90분 | Docker Compose, 셀프호스팅 n8n·WordPress·MariaDB, 카테고리 설계 | 인프라 3종 |
| 1교시 | 60분 | Docker 내부 통신, AI Credential, 프롬프트 JSON 출력, Code 파싱·시즌 로직 | **아이디어** |
| 2교시 | 60분 | 패션 톤앤매너, 2단 프롬프트(SEO 구조 → 본문), 규칙 기반 품질 채점, MD→HTML | 아이디어 → **글 + 품질점수** |
| 3교시 | 60분 | 카테고리별 이미지 프롬프트, Gemini 이미지, WP Application Password, REST Media 업로드, Featured Media | 글 → **이미지 → WP 초안** |
| 4교시 | 60분 | 노드 통합, IF 품질 게이트, Schedule·요일 로테이션, 운영·비용 관리 | **카테고리 1개 입력 → 전 과정 자동** |

실습 1 → 2 → 3 → 4가 **앞 실습을 "Duplicate"해서 확장**하는 누적형 구조입니다. 실습 4는 실습 1의 아이디어 생성 개념과 실습 3의 파이프라인을 합칩니다.

### 4-2. 가이드 ↔ JSON 대응표

| 가이드 실습 | 제목 | JSON | 일치도 |
|---|---|---|---|
| 실습 1 | 패션 트렌드 아이디어 자동 생성기 | `실습1_패션트렌드아이디어.json` | ✅ 높음(옵션만 누락) |
| 실습 2 | 패션 블로그 글 자동 생성기 | `실습2_패션블로그생성기.json` | ✅ 높음(옵션·타입 차이) |
| 실습 3-1 | 카테고리별 이미지 자동 생성 | `실습3_이미지포함_패션.json`에 포함 | ✅ |
| 실습 3-2 | WordPress 자동 초안 저장 | `실습3_이미지포함_패션.json`에 포함 | ✅ |
| 실습 3-3 ⭐ | 생성한 이미지를 WordPress에 실제로 반영하기 | `실습3_이미지포함_패션.json`에 포함 | 🟡 부분(HTTP 업로드·본문 삽입은 있음, **Featured Media 없음**) |
| 실습 4 | 올인원 패션 블로그 자동화 시스템 | `실습4_올인원파이프라인.json` | 🔴 낮음(본문 생성·이미지 업로드·FALSE 분기 누락) |
| 4-2 | Schedule Trigger & 요일별 로테이션 (`실습4_스케줄_버전`) | ❌ 없음 | — |
| (사전 준비) | docker-compose.yml | ❌ 별도 파일 없음(가이드 본문에 YAML만 있음) | — |

---

## 5. 사용 기술·도구·외부 서비스

| 구분 | 이름 / 버전 | 사용처 | 비고 |
|---|---|---|---|
| 컨테이너 | Docker Desktop(WSL 2), Docker Compose v2 | 사전 준비 | 서비스 3개, 볼륨 3개, `blog_net` |
| 자동화 | n8n 2.12.3(가이드), `n8nio/n8n:latest`(compose) | 전체 | 셀프호스팅, `localhost:5678`, Task Runner on |
| CMS | WordPress `latest` (한국어) | 3·4교시 | `localhost:8080`, 사이트 「룩북 다이어리」 |
| DB | MariaDB 11 | WordPress용 | `fashion_db` |
| LLM | OpenAI `gpt-4.1-mini`(JSON·가이드 설정표) / `gpt-4o-mini`(문제 해결·비용표 표기) | 아이디어·SEO·본문 | 노드 `@n8n/n8n-nodes-langchain.openAi` v2.1, 응답 경로 `output[0].content[0].text` |
| 이미지 생성 | Google Gemini `models/gemini-2.5-flash-image` (Nano Banana) | 3·4교시 | 노드 `googleGemini` v1.1, Binary `data` 출력 |
| LLM(선택) | Anthropic Claude | 1교시 Credential만 | 실습에 쓰이지 않음 |
| n8n 노드 | Manual Trigger, Schedule Trigger, Edit Fields(Set), Code(JS), IF, HTTP Request, WordPress(Post Create) | 전체 | — |
| API | WordPress REST API `/wp-json/wp/v2/media`, Application Password, Basic Auth | 3-3 | 기본 WordPress 노드가 Media를 지원하지 않아 우회 |
| 편집 도구 | PowerShell / Terminal, Notepad, nano | 환경 구축 | `wp-config.php` 수정 |
| 기타 개념 | SEO 메타, 키워드 밀도, E-E-A-T, Gutenberg `<!-- wp:image -->` 블록 | 2·3교시 | — |
| 후속 언급 | VPS(AWS Lightsail, Vultr), GA4, Search Console API, MCP | FAQ·다음 단계 | 과정 범위 밖 |

---

## 6. 특이사항

### 6-1. 민감정보 점검
| 위치 | 내용 | 판단 |
|---|---|---|
| JSON 4개 | Credential 이름만 있음("OpenAI account", "Google Gemini(PaLM) Api account", "Wordpress account", httpBasicAuth "Unnamed credential"). API 키·토큰·Webhook URL은 **없음**. `instanceId`만 포함 | 🟢 실제 자격증명 노출 없음 |
| 가이드 docker-compose.yml | **MariaDB root·사용자 비밀번호, WordPress DB 비밀번호가 평문 예시값**으로 적혀 있음(값 마스킹) | 🟠 교육용 기본값이지만 수강생이 그대로 복사해 VPS 등에 배포하면 위험합니다. 운영 전에 반드시 바꾸고 `.env`로 분리하라고 안내해야 합니다 |
| 가이드 n8n owner 계정 | 예시 비밀번호(8자, 숫자 포함)를 평문으로 제시(마스킹) | 🟡 약한 비밀번호 예시. 실사용 금지 안내 필요 |
| 가이드 compose 설정 | `N8N_PROTOCOL=http`, `N8N_SECURE_COOKIE=false`, `wp-config.php`로 **HTTP에서 Application Password 허용** | 🟡 로컬 전용 설정입니다. 외부 공개 서버에 그대로 쓰면 인증정보가 평문으로 전송됩니다(SSL 필요) |
| API 키·앱 비밀번호 예시 | `sk-proj-...`, `AIza...`, `Abcd efgh ijkl ...` | 🟢 플레이스홀더 |
| 예시 이메일 | 로컬용 가상 주소 | 🟢 실존 정보 아님(추정) |

### 6-2. 누락·불일치
- **실습 4 JSON 불완전**: 위 3-2(4) 참고. 본문 생성 노드가 아이디어 프롬프트로 잘못 복제되었고, 이미지 업로드·미디어 병합·재작성 로그 노드가 빠졌으며, `catId`라는 존재하지 않는 필드를 참조합니다. 수업 배포용으로는 수정이 필요합니다.
- **실습 3 JSON**: Featured Media 미설정(가이드의 ⭐ 핵심 단계 누락).
- **노드 수 표기 불일치**: 4교시 본문 "총 13개 노드", 수료 체크리스트·핵심 정리는 "11개(노드)", 실제 JSON은 12개.
- **카테고리 ID 불일치**: 사전 준비 메모 예시는 트렌드=2…룩북=6인데, Code의 `categoryMap`은 트렌드=3…룩북=7입니다. 2교시 예상 출력은 스타일링=3, 3-3 예상 출력은 스타일링=4입니다. 가이드가 "환경마다 ID가 다를 수 있음"이라고 단서를 달긴 했습니다. 2교시 체크포인트의 "카테고리 ID 매핑이 포함됨"은 실제로는 3교시 이미지 프롬프트 Code에서 처리됩니다.
- **OpenAI 응답 참조 경로 혼재**: 「핵심 Expression 표현」과 4교시 Code_아이디어선택 예시는 `$json.message.content`인데, 실제 JSON과 1·2교시 코드는 `$json.output[0].content[0].text`(OpenAI 노드 v2.1)를 씁니다. JSON 쪽이 현행 노드에 맞습니다(추정).
- **모델명 혼재**: 설정표·JSON은 `GPT-4.1-MINI`인데, 1교시 문제 해결은 "모델명이 `gpt-4o-mini`인지 확인", 비용표는 "GPT-4o-mini"라고 적혀 있습니다.
- **노드명 참조 혼재**: 가이드 3-2는 `$('Code in JavaScript1')`, 최종 보고와 미디어병합은 `$('Code')`를 쓰는데, JSON의 노드명 체계(품질 체크 = "Code in JavaScript", 이미지 프롬프트 = "Code")와 다릅니다.
- **Schedule 버전 JSON 없음**: 4-2의 `실습4_스케줄_버전`(요일 로테이션 Code)은 가이드 코드로만 존재합니다.
- docker-compose.yml이 별도 파일로 들어 있지 않아 가이드 본문에서 복사해야 합니다.

### 6-3. 실행 환경
- **완전 셀프호스팅(로컬 Docker)** 전제입니다. n8n Cloud 사용 안내는 없습니다. n8n에서 WordPress를 호출할 때는 서비스명 `http://wordpress`를 써야 한다는 점이 가장 중요한 개념으로 강조됩니다.
- n8n은 `latest` 태그라서 시점에 따라 2.12.3과 UI·노드 버전이 달라질 수 있습니다. 버전을 고정(`n8nio/n8n:2.12.3`)하는 것이 좋습니다.
- Schedule은 PC가 켜져 있을 때만 동작하므로 24시간 운영에는 VPS 이전이 필요하다고 명시합니다.
- 비용: OpenAI 월 $5~8(월 20~30개 글), Gemini 이미지는 무료 티어(가이드 기준).

### 6-4. 샘플 미디어
- 이 zip에는 이미지·오디오 등 샘플 미디어가 **없습니다**. 이미지는 실습 중 Gemini가 생성하고, 입력값은 모두 Edit Fields/Code 고정값입니다.

---

## 7. 활용 포인트

1. **「AI 블로그 자동 발행 머신」 템플릿 상품화**: 실습 3(보강판)과 실습 4를 완성 상태로 고쳐서(본문 노드, HTTP 업로드, Featured Media, `카테고리ID`, FALSE 분기) docker-compose 키트(.env 분리)와 함께 판매합니다. 패션 외에 뷰티·인테리어·여행·IT 리뷰 등 **카테고리별 프롬프트 팩**으로 버티컬을 복제하기 쉽습니다(`prompts`·`categoryMap`·톤만 교체).
2. **4시간 → 6·8시간 단계형 강의 라인업**: 가이드가 직접 예고한 6시간(RSS 트렌드 수집·콘텐츠 캘린더·다중 AI 교차 검수·이미지 SEO)과 8시간(MCP·Webhook·고급 Code) 과정을 후속 상품으로 설계합니다. 사전 준비(Docker)는 "설치 대행·원격 세팅" 유료 옵션으로 분리할 수 있습니다.
3. **블로그 콘텐츠 자동화 SaaS의 핵심 모듈 재사용**: 「11항목 품질 채점 + S/A/B/C 등급 + IF 게이트」와 「SEO 구조 → 본문」 2단 프롬프트를 SaaS 백엔드(예: 블로그 팩토리류 서비스)의 검수 엔진으로 옮깁니다. WordPress 외에 네이버 블로그·티스토리·Ghost용 발행 어댑터를 붙이면 멀티 채널 발행 기능이 됩니다.
4. **에이전시형 "운영 대행" 서비스**: 4-2 요일 로테이션 + Draft 저장 + "운영 5계명"을 바탕으로, 쇼핑몰·인플루언서에게 VPS에서 매일 초안을 자동 생성하고 사람이 검수·발행하는 월정액 대행 상품을 만듭니다. E-E-A-T 보강(실착 후기 입력 폼)을 추가 기능으로 넣을 수 있습니다.
5. **강의 교재 품질 개선판(차별화)**: 문서의 불일치(모델명, 응답 경로, 카테고리 ID, 노드명, 노드 수)와 보안 설정(평문 DB 비밀번호, HTTP 쿠키)을 바로잡은 "검증 완료판 + 오류 해결 체크리스트"를 만들면, 같은 주제의 경쟁 강의보다 신뢰도가 높은 교재가 됩니다.
