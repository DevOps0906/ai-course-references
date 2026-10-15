# AI_Voice — 「음성 AI 전문가 과정(160h)」 1~2주차 Day 1~7 강의 교재 세트 (슬라이드 · Colab 실습 노트북 · 인터랙티브 애니메이션 · 워크시트)
> ℹ️ 이 문서는 자료를 처음 분석할 때 작성한 정리본입니다. 레포에 넣으면서 원본 표기·연락처·토큰·문서 ID는 정리되었으니, 6장의 "노출" 항목은 **정리 전 원본 기준** 기록입니다.

> - **원본 버전**: 커밋 `0d1745e` 기준 (최신 여부는 `python3 tools/sync.py`로 확인)
> - **총 파일 수**: 37개 (html 14 · ipynb 10 · pdf 7 · pptx 6), README / LICENSE 없음
> - **총 용량**: 32,279,578 바이트 (약 30.8 MB)
> - **자료 성격**: 40일(160시간) 과정 중 **Day 1~7**에 해당하는 강의 교재 세트입니다. Day마다 ① 발표자 노트가 들어 있는 슬라이드(pptx/pdf), ② 빈칸 실습과 정답(접힘)이 들어 있는 Colab 실습 노트북, ③ 브라우저 단독 실행형 인터랙티브 애니메이션(animation.html, 탭 9개), ④ 자동 채점 개념 워크시트(worksheet.html)로 구성됩니다. Day 4~6에는 **강사용 노트북(강사 스크립트 포함)**이 추가로 들어 있습니다.

---

## 1. 한눈에 보기

| 항목 | 내용 |
|---|---|
| 주제 | 음성 AI 기초: 디지털 오디오 → 주파수 분석 → 전처리/VAD → 딥러닝 분류(KWS) → ASR 원리(CTC·AED·RNN-T·자기지도) → Whisper 심층 분석 |
| 과정 전체 | 「음성 AI 전문가 과정」 160시간, 8주, 40일 (슬라이드 표기 "Day N / 40"). 이 zip에는 **Day 1~7만** 들어 있음 |
| 주차 표기 | D1~D5: `1주차 M1`, D6~D7: `2주차 M2` (각 4시간) |
| 하루 구성 | 4교시 × 50분 (+10분 휴식). 교시마다 노트북 Part, 빈칸 실습, 워크시트 탭이 맞물림 |
| 추정 대상 학습자 | Python 기초가 있고 음성 AI 실무자가 되려는 개발자·취업 준비생 (추정). 수식(dB, DFT, softmax, CTC α 등)을 "비유 → 소리 → 그림 → 수식" 순서로 풀어 설명하므로 비전공자도 따라올 수 있게 설계됨 |
| 수업 방식 | 문제 상황 → 핵심 개념 → Animation → Colab 실습 → 빈칸 실습 → Worksheet → 정리 (D1 슬라이드 6) |
| 실행 환경 | Google Colab, **T4 GPU** 권장, Python 3.13 (Colab 기본). 로컬은 `uv` 사용 안내 |
| 자료 형식 | pptx(발표자 노트 포함) + pdf(같은 내용, 노트 제외) / ipynb(실습·강사용) / html(애니메이션·워크시트) |
| 핵심 키워드 | 16kHz mono WAV, 샘플링·Aliasing·양자화, FFT/STFT/Log-Mel/MFCC, SNR·Wiener·spectral gating, Silero VAD, Speech Commands KWS CNN, SpecAugment, CTC·forward(α), Wav2Vec2·HuBERT, Attention Enc-Dec, RNN-T, Whisper 특수 토큰·beam·temperature·환각 대응, RTF·CER |

---

## 2. 폴더·파일 구성

```
AI_Voice-main/
└── AI_Voice-main/
    ├── day01/  D1_음성AI_첫걸음_slides.pdf · .pptx · D1_음성AI_첫걸음_실습.ipynb · animation.html · worksheet.html
    ├── day02/  D2_디지털오디오기초_slides.pdf · .pptx · D2_디지털오디오기초_실습.ipynb · animation.html · worksheet.html
    ├── day03/  D3_주파수분석_slides.pdf · .pptx · D3_주파수분석_실습.ipynb · animation.html · worksheet.html
    ├── day04/  D4_오디오전처리_slides.pdf · .pptx · D4_오디오전처리_실습.ipynb · D4_오디오전처리_강사용.ipynb · animation.html · worksheet.html
    ├── day05/  D5_딥러닝오디오분류_slides.pdf · .pptx · D5_딥러닝오디오분류_실습.ipynb · D5_딥러닝오디오분류_강사용.ipynb · animation.html · worksheet.html
    ├── day06/  D6_ASR원리_slides.pdf · .pptx · D6_ASR원리_실습.ipynb · D6_ASR원리_강사용.ipynb · animation.html · worksheet.html
    └── day07/  D7_Whisper심층분석_slides.pdf · D7_Whisper심층분석_실습.ipynb · animation.html · worksheet.html   (※ pptx 없음)
```

| 파일명 | 형식 | 크기 | 역할 |
|---|---|---|---|
| day01/D1_음성AI_첫걸음_slides.pptx | pptx | 904.9 KB | 강의 슬라이드 25장, 슬라이드마다 `[노트]` 발표자 노트 |
| day01/D1_음성AI_첫걸음_slides.pdf | pdf | 639.4 KB | pptx와 같은 25쪽 (노트 제외) |
| day01/D1_음성AI_첫걸음_실습.ipynb | ipynb | 515.1 KB | Part 0~7, 빈칸 6개 + 정답 |
| day01/animation.html | html | 52.6 KB | 탭 9개 (마이크 실시간, 브라우저 TTS) |
| day01/worksheet.html | html | 26.6 KB | 15문항, 채점, 인쇄/PDF 저장 |
| day02/D2_디지털오디오기초_slides.pptx | pptx | 1.10 MB | 슬라이드 22장 + 노트 |
| day02/D2_디지털오디오기초_slides.pdf | pdf | 713.4 KB | 22쪽 |
| day02/D2_디지털오디오기초_실습.ipynb | ipynb | 1.46 MB | Part 0~7, 빈칸 7개, 수식 검증 6개 |
| day02/animation.html | html | 71.7 KB | 탭 D2-1~D2-9 |
| day02/worksheet.html | html | 33.0 KB | 4교시 × 10문항 = 40문항 |
| day03/D3_주파수분석_slides.pptx | pptx | 1.67 MB | 슬라이드 23장 + 노트 |
| day03/D3_주파수분석_slides.pdf | pdf | 1.15 MB | 23쪽 |
| day03/D3_주파수분석_실습.ipynb | ipynb | 1.49 MB | Part 0~7, 빈칸 7개, 수식 검증 5개 |
| day03/animation.html | html | 62.0 KB | 탭 D3-1~D3-9 (마이크 사용) |
| day03/worksheet.html | html | 33.2 KB | 40문항 |
| day04/D4_오디오전처리_slides.pptx | pptx | 1.82 MB | 슬라이드 20장 + 노트 |
| day04/D4_오디오전처리_slides.pdf | pdf | 1.12 MB | 20쪽 |
| day04/D4_오디오전처리_실습.ipynb | ipynb | 1.57 MB | 학생용, Part 0~7, 빈칸 9개 |
| day04/D4_오디오전처리_강사용.ipynb | ipynb | 1.65 MB | 학생용 셀 전체 + 강사 스크립트 셀 53개 |
| day04/animation.html | html | 79.0 KB | 탭 D4-1~D4-9 (마이크 사용) |
| day04/worksheet.html | html | 36.2 KB | 40문항 |
| day05/D5_딥러닝오디오분류_slides.pptx | pptx | 1.47 MB | 슬라이드 19장 + 노트 |
| day05/D5_딥러닝오디오분류_slides.pdf | pdf | 986.8 KB | 19쪽 |
| day05/D5_딥러닝오디오분류_실습.ipynb | ipynb | 1.30 MB | 학생용, Part 0~7, 빈칸 9개 |
| day05/D5_딥러닝오디오분류_강사용.ipynb | ipynb | 1.36 MB | 학생용 셀 전체 + 강사 스크립트 셀 42개 |
| day05/animation.html | html | 61.2 KB | 탭 D5-1~D5-9 |
| day05/worksheet.html | html | 34.3 KB | 40문항 |
| day06/D6_ASR원리_slides.pptx | pptx | 1.73 MB | 슬라이드 20장 + 노트 |
| day06/D6_ASR원리_slides.pdf | pdf | 1.32 MB | 20쪽 |
| day06/D6_ASR원리_실습.ipynb | ipynb | 1.67 MB | 학생용, Part 0~7, 빈칸 9개 |
| day06/D6_ASR원리_강사용.ipynb | ipynb | 1.71 MB | 학생용 셀 전체 + 강사 스크립트 셀 27개 |
| day06/animation.html | html | 68.0 KB | 탭 D6-1~D6-9 |
| day06/worksheet.html | html | 35.9 KB | 40문항 |
| day07/D7_Whisper심층분석_slides.pdf | pdf | 1.27 MB | 20쪽 (pptx 원본 없음, 발표자 노트 없음) |
| day07/D7_Whisper심층분석_실습.ipynb | ipynb | 1.57 MB | Part 0~6, 빈칸 9개 |
| day07/animation.html | html | 64.9 KB | 탭 D7-1~D7-9 |
| day07/worksheet.html | html | 36.0 KB | 40문항 |

> 노트북 용량이 큰 이유: 모든 노트북의 셀 출력은 비어 있고(outputs 0), 설명 그림이 markdown 셀 안에 base64 이미지로 직접 들어 있습니다.

---

## 3. Day별 상세 내용

### 공통 구성 (D2~D7)
- **노트북**: `## 학습 목표` → `오늘의 실습 흐름`(교시표) → Part 0 준비 → Part 1~6 → `Part 7. 정리 & 과제`. 각 Part에 `📐 수식으로 보기`, `▶️ 수식 검증 N`, `🔍 코드 해설`(코드|하는 일 표), `🧩 빈칸 실습 N`(`____` 채우기 + `check()` 자동 판정), `🔑 정답 및 해설 보기 (클릭)`(`<details>` 접힘)이 들어 있고, 교시 끝마다 `📝 N교시 마무리: 개념 워크시트` 안내가 있습니다.
- **animation.html**: 탭 9개(DN-1 "오늘의 흐름" ~ DN-9). 탭 번호가 노트북·워크시트·슬라이드의 🎬 번호와 같습니다. canvas 기반이고, 외부 리소스는 Google Fonts만 씁니다.
- **worksheet.html**: 교시 탭 4개 × 10문항(객관식 5 · OX 2 · 선잇기 1 · 순서 맞추기 1 · 모두 고르기 1). 채점 → 정오·해설·결과 코드 → **제출**(오답 정리) → **📋 캡처 (노션용 복사)**로 노션 제출 페이지에 붙여 넣는 방식입니다. "이름은 결과 코드 계산에만 쓰이며 저장되지 않습니다."

---

### Day 1 — 「음성 AI 첫걸음: 기술 지형도 & 개발환경 구축」

**학습 목표 (노트북 원문 요약)**
1. 음성 AI 4대 기술(ASR, TTS, Speech-to-Speech, Voice Agent)을 구분한다.
2. Colab GPU 환경을 점검하고 로컬 개발환경(uv) 구성 방법을 안다.
3. TTS(글자→소리)와 ASR(소리→글자)을 직접 실행한다.
4. 듣고, 생각하고, 말하는 **미니 음성 비서**를 만든다.

**교시**: 1교시 OT·지형도·발전사(Part 0) / 2교시 개발환경·TTS·소리 보기(Part 1~3) / 3교시 녹음·ASR·정확도(Part 4~5) / 4교시 미니 음성 비서·정리·퀴즈(Part 6~7)

**슬라이드 흐름 (25장)**: 표지 "Listen → Think → Speak" → 1.1 "이 과정이 답하려는 질문"(질문 5개: Whisper가 보는 것 D3·D7 / 정확도 수치화 D10 / 전문용어 D12·D13 / 음성 복제와 윤리 D19 / 응답 지연 D21·D28) → "8주 Roadmap"(음성 비서 단면도) → "이 과정의 범위" → "학습 방법" → 1.2 "음성 AI 4대 기술", "우리 주변의 음성 AI", "기술 발전사"(1952 Audrey → HMM → 2012 딥러닝 → 2016 WaveNet → 2022 Whisper → 2024 실시간 음성 대화 → 2025~ Voice Agent) → 1.3 "실습 환경 기준", "개발환경 층", "도구 설치", "로컬 개발환경(uv)" → 1.4 "TTS 맛보기", "소리 눈으로 보기", "샘플 수와 길이" → 1.5 "ASR 받아쓰기", "RTF", "CER", "단계별 관찰", "Colab에서 알아 둘 점(오류 해결표)" → 1.6 "미니 음성 비서", "음성용 답변", "응답 시간" → 정리

**실습 항목**
| Part | 제목 (원문) | 하는 일 |
|---|---|---|
| 0 | 음성 AI 4대 기술 지형도 | 표: ASR(Whisper, faster-whisper) / TTS(Kokoro, Chatterbox, edge-tts) / S2S(OpenAI Realtime, Gemini Live) / Voice Agent(Pipecat, LiveKit Agents, MCP) |
| 1 | 개발환경 확인 및 설치 | `!nvidia-smi`, Python·PyTorch·CUDA·cuDNN·FFmpeg 점검, `pip install faster-whisper edge-tts anthropic jiwer librosa soundfile`, `check()` 채점 도우미, uv 로컬 설치 안내 |
| 2 | TTS 맛보기: 글자 → 소리 | `edge_tts.list_voices()`로 ko- 목소리 나열, `tts()`(edge-tts mp3 → ffmpeg `-ar 16000 -ac 1` → WAV), 실습 2-1 목소리·속도(`rate`) 바꾸기 |
| 3 | 소리 눈으로 보기: 파형과 스펙트로그램 | `show_audio()`: `librosa.load`, `waveshow`, `melspectrogram(n_fft=400, hop_length=160, n_mels=80)`, `power_to_db` |
| 4 | 내 목소리 녹음하기 (Colab 브라우저 마이크) | JS `MediaRecorder` + `google.colab.output.eval_js`로 webm 녹음 → 16kHz WAV |
| 5 | ASR 맛보기: 소리 → 글자 (faster-whisper) | `nvidia-cublas-cu12`, `nvidia-cudnn-cu12==9.*` 설치 + `preload_cuda12_libs()`(ctypes 미리 로드), GPU면 `large-v3-turbo`(cuda, float16) / CPU면 `small`(int8), `transcribe()`(beam_size=5, vad_filter=True), RTF 출력. 5-1 CER(`jiwer.cer` + `normalize_ko`), 실습 5-2 어려운 문장·빠른 말 CER |
| 6 | 미니 음성 비서 만들기: 듣고 → 생각하고 → 말하기 | Colab Secrets의 `ANTHROPIC_API_KEY`(선택), `LLM_MODEL = "claude-haiku-4-5-20251001"`, 음성용 `SYSTEM_PROMPT`, 키 없을 때 `rule_based_reply()`, `voice_agent()` 단계별 지연(STT/LLM/TTS) 막대그래프 |
| 7 | 정리 & 과제 | 과제 1 템플릿: small/medium/large-v3-turbo CER·RTF 비교 표(pandas) |

**빈칸 실습 6개 (정답)**: ① `torch.cuda.is_available()` ② 남성 목소리 `ko-KR-InJoonNeural` ③ `len(y) / sr` ④ `transcribe(my_wav)` ⑤ `jiwer.cer` ⑥ `transcribe` → `llm_reply` → `tts`

**과제**: 1) 모델 3종 CER·처리 시간 비교 2) `SYSTEM_PROMPT`로 나만의 음성 비서 캐릭터 만들기 3) 로컬 uv 환경에서 `torch.cuda.is_available()` 캡처 제출

**animation.html (9탭)**: 오늘의 흐름 / 4대 기술 / 개발환경 층 / 소리 파일의 여행 / 샘플링 체험(8k·16k·44.1kHz 비교 듣기, 길이 계산기) / 내 목소리 보기(**마이크 실시간 파형·스펙트로그램**, VAD 감도) / 받아쓰기와 RTF(슬라이더) / CER 계산기(직접 입력) / 음성 비서 시뮬레이터(**브라우저 speechSynthesis**로 읽기, Streaming 비교). "마이크 소리는 이 페이지 안에서만 그려지고 어디에도 저장되거나 전송되지 않습니다."

**worksheet.html**: 15문항(객관식 4, 선잇기 3, 순서 맞추기 3, OX 2, 계산 2, 복수 선택 1), 이름·소속 입력, 채점, 오답만 보기, **인쇄 / PDF 저장**(D2~ 형식과 다름)

---

### Day 2 — 「디지털 오디오 기초: 소리는 어떻게 숫자가 될까」

**학습 목표**: 1) 주파수·진폭 구분 2) 샘플링 레이트·비트 깊이·채널의 영향 확인 3) WAV·FLAC·MP3·Opus 비교 4) librosa·soundfile·pydub·ffmpeg 역할 구분, 어떤 파일이든 **16kHz mono WAV**로 바꾸는 전처리기 5) 사인파·샘플링 정리·Aliasing·양자화 잡음·비트레이트·데시벨을 수식으로 설명하고 코드로 검증

**교시**: 1교시 소리의 정체·샘플링(Part 1~2) / 2교시 양자화·채널(Part 3~4) / 3교시 파일 포맷(Part 5) / 4교시 pydub 편집·전처리기(Part 6~7, 노션 제출)

**슬라이드 (22장)**: "2.0 오늘 답할 질문: 어제 쓴 16kHz WAV, 정확히 무엇이었을까" → 2.1 소리의 정체, 소리 만들기 → 2.2 샘플링, 절반 규칙, Aliasing, 바르게 줄이기 → 2.3 양자화, subtype → 2.4 채널 → 2.5 파일 포맷, 네 가지 포맷, WAV 크기 예측 → 2.6 오디오 도구, pydub 편집, 미니 프로젝트, 전처리 결과, Colab 오류(`No module named 'audioop'` → `audioop-lts`), 수식으로 정리 → 정리·다음 시간

**실습 항목**
| Part | 제목 (원문) | 주요 내용·함수 |
|---|---|---|
| 0 | 준비 | `pip install edge-tts pydub "audioop-lts; python_version >= '3.13'" librosa soundfile`, `ffmpeg()` 도우미, edge-tts로 speech.mp3 → 44.1kHz stereo/16kHz mono WAV, `sf.info` |
| 1 | 소리의 정체: 공기의 떨림이 숫자가 되기까지 | `tone()` 사인파, `Audio(normalize=False)`, 1-1 사인파와 데시벨(수식 검증 1: 주기·dB·RMS) |
| 2 | 샘플링: 1초에 몇 번 측정할까 | `librosa.load(sr=None)`, `librosa.resample`, 2-1 Aliasing(`librosa.chirp` + `[::4]`, `stft`, `specshow`), 수식 검증 2(`np.fft.rfft` + Hann으로 alias 주파수 예측 vs 측정) |
| 3 | 양자화: 소리의 크기를 몇 단계로 적을까 | `quantize(y, bits)`, `sf.write(subtype="PCM_16"/"PCM_24"/"FLOAT")`, 수식 검증 3(SNR ≈ 6.02b + 1.76) |
| 4 | 채널: mono와 stereo | `np.stack`, `(2,N)` vs `(N,2)`, `librosa.load(mono=False)`, 수식 검증 4 |
| 5 | 오디오 파일 포맷: WAV, FLAC, MP3, Opus | FLAC 저장, ffmpeg MP3 64k / `libopus` 24k, `decode()`로 공정 비교, 수식 검증 5(비트레이트·크기 예측) |
| 6 | 오디오 다루는 도구들과 전처리기 | 6-1 pydub(`AudioSegment`, ms 슬라이싱, `+6` dB, `silent`, `export`), 수식 검증 6, 6-2 미니 프로젝트 `make_model_ready()`(load 16k mono → `librosa.effects.trim(top_db=30)` → peak normalize 0.9 → PCM_16), `describe()`, 6-3 내 목소리 녹음(선택) |
| 7 | 정리 & 과제 | 개념·수식 요약표 |

**빈칸 실습 7개 (정답)**: `tone(880)` / `target_sr=16000` / `subtype="PCM_16"` / `stereo.mean(axis=0)` / `bytes_per_sample = 2` / `audio[:2000]` / `make_model_ready()`의 `sr=16000, mono=True`

**과제**: 1) 휴대폰 녹음(m4a 등)을 `make_model_ready()`로 변환하고 `describe()` 전후 비교 2) MP3 32k/64k/128k 크기·음질 비교 3) `tone()`으로 "도레미파솔"(262, 294, 330, 349, 392 Hz) 이어 붙이기(`np.concatenate`)

**animation.html**: D2-1 오늘의 흐름 · D2-2 소리의 정체 · D2-3 샘플링 · D2-4 양자화 · D2-5 채널 · D2-6 포맷 계산기 · D2-7 도구 고르기 · D2-8 pydub 편집기 · D2-9 전처리 파이프라인 ("소리가 나오는 탭이 많으니 이어폰을 준비하세요")

**worksheet**: 1교시 소리의 정체·샘플링 / 2교시 양자화·채널 / 3교시 파일 포맷·비트레이트 / 4교시 편집·전처리기 (예: "44,100 Hz의 7,000 Hz 소리를 [::4]로 건너뛰어 11,025 Hz로 만들면 몇 Hz로 들립니까?")

---

### Day 3 — 「주파수 분석: FFT · STFT · Mel · MFCC」

**학습 목표**: 1) 복잡한 소리 = 여러 사인파의 합 2) DFT를 "시험 사인파와 곱해서 더하기"로 이해하고 직접 구현해 `np.fft`와 비교 3) Δf = f_s/N, Hann 창과 spectral leakage 4) STFT 스펙트로그램과 시간-주파수 트레이드오프 5) Mel 필터뱅크로 **Whisper 입력(80 × 3000 Log-Mel)**을 만들고, MFCC가 포먼트를 담는 이유 설명

**교시**: 1교시 사인파의 합·배음·포먼트·DFT 원리 / 2교시 FFT(해상도·창 함수·dB) / 3교시 STFT·트레이드오프 / 4교시 Mel·Log-Mel·MFCC·특징 추출기

**슬라이드 (23장)**: 3.0 "Whisper가 읽는 '소리 그림'은 어떻게 만들어질까" → 3.1 사인파의 합, 포먼트, 두 가지 시점 → 3.2 DFT 원리, 오일러 공식, DFT 공식, FFT("결과는 같고, 계산은 약 100배 빠르다") → 3.3 주파수 해상도, 창 함수 → 3.4 STFT, frame 수와 모양, 트레이드오프 → 3.5 Mel, Log-Mel("Whisper 입력 80 × 3000의 정체") → 3.6 MFCC, 봉우리 vs 음 높이, 미니 프로젝트 `extract_features()`, 수식으로 정리, 알아 둘 점 → 정리

**실습 항목**
| Part | 제목 (원문) | 주요 내용 |
|---|---|---|
| 0 | 준비 | edge-tts, librosa, `scipy.fft`, D2 `make_model_ready()` 재사용 |
| 1 | 소리는 사인파의 합이다 | 배음 합성, 1-1 푸리에 급수와 포먼트(`vowel()`: 아 F1≈700/F2≈1200, 이 300/2300, 우 300/800 Hz) |
| 2 | DFT: 어떤 높이가 얼마나 들어 있는지 재는 방법 | `dft()`(X = W @ x) 직접 구현, bin→Hz, 수식 검증 1(진폭 A = 2\|X[k]\|/N) |
| 3 | FFT 실습: 해상도, 창 함수, dB | Δf, Hann 창과 leakage, 수식 검증 2 |
| 4 | STFT와 스펙트로그램 | `my_stft()`(자르기 → 창 → rfft), n_fft 2048/400/128 비교(협대역/광대역), 수식 검증 3(frame 수, 30초 = 3000 frame) |
| 5 | Mel 스펙트로그램: 사람 귀에 맞춘 주파수 축 | 삼각형 필터뱅크, `melspectrogram(n_fft=400, hop_length=160, n_mels=80)`, 수식 검증 4 |
| 6 | MFCC: 소리의 봉우리 모양을 13개 숫자로 | DCT, 수식 검증 5(앞 K개 계수로 Log-Mel 복원), 6-2 미니 프로젝트 **음성 특징 추출기 `extract_features()`**(전처리 → STFT → Mel → Log → DCT 13) |
| 7 | 정리 & 과제 | 수식 요약표(DFT, Hann, STFT, Mel `m = 2595log10(1+f/700)`, MFCC) |

**빈칸 실습 7개 (정답)**: `tone(392)` / `SR / N`, `np.abs(X)` / `np.hanning(N)` / `hop = int(0.010 * SR)` / `n_mels=80` / `n_mfcc=13` / `n_fft=400, hop_length=160`

**과제**: 1) "아, 이, 우" 녹음 → MFCC 평균과 모음 간 거리 표 2) n_fft 256/400/1024/2048 스펙트로그램 비교 3) `dft()` vs `np.fft.fft` 계산 시간 그래프(N = 256~2048)

**animation.html**: D3-1 오늘의 흐름 · D3-2 사인파의 합 · D3-3 DFT 원리 · D3-4 주파수 해상도 · D3-5 창 함수 · D3-6 STFT 프레이밍 · D3-7 시간-주파수 트레이드오프 · D3-8 Mel 필터뱅크 · D3-9 MFCC (마이크 입력 사용)

---

### Day 4 — 「오디오 전처리: 정규화 · 노이즈 제거 · VAD」

**학습 목표**: 1) SNR 정의, 원하는 SNR로 잡음 섞기 2) peak·RMS·dBFS 정규화, DC 제거, pre-emphasis, high-pass 3) STFT 위에서 **스펙트럼 차감**과 **Wiener 이득** 직접 구현 4) `noisereduce` spectral gating과 트레이드오프 5) **에너지·ZCR VAD**(히스테리시스)를 만들고 **Silero VAD**와 비교해 전처리 파이프라인 완성

**교시**: 1교시 잡음·SNR·정규화·필터(Part 1~2) / 2교시 스펙트럼 차감·Wiener·spectral gating(Part 3~4) / 3교시 VAD 원리(Part 5) / 4교시 Silero VAD·`preprocess()`(Part 6~7)

**슬라이드 (20장)**: "시끄러운 녹음을 모델이 좋아하는 음성으로 바꾸려면" → 1.1 잡음과 SNR, 원하는 SNR로 섞기 → 2.1 정규화, 2.2 pre-emphasis·high-pass → 3.1 스펙트럼 차감, 3.2 Wiener 이득 → 4.1 spectral gating, 4.2 "무엇이 더 좋은가: 지표 하나로 판단하지 않는다" → 5.1 VAD, 5.2 히스테리시스 VAD, 5.3 에너지 VAD의 한계 → 6.1 Silero VAD, 확률 곡선과 강인성 → 6.2 미니 프로젝트 `preprocess()` → 6.3 수식 정리, 헷갈리기 쉬운 것 → 정리

**실습 항목**
| Part | 제목 (원문) | 주요 내용 |
|---|---|---|
| 0 | 준비 | `pip install edge-tts librosa soundfile noisereduce silero-vad`, `scipy.signal`, 앞 0.8초·뒤 0.5초 무음을 붙인 음성 |
| 1 | 잡음이 섞인 음성과 SNR | white/pink(1/f)/hum 잡음, `add_noise()`(g 공식), 수식 검증 1 |
| 2 | 정규화와 기본 필터 | peak vs RMS 정규화(−20 dBFS), pre-emphasis(α=0.97), Butterworth high-pass(60 Hz 험 제거), 수식 검증 2(\|H\|² 예측 vs 측정) |
| 3 | 노이즈 제거 1: 스펙트럼 차감과 Wiener 이득 | 앞부분 프레임으로 잡음 추정, `spectral_subtract()`(β 과차감, γ floor), Wiener `G = ξ/(1+ξ)`, 수식 검증 3 |
| 4 | 노이즈 제거 2: spectral gating (`noisereduce`) | `nr.reduce_noise(y_noise=..., stationary=True)`, 지표 3개(전체 SNR·무음 잡음 감소·음성 크기 변화), (선택) DeepFilterNet 주석 코드, 수식 검증 4(T_k = μ_k + 1.5σ_k) |
| 5 | VAD 1: 에너지와 ZCR로 말소리 구간 찾기 | 프레임 에너지(dB)·ZCR, `energy_vad()` 히스테리시스(T_high = floor+12, T_low = floor+6 dB, hangover), 수식 검증 5 |
| 6 | VAD 2: Silero VAD와 전처리 파이프라인 | `load_silero_vad`, `get_speech_timestamps`, 32 ms(512샘플) 확률 곡선, 파라미터 실험과 잡음 강인성, 6-2 미니 프로젝트 **`preprocess()`**(16k mono → DC·high-pass → Silero VAD → VAD 무음 구간을 `y_noise`로 noisereduce → RMS −20 dBFS·peak 0.99 → 구간별 자르기), 수식 검증 6 |
| 7 | 정리 & 과제 | 수식 요약표 13행 |

**빈칸 실습 9개 (정답)**: `snr_db` / `/ 20` / `alpha` / `beta` / `1 + xi` / `0.5`(잡음 구간 초) / `20 * log10`, `T_lo` / `CHUNK = 512` / `noise_mask[...] = False`

**과제**: 1) 조용한 방·시끄러운 곳 녹음을 `preprocess()`로 비교 2) white·pink·hum × SNR 20/10/5/0 dB × 3방법 결과 표 3) Silero `threshold`(0.3/0.5/0.7) × `min_silence_duration_ms`(100/300/1000) 표와 실시간 비서용 권장값

**animation.html**: D4-1 오늘의 흐름 · D4-2 잡음과 SNR · D4-3 정규화 · D4-4 pre-emphasis·high-pass · D4-5 스펙트럼 차감·Wiener · D4-6 spectral gating · D4-7 에너지·ZCR VAD · D4-8 Silero VAD · D4-9 전처리 파이프라인 (마이크 사용)

**강사용 노트북 추가 내용**: "이 강사용 노트북 사용법"(🎯 핵심 · 🗣️ 강사 멘트 · 🍎 비유 · 🖥️ 화면 시연 · ❓ 질문→예상 답 · 🆘 단계별 힌트 · ⚠️ 오개념 · ➡️ 연결 멘트 · ⏱️ 권장 시간), "하루 시간표와 수업 전 점검"(교시별 빈칸·애니메이션·슬라이드 페이지 매핑, **진도가 밀릴 때 줄이는 순서**, 수업 15분 전 체크리스트), "오늘의 난이도 경고"(비유 → 소리 → 그림 → 수식 순서)

---

### Day 5 — 「딥러닝 오디오 분류 + 미니 프로젝트: Speech Commands 키워드 인식」

**학습 목표**: 1) Speech Commands(1초 · 16 kHz · 35단어 · 화자 기준 분할)를 `torchaudio`로 내려받기 2) Log-Mel (1 × 64 × 101)을 `Dataset`·`DataLoader`로 묶기 3) CNN 합성곱·풀링·출력 크기·파라미터 수, softmax·cross-entropy 4) 학습 루프 직접 작성, 학습 곡선·정확도·혼동 행렬 평가 5) **SpecAugment** 적용, 내 음성 키워드를 맞히는 `predict_keyword()` 완성

**교시**: 1교시 데이터셋·1초 맞추기·Log-Mel·DataLoader / 2교시 CNN·softmax·CE / 3교시 학습 루프·곡선·혼동 행렬 / 4교시 SpecAugment·`predict_keyword()`·저장

**슬라이드 (19장)**: "1초 음성을 듣고 단어를 맞히는 모델은 어떻게 만들까" → 1.1 Speech Commands, 1.2 입력 모양 맞추기 → 2.1 Log-Mel 특징, 2.2 Dataset·DataLoader → 3.1 합성곱, 3.2 KWSNet("Conv 블록 4개 + GAP + Linear: 약 6만 개 파라미터"), 3.3 softmax·cross-entropy → 4.1 경사 하강법, 4.2 학습 루프, 4.3 학습 곡선 읽기 → 5.1 혼동 행렬 → 6.1 SpecAugment, 6.2 미니 프로젝트 → 수식 정리, 헷갈리기 쉬운 것 → 정리

**실습 항목**
| Part | 제목 (원문) | 주요 내용 |
|---|---|---|
| 0 | 준비 | `pip install gTTS soundfile`, torch·torchaudio·`torchaudio.transforms`, GPU 유무로 `MAX_TRAIN`(1500/400), `MAX_EVAL`(300/100), `EPOCHS`(12/5) 자동 조정, `torchaudio.datasets.SPEECHCOMMANDS` v0.02 다운로드(**약 2.3 GB**) |
| 1 | Speech Commands 데이터셋 | 10 키워드 `yes, no, up, down, left, right, on, off, stop, go`, 화자 기준 분할(80/10/10), 1-2 `pad_or_trim()` |
| 2 | 특징: 1초 음성 → Log-Mel 이미지 (1 × 64 × 101) | n_fft 400, hop 160, n_mels 64, 특징 미리 계산, Dataset 클래스, `BATCH = 128` |
| 3 | CNN: 소리 이미지를 보는 신경망 | **KWSNet**(Conv3×3+BN+ReLU+MaxPool ×4 → GAP → Dropout 0.3 → Linear 64→10), 수식 검증 1(forward hook으로 층별 모양·파라미터), 3-3 softmax 직접 구현 |
| 4 | 학습: forward → loss → backward → step | `fit()`(Adam, lr=1e-3), 학습 곡선, 4-2 곡선 읽는 법(과적합/과소적합/NaN) |
| 5 | 평가: 정확도와 혼동 행렬 | `argmax`, 수식 검증 2(클래스별 정밀도·재현율·F1, 가장 헷갈린 쌍), 틀린 예 들어 보기 |
| 6 | 성능 높이기: SpecAugment, 그리고 미니 프로젝트 | `T.FrequencyMasking`, `T.TimeMasking`으로 재학습, **`predict_keyword()`**(16k → 무음 자르기·1초 중심 → Log-Mel → 학습 세트 μ·σ 정규화 → softmax top-3), gTTS(영어) 음성으로 시험, `kws_cnn.pt` 저장(가중치 + μ·σ·키워드) |
| 7 | 정리 & 과제 (미니 프로젝트 보고서) | 수식·코드 요약표 13행 |

**빈칸 실습 9개 (정답)**: `n`(1초 샘플 수) / `HOP` / `self.X[i]` / `n_classes` / `dim=1` / `loss.backward()`, `opt.step()` / `argmax(dim=1)` / `augment=augment` / `- MU`

**과제**: 1) 키워드를 `zero~nine`으로 바꿔 재학습, 가장 헷갈린 쌍 보고 2) n_mels(40/64/80) · 채널 수(반/두 배) · 학습률(1e-2/1e-3/1e-4) 중 하나 비교 3) 휴대폰으로 키워드 10개 녹음 → `predict_keyword()` 오답 분석

**animation.html**: D5-1 오늘의 흐름 · D5-2 데이터셋과 분할 · D5-3 1초 음성 → Log-Mel · D5-4 합성곱 · D5-5 모델 구조 · D5-6 softmax·loss · D5-7 경사 하강법·학습 곡선 · D5-8 혼동 행렬 · D5-9 SpecAugment

**강사용 노트북**: 강사 스크립트 셀 42개 (🗣️ 56회 · 🍎 30회 · 🆘 10회 · "예상 출력" 12회)

---

### Day 6 — 「ASR 원리: CTC · Attention Encoder-Decoder · Transducer, Wav2Vec2 · HuBERT」

**학습 목표**: 1) 음성 인식의 **정렬 문제**(T ≫ U, 정렬 라벨 없음) 2) CTC blank·접기 규칙 𝓑·forward(α) 직접 구현 → `F.ctc_loss` 비교 3) **Wav2Vec2 + CTC** 실전: 프레임 수 `T = ⌊(L − 400)/320⌋ + 1`, greedy 디코딩, 글자 타임스탬프 4) AED(Whisper) scaled dot-product attention과 한 토큰씩 생성 루프, cross-attention 정렬 5) **Transducer(RNN-T)** T × (U+1) 격자와 α 점화식, 세 방식 비교 6) **자기지도 학습**: wav2vec 2.0 마스킹·양자화·InfoNCE, HuBERT k-means 가짜 라벨

**교시**: 1교시 정렬 문제·CTC(Part 0~2) / 2교시 Wav2Vec2+CTC 실전(Part 3) / 3교시 AED·Transducer·비교(Part 4~5) / 4교시 자기지도 학습(Part 6~7)

**슬라이드 (20장)**: "소리 200프레임을 글자 11개로, 정렬도 모른 채 어떻게 배울까" → 1.1 정렬 문제 → 2.1 CTC blank와 접기 규칙, 2.2 CTC 확률과 경로 수, 2.3 forward(α) 알고리즘 → 3.1 Wav2Vec2 프레임 수, 3.2 greedy 디코딩과 CTC 스파이크, 3.3 CTC 타임스탬프 → 4.1 Attention Encoder-Decoder, 4.2 scaled dot-product attention, 4.3 Whisper로 직접 확인 → 5.1 Transducer, 5.2 세 방식 비교("빠른 CTC, 똑똑한 AED, 스트리밍 Transducer") → 6.1 wav2vec 2.0 사전학습, 6.2 HuBERT와 모델 비교 → 수식 정리, 헷갈리기 쉬운 것 → 정리

**실습 항목**
| Part | 제목 (원문) | 주요 내용·모델 |
|---|---|---|
| 0 | 준비 | `pip install gTTS`, gTTS 영어 문장 → 16 kHz |
| 1 | 음성 인식은 무엇이 어려운가: 정렬 문제 | T vs U 비교, 세 방식 개요 표 |
| 2 | CTC: 모든 정렬 경로를 더하기 | `ctc_collapse()`, 경로 전수 열거(작은 T), forward(α) 구현, 수식 검증 1(내 α = 전부 더하기 = `F.ctc_loss`) |
| 3 | Wav2Vec2 + CTC로 실제 음성 받아 적기 | **`facebook/wav2vec2-base-960h`**(`Wav2Vec2ForCTC`, `Wav2Vec2Processor`), 프레임 수 공식, greedy 디코딩, CTC 스파이크·blank 비율, 글자·단어 타임스탬프(0.02 s) |
| 4 | Attention Encoder-Decoder: 한 글자씩 생성하기 | attention 직접 구현, 수식 검증 2(√d 스케일), **`openai/whisper-tiny`**(`attn_implementation="eager"`), 한 토큰씩 greedy 루프 vs `generate()`, alignment_heads cross-attention 그림 |
| 5 | Transducer (RNN-T): 스트리밍을 위한 방법 | log 공간 α 점화식, 수식 검증 3(`torchaudio.functional` RNN-T 손실 비교, 경로 수 비교), 5-2 세 방식 비교표 |
| 6 | 자기지도 학습: 라벨 없이 소리를 먼저 배우기 | 수식 검증 4(마스킹 비율 1−(1−p)^M), InfoNCE, **`facebook/wav2vec2-base`**(`Wav2Vec2ForPreTraining`, `_compute_mask_indices`, `_sample_negative_indices`), 6-4 **`facebook/hubert-base-ls960`** + sklearn `KMeans` 가짜 라벨, "피치 +4" 실험 |
| 7 | 정리 & 과제 | 수식·코드 요약표 13행 |

**빈칸 실습 9개 (정답)**: `blank` / `lp[s - 2]` / `S_TOT` / `argmax(dim=-1)` / `FRAME_SEC = S_TOT / SR` / `math.sqrt(d)` / `logits_w[0, -1]` / `y[u - 1]` / `[:, 0]`

**과제**: 1) `kresnik/wav2vec2-large-xlsr-korean`으로 gTTS 한국어 2문장 받아 적기(어휘가 음절인지 자모인지 확인) 2) 문장 길이별 CTC blank 비율·글자당 프레임 수, `slow=True` 비교 3) 설계 보고서: "AI 콜센터 실시간 자막 + 통화 후 정확한 녹취록"에 CTC/AED/Transducer 선택 근거

**animation.html**: D6-1 오늘의 흐름 · D6-2 정렬 문제 · D6-3 CTC 접기 · D6-4 CTC 격자·α · D6-5 Wav2Vec2 프레임·디코딩 · D6-6 Cross-attention · D6-7 Transducer 격자 · D6-8 세 방식 비교 · D6-9 자기지도 학습

**강사용 노트북**: 강사 스크립트 셀 27개, "오늘의 비유 사전 (먼저 읽어 두기)", Part별 ⏱️ 분 단위 배분(예: "Part 2-2 ~ 2-3 경로 수와 α ⏱️ 12분"), 🆘 힌트 24회

---

### Day 7 — 「Whisper 심층 분석: 구조 · 모델 크기 · 언어 감지 · 디코딩 옵션 · 환각 대응」

**학습 목표**: 1) **30초 창 → Log-Mel → Encoder(귀) → Decoder(손)** 구조, 특수 토큰으로 언어·작업 바꾸기 2) tiny~large-v3·turbo 속도·정확도 교환(RTF, CER) 3) 언어 감지(첫 토큰 확률), 받아쓰기 ↔ 영어 번역 4) greedy·beam·temperature·타임스탬프·프롬프트 비교 5) 무음·반복 **환각**을 만들고 VAD·무음 확률·압축률·temperature fallback으로 막기

**교시**: 1교시 구조·특수 토큰(Part 0~1) / 2교시 모델 크기·언어 감지·번역(Part 2~3) / 3교시 디코딩 옵션(Part 4) / 4교시 환각(Part 5~6)

**노트북 표기 체계(D7에서 새로 추가)**: 💬 쉽게 말하면 · 🍎 비유 · 👣 한 단계씩 · 📐 핵심 식 하나 · ❓ 생각해 보기 · 🔍 코드 해설

**슬라이드 (pdf 20쪽)**: "Whisper를 '잘 쓰는' 사람이 되기 위한 다섯 질문" → 1.1 Whisper 구조(🍎 통역 부스의 두 사람), 1.2 30초 창, 1.3 특수 토큰(🍎 식당 주문서) → 2.1 모델 크기(🍎 자동차 배기량), 2.2 RTF와 CER → 3.1 언어 감지, 3.2 번역 → 4.1 greedy vs beam search(🍎 길 찾기), 4.2 temperature, 4.3 타임스탬프와 프롬프트 → 5.1 환각(🍎 빈칸을 못 견디는 학생), 5.2 환각을 숫자로 잡기, 5.3 기본 안전장치, 5.4 VAD 먼저, 5.5 환각 대응 체크리스트 → 6.1 헷갈리기 쉬운 것 → 정리

**실습 항목**
| Part | 제목 (원문) | 주요 내용·모델 |
|---|---|---|
| 0 | 준비 | `pip install gTTS jiwer silero-vad`, `zlib`, transformers `WhisperProcessor`/`WhisperForConditionalGeneration`, 기본 모델 **`openai/whisper-small`**(GPU float16), 시험 문장(ko, ko_terms 등) |
| 1 | Whisper의 구조: 귀가 듣고, 손이 받아 적는다 | 1-1 30초 창(480,000샘플 → 80 × 3000, large-v3·turbo는 128 mel), 1-2 Encoder 3000 → 1500칸(Conv 보폭 2), 1-3 특수 토큰(`<\|startoftranscript\|>`, `<\|ko\|>`, `<\|transcribe\|>`/`<\|translate\|>`, `<\|notimestamps\|>`, `<\|endoftext\|>`), 주문서를 직접 써서 디코딩 |
| 2 | 모델 크기: 빠르게 vs 정확하게 | 크기 표(tiny 39M ~ large-v3 1550M, turbo 809M·Dec 4층·번역 학습 안 함), CER·RTF, 후보 `whisper-tiny/base/small` + GPU면 **`whisper-large-v3-turbo`** |
| 3 | 언어 감지와 번역 | SOT 다음 언어 토큰 99개 softmax, 감지 오류와 대처표, `task="translate"`(영어로만, turbo 불가) |
| 4 | 디코딩 옵션: 같은 모델, 다른 받아쓰기 | 1.25배 빠르기 + SNR 5 dB "어려운 음성", greedy vs `num_beams=5`, temperature 반복 실험, `return_timestamps=True`(0.02초 시각 토큰, `output_offsets`), 프롬프트 `proc.get_prompt_ids("노마드랩 연구소, 라이브킷, 파이프캣, 음성 에이전트.")` |
| 5 | 환각(hallucination): 들리지 않은 말을 지어낸다 | 유형 4가지 표, 5-1 무음 입력 실험, 5-2 `<\|nospeech\|>` 확률(0.6), 5-3 압축률(zlib), 5-4 안전장치 세트(`compression_ratio_threshold=1.35`, `logprob_threshold=-1.0`, `no_speech_threshold=0.6`, temperature 사다리 0.0~1.0, `condition_on_prev_tokens=False`), 5-5 Silero VAD로 무음 먼저 자르기, 5-6 환각 대응 체크리스트 |
| 6 | 정리 & 과제 | 개념·코드 요약표 |

**빈칸 실습 9개 (정답)**: `CHUNK_SEC = 30` / `"<|ko|>"` / `RTF = elapsed / dur` / `LANG_IDS` / `TASK = "translate"` / `NUM_BEAMS = 5` / `PROMPT` / `probs[NOSPEECH]` / `zlib.compress`

**과제**: 1) 30초 한국어 녹음(전문 용어 3개 이상)을 tiny·small·turbo로 RTF·CER·오류 단어 표 2) **환각 사냥**: 1분 이상 음성을 ① 안전장치 없음 ② 안전장치 세트 ③ VAD 먼저 로 비교 3) 설계 메모: "공장 현장 안전 점검 음성 보고 앱"의 모델 크기·language·프롬프트 용어·환각 대응

**animation.html**: D7-1 오늘의 흐름 · D7-2 30초 창과 구조 · D7-3 특수 토큰 주문서 · D7-4 모델 고르기 · D7-5 언어 감지 · D7-6 빔 서치 · D7-7 temperature·fallback · D7-8 타임스탬프·프롬프트 · D7-9 환각 실험실

**다음 시간(D8) 예고**: faster-whisper(CTranslate2), whisper.cpp, int8 양자화, 청크 기반 스트리밍 인식

---

## 4. 커리큘럼 흐름

### 이 zip이 다루는 범위 (Day 1~7)
| 단계 | Day | 핵심 질문 | 만드는 결과물 | 다음 날로 넘어가는 것 |
|---|---|---|---|---|
| ① 전체 맛보기 | D1 | 음성 AI는 무엇을 넣고 무엇을 얻나? | TTS → ASR → LLM → TTS **미니 음성 비서** | "샘플 80,000개는 어떻게 만들어지나?" |
| ② 소리 → 숫자 | D2 | 16kHz WAV의 정체는? | `make_model_ready()` 전처리기 | 16k mono 배열 |
| ③ 숫자 → 그림 | D3 | Whisper가 읽는 소리 그림은? | `extract_features()`(Log-Mel 80 × T, MFCC 13) | Log-Mel 특징 |
| ④ 그림 정리 | D4 | 시끄러운 녹음을 어떻게 고치나? | `preprocess()`(필터·VAD·잡음 제거·정규화·자르기) | 정리된 음성 구간 |
| ⑤ 그림 → 단어 | D5 | 1초 음성으로 단어를 맞히려면? | KWSNet CNN + `predict_keyword()` | Log-Mel·CNN·학습 루프 개념 |
| ⑥ 그림 → 문장(원리) | D6 | 정렬 없이 어떻게 받아쓰기를 배우나? | CTC α / AED 디코딩 루프 / RNN-T α 직접 구현 | AED의 예로서 Whisper |
| ⑦ Whisper 실전 | D7 | Whisper를 잘 쓰려면? | 모델 선택표, 디코딩 옵션 비교, 환각 대응 체크리스트 | D8 고속화·스트리밍 |

### 과정 전체 로드맵 (D1 슬라이드 4 "음성 비서 단면도로 보는 8주")
```
1주  입력·오디오 : 디지털 오디오 · 샘플링 · 스펙트로그램 · VAD          ← D1~D5 (이 zip)
2주  ASR 듣기    : Whisper · faster-whisper · 화자 분리                 ← D6~D7 (이 zip), D8~D10은 없음
3주  ASR         : 한국어 Fine-tuning
4주  TTS 말하기  : Kokoro · Chatterbox · Voice Cloning과 윤리
5주  LLM 생각하기: Claude API · Tool Calling · RAG · MCP
6주  실시간      : Pipecat · LiveKit · Streaming
7주  배포        : FastAPI · Docker · Edge
8주  최종 프로젝트: AI 콜센터, 키오스크 음성 주문, 회화 튜터 등
평가(모든 층)    : CER · WER(정확도), RTF(속도), MOS(음질), Latency(응답)
```

---

## 5. 사용 기술·도구·외부 서비스

| 분류 | 이름 | 사용 Day | 용도 |
|---|---|---|---|
| 실행 환경 | Google Colab (T4 GPU, Python 3.13) | 전체 | 모든 실습. D1·D5·D6·D7 노트북 메타데이터에 `accelerator: GPU`, `gpuType: T4` |
| 실행 환경 | uv | D1 | 로컬 Python 환경(`uv init`, `uv add`, `uv run jupyter lab`) |
| 실행 환경 | FFmpeg | D1·D2 | mp3/webm/m4a → 16kHz mono WAV, MP3/Opus 인코딩 |
| 오디오 | librosa | 전체 | load, resample, stft, melspectrogram, mfcc, effects.trim, chirp, display |
| 오디오 | soundfile | D2~ | 읽기/쓰기, `subtype`(PCM_16/24/FLOAT), `sf.info` |
| 오디오 | pydub (+ audioop-lts) | D2 | ms 단위 편집, 볼륨, 이어 붙이기 |
| 수치 | numpy, scipy (fft, signal) | 전체 | DFT/FFT, Butterworth 필터 |
| 잡음 제거 | noisereduce | D4 | spectral gating |
| 잡음 제거 | DeepFilterNet (선택, 주석) | D4 | 48 kHz 딥러닝 잡음 제거 |
| VAD | Silero VAD (`silero-vad`) | D4·D7 | `load_silero_vad`, `get_speech_timestamps` |
| 딥러닝 | PyTorch, torchaudio | D1·D4~D7 | CNN 학습, SpecAugment(`FrequencyMasking`, `TimeMasking`), `F.ctc_loss`, RNN-T 손실 |
| 딥러닝 | Hugging Face transformers | D6·D7 | Wav2Vec2ForCTC, Wav2Vec2ForPreTraining, HubertModel, WhisperForConditionalGeneration |
| ML | scikit-learn | D6 | KMeans, StandardScaler (HuBERT 가짜 라벨) |
| ASR 모델 | faster-whisper (`large-v3-turbo` / `small` / `medium`) | D1 | CTranslate2 기반 받아쓰기 |
| ASR 모델 | `openai/whisper-tiny`, `-base`, `-small`, `-large-v3-turbo` | D6·D7 | AED 구조 실습, 크기 비교 |
| ASR 모델 | `facebook/wav2vec2-base-960h`, `facebook/wav2vec2-base`, `facebook/hubert-base-ls960` | D6 | CTC 받아쓰기, 자기지도 사전학습 확인 |
| ASR 모델 (과제) | `kresnik/wav2vec2-large-xlsr-korean` | D6 과제 | 한국어 CTC |
| 평가 | jiwer | D1·D7 | CER(WER) |
| TTS (외부, 인터넷 필요) | edge-tts (Microsoft Edge 온라인 Neural TTS) | D1~D4 | `ko-KR-SunHiNeural`, `ko-KR-InJoonNeural` |
| TTS (외부, 인터넷 필요) | gTTS (Google) | D5~D7 | 시험용 영어/한국어 음성 |
| LLM (외부, 선택) | Anthropic Claude API (`claude-haiku-4-5-20251001`) | D1 | 미니 음성 비서 응답. 키가 없으면 규칙 기반 응답으로 대체 |
| 데이터셋 | Google Speech Commands v0.02 (torchaudio, 약 2.3 GB) | D5 | 키워드 인식 |
| 브라우저 API | MediaRecorder, getUserMedia, Web Audio, speechSynthesis, Canvas | 노트북 녹음·animation.html | 마이크 녹음, 실시간 시각화, 브라우저 TTS |
| 제출 | Notion | D2~D7 | 워크시트 결과를 클립보드로 복사해 붙여 넣기 |
| 웹 호스팅 | GitHub Pages (`04-voice-ai`) | 전체 | 애니메이션·워크시트 온라인 링크 |
| 슬라이드 제작 | PptxGenJS → LibreOffice 24.2 Impress로 PDF 변환 | 전체 | PDF 메타데이터(Author: PptxGenJS, Producer: LibreOffice 24.2) |
| 언급만 (후속 주차) | Kokoro, Chatterbox, OpenAI Realtime, Gemini Live, Pipecat, LiveKit Agents, MCP, whisper.cpp | D1·D7 | 로드맵·예고 |

---

## 6. 특이사항

| 구분 | 내용 |
|---|---|
| **pdf vs pptx** | D1~D6은 pptx와 pdf의 장 수가 같고(25/22/23/20/19/20) 슬라이드 본문도 같습니다. 차이는 **발표자 노트(`[노트]`)가 pptx에만 있다**는 점입니다(pdf에는 0개). pdf는 pptx를 LibreOffice로 변환한 것입니다. |
| **누락** | **day07에는 pptx가 없습니다**(pdf 20쪽만 있음). 따라서 D7은 발표자 노트도 없습니다. D7 pdf 메타데이터상 원본은 PptxGenJS로 만든 pptx입니다. |
| **누락** | **D1~D3, D7에는 강사용 노트북이 없습니다**(강사용은 D4·D5·D6만 있음). README·LICENSE 파일이 없어 이용 조건이 명시되어 있지 않습니다. |
| **과정 일부만 포함** | 슬라이드에 "Day N / 40" 표기가 있습니다. 160시간 과정 중 Day 1~7(약 28시간)만 들어 있고, D8 이후 자료는 없습니다. |
| **강사용 vs 실습용** | 강사용 = 학생용 노트북의 **모든 셀(코드 셀 100% 동일)** + 인용 블록(`>`) 형식의 🎤 강사 스크립트 markdown 셀(D4 53개, D5 42개, D6 27개). 제목 셀에만 "— 🎤 강사용"이 붙습니다. 강사 스크립트에는 시간표, 슬라이드·애니메이션 매핑, 그대로 읽어도 되는 멘트, 비유, 예상 질문과 답, 단계별 힌트, **예상 출력**, 진도 조절 순서가 들어 있습니다. |
| **정답 노출** | 학생용 노트북에도 빈칸 정답과 해설이 `<details>`("🔑 정답 및 해설 보기")로 접혀 들어 있습니다. 강사용에만 있는 것은 정답이 아니라 수업 운영 스크립트입니다. 강사용 노트북에 "**학생에게는 이 파일을 배포하지 마세요**"라고 적혀 있지만 같은 레포에 함께 들어 있습니다. |
| **워크시트 정답** | worksheet.html은 클라이언트에서 채점하므로 **정답과 해설이 JS 배열(`const Q=`)에 평문으로 들어 있습니다**(페이지 소스를 보면 확인 가능). D1은 15문항·인쇄/PDF 제출, D2~D7은 40문항·노션 복사 제출로 형식이 다릅니다. |
| **실행 환경 요구** | Colab T4 GPU 권장. D1 faster-whisper는 Colab에서 CUDA 12 cuBLAS/cuDNN을 추가 설치하고 ctypes로 미리 로드합니다(`libcublas.so.12` 오류 대응). PyAV 충돌(`metadata_errors`)을 피하려고 numpy 배열을 직접 넘깁니다. D2의 pydub은 Python 3.13에서 `audioop-lts`가 필요합니다. GPU가 없으면 D1은 `small` 모델, D5는 데이터·epoch를 줄여 자동으로 대체합니다. |
| **인터넷·다운로드** | edge-tts, gTTS는 온라인 서비스입니다. D5는 Speech Commands **약 2.3 GB**를 받고, D6·D7은 Hugging Face 모델(최대 whisper-large-v3-turbo)을 받습니다. 마이크 녹음은 Colab 브라우저 권한이 필요하고, 실패하면 sample.wav로 대체합니다. |
| **API 키 등 민감정보** | 노출되지 않았습니다. `ANTHROPIC_API_KEY`는 Colab Secrets(`google.colab.userdata.get`)로만 읽고, 하드코딩된 키·토큰·비밀번호는 없습니다(sk-ant, hf_, ghp_, AIza 등 패턴 검색 결과 0건). |
| **HTML 외부 의존** | animation/worksheet는 단일 파일이고 외부 리소스는 Google Fonts뿐입니다. 서버 전송은 없고 localStorage도 쓰지 않습니다. D1·D3·D4 animation은 마이크를 사용합니다. |
| **노트북 상태** | 10개 노트북 모두 셀 출력이 비어 있습니다(실행 전 상태). 그림은 markdown 안에 base64로 들어 있어 파일이 큽니다(최대 1.71 MB). |
| **표기 불일치** | D1 노트북 Part 1 안에 "1-4"가 두 번 나옵니다(빈칸 실습 준비 / 로컬 uv). D4 슬라이드 절 번호는 "0.0, 1.1, 2.1…" 형식이고, D2·D3는 "2.1, 3.1…" 형식입니다. |
| **폴더 구조** | zip을 풀면 `AI_Voice-main/AI_Voice-main/` 이중 폴더가 됩니다. 원본 파일명은 한글입니다. |

---

## 7. 활용 포인트


1. **강의 상품: "4자료 세트" 포맷을 자체 바이브코딩·AI 강의의 표준 템플릿으로 쓰기**
   슬라이드(발표자 노트) + 빈칸 노트북(`check()` 자동 판정 + `<details>` 정답) + 탭 9개 애니메이션 + 자동 채점 워크시트로 구성된 Day 단위 패키지 구조를 그대로 가져와 디지털노마드연구소 커리큘럼(예: "음성 에이전트 만들기 7일")의 표준 포맷으로 씁니다. 강사용 노트북의 이모지 마커 체계(🎯 🗣️ 🍎 🆘 ⏱️)는 공동 강사나 외부 강사용 **강사 매뉴얼 상품**으로도 만들 수 있습니다.

2. **전자책: 『Whisper를 제대로 쓰는 법: 환각 대응과 한국어 음성 인식 실전』**
   D7의 "환각 대응 체크리스트", 모델 크기 선택표, 디코딩 옵션 비교와 D4의 `preprocess()` 파이프라인을 실무 중심으로 다시 써서 9,900원대 실전 가이드로 냅니다. "비유 → 소리 → 그림 → 수식" 서술 순서와 💬/🍎/👣 표기법을 전자책 레이아웃 규칙(WeasyPrint 템플릿)에 반영할 수 있습니다.

3. **템플릿·도구 상품: 자동 채점 워크시트 생성기**
   worksheet.html은 문항 JSON(`{ty: mc/ox/match/order/multi, p, o, a, w}`)만 바꾸면 되는 구조입니다. 이 방식을 본떠 "문항 JSON → 단일 HTML 워크시트(채점·해설·노션 복사·PDF 저장)" 생성기를 만들어 교강사용 템플릿으로 팔거나, Claude로 문항 JSON을 자동 생성하는 SaaS 기능으로 붙입니다(정답을 서버에서 채점하도록 바꾸면 차별점이 됩니다).

4. **SaaS·자동화: 한국어 녹취·자막 품질 파이프라인 API**
   D4 `preprocess()`(Silero VAD + noisereduce + RMS 정규화) → D7 안전장치 세트(no_speech·압축률·temperature fallback + VAD 선처리) → 환각 문장 블랙리스트 후처리를 하나로 묶어 "환각 없는 회의록/강의 자막" API로 만들고, NOMAD Shopping Shorts Factory나 ShortsOS의 자막 단계, 역사 유튜브 채널 대본 받아쓰기에 적용합니다.

5. **음성 에이전트 프로젝트 연결: D1 `voice_agent()` 구조로 MVP 만들기**
   STT(faster-whisper) → LLM(Claude Haiku, 음성용 SYSTEM_PROMPT) → TTS(edge-tts)와 단계별 지연 측정 막대그래프 구조를 진행 중인 음성 에이전트·JARVIS 프로젝트의 첫 MVP와 벤치마크 기준(RTF, CER, Latency)으로 씁니다. 과정 로드맵(Pipecat·LiveKit 스트리밍, MCP)은 이후 확장 계획을 세울 때 체크리스트로 활용할 수 있습니다.
