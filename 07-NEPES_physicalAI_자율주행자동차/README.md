# 07 · Physical AI 자율주행 — Jetson 위에서 인지·판단·행동을 잇는 5일 과정

> Jetson(Ubuntu) 실습 환경에서 Python·C++ 기초 → LLM·VLM → OpenCV·MediaPipe·ROS 2 → 좌표 기반 Pseudo-VLA → 학습된 VLA 정책·시뮬레이션까지, **하나의 작업대 사례**를 5일 동안 발전시키는 과정입니다.
> 문제은행은 [`develop/dist/07-physical-ai/`](../develop/dist/07-physical-ai)에 있습니다(허브의 '07 Physical AI · 자율주행').

## 📚 구성

| 일차 | 슬라이드 (`____/`) | 노트북 | 주제 |
|---|---|---|---|
| 1일차 | `1__.pdf` → **`1___v2.pdf`** | `02.Python/` · `03.C++/` | Physical AI 개념, Jetson·Ubuntu·Docker·원격 접속, Python·C++ 기초 |
| 2일차 | `2__.pdf` (LLM 학습 원리) · **`_____2___v2.pdf`** (LLM 활용 5h + VLM 3h) | `04.LLM/` · **`04.LLM_v2/`** · `05.VLM/` · **`05.VLM_v2/`** | v1: 훈련·RNN·LSTM·Seq2Seq·Transformer / v2: 프롬프트·Tool·RAG·에이전트, VLM |
| 3일차 | `3__.pdf` → **`_____3___v2.pdf`** | **`06.OpenCV_v2/`** · **`07.Mediapipe_v2/`** · **`08.ROS_v2/`** | 영상 배열·색·letterbox, 얼굴·손 특징점, ROS 2 노드·토픽·launch |
| 4일차 | `4__.pdf` → **`_____4___v2.pdf`** | **`09.Pseudo-VLA_v2/`** | 손 위치 추종, VLM FOLLOW/STOP JSON 계약, 지연, YOLO 검출·pose·segmentation |
| 5일차 | `5__.pdf` → **`_____5___v2.pdf`** | **`10.VLA_v2/`** | VLA 이론·행동 묶음·폐루프, LIBERO 시뮬레이션, 추론·rollout·평가, 자습(시연 데이터·학습·배포) |

- **굵게** 표시한 v2가 최신 개정판입니다. v1 폴더(`04.LLM` 등)와 `appendix/previous_4h`는 이전 판입니다.
- 2일차는 v1(학습 원리)과 v2(활용)의 내용이 달라 문제은행도 따로 만들었습니다.
- `04.LLM_v2/data/*.pdf`는 RAG 실습용 가상 문서입니다.

## 🎯 문제은행 (10개)

`01-jetson-ubuntu` · `02-python` · `03-cpp` · `04-llm-training` · `05-llm-apps` · `06-vlm` · `07-opencv-mediapipe` · `08-ros` · `09-pseudo-vla` · `10-vla`

- 슬라이드 PDF는 `develop/ingest.py`로 추출했습니다. 추출본은 `develop/sources/07-physical-ai/`에 있으며, 레포에는 올리지 않습니다. 노트북은 직접 읽었습니다.
- 자료 위치(📖)는 "N일차 슬라이드 · 섹션 (p.N)" 또는 "노트북 이름 · 섹션" 형식입니다.

## 🔒 정리 메모

- 문제은행에는 원 출처 회사명·고객사명·주소를 쓰지 않았습니다. 실습 경로(`/home/nvidia/…`)는 '작업폴더'로 일반화했습니다. `develop/validate.py`가 이를 검사합니다.
- **원본 파일은 수정하지 않았습니다.** 슬라이드마다 원 저작권자 표기가 있어 그대로 둡니다.
- `____/` 폴더와 PDF 파일 이름은 압축 해제 과정에서 한글이 깨진 것으로 보입니다. `@PaxHeader`는 압축 메타데이터 파일이라 무시해도 됩니다.
