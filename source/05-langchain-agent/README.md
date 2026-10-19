# 05-langchain-agent — LangChain(LCEL) 프롬프트 → RAG → Agent·Gradio 챗봇 → Whisper 음성 RAG → LangGraph 멀티에이전트까지 14일 실습 Colab 노트북 세트

> - **출처 형태**: 업로드한 zip `교육과정.zip`, 원본 저장소 없음 — 자동 동기화 대상 아님
> - **총 파일 수**: 56개 (ipynb 16 · mp3 40, 이 README 제외). 원본 zip에는 README / LICENSE 없음
> - **총 용량**: 104,480,562 바이트 (약 99.6 MB) — 노트북 16개 2,537,199 바이트(약 2.4 MB) + mp3 40개 101,943,363 바이트(약 97.2 MB)
> - **자료 성격**: LangChain 강의 14일치(day01~day14)의 Google Colab 실습 노트북입니다. 날짜마다 노트북 1개가 기본이고, 6일차·12일차는 **`배포`(빈칸 실습용)와 `배포완성`(완성본)** 2개가 짝으로 들어 있습니다. 1일차·11일차는 `배포완성`만, 나머지는 `배포`만 있습니다. 실습용 노트북도 **강사가 한 번 실행한 출력이 그대로 남은 상태에서 코드만 지운 형태**라, 빈칸 셀 아래에 정답 실행 결과가 보입니다. 13일차 폴더에는 Whisper 실습용으로 보이는 한국어 읽기 교재 음성 mp3 40개가 함께 들어 있습니다.

---

## 1. 한눈에 보기

| 항목 | 내용 |
|---|---|
| 주제 | LangChain 최신 표준(LCEL `prompt \| model \| parser`) 기반 LLM 앱 개발: 프롬프트 템플릿·Few-shot → LCEL 복합 체인·라우팅·출력 파서 → Document Loader → Runnable 인터페이스 → RAG(FAISS·Chroma, 메모리, 하이브리드 검색) → Gradio PDF 챗봇 → Whisper 음성 RAG·회의록 멀티에이전트 → LangGraph 메일 에이전트 |
| 추정 대상 | Python 기초가 있고 LLM 앱(챗봇·RAG·에이전트)을 처음 만들어 보는 개발 입문자·국비/부트캠프 수강생 (추정). 셀마다 "기존 코드(legacy) vs 개선 코드(최신 LCEL)" 비교와 줄 단위 주석이 붙어 있고, 날짜마다 `문제)`·`TODO` 실습이 이어짐 |
| 구성 (14일차) | D1~D3 프롬프트 / D4~D5 LCEL 복합 체인·출력 파서 / D6 문서 로더 / D7 Runnable 인터페이스 / D8~D9 RAG 기초·파이프라인·메모리 / D10~D11 다문서 RAG QA 챗봇(Chroma·임베딩·VectorStore) / D12 Gradio PDF 챗봇 / D13 Whisper 음성 RAG·멀티에이전트·LangGraph / D14 LangGraph 메일 작성 에이전트 |
| 실행 환경 | Google Colab (출력 경로 기준 Python 3.12), CPU로도 실행 가능한 구성 (노트북 메타데이터에 GPU 지정 없음). Colab 전용 기능(`google.colab.userdata`, `files.upload()`, `drive.mount()`)을 씀 |
| 자료 형식 | ipynb 16개(셀 출력 포함 — 실행된 상태) + mp3 40개(44.1 kHz 스테레오 320 kbps) |
| 핵심 키워드 | `ChatOpenAI`, `ChatPromptTemplate.from_messages`, `PromptTemplate`, `FewShotPromptTemplate`·`FewShotChatMessagePromptTemplate`, `SemanticSimilarityExampleSelector`, LCEL `\|`, `StrOutputParser`·`CommaSeparatedListOutputParser`·`JsonOutputParser`(+Pydantic), `RunnablePassthrough`(`.assign`)·`RunnableParallel`·`RunnableLambda`·`ConfigurableField`·`@chain`, `stream/batch/ainvoke/abatch/astream`, PyPDF·Docx2txt·CSV·WebBase·Text·Directory·PDFPlumber·PyMuPDF Loader, Character/RecursiveCharacterTextSplitter(tiktoken), OpenAIEmbeddings·HuggingFace(ko-sbert-nli, bge-m3-korean), FAISS·Chroma, BM25 + EnsembleRetriever, MMR, `RunnableWithMessageHistory`, Multi Query·Query Rewriting, Gradio `Blocks`/`ChatInterface`, Whisper(`whisper-1` API·로컬 `small`), LangGraph `StateGraph`·조건부 엣지·Supervisor |

---

## 2. 폴더·파일 구성

```
05-langchain-agent/
├── day01/  1일차_LangChain_프롬프트_1_new_배포완성.ipynb
├── day02/  2일차_LangChain_프롬프트-2_new_배포.ipynb
├── day03/  3일차_LangChain_Few-shot 프롬프트_new_배포.ipynb
├── day04/  4일차_LCEL_LangChain_복합체인_모델_출력파서_new_배포.ipynb
├── day05/  5일차_LCEL_JSON 파서 문제 풀이_new_배포.ipynb
├── day06/  6일차_LCEL_LangChain_Document_Loaders_new_배포.ipynb
│           6일차_LCEL_LangChain_Document_Loaders_new_배포완성.ipynb
├── day07/  7일차_LLM_LCEL 인터페이스_Runnable Interface_new_배포.ipynb
├── day08/  8일차_LLM_LCEL_Runnable Interface_RAG_기본_사용법_new배포_.ipynb
├── day09/  9일차_RAG LCEL_파이프라인_배포_new.ipynb
├── day10/  10일차_Agent_LLM_여러 문서에서 답변찾는 RAG 기반_QA챗봇_시스템 단계-1_배포_new.ipynb
├── day11/  11일차_Agent_LLM_여러_문서에서_답변찾는_RAG_기반_QA챗봇_시스템_단계_2_배포완성_new.ipynb
├── day12/  12일차_Agent_Gradio_PDF 파일 기반_챗봇_배포_new.ipynb
│           12일차_Agent_Gradio_PDF_파일_기반_챗봇_배포완성_new.ipynb
├── day13/  13일차_Agent_음성을 텍스트로 변환하기_RAG+Whisper 모델+gradio_배포_new.ipynb
│           문화가 있는 한국어 읽기_mp3/   문화가 있는 한국어 읽기 1_01.mp3 ~ 1_40.mp3 (40개)
└── day14/  14일차. Langgraph_Agent_메일 작성기 응용+gradio_배포_new.ipynb
```

| 경로 | 형식 | 크기 | 역할 |
|---|---|---|---|
| day01/1일차_LangChain_프롬프트_1_new_배포완성.ipynb | ipynb | 30.3 KB | **완성본** (셀 16개, 빈칸 없음). 실습용 짝 없음 |
| day02/2일차_LangChain_프롬프트-2_new_배포.ipynb | ipynb | 50.0 KB | **실습용** (셀 24개, 빈칸 셀 4개 + TODO 문제 4개) |
| day03/3일차_LangChain_Few-shot 프롬프트_new_배포.ipynb | ipynb | 52.7 KB | **실습용** (셀 28개, 빈칸 셀 약 10개) |
| day04/4일차_LCEL_LangChain_복합체인_모델_출력파서_new_배포.ipynb | ipynb | 112.7 KB | **실습용** (셀 57개, 빈칸 셀 약 18개) |
| day05/5일차_LCEL_JSON 파서 문제 풀이_new_배포.ipynb | ipynb | 19.1 KB | **실습용** (셀 19개). 4일차 후반부(출력 파서·문제 2개)를 다시 싣고 문제 1개 추가 |
| day06/6일차_LCEL_LangChain_Document_Loaders_new_배포.ipynb | ipynb | 183.4 KB | **실습용** (셀 45개, 빈칸 셀 약 9개) |
| day06/6일차_LCEL_LangChain_Document_Loaders_new_배포완성.ipynb | ipynb | 205.6 KB | **완성본** (셀 51개). 실습용에 셀 6개 추가 |
| day07/7일차_LLM_LCEL 인터페이스_Runnable Interface_new_배포.ipynb | ipynb | 141.7 KB | **실습용** (셀 81개, 빈칸 셀 약 26개) |
| day08/8일차_LLM_LCEL_Runnable Interface_RAG_기본_사용법_new배포_.ipynb | ipynb | 81.8 KB | **실습용** (셀 34개, 빈칸 셀 약 6개) |
| day09/9일차_RAG LCEL_파이프라인_배포_new.ipynb | ipynb | 134.5 KB | **실습용** (셀 52개, 빈칸 셀 약 8개) |
| day10/10일차_…_단계-1_배포_new.ipynb | ipynb | 259.4 KB | **실습용** (셀 69개, 빈칸 셀 약 14개) |
| day11/11일차_…_단계_2_배포완성_new.ipynb | ipynb | 404.0 KB | **완성본** (셀 59개, 마지막 실행 셀 1개에만 빈칸 남음). 실습용 짝 없음 |
| day12/12일차_Agent_Gradio_PDF 파일 기반_챗봇_배포_new.ipynb | ipynb | 232.7 KB | **실습용** (셀 56개, 빈칸 셀 약 19개) |
| day12/12일차_Agent_Gradio_PDF_파일_기반_챗봇_배포완성_new.ipynb | ipynb | 287.0 KB | **완성본** (셀 56개). 단, 후반부(카톡·텔레그램 챗봇 등) 셀 8개는 빈칸이 그대로 |
| day13/13일차_Agent_음성을 텍스트로 변환하기_RAG+Whisper 모델+gradio_배포_new.ipynb | ipynb | 216.4 KB | **실습용** (셀 49개, 빈칸 셀 약 14개). 안에 `정답` 셀 포함 |
| day13/문화가 있는 한국어 읽기_mp3/*.mp3 (40개) | mp3 | 1.38~4.22 MB (합계 약 97.2 MB) | 13일차 Whisper 전사 실습용 음성 (추정). 곡당 36.2~110.6초, 평균 63.7초, 합계 약 42.5분 |
| day14/14일차. Langgraph_Agent_메일 작성기 응용+gradio_배포_new.ipynb | ipynb | 66.4 KB | **실습용** (셀 17개, 빈칸 셀 약 7개) |

> 빈칸 수는 `변수 =` 뒤가 비어 있는 줄과 `add_edge( )`처럼 인자가 빠진 줄을 센 값이라 근사치입니다. 실습용·완성본 모두 셀 출력이 남아 있습니다(빈칸 셀도 정답 실행 결과가 보임).

---

## 3. Day별 상세 내용

### 공통 구성
- **노트북 첫머리**: `!pip install -qU langchain langchain-openai langchain-community langchain-text-splitters` + `faiss-cpu tiktoken python-dotenv` 설치 → `os.environ['OPENAI_API_KEY'] = userdata.get("OPENAI_API_KEY")`(Colab Secrets) 셀이 거의 매일 반복됩니다.
- **코드 서술 방식**: D7 이후 코드 셀은 `# 1. 상세 설명` → `# 2. 기존 코드 (원본 유지)` → `# 3. 개선 코드 (…)` → `# 4. 라인별 주석` → `# 5. 핵심 포인트` 형식이 많고, legacy 코드(`LLMChain`, `langchain.prompts`, `chatgpt(...)` 직접 호출, `get_relevant_documents`, `RetrievalQA…`)를 주석으로 남긴 뒤 최신 LCEL로 바꿔 씁니다.
- **실습 방식**: `문제)` 마크다운 + `# TODO N` 블록(요구사항·입력 예시·출력 예시 포함)으로 직접 채우게 합니다. 정답 코드는 해당 Day 완성본이나 같은 노트북의 다음 셀에 있는 경우가 있습니다.
- **기본 모델**: `ChatOpenAI(model="gpt-4o-mini")`가 기본이고, `gpt-4o`, `gpt-4.1-mini`, `gpt-3.5-turbo`, `gpt-4`(legacy 예제)도 등장합니다.

---

### Day 1 — 「LangChain 프롬프트 1」 (완성본)

**학습 목표 (노트북 내용 기준 정리)**: 프롬프트 작성 6대 원칙과 템플릿 4요소(지시·예시·맥락·질문)를 이해하고, legacy `PromptTemplate` 문자열 방식을 최신 `ChatPromptTemplate` + LCEL로 바꾸며, `RunnableWithMessageHistory`로 대화형 Gradio 챗봇을 만든다.

**주요 목차**: `프롬프트 (Prompt) 정의` → `챗 프롬프트 템플릿` → `리팩토링 요약` → `assist() 대신 체인 생성 (standard runnable composition)` → `Gradio 웹 UI에서 ChatGPT처럼 대화 가능`

**실습 항목**
| 셀 | 하는 일 |
|---|---|
| legacy 문자열 템플릿 | `PromptTemplate.from_template('… {name} … {age}')` → `.format()` |
| 최신 표준 리팩토링 | `ChatPromptTemplate.from_template` + `ChatOpenAI(model="gpt-4o-mini", temperature=0.7)` + `StrOutputParser()`, `chain.invoke({...})` |
| 템플릿 결합 | legacy `PromptTemplate + PromptTemplate + 문자열` vs `ChatPromptTemplate.from_messages([("human", …) × 3])` (번역 예제) |
| 메시지 유형 | SystemMessage / HumanMessage / AIMessage / FunctionMessage / ToolMessage 설명 |
| 기술 문서 작성기 | system 프롬프트로 `## 개요 / ## 핵심 개념 / ## 파이썬 코드 예제 / ## 참고 자료` 마크다운 구조 강제 (`gpt-4o`) |
| Gradio 대화형 챗봇 | `MessagesPlaceholder("history")` + `ChatMessageHistory` 세션 저장소 + `RunnableWithMessageHistory` → `gr.ChatInterface(fn=respond).launch(share=True)` |

**사용 라이브러리·클래스·모델**: `langchain_core.prompts`(PromptTemplate, ChatPromptTemplate, MessagesPlaceholder), `StrOutputParser`, `ChatOpenAI`(gpt-4o-mini, gpt-4o, 기본값), `RunnableWithMessageHistory`, `langchain_community.chat_message_histories.ChatMessageHistory`, `gradio`

**실습용 vs 완성본**: 완성본만 있음.

---

### Day 2 — 「LangChain 프롬프트 2」 (실습용)

**학습 목표 (정리)**: LangGraph로 상태 기반 어시스턴트의 뼈대를 맛보고, `chain.stream()`, `SystemMessagePromptTemplate`/`HumanMessagePromptTemplate`, legacy → LCEL 변환, 다단계 LCEL 파이프라인과 `RunnableLambda` 분기를 연습한다.

**주요 목차**: `LangGraph + LangChain OpenAI 를 활용한 Assistant` → `LangChain chain.stream() 활용 예제` → `MessagePromptTemplate` → `ChatCPT와 프롬프트템플릿을 활용하여 대화하기` → `문제) 아래 문제를 전부 LCEL 방식 (prompt | model | parser) 기반으로 해결하라.` → `문제) ChatPromptTemplate.from_messages()를 다루는 문제입니다.`

**실습 항목**
| 구분 | 내용 |
|---|---|
| LangGraph 어시스턴트 (빈칸) | `class State(TypedDict)` + `add_messages`, `chatbot` 노드, `StateGraph` → `START → chatbot → END`, `compile()`, 그래프 이미지 출력. Mermaid 출력(https://mermaidviewer.com/ko 에 붙여넣기 안내), `graphviz.Digraph`로 노드·엣지 직접 그리기 |
| 스트리밍 (빈칸) | `for chunk in chain.stream(...)` |
| MessagePromptTemplate (빈칸) | System/Human 템플릿 객체 방식 → 튜플 방식 권장 |
| 요리사 프롬프트 | `<재료>{ingredients}</재료>` 태그 입력, legacy `chatgpt(chat_prompt.format_prompt(...).to_messages())` → LCEL 리팩토링(빈칸) |
| LCEL STRUCTURE MASTER EXERCISE (TODO 0~6) | 문서 생성기 / legacy `SystemMessage+HumanMessage` 문법 교정기 → LCEL / 요약 체인 / **2-stage pipeline**(질문 재작성 → 답변) / `RunnableLambda` 길이 기반 라우터(expand vs summarize) |
| from_messages MASTER EXERCISE | 기본(파이썬 강사) / 심화 1(AI 메시지 포함 여행 대화) / 심화 2(변수 여러 개: food·budget·people) |

**사용 라이브러리·클래스·모델**: `langgraph.graph`(StateGraph, START, END), `add_messages`, `graphviz`, `ChatPromptTemplate`, `SystemMessagePromptTemplate`, `HumanMessagePromptTemplate`, `RunnableLambda`, `ChatOpenAI`(gpt-4o-mini, gpt-4o)

**실습용 vs 완성본**: 실습용만 있음. LangGraph 셀은 State·노드·그래프 구성 줄이 비어 있고 출력은 남아 있습니다.

---

### Day 3 — 「LangChain Few-shot 프롬프트」 (실습용)

**학습 목표 (정리)**: Zero-shot과 Few-shot의 차이를 보고, `FewShotPromptTemplate` → `SemanticSimilarityExampleSelector`(Chroma) → `FewShotChatMessagePromptTemplate` 순서로 고정·동적 예제 선택을 익힌다.

**주요 목차**: `문제) ChatPromptTemplate.from_messages()…`(심화 3·4) → `Few-shot Prompt` → `Few-shot 예제 포맷터 사용` → `Few-Shot 학습의 모델 성능을 향상시키는 방법`(고정예제/동적예제) → `최신 권장 코드 (LCEL + ChatPromptTemplate 통합)` → `특징`(LangGraph + Chroma) → `문제) Few-shot prompting (LCEL 최신 방식 기준)`

**실습 항목**
| 구분 | 내용 |
|---|---|
| 심화 문제 3·4 | Markdown 형식 강제 답변 / 번역기(`{text}`, `{language}`) |
| 삼행시 Few-shot | 예시(호날두·김민재) → "손흥민" 삼행시, Few-shot 사용 vs 미사용 비교, `chatgpt.invoke([...])` |
| 과학 Q&A Few-shot | 예제 6개(대기 질소, 광합성, 피타고라스 등) + `PromptTemplate('질문 : {question}\n답변 : {answer}\n')` |
| 예제 선택기 | `SemanticSimilarityExampleSelector` + `Chroma` + `OpenAIEmbeddings`, `from_vectorstore` 방식 |
| 고정 예제 | `FewShotChatMessagePromptTemplate` + 최종 `ChatPromptTemplate` 조합 |
| LangGraph + 예제 선택기 | `assistant_node`에서 마지막 메시지로 유사 예제 선택 → LLM 호출, `app.stream(inputs)`, `draw_mermaid_png()`로 그래프 저장 |
| FEW-SHOT LCEL MASTER EXERCISE | 문장 교정기 few-shot(`"i goes to school yesterday"` 등) |

**사용 라이브러리·클래스·모델**: `FewShotPromptTemplate`, `FewShotChatMessagePromptTemplate`, `SemanticSimilarityExampleSelector`, `langchain_chroma.Chroma`, `chromadb`, `OpenAIEmbeddings`, `langgraph`, `ChatOpenAI`(gpt-4o-mini, gpt-4o)

**실습용 vs 완성본**: 실습용만 있음. Chroma 설치 시 opentelemetry 버전 충돌을 피하려고 `opentelemetry-*==1.24.0`으로 재설치하는 셀이 있습니다.

---

### Day 4 — 「LCEL: LangChain 복합 체인 · 모델 · 출력 파서」 (실습용)

**학습 목표 (정리)**: LCEL 기본 체인(프롬프트·모델·파서)을 만들고, FAISS로 "문맥만 기반으로 답하는" 미니 RAG, 분류기 기반 라우팅(복합 체인), 모델 파라미터·`bind()`, CSV/JSON 출력 파서를 익힌다.

**주요 목차**: `프롬프트 템플릿 적용` → `LCEL` → `템플릿 내용 변경하여 테스트` → `문맥만을 기반으로 답변을 생성하는 체인` → `LangChain Expression Language에서 라우팅을 수행하는 방법` → `복합 체인(Composite Chain)이란?` → `RunnableLambda로 동적 분기` → `LangChain의 언어 모델(Model)` → `LangChain의 LLM 모델 파라미터` → `문제) 다음의 조건을 보고 리팩토링 하시오.` → `LLM 모델 파라미터를 추가로 바인딩` → `출력 파서 (Output Parser)` → `실무 예시: JsonOutputParser 활용` → `문제) sonOutputParser를 활용한 여행 일정 생성기` → `문제) JsonOutputParser를 활용한 AI 이력서 평가 시스템`

**실습 항목**
| 구분 | 내용 |
|---|---|
| 천문학 전문가 프롬프트 | `from_template` vs system 메시지 분리("30년 경력의 천문학 전문가") |
| AIMessage vs 문자열 | 파서 없이 `.content` / `StrOutputParser()` 사용 비교 |
| 영어 회화 템플릿 | "10년차 영어 선생님", `[FORMAT]`(영어 회화·한글 해석) |
| 미니 RAG | `FAISS.from_texts` → `as_retriever()` → `{"context": retriever, "question": RunnablePassthrough()}` → `chain.get_graph().print_ascii()`(grandalf), `RunnableLambda` 버전과 nodes/edges 출력 |
| 라우팅 | legacy: 분류 체인(수학/과학/기타) + 체인 3개 개별 호출(`gpt-4`) → 개선: `{"topic": classifier, "question": RunnablePassthrough()} \| RunnableLambda(route)` 단일 체인, `router_chain = RunnableLambda(router)` |
| 모델 파라미터 | Temperature, Max Tokens, Top P, Frequency/Presence Penalty, Stop Sequences 설명, `llm_params` 딕셔너리 언패킹 + `model_kwargs`(stop=["\n"]) 리팩토링 문제, `bind(max_tokens=50)` |
| 출력 파서 | `CommaSeparatedListOutputParser`(`get_format_instructions()`), `JsonOutputParser`(+`partial_variables`), Pydantic `CusineRecipe` 스키마 |
| 문제 | 여행 일정 생성기(제주도 3일 → destination/days/schedule) / AI 이력서 평가(name, career_level, skills, strengths, weaknesses, score, interview_questions) |

**사용 라이브러리·클래스·모델**: `PromptTemplate`, `ChatPromptTemplate`, `StrOutputParser`, `CommaSeparatedListOutputParser`, `JsonOutputParser`, `pydantic.BaseModel/Field`, `RunnablePassthrough`, `RunnableLambda`, `FAISS`, `OpenAIEmbeddings`, `grandalf`, `ChatOpenAI`(gpt-4o-mini, gpt-4o, gpt-4)

**실습용 vs 완성본**: 실습용만 있음.

---

### Day 5 — 「LCEL JSON 파서 문제 풀이」 (실습용)

**학습 목표 (정리)**: `JsonOutputParser` + Pydantic 스키마 + `get_format_instructions()` 패턴을 문제 3개로 반복 연습한다.

**주요 목차**: `출력 파서 (Output Parser)` → `실무 예시: JsonOutputParser 활용` → `문제) sonOutputParser를 활용한 여행 일정 생성기` → `문제) JsonOutputParser를 활용한 AI 이력서 평가 시스템` → `문제) JsonOutputParser를 활용한 고객 문의 자동 분류 시스템`

**실습 항목**: 4일차 cell 43~56(CSV·JSON 파서 예제 + 문제 2개)과 같은 내용 + **고객 문의 자동 분류 문제**(category, priority, sentiment, summary, recommended_action — 예: "주문한 상품이 아직 도착하지 않았습니다" → 배송/높음/부정). 모든 문제는 TODO 주석만 있고 코드가 비어 있습니다.

**사용 라이브러리·클래스·모델**: `CommaSeparatedListOutputParser`, `JsonOutputParser`, `PromptTemplate`, `pydantic`, `ChatOpenAI`(gpt-4o-mini)

**실습용 vs 완성본**: 실습용만 있음. 첫 코드 셀이 비어 있습니다.

---

### Day 6 — 「LCEL: LangChain Document Loaders」 (실습용 + 완성본)

**학습 목표 (문제 셀 `[학습 목표]` 원문 요약)**: 1) 다양한 Document Loader를 사용할 수 있다 2) 파일 확장자에 따라 적절한 Loader를 선택할 수 있다 3) LCEL로 문서를 요약할 수 있다 4) 여러 Document를 하나의 문자열로 결합해 종합 분석할 수 있다 5) `JsonOutputParser`로 구조화된 JSON을 생성할 수 있다.

**주요 목차**: `문서 로더`(load / load_and_split / lazy_load / aload) → `URL Document Loader` → `PDF Document Loader` → `Word Document Loader` → `CSV Document Loader` → `LangChain 외 방식으로 텍스트 추출하기` → `문제) PDF + Word + CSV 자동 판별기` → `문제) Multi Document Analyzer(여러 문서 업로드 및 통합 분석)` → `문제) Universal AI Document Analyzer (JSON 출력)` → (완성본만) `ngrok 토큰 발급 방법`

**실습 항목**
| 구분 | 내용 |
|---|---|
| WebBaseLoader | 네이버 뉴스 기사 URL 로드, `page_content[:500]` |
| PyPDFLoader | Google Drive의 `[이슈리포트 2022-2호] 혁신성장 정책금융 동향.pdf` → `load_and_split()`(18페이지), metadata 확인 |
| Docx2txtLoader | `해커톤.docx`(식단 기반 영양제 추천 서비스 기획서) |
| CSVLoader | `최종 필터링 데이터 (호텔, 지형) - 시트3.csv`(Country·City·hotel·mountain·beach·plain), 전체 행을 하나의 `Document`로 합친 뒤 `PromptTemplate`(`{content}`, `{query}`)로 "산이 포함된 도시의 호텔" 표 답변 |
| LangChain 외 추출 | PyMuPDF(`fitz`, 샘플 PDF 다운로드) / python-pptx / python-docx / openpyxl / **HWP**(`olefile` + `zlib` + `struct`로 BodyText 섹션 레코드 67 파싱, 한글 정규식 정제) — `files.upload()`로 업로드 |
| 문제 1 자동 판별기 | `os.path.splitext()` → pdf/docx/csv Loader 선택 → 5줄 요약 |
| 문제 2 Multi Document Analyzer | 여러 파일 업로드 → `documents.extend()` → 종합 분석 |
| 문제 3 Universal Analyzer | PDF·DOCX·CSV·TXT·MD(`TextLoader`, `UnstructuredMarkdownLoader` 등) + Pydantic + `JsonOutputParser`(documents[filename, summary] / keywords / overall_summary / recommendation) |

**사용 라이브러리·클래스·모델**: `langchain_community.document_loaders`(WebBaseLoader, PyPDFLoader, Docx2txtLoader, CSVLoader, TextLoader, UnstructuredMarkdownLoader, UnstructuredExcelLoader, UnstructuredPowerPointLoader), `langchain_core.documents.Document`, `pypdf`, `unstructured`, `pdf2image`, `docx2txt`, `pdfminer`, `PyMuPDF`, `python-pptx`, `python-docx`, `openpyxl`, `olefile`, `msoffcrypto-tool`, `pandas`, `ChatOpenAI`(gpt-4o-mini / 완성본 gpt-4o)

**실습용 vs 완성본 차이**
| 항목 | 실습용(`배포`) | 완성본(`배포완성`) |
|---|---|---|
| 셀 수 | 45 | 51 (+6) |
| Drive 마운트 | `drive.mount` 코드 비어 있음 | `drive.mount("/content/drive")` 작성 |
| Loader 코드 | `loader =`, `data =`, `pages =` 빈칸 | 모두 작성 |
| CSV | `csv_args` 없음 → 첫 행이 빈 값 Document | `csv_args`(delimiter·quotechar·fieldnames) 지정 + **pandas `read_csv(header=1)`로 행별 Document 직접 만드는 셀 2개 추가** |
| 데이터 경로 | `/content/drive/MyDrive/AI_ChatBot/LLM_원본/자료/…` | `/content/drive/MyDrive/AI_멀티_MultiAgent/Multi_Agent_2607/Agent_2607/Agent_data/…` (pandas 셀은 이전 경로 그대로) |
| 문제 1·2 | TODO만 | 정답 코드 작성 (TODO에는 `gpt-4.1-mini`라 적혀 있으나 정답은 `gpt-4o`) |
| 문제 3 (Universal) | TODO만 | **TODO만 (완성본에도 미작성)** |
| 기타 | — | 끝에 `ngrok 토큰 발급 방법` 마크다운 (이 노트북에서 ngrok 코드는 쓰지 않음) |

---

### Day 7 — 「LLM · LCEL 인터페이스 · Runnable Interface」 (실습용)

**학습 목표 (정리)**: LLM vs Chat Model 인터페이스, 순차 체인 연결, Runnable 프로토콜(`invoke/batch/stream` + 비동기 `ainvoke/abatch/astream`), `RunnableParallel`·`RunnablePassthrough`(`.assign`)·`RunnableLambda`, 런타임 구성(`ConfigurableField`), `@chain` 데코레이터와 커스텀 `Runnable` 클래스를 익힌다.

**주요 목차**: `LLM(Model)` → `Chat Model 인터페이스` → `LCEL 응용`(멀티 체인) → `순차적인 체인연결` → `LCEL 인터페이스` → `체인을 실행하는 방법` → `batch + stream 개념` → `문제)` → `비동기 실행을 위한 개선 코드를 작성하시오.` → `RunnableParallel` → `batch()에서의 병렬 처리` → `데이터를 효과적으로 전달하는 방법`(RunnablePassthrough) → `RunnableLambda를 사용하여 사용자 정의 함수 맵핑` → `RunnableLambda로 동적 분기` → `런타임에 체인 내부 구성하기` → `## 동적 속성 지정` → `@chain` 상세 설명 → 텍스트 전처리·요약·GPT 질의응답 파이프라인

**실습 항목**
| 구분 | 내용 |
|---|---|
| legacy 설치 | `langchain==0.3.27`, `langchain-core==0.3.79`, `langchain-openai==0.3.33`, `langchain-community==0.3.29`, `langchain-text-splitters==0.3.11`, `faiss-cpu==1.12.0`, `tiktoken==0.11.0`, `python-dotenv==1.1.1` 고정 설치 셀 |
| LLM vs Chat | `langchain_openai.OpenAI()`(completion) vs `ChatOpenAI` — 한국 관광지 5곳 |
| 순차 체인 | chain1(한국어→영어) 출력을 `{"english_word": chain1}`로 chain2(옥스퍼드 사전식 설명)에 연결 |
| Runnable 실행 | `stream`(flush=True) / `invoke` / `batch` / `batch(config={"max_concurrency": N})`, 순차 스트리밍, `nest_asyncio` + `async def` 안에서 `astream/ainvoke/abatch` (`asyncio.run()` 대신 `await`) |
| 문제 | `"{topic}에서 인공지능에 대해 간단히 설명해 주세요."` → invoke(컴퓨터 과학) / batch(로봇공학·사회경제학·인문학) / stream·ainvoke(자율주행자동차) |
| RunnableParallel | 수도·면적 체인 동시 실행 → `{'capital':…, 'area':…}`, batch와 결합 시 `List[Dict]` |
| RunnablePassthrough | `{num}의 100배는?`, 값만 넘기기(`chain.invoke(5)`), `.assign(new_num=lambda x: x['num']*3)`, `passed/extra/modified` 병렬 예제 |
| RunnableLambda | `get_today()`(datetime) → "오늘 날짜가 생일인 유명인" 체인, 수학/과학/기타 라우터 재사용 |
| 런타임 구성 | `configurable_fields` / `configurable_alternatives` 설명, `ConfigurableField`로 gpt-4o ↔ gpt-3.5-turbo ↔ gpt-4o-mini 교체, `with_config` |
| `@chain` | `RunnableLambda(add_one)` vs `@chain` 함수, dict 입력, prompt1(설명) → prompt2(영어 번역·이모지) `custom_chain` |
| 커스텀 Runnable | `CleanText` / `SummarizeText` / `AskGPT` 클래스(Runnable 상속) + `@chain` 파이프라인 / `ProcessPipeline` 클래스 |

**사용 라이브러리·클래스·모델**: `OpenAI`, `ChatOpenAI`(gpt-4o-mini, gpt-4o, gpt-3.5-turbo), `RunnableParallel`, `RunnablePassthrough`, `RunnableLambda`, `ConfigurableField`, `langchain_core.runnables.chain`, `Runnable`, `asyncio`, `nest_asyncio`

**실습용 vs 완성본**: 실습용만 있음. 빈칸 셀이 26개로 가장 많은 편입니다.

---

### Day 8 — 「LLM · LCEL · Runnable Interface · RAG 기본 사용법」 (실습용)

**학습 목표 (정리)**: RAG가 필요한 이유(최신 정보·사내 문서·환각)와 전체 흐름을 이해하고, Text Splitter → Embedding → FAISS → Retriever → LCEL RAG 체인을 처음부터 구성한다.

**주요 목차**: `# RAG(Retrieval-Augmented Generation)`(RAG란? / 필요한 이유 / 전체 동작 과정) → (RunnableParallel 복습) → `CharacterTextSplitter` → `RecursiveCharacterTextSplitter` → `# 실무 RAG 기본 아키텍처` → `RAG + LCEL 기반 AI 여행 플래너 서비스` → `문제) LCEL + FAISS 기반 RAG Chain 완성`

**실습 항목**
| 구분 | 내용 |
|---|---|
| Runnable 복습 | `{'country': RunnablePassthrough()} \| prompt \| ChatOpenAI()` 체인 2개를 `RunnableParallel(capital=…, area=…)`로 |
| Text Splitter | `CharacterTextSplitter` 예문 분할, `TextLoader`로 업로드한 `AI 최신 동향과 정책.txt` 분할(chunk_size·overlap 바꿔 개수·길이 비교), `RecursiveCharacterTextSplitter` 비교 ("실무 RAG 표준") |
| Vector DB | `OpenAIEmbeddings()` + `FAISS.from_documents()` + 유사도 검색 |
| 실무 RAG 기본 | `retriever` + `ChatPromptTemplate` + `gpt-4o-mini` + `RunnablePassthrough` → "이 문서의 핵심 내용은 뭐야?" |
| 도서 추천 RAG | 원본 문서(도서 목록) → FAISS → `format_docs` → `RunnableParallel` + `RunnableLambda` |
| 여행 플래너 문제 | TODO: question → retriever → context → prompt → llm → 문자열 (`gpt-4.1-mini`, `retriever_chain = retriever \| RunnableLambda(format_docs)`) |

**사용 라이브러리·클래스·모델**: `CharacterTextSplitter`, `RecursiveCharacterTextSplitter`, `TextLoader`, `OpenAIEmbeddings`, `FAISS`, `RunnableParallel`, `RunnablePassthrough`, `RunnableLambda`, `ChatOpenAI`(gpt-4o-mini, gpt-4.1-mini)

**실습용 vs 완성본**: 실습용만 있음.

---

### Day 9 — 「RAG LCEL 파이프라인」 (실습용)

**학습 목표 (정리)**: RAG 8단계(로드 → 분할 → 임베딩 → 벡터DB → 검색기 → 프롬프트 → LLM → 체인)를 PDF·웹 뉴스에 적용하고, Chat Memory, Multi Query, Conversational RAG(질문 재작성), BM25·FAISS·앙상블 리트리버 비교까지 확장한다.

**주요 목차**: `PDF 문서 기반 QA(Question-Answer)`(1~8단계) → `네이버 뉴스기사 QA(Question-Answer)` → `LLM에 들어가는 입력을 통제해서 RAG 결과를 안정화한 코드` → `LangChain 기반 RAG 워크플로우`(인덱싱 Offline / 검색+생성 Online) → `RAG 의 기능별 다양한 모듈 활용기` → `전체 기능 요약` → `# 개선된 실무용 RAG`(Chat Memory + Multi Query RAG) → `# 이전 대화를 기억하는 Chain 생성방법` → `## 1. 일반 Chain 에 대화기록 추가` → `## 2. RAG + RunnableWithMessageHistory` → `대화를 저장할 함수 정의 - 수동` → Conversational RAG → `청크 분할 실험:`

**실습 항목**
| 구분 | 내용 |
|---|---|
| PDF QA | `files.upload()`로 `★ 서울특별시 스마트도시 및 정보화 기본계획(홈페이지 게시용).pdf` → `PyPDFLoader` → `RecursiveCharacterTextSplitter` → FAISS → `gpt-4.1-mini` |
| URL PDF QA | `requests`로 PDF 다운로드 → `PyMuPDFLoader` (단, 지정 URL `https://spri.kr/posts/view/23908`은 웹페이지라 출력이 `문서에 없음`) |
| 뉴스 QA | `WebBaseLoader` + `bs4.SoupStrainer`로 본문만 추출(네이버 뉴스, 부영그룹 출산 장려 기사) → FAISS → `RunnableMap`, `format_docs`로 Document → string 강제 |
| Multi Query + Memory | 질문 하나를 유사 질문 여러 개로 생성 → 각각 검색·통합, `RunnableWithMessageHistory` + `ChatMessageHistory` |
| 대화 기록 체인 | `MessagesPlaceholder` + `session_id`("abc123")로 "제 이름은 홍길동" → "제 이름이 뭐죠?" |
| RAG + 메모리 | `PDFPlumberLoader` + `text-embedding-3-small` + `as_retriever(search_kwargs={"k": 3})` + `{chat_history}` 프롬프트, `itemgetter` 수동 버전 |
| Conversational RAG | chat history 기반 **Query Rewriter** → `build_context()` → 최종 프롬프트 |
| 리트리버 비교 | chunk_size/overlap 실험 함수, `BM25Retriever` + FAISS + `EnsembleRetriever(weights=[0.5, 0.5])`, `test_rag()` |

**사용 라이브러리·클래스·모델**: `PyPDFLoader`, `PyMuPDFLoader`, `PDFPlumberLoader`, `WebBaseLoader`, `bs4`, `RecursiveCharacterTextSplitter`(`langchain.text_splitter` 경로도 사용), `OpenAIEmbeddings`(기본, text-embedding-3-small), `FAISS`, `BM25Retriever`, `EnsembleRetriever`, `RunnableMap`, `RunnableParallel`, `RunnableWithMessageHistory`, `ChatMessageHistory`, `ChatOpenAI`(gpt-4o-mini, gpt-4.1-mini, gpt-3.5-turbo)

**실습용 vs 완성본**: 실습용만 있음. 앙상블 셀 앞에서 `langchain`(1.3.11)을 지우고 `langchain==0.3.0`으로 다시 설치합니다.

---

### Day 10 — 「Agent · LLM: 여러 문서에서 답변 찾는 RAG 기반 QA 챗봇 시스템 단계 1」 (실습용)

**학습 목표 (정리)**: TechCrunch 기사 21개로 Chroma 기반 다문서 RAG QA 챗봇을 만들고, 문서 로딩·청킹·Chunk 품질 평가·Chroma 저장/로드·Retriever·체인 구성, Text Splitter 종류(문자·재귀·토큰 단위)를 실무 관점에서 익힌다.

**주요 목차**: `여러 문서에서 찾아서 답변하는 챗봇 만들기`(QA Chatbot / Langchain / ChatGPT / ChromaDB) → `기본 구조` → `실무`(문서 로딩 / chunking / Chunk Quality 자동 평가) → `Create Chroma DB` → `Retriever 생성` → `Chain 생성` → `Query` → `Text Splitter` → `CharacterTextSplitter` → `RecursiveCharacterTextSplitter` → `토큰단위 텍스트 분할기` → `문제) 빈칸 채우기`

**실습 항목**
| 구분 | 내용 |
|---|---|
| 데이터 | `!wget -q https://github.com/kairess/toy-datasets/raw/master/techcrunch-articles.zip` → `articles/*.txt` 21개 |
| 기본 구조 (통합 버전) | 세션 메모리 + Query Rewriting + `build_context()` + Chroma + `RunnableWithMessageHistory` |
| 문서 로딩·청킹 | `DirectoryLoader('./articles', glob="*.txt", loader_cls=TextLoader)` → 233 chunk |
| Chunk Quality 리포트 | 너무 짧은/긴 chunk, 문장 깨짐 휴리스틱 / 임베딩 기반 내부 coherence·chunk 간 similarity(`sklearn` cosine) |
| Chroma DB | `Chroma.from_documents(persist_directory='db')` → `persist()` → 메모리 해제 → `Chroma(persist_directory=…)` 재로드 |
| Retriever·Chain | `as_retriever(search_kwargs={"k": …})`, `get_relevant_documents` → `invoke`, dict→string 래핑으로 타입 에러 회피, 직렬 RAG 함수 `rag_pipeline()`, legacy `RetrievalQA` 출력 함수 대체 `process_llm_response()` |
| Query 예 | "What is Generative AI?", Pando 투자 유치 금액, "CMA는 무엇인가?" |
| Text Splitter | 혁신성장 PDF + `tiktoken_len` + 한국어 임베딩 `jhgan/ko-sbert-nli` + FAISS 검색, `state_of_the_union.txt`로 Character vs Recursive chunk 길이 통계, 토큰 단위 분할 빈칸 문제 |

**사용 라이브러리·클래스·모델**: `DirectoryLoader`, `TextLoader`, `PyPDFLoader`, `CharacterTextSplitter`, `RecursiveCharacterTextSplitter`, `tiktoken`, `Chroma`(`langchain_community.vectorstores`), `chromadb`, `FAISS`, `OpenAIEmbeddings`, `HuggingFaceEmbeddings`(jhgan/ko-sbert-nli), `RunnableLambda`, `RunnablePassthrough`, `RunnableWithMessageHistory`, `numpy`, `scikit-learn`, `ChatOpenAI`(gpt-4o-mini, gpt-3.5-turbo)

**실습용 vs 완성본**: 실습용만 있음 (단계 2 = 11일차 완성본).

---

### Day 11 — 「Agent · LLM: 여러 문서에서 답변 찾는 RAG 기반 QA 챗봇 시스템 단계 2」 (완성본)

**학습 목표 (정리)**: RAG 3~4단계인 Embedding과 VectorStore를 깊게 다룬다 — OpenAI·HuggingFace·한국어 임베딩 비교, 코사인 유사도·Recall@K, FAISS 저장/로드·점수 검색·MMR, 그리고 FAISS·Chroma 기반 완성형 RAG 챗봇.

**주요 목차**: `여러 문서에서 찾아서 답변하는 챗봇 만들기` → `Embedding` → `OpenAIEmbeddings` → `Huggingface Embedding` → `한국어 사전학습 모델 임베딩`(ko-sbert-nli) → `한국어 파인 튜닝` → `VectorStore` → `Chroma` → `FAISS` → (FAISS vs Chroma 비교표) → `relevance score 의미` → `Retriever` → `FAISS + GPT LCEL 기반 완전 RAG 챗봇` → `여러 문서에서 답변찾는 RAG 기반_QA 에이전트`

**실습 항목**
| 구분 | 내용 |
|---|---|
| OpenAIEmbeddings | 문장 5개 → 1536차원, 질문/답변 임베딩, `cos_sim()` 직접 구현 |
| HuggingFace | `HuggingFaceBgeEmbeddings`(`BAAI/bge-small-en`, 384차원), "홍길동 아버지 이름" 유사도 실험 |
| 한국어 모델 | `jhgan/ko-sbert-nli`, `upskyy/bge-m3-korean`(Top-K 검색 + Recall@K 평가) |
| FAISS vs Chroma 표 | 저장 방식(인메모리 vs 디스크) / 장점 / 단점 / 적합한 용도 |
| FAISS 실습 | 혁신성장 PDF → tiktoken 분할 → ko-sbert-nli → `similarity_search_with_relevance_scores`, `save_local("faiss_index")` / `load_local` ("6대 먹거리 산업은?"), `max_marginal_relevance_search`(MMR) |
| 완전 RAG 챗봇 | `{"context": retriever \| format_docs, "question": RunnablePassthrough()}` + `gpt-3.5-turbo` (같은 구성 2회) |
| QA "에이전트" | TechCrunch 기사(`unstructured[local-inference]`, `python-magic`, `apt-get install -y libmagic1`) → Chroma(k=5) → `gpt-4o-mini` RAG 실행 루프. 끝에 "Agent + RAG 구조"(RAG Tool·Web Tool·Calculator Tool 선택) 설명만 문자열로 있음 |

**사용 라이브러리·클래스·모델**: `OpenAIEmbeddings`(기본, text-embedding-3-small 언급), `HuggingFaceBgeEmbeddings`, `HuggingFaceEmbeddings`, `sentence_transformers`, `FAISS`, `Chroma`, `DirectoryLoader`, `TextLoader`, `PyPDFLoader`, `tiktoken`, `ChatOpenAI`(gpt-3.5-turbo, gpt-4o-mini)

**실습용 vs 완성본**: 완성본만 있음. 마지막 TechCrunch RAG 셀의 embedding 모델명 등 몇 줄은 비어 있습니다. 마크다운은 `initialize_agent()`로 만든 에이전트라고 설명하지만, 실제 코드에는 `initialize_agent`·Tool 정의가 없고 LCEL RAG 체인만 있습니다.

---

### Day 12 — 「Agent · Gradio: PDF 파일 기반 챗봇」 (실습용 + 완성본)

**학습 목표 (정리)**: Gradio로 OpenAI 챗봇 UI를 만들고, PDF → FAISS → LCEL RAG 체인을 붙여 출처를 함께 보여 주는 PDF QA 챗봇, PDF 업로드형 챗봇, 카카오톡·텔레그램 스타일 UI까지 만든다.

**주요 목차**: `Agent_Gradio` → `그라디오 챗봇과 OpenAI API연동` → `PDF 파일 기반 질의 응답 챗봇`(랭체인·그라디오·ChatGPT) → `문제) 다음 기존 코드 (보존)를 참고하여 코드를 완성하시오.` → `Colab + Gradio 에서 실행 가능한 pdf 기반 QA 챗봇` → `문제) 다음 주어진 내용을 참고하여 카카오톡 대화창을 완성하시오. 단, css는 라이브코딩.` → `카톡 말풍선 적용 -> css 추가` → `개선된 챗봇`(텔레그램 스타일) → `#다음 대화 시 이전 대화 사라지는 텔레그램` → `# 일정시간 이후 대화 내용 사라지는 텔레그램 챗봇`

**실습 항목**
| 구분 | 내용 |
|---|---|
| Gradio + OpenAI SDK | `openai.OpenAI().chat.completions.create(model="gpt-4o-mini", max_tokens=256)`, `gr.Blocks` + `gr.Chatbot` + `gr.Textbox` + 초기화 버튼, "대화 종료" 버튼(`gr.update(interactive=False)`) |
| PDF RAG | KOCW 강의 PDF(`http://kocw-n.xcache.kinxcdn.com/data/keris/2023/keris0514/01.pdf`, "인공지능으로 인한 변화와 윤리적 이슈", 11쪽 → 26 chunk) → `text-embedding-3-small` + FAISS(k=2) → `ChatPromptTemplate` → "강의의 주요 내용은?", "자율자동차의 지원은?" |
| legacy 보존 문제 | `RetrievalQAWithSourcesChain`(주석) → LCEL 체인으로 재작성, `retriever.invoke()`로 source 문서 별도 출력 |
| Gradio PDF 챗봇 | 답변 + `[n] source (page)` 출처 문자열, messages 형식(`{"role", "content"}`) |
| PDF 업로드형 | `build_rag(pdf_file)` 전역 retriever, `gr.File` |
| 카카오톡 스타일 | `load_pdf → split_documents → create_embeddings → create_vectorstore → create_retriever → create_rag_chain` 함수 분리 + 말풍선 CSS |
| 텔레그램 스타일 | 답변 표시 후 2초 뒤 대화 삭제 / PDF Q&A(`Chroma` + `CharacterTextSplitter`, `gr.State`) 10초 후 자동 삭제 |

**사용 라이브러리·클래스·모델**: `gradio`(6.20.0 출력), `openai`, `PyPDFLoader`, `RecursiveCharacterTextSplitter`, `CharacterTextSplitter`, `OpenAIEmbeddings`(text-embedding-3-small), `FAISS`, `Chroma`, `ChatPromptTemplate`, `RunnablePassthrough`, `RunnableLambda`, `StrOutputParser`, `ChatOpenAI`(gpt-4o-mini, gpt-3.5-turbo), (설치만) `streamlit`, `pyngrok`

**실습용 vs 완성본 차이**
| 항목 | 실습용(`배포`) | 완성본(`배포완성`) |
|---|---|---|
| 셀 수 | 56 | 56 (같음) |
| 앞~중반 (Gradio 기본, PDF RAG, 보존 문제, Gradio PDF 챗봇 — cell 0~28) | `model=`, `messages=`, `fn=`, `inputs=`, `text_splitter =`, `retriever =`, `prompt =`, `chain =` 등 빈칸 약 19개 셀 | 모두 작성 (예: `chunk_size=1000, chunk_overlap=200`, `search_type="similarity", k=2`, 출처 문자열 조립) |
| 후반 (PDF 업로드형·카톡·텔레그램 — cell 30~55) | 빈칸 | **빈칸 그대로 (차이 없음)** |
| 기타 | 버전 출력 `LangChain Version : 1.3.13`, `Gradio Version : 6.20.0` | 해당 출력 없음, 실행 URL만 다름 |

---

### Day 13 — 「Agent: 음성을 텍스트로 변환하기 — RAG + Whisper 모델 + Gradio」 (실습용)

**학습 목표 (정리)**: Whisper(OpenAI API `whisper-1`·로컬 `openai-whisper`)로 STT·음성 번역을 하고, LLM 교정·요약, FAISS RAG와 결합한 음성 QA, 회의록 분석 멀티에이전트, LangGraph 상태 머신·Supervisor 구조로 발전시킨다.

**주요 목차**: (VOICE RAG AGENT) → `음성파일 url` → `STT 후처리 + 도메인 보정` → `Whisper 전사 + 번역 + GPT 한글 요약 에이전트` → `"음성 번역기" 구조` → `Whisper 모델로 구성` → `Whisper 음성 인식` → `최신 OpenAI Python SDK 1.x 기준의 Speech-to-Summary AI Pipeline 구현` → `문제 설명)` → `정답` → `실습 문제 : AI 음성 기반 RAG QA 시스템` → `AI 회의록 분석 Agent (Whisper + RAG + GPT)` → `번역언어 선택 포함` → `멀티에이전트 아키텍처 설계` → `음성 기반 회의 분석 + RAG + Multi-Agent + 다국어 번역까지 포함된 완성형 AI 파이프라인` → `LangGraph 기반 상태 머신형 AI 워크플로우 시스템` → `선형적 에이전트 구조` → `슈퍼바이저 에이전트를 포함한 Hub-and-Spoke 아키텍처`

**실습 항목**
| 구분 | 내용 |
|---|---|
| Voice RAG Agent | 음성 → Whisper STT → FAISS(`FAISS_INDEX_PATH` 없으면 샘플 문장으로 생성 후 `save_local`) → LCEL 체인 → Gradio (빈칸) |
| 음성 파일 출처 | 마크다운 `음성파일 url`: `https://www.darakwon.co.kr/mp3/FileDown_kor2.asp?p_id=8085&pf_type=5` (다락원) |
| 전사·번역 | `client.audio.transcriptions` / `translations`(`whisper-1`), `traceback` 오류 처리, Gradio 2열 UI |
| STT 교정 | `correct_transcription()` — Whisper 오인식을 LLM으로 교정 (전사기 Tool / 번역기 Tool) |
| 전사→번역→요약 | STT Agent → Translation Agent → Summary Agent → `agent_pipeline()` Orchestrator, `gr.Audio(type="filepath")` |
| 로컬 Whisper + legacy SDK | `openai==0.28.0` + `git+https://github.com/openai/whisper.git`, `whisper.load_model("small")`, `openai.ChatCompletion.create` |
| 문제: AI 음성 요약기 (TODO 1~12) | 로컬 Whisper small + `client.chat.completions.create(gpt-4o-mini)` + Gradio(Audio·원문·요약·버튼) + `demo.launch(share=True)`, 바로 뒤에 `정답` 셀 (small 모델 461 MB 다운로드) |
| 문제: 음성 기반 RAG QA (TODO 1~9) | Whisper → `Document` → `RecursiveCharacterTextSplitter` → `OpenAIEmbeddings` → FAISS → Retriever → LCEL |
| 회의록 분석 Agent | LangChain 없이 `faiss` + `numpy` + `text-embedding-3-small` 직접 임베딩, 회의 규칙 지식베이스 RAG, `meeting_analysis_agent()`, 번역 언어 선택 버전 |
| 멀티에이전트 | 설계 표(WhisperAgent / TranslatorAgent / TTSAgent / CoordinatorAgent), Summary·Action Item·Risk·Decision Agent(`call_agent(role, …)`) + Translation Layer, 한계 주석(프롬프트 overflow, 순차 호출 지연, 토큰 한도) |
| LangGraph 선형 | `MeetingState(TypedDict)` + `rag_retrieval_node → summary/action/risk/decision → translation_and_merge_node`, `set_entry_point` 빈칸, 그래프 시각화 |
| LangGraph Supervisor | `supervisor_node`(각 Agent 완료 여부 YES/NO를 보고 다음 step 또는 FINISH를 JSON으로 결정) + `supervisor_router` + `add_conditional_edges`, `draw_mermaid_png()` |

**사용 라이브러리·클래스·모델**: `openai`(SDK 1.x `OpenAI` 클라이언트, 일부 0.28), `whisper-1`, `openai-whisper`(small), `gradio`(`gr.Audio(sources=["microphone","upload"])`), `faiss`, `numpy`, `langchain_openai`(ChatOpenAI gpt-4o-mini, OpenAIEmbeddings text-embedding-3-small), `FAISS`, `Document`, `RecursiveCharacterTextSplitter`, `langgraph.graph`(StateGraph, END), `json`, `traceback`

**실습용 vs 완성본**: 실습용만 있음. 음성 요약기 문제는 같은 노트북 안에 `정답` 셀이 있습니다. LangGraph 선형 구조 셀은 엔트리 포인트 등이 비어 있습니다.

**함께 들어 있는 mp3 (`day13/문화가 있는 한국어 읽기_mp3/`)**
| 항목 | 내용 |
|---|---|
| 파일 | `문화가 있는 한국어 읽기 1_01.mp3` ~ `1_40.mp3` (40개) |
| 출처 | 노트북에 적힌 다운로드 주소가 다락원(darakwon.co.kr) MP3 자료실이고, 폴더명이 「문화가 있는 한국어 읽기 1」이므로 **다락원 한국어 교재 『문화가 있는 한국어 읽기 1』의 부속 음성**으로 보입니다 (교재명은 폴더·파일명 기준) |
| 형식 | MP3, 44.1 kHz, 스테레오, 320 kbps (40개 모두 같음), ID3 태그 없음 |
| 길이 | 36.2초 ~ 110.6초, 평균 63.7초, 합계 약 2,549초(약 42.5분) |
| 크기 | 1.38 MB ~ 4.22 MB, 합계 101,943,363 바이트 |
| 노트북에서의 사용 | 노트북 코드는 파일 경로를 직접 참조하지 않습니다. Gradio `gr.Audio`에 업로드해 전사·번역·요약할 샘플로 쓰는 용도로 보입니다 (추정) |

---

### Day 14 — 「LangGraph Agent: 메일 작성기 응용 + Gradio」 (실습용)

**학습 목표 (정리)**: LangGraph `StateGraph`로 이메일 처리 워크플로(발신자 추출 → 요약 → 답장 → 태깅)를 만들고, LCEL 순차 멀티에이전트 메일 분석기, RAG + 검토/재작성 루프가 있는 이메일 생성 에이전트로 확장한다.

**주요 목차**: (마크다운이 2개뿐) `#문제) 아래의 조건을 참고하여 { }, ( ), [ ] 안에 들어갈 코드를 완성하세요.` → `#문제) LCEL 기반의 메일분석기입니다. 다음 비어있는 빈칸을 완성하세요.` — 나머지는 코드 셀 안의 docstring·구조도로 설명

**실습 항목**
| 구분 | 내용 |
|---|---|
| LangGraph 메일 워크플로 (빈칸) | `EmailState(TypedDict)`(sender_name 등), 노드 `extract_sender → summarize_email → draft_reply(sender_name 강제 삽입) → tag_email`, `add_edge(START, )` 등 엣지 빈칸 → 결과 예: "Sender: 김영희" |
| 같은 구조 + Gradio | `run_agent(email_text)` → Gradio UI |
| Email Generator Agent | `PromptTemplate` + `load_language_model()` + `input()`으로 받은 요청("산행 모임을 같이할 분 모집합니다") → 제목·본문 생성 |
| Email Writing Agent (LCEL) | 설명에는 `ConversationBufferMemory`가 있으나 코드는 `RunnableLambda` + LCEL + Gradio |
| 이메일 Agent (헤더+본문) | `parse_email_header` / `detect_recipient_role` / `summarize_email` / `draft_reply` / `tag_email` + `process_email()` Orchestrator, `run_chain(template, inputs)` 공통 실행기 |
| LCEL 메일분석기 문제 (빈칸) | Split → Header Parsing → Role Detection → Summarization → Reply Generation → Tagging 6단계 |
| RAG + LangGraph 이메일 에이전트 | 샘플 문서(회의 규칙 등) FAISS → `retrieve → generate → review(LLM Judge, score·approved) → rewrite` 루프, `add_conditional_edges("review", route, {"END": END, "rewrite": "rewrite"})` + `add_edge("rewrite", "review")` |

**사용 라이브러리·클래스·모델**: `langgraph.graph`(StateGraph, START, END), `ChatOpenAI`(gpt-4o-mini), `PromptTemplate`, `StrOutputParser`, `RunnableLambda`, `Document`, `FAISS`, `langchain_community.embeddings.OpenAIEmbeddings`, `gradio`, `requests`·`beautifulsoup4`(확장용 import만)

**실습용 vs 완성본**: 실습용만 있음.

---

## 4. 커리큘럼 흐름

### 단계표
| 단계 | Day | 핵심 질문 | 만드는 결과물 | 다음 단계로 넘어가는 것 |
|---|---|---|---|---|
| ① 프롬프트 | D1~D3 | LLM에 무엇을 어떤 형식으로 넣나? | 기술 문서 작성기, 요리 추천, 번역기, 삼행시·과학 Q&A Few-shot, Gradio 대화 챗봇 | `ChatPromptTemplate`, 예제 선택기(벡터 검색 첫 경험) |
| ② LCEL | D4~D5 | 프롬프트·모델·파서를 어떻게 잇고 분기하나? | 라우팅 복합 체인, JSON 출력(여행 일정·이력서 평가·고객 문의 분류) | `\|` 연결, `RunnablePassthrough`, 구조화 출력 |
| ③ 문서 로더 | D6 | 내 문서(PDF·Word·CSV·HWP·웹)를 어떻게 읽나? | 확장자 자동 판별 요약기, Multi Document Analyzer | `Document`(page_content + metadata) |
| ④ Runnable | D7 | 체인을 어떻게 실행·병렬화·조립하나? | stream/batch/async 실행, `RunnableParallel`, `ConfigurableField`, `@chain`, 커스텀 Runnable | 병렬 context/question 구성 |
| ⑤ RAG | D8~D11 | 검색한 문서로 답하게 하려면? | FAISS·Chroma RAG, 메모리 RAG, Multi Query, Conversational RAG, BM25+FAISS 앙상블, 한국어 임베딩 비교, 다문서 QA 챗봇 | retriever + `format_docs` + 프롬프트 |
| ⑥ Agent/챗봇 UI | D12 | 사용자가 쓰는 화면은? | Gradio PDF QA 챗봇(출처 표시), 업로드형, 카톡·텔레그램 스타일 | Gradio `Blocks`/`Chatbot` |
| ⑦ 음성 RAG | D13 | 음성 입력을 RAG·에이전트에 넣으려면? | Whisper 전사·번역·요약, 음성 RAG QA, 회의록 분석 멀티에이전트 | 역할별 Agent 함수, Orchestrator |
| ⑧ LangGraph | D13 후반~D14 | 에이전트 흐름을 상태 그래프로 어떻게 제어하나? | 선형·Supervisor 회의 분석 그래프, 메일 처리 워크플로, 검토/재작성 루프 이메일 에이전트 | `StateGraph`, 조건부 엣지 |

### 흐름도
```
프롬프트(D1~3) ─ ChatPromptTemplate · Few-shot · 예제 선택기
   │
LCEL(D4~5) ─ prompt | model | parser · 라우팅 · JSON 파서
   │
문서 로더(D6) ─ PDF / DOCX / CSV / Web / HWP → Document
   │
Runnable(D7) ─ invoke·batch·stream·async · Parallel · Passthrough · Lambda · @chain
   │
RAG(D8~11) ─ Splitter → Embedding → FAISS/Chroma → Retriever → (Memory · Multi Query · Ensemble)
   │
챗봇 UI(D12) ─ Gradio PDF QA 챗봇
   │
음성 RAG(D13) ─ Whisper STT → RAG → 멀티에이전트(요약·액션·리스크·결정·번역)
   │
LangGraph(D13~14) ─ StateGraph · Supervisor · 조건부 루프(검토 → 재작성)
```

> D2·D3에서 LangGraph를 미리 짧게 보여 주고(어시스턴트 그래프), D13~D14에서 본격적으로 다시 씁니다.

---

## 5. 사용 기술·도구·외부 서비스

| 분류 | 이름 | 사용 Day | 용도 |
|---|---|---|---|
| 실행 환경 | Google Colab (Python 3.12) | 전체 | 모든 실습. GPU 지정 없음 |
| 실행 환경 | Colab Secrets (`google.colab.userdata`) | 전체 | `OPENAI_API_KEY`를 `userdata.get()`으로 읽어 환경변수 등록 |
| 실행 환경 | Colab `files.upload()` / `drive.mount()` | D6·D8·D9·D10·D11 | 업로드·Google Drive 데이터 접근 |
| 프레임워크 | `langchain`, `langchain-core`, `langchain-openai`, `langchain-community`, `langchain-text-splitters` | 전체 | LCEL, 프롬프트, 파서, Runnable, 로더, 벡터스토어. D7에 0.3.x 고정 버전 설치 셀, D9에 `langchain==0.3.0` 재설치 |
| 프레임워크 | `langgraph` | D2·D3·D13·D14 | StateGraph, add_messages, 조건부 엣지, Supervisor |
| 프레임워크 | `langchain-chroma`, `chromadb` | D3·D10·D11·D12 | 예제 선택기, 다문서 RAG |
| 벡터 검색 | `faiss-cpu` | D1·D3~D4·D8~D14 | FAISS 벡터 DB (`langchain` 래퍼 + D13 `faiss` 직접 사용) |
| 검색 | `BM25Retriever`, `EnsembleRetriever` (`rank_bm25` 계열, 추정) | D9 | 키워드 + 의미 하이브리드 검색 |
| 토크나이저 | `tiktoken` | D1·D4·D10·D11 | 토큰 길이 기반 분할 |
| 로더 | `pypdf`, `pdfplumber`, `PyMuPDF`, `unstructured`(+`[local-inference]`, `python-magic`, `libmagic1`), `pdf2image`, `docx2txt`, `pdfminer`, `msoffcrypto-tool`, `beautifulsoup4` | D6·D9~D12·D14 | PDF·Office·웹 문서 로드 |
| 텍스트 추출 | `python-pptx`, `python-docx`, `openpyxl`, `olefile`(+zlib·struct) | D6 | LangChain 밖 PPTX·DOCX·XLSX·HWP 추출 |
| 임베딩 | `OpenAIEmbeddings`(기본값, `text-embedding-3-small`) | D3·D4·D8~D14 | 벡터화 |
| 임베딩 | HuggingFace: `BAAI/bge-small-en`, `jhgan/ko-sbert-nli`, `upskyy/bge-m3-korean` (`sentence_transformers`) | D10·D11 | 무료·한국어 임베딩 비교 |
| LLM | OpenAI `gpt-4o-mini`(기본), `gpt-4o`, `gpt-4.1-mini`, `gpt-3.5-turbo`, `gpt-4`, `OpenAI()` completion | 전체 | 생성·분류·요약·번역·평가 |
| 음성 | OpenAI Whisper API `whisper-1` (transcriptions / translations) | D13 | STT, 음성 → 영어 번역 |
| 음성 | `openai-whisper`(로컬 `small`, GitHub 설치) | D13 | API 없이 Colab에서 STT |
| SDK | `openai` 1.x (`OpenAI().chat.completions.create`), `openai==0.28.0`(`ChatCompletion.create`) | D12·D13 | LangChain 없이 직접 호출 |
| UI | `gradio` (`ChatInterface`, `Blocks`, `Chatbot`, `Audio`, `File`, `State`, `share=True` 공개 링크) | D1·D12·D13·D14 | 챗봇·음성 앱 UI |
| 시각화 | `graphviz`, `grandalf`, Mermaid(`draw_mermaid_png`, mermaidviewer.com) | D2·D3·D4·D13 | 체인·그래프 구조도 |
| 기타 | `pandas`, `numpy`, `scikit-learn`, `nest_asyncio`, `python-dotenv`, `requests`, `pydantic` | 여러 Day | 데이터 처리·비동기·스키마 |
| 설치만 / 언급만 | `streamlit`, `pyngrok`(D12 설치), ngrok 토큰 발급 안내(D6 완성본), Anthropic·Google·Ollama(D7 설명) | — | 실제 사용 코드는 없음 |
| 외부 데이터 | TechCrunch 기사 zip (`github.com/kairess/toy-datasets`, wget) | D10·D11 | 다문서 RAG |
| 외부 데이터 | 네이버 뉴스 기사, KOCW 강의 PDF, pdfobject.com 샘플 PDF, spri.kr 페이지 | D6·D9·D12 | 웹·PDF 로더 실습 |
| 외부 데이터 | 다락원 MP3 자료실 (`darakwon.co.kr`) | D13 | 음성 파일 원래 다운로드 주소 |

**필요한 API 키**
| 키 | 필요 여부 | 읽는 방식 |
|---|---|---|
| `OPENAI_API_KEY` | **필수** (모든 Day) | Colab Secrets `userdata.get("OPENAI_API_KEY")` → `os.environ`. D13 음성 요약기 문제 셀의 실행 출력에는 "Colab 시크릿에 키가 없네요. 직접 입력해주세요" 프롬프트가 남아 있음(강사가 실행할 때 키를 직접 입력한 흔적, 해당 코드는 빈칸) |
| HuggingFace 토큰 | 불필요 (공개 모델만 사용) | — |
| ngrok authtoken | 불필요 (안내 마크다운만 있음) | — |

---

## 6. 특이사항

| 구분 | 내용 |
|---|---|
| **레포에 넣으며 정리한 내용 ①** | 원래 zip에는 **3일차 노트북이 같은 내용으로 2개** 있었습니다. 하나는 중복이라 제외하고 1개만 넣었습니다. |
| **레포에 넣으며 정리한 내용 ②** | 5일차 파일 확장자가 `.배포ipynb`로 잘못돼 있어 `.ipynb`로 고쳤습니다(파일명 `5일차_LCEL_JSON 파서 문제 풀이_new_배포.ipynb`). |
| **레포에 넣으며 정리한 내용 ③** | 13일차 노트북 실행 결과(음성 요약기 TODO 문제 셀의 키 입력 프롬프트 출력)에 **실제 OpenAI API 키가 찍혀 있어 `<YOUR_API_KEY>`로 바꿨습니다**. 원본 zip을 다른 곳에 공유했다면 해당 키는 폐기(재발급)하는 것이 안전합니다. 현재 레포의 노트북 16개에서는 `sk-` 패턴 키가 검색되지 않습니다. |
| **실습용·완성본 짝** | 짝이 있는 날은 **6일차·12일차뿐**입니다. 1·11일차는 완성본만, 2~5·7~10·13·14일차는 실습용만 있습니다. 6일차 완성본도 마지막 문제(Universal Analyzer)는 비어 있고, 12일차 완성본도 후반 셀 8개(업로드형·카톡·텔레그램)는 실습용과 똑같이 비어 있습니다. |
| **실습용인데 출력이 남음** | 실습용 노트북은 코드를 지웠지만 **셀 출력(정답 실행 결과)은 지우지 않았습니다**. 빈칸을 채울 때 출력이 힌트가 되지만, 정답 코드 자체는 없는 경우가 대부분입니다. |
| **중복 내용** | 5일차는 4일차 cell 43~56(출력 파서 + 문제 2개)과 거의 같고, 고객 문의 분류 문제 1개만 추가됐습니다. 4일차·7일차의 수학/과학/기타 라우터 예제도 겹칩니다. 11일차는 같은 FAISS RAG 챗봇 셀이 2번 들어 있습니다. |
| **실행 환경 요구** | Colab 전용 API(`google.colab.userdata`, `files.upload()`, `drive.mount()`, Gradio `share=True`)를 쓰므로 로컬에서는 키 로딩·업로드 부분을 바꿔야 합니다. 13일차 로컬 Whisper `small`은 약 461 MB를 내려받고, 출력에 `FP16 is not supported on CPU; using FP32 instead` 경고가 있어 강사도 CPU 런타임에서 돌린 것으로 보입니다(GPU 런타임이면 더 빠름). D11의 `unstructured`는 `apt-get install -y libmagic1`이 필요합니다. |
| **패키지 버전 혼재** | 실행 출력 기준으로 langchain 0.3.27(D4) / 1.3.11 → 0.3.0 재설치(D9·D10) / 1.3.13(D12), gradio 6.20.0, openai 2.4x가 섞여 있습니다. D7에는 0.3.x 고정 설치 셀이, D13에는 `openai==0.28.0` 설치 셀(이후 1.x 코드와 충돌 → 세션 재시작 필요)이 있어 **위에서부터 순서대로 다 실행하면 버전이 꼬일 수 있습니다**. `langchain.retrievers.ensemble`, `langchain.text_splitter`, `langchain.chat_models`, `langchain.chains` 같은 경로는 LangChain 1.x에서 바뀌거나 빠졌을 수 있어 0.3 계열을 전제로 합니다(추정). |
| **deprecated 경고 (출력에 찍힌 것)** | `langchain-community is being sunset and is no longer actively maintained`(DeprecationWarning, 여러 Day) / `RunnableWithMessageHistory is deprecated. Use LangGraph's built-in persistence instead.`(D1·D10) / `HuggingFaceEmbeddings` deprecated(→ `langchain-huggingface`, D10·D11) / Chroma `persist()` "Since Chroma 0.4.x the manual persistence method is no longer supported"(D10) / `ChatOpenAI` 구 경로 deprecated(D2) / `model_kwargs`로 넘긴 `stop`·penalty 파라미터는 명시적으로 지정하라는 UserWarning(D4) / `USER_AGENT environment variable not set`(WebBaseLoader) / Gradio 6 `Blocks(css=…)` 파라미터 이동 경고(D12). Chroma 설치 시 opentelemetry 충돌(D3)과 `pip` 의존성 충돌 ERROR(D4) 출력도 있습니다. |
| **누락 (데이터 파일)** | 노트북이 참조하는 데이터 대부분이 레포에 없습니다. **Google Drive 개인 경로**(`/content/drive/MyDrive/AI_ChatBot/LLM_원본/자료/…`, `/content/drive/MyDrive/AI_멀티_MultiAgent/…/Agent_data/…`)의 `[이슈리포트 2022-2호] 혁신성장 정책금융 동향.pdf`, `해커톤.docx`, `최종 필터링 데이터 (호텔, 지형) - 시트3.csv`, `state_of_the_union.txt`와, 업로드 방식의 `AI 최신 동향과 정책.txt`, `★ 서울특별시 스마트도시 및 정보화 기본계획(홈페이지 게시용).pdf`, PPTX·DOCX·XLSX·HWP 샘플은 직접 준비해야 합니다. TechCrunch 기사는 **`!wget`으로 GitHub(kairess/toy-datasets)에서 받고**, KOCW PDF·네이버 뉴스·pdfobject 샘플은 URL로 직접 읽습니다(링크가 바뀌면 실패). |
| **코드·설명 불일치** | 11일차 마크다운은 `initialize_agent()` 기반 에이전트라고 하지만 코드는 LCEL RAG 체인뿐입니다(Agent + Tool 구조는 문자열 설명만). 14일차 Email Writing Agent 설명의 `ConversationBufferMemory`도 코드에는 없습니다. 6일차 TODO는 `gpt-4.1-mini`라 적혀 있지만 정답은 `gpt-4o`입니다. 9일차 URL PDF 예제는 PDF가 아닌 웹페이지 주소라 답이 `문서에 없음`으로 나옵니다. |
| **표기 오류** | 4일차 마크다운에 LCEL을 "Language Chain Execution Layer"로 적었지만 정식 명칭은 LangChain Expression Language입니다(같은 노트북 다른 셀은 올바르게 씀). `문제) sonOutputParser…`(JsonOutputParser), `RunnableParaller`, `RunnalbePassthrough`, `ChatCPT`, `CusineRecipe`, 8일차 파일명 `new배포_` 등 오탈자가 있습니다. |
| **mp3 저작권 참고** | `day13/문화가 있는 한국어 읽기_mp3/`는 **출판사(다락원) 교재의 부속 음성**입니다(노트북의 다운로드 주소 기준). 출판사가 교재 구매자·학습자용으로 공개한 자료이므로 **개인 학습용으로만** 쓰고, 재배포·공개 레포 업로드·상업 서비스(데모 포함) 사용은 하지 않는 것이 맞습니다. 용량도 레포의 대부분(약 97%)을 차지합니다. |
| **README·LICENSE** | 원본 zip에 README·LICENSE가 없어 이용 조건이 명시되어 있지 않습니다. 강사·기관명도 노트북 안에 없습니다(13일차 출력에 "제니가 추천하는…" 문구만 있음). |

---

## 7. 활용 포인트

1. **사내·고객 문서 RAG 챗봇 SaaS 템플릿 (D6 + D9 + D11 + D12)**
   D6의 "확장자 자동 판별 로더"(PDF·DOCX·CSV·TXT·MD + HWP 파서)와 D12의 Gradio PDF QA 챗봇(답변 + `[n] source (page)` 출처 표시)을 합치고, D9의 BM25 + FAISS 앙상블과 D11의 한국어 임베딩(`upskyy/bge-m3-korean`) 비교 결과로 검색 품질을 맞추면 한국어 문서(특히 HWP) 대응 RAG 챗봇을 만들 수 있습니다. FLORA나 platform-docs의 기획 문서 검색, 고객사 납품용 화이트라벨 챗봇의 기본 골격으로 쓰기 좋습니다.

2. **음성 에이전트 프로젝트: Whisper → RAG → 멀티에이전트 → 번역 (D13)**
   D13의 회의록 분석 파이프라인(STT → FAISS 지식베이스 → Summary·Action·Risk·Decision Agent → 번역)과 LangGraph Supervisor 구조를 음성 에이전트·JARVIS 프로젝트의 "듣기 → 판단" 단계 MVP로 바로 옮길 수 있습니다. 노트북 주석이 짚은 한계(Agent 순차 호출 지연, 프롬프트 overflow)는 LangGraph 병렬 분기와 context 길이 제한으로 개선 과제로 삼으면 됩니다.

3. **메일 작성·분류 자동화 에이전트 (D14 + D5)**
   D14의 `retrieve → generate → review(score·approved) → rewrite` 조건부 루프와 D5의 고객 문의 JSON 분류(category·priority·sentiment·recommended_action)를 묶으면, 문의 메일을 분류하고 사내 규칙 문서를 근거로 답장 초안을 만든 뒤 스스로 검토해 고치는 CS 자동화 에이전트가 됩니다. NOMAD Funnel Engine(CRM)이나 SellingStudio의 고객 응대 기능으로 붙일 수 있습니다.

4. **구조화 출력 기반 콘텐츠·분석 API (D4~D5 + D7)**
   `JsonOutputParser` + Pydantic 스키마(여행 일정, 이력서 평가)와 D7의 `RunnableParallel`·`batch(max_concurrency)`·`ConfigurableField`(모델 런타임 교체)를 조합하면, 하나의 입력으로 제목·요약·태그·해시태그를 병렬 생성하고 비용에 따라 gpt-4o-mini ↔ gpt-4o를 바꾸는 콘텐츠 생성 API를 만들 수 있습니다. NOMAD Blog Factory나 ShortsOS의 대본·메타데이터 생성 단계에 맞습니다.

5. **바이브코딩 커리큘럼 교재로 재구성**
   "legacy 코드 → 최신 LCEL 개선 코드" 비교 서술과 `문제) + TODO`(요구사항·입력 예시·출력 예시) 형식은 디지털노마드연구소 강의 교안 포맷으로 그대로 쓸 만합니다. 다만 이 자료는 짝(실습용/완성본)이 일부 날짜에만 있고 버전이 섞여 있으므로, 자체 교재로 만들 때는 Day별 실습용·정답본을 모두 갖추고 LangChain 1.x·LangGraph 기준으로 다시 고정하는 것이 차별점이 됩니다.
