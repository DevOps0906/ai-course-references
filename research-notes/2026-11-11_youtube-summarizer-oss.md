# 유튜브 링크 → 요약·정리·캡처 오픈소스 조사

작성 2026-11-11. 목적: 유튜브 링크를 넣으면 문서 요약, 내용 정리, 영상 캡처가 되는 오픈소스와 유사 서비스 확인.

> **확인 범위**: 각 저장소·패키지 페이지의 설명을 읽고 정리했습니다. 코드를 내려받아 실행하거나 품질·유지보수 상태를 확인하지는 않았습니다. 별 개수·최근 커밋 같은 활성도는 확인하지 않았습니다.
> 사용자가 찾던 "readray"는 검색에서 확인하지 못했습니다. 비슷한 유형의 서비스는 Lilys AI, SecondB 등입니다.

## 1. 후보 비교

| 후보 | 요약 | 정리 | 스크린샷 | 형태 | 라이선스 |
|---|---|---|---|---|---|
| [bhopy/YT2](https://github.com/bhopy/YT2) | O (구간별) | 부분적 | 장면 전환별 키프레임 | 링크 입력 → 단일 HTML 페이지 | MIT |
| [digestvid](https://pypi.org/project/digestvid/0.2.1) | O (OpenAI) | 전사본·요약 저장 | 영상 중간 지점 1장 | CLI (`pip install`) | MIT |
| [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | Claude가 분석 | Claude 활용 | 영상 길이에 맞춘 프레임 추출 | Claude Code 플러그인/스킬 | MIT |
| [SecondB.ai](https://news.hada.io/topic?id=26041) | O | 요약 목록 저장 | 언급 없음 | 웹서비스 + 크롬 확장 (오픈소스 아님) | - |

## 2. 가장 가까운 후보: YT2

- 흐름: yt-dlp 다운로드 → Whisper 전사 → PySceneDetect 장면 전환 감지 → FFmpeg 프레임 추출 → Ollama(기본 mistral) 구간 요약 → 단일 HTML 출력
- 요구 사항: Python 3.10+, yt-dlp, FFmpeg, Ollama. 설치 안내가 Windows 배치 파일(`setup.bat`, `run.bat`) 기준
- 한계: 요약 모델이 로컬 Ollama라 한국어 품질이 약할 수 있음. 요약 단계를 Claude API로 바꾸는 것이 현실적
- 별도로 세로형 쇼츠 클립 제작(단어 단위 자막)과 GUI 기능이 있다고 소개됨

## 3. 나머지 후보 메모

- **digestvid**: Whisper 전사 + OpenAI 요약. 스크린샷은 영상 중간 지점 1장이라 "장면별 캡처"에는 부족. OpenAI API 키·비용 별도
- **claude-video**: Claude가 영상을 직접 볼 수 없는 한계를 보완. 자막이 있으면 우선 사용하고 없으면 Whisper API(Groq 또는 OpenAI)로 전사. 비공개(인증 필요) 영상은 지원하지 않고, Whisper는 파일당 약 50분 제한, 10분 넘는 영상은 구간 지정을 권장. 서비스용이 아니라 Claude Code 작업용에 적합
- **Agent-Reach**: 유튜브 등을 읽도록 에이전트에 연결하는 도구. 요약·정리·캡처 기능은 확인되지 않음 (`2026-11-11_tiktok-ai-video-analysis.md` 참고)

## 4. 서비스로 만들 때 주의할 점

1. **YouTube 다운로드 차단 위험**: 한 개발자가 yt-dlp 차단으로 유튜브 요약 서비스를 중단했다고 밝힌 사례가 있다([GeekNews](https://news.hada.io/topic?id=21519)). 서버에서 영상을 내려받는 방식은 안정적인 서비스에 위험 요소다.
2. **약관·저작권**: 영상을 내려받아 상업 서비스로 제공하는 것은 YouTube 약관과 저작권 이슈가 따를 수 있어 서비스 전에 확인이 필요하다.
3. **대안 구조**: 크롬 확장으로 사용자 브라우저에서 자막을 가져오거나, 자막 기반 요약만 서버에서 처리하고 스크린샷은 사용자가 올린 영상 파일로 처리하는 방식이 위험이 낮다.

## 5. 검증 순서

1. YT2를 로컬에 설치해 영상 3~5개(한국어 포함)를 돌려 결과 품질을 확인한다.
2. 요약 단계를 Claude API로 바꿔 한국어 품질을 비교한다.
3. 품질이 괜찮으면 자료 분석 서비스(KNOWFLOW AI)의 "유튜브 입력" 모듈로 붙일지 정한다.

## 출처

- https://github.com/bhopy/YT2
- https://pypi.org/project/digestvid/0.2.1
- https://github.com/bradautomates/claude-video
- https://news.hada.io/topic?id=26041 (SecondB.ai 소개)
- https://news.hada.io/topic?id=21519 (유튜브 RSS 서비스 중단 사례)
