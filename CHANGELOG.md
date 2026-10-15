# CHANGELOG

## 2026-10-15 05-langchain-agent 추가
- 업로드한 `교육과정.zip`(LangChain·RAG·Agent 14일 과정)을 `05-langchain-agent/day01~day14`로 배치
- 3일차 중복 노트북 1개 제외, 5일차 확장자 `.배포ipynb` → `.ipynb` 수정
- 13일차 노트북 출력의 OpenAI API 키 → `<YOUR_API_KEY>` (정리 규칙에 API 키 패턴 추가)
- Whisper 실습용 mp3 40개는 `day13/문화가 있는 한국어 읽기_mp3/`에 배치
- `tools/sync.py`: 원본 저장소 없는 수동 업로드 자료는 건너뛰도록 변경

## 2026-10-15 최초 구성
- 자료 8종(98개 파일)을 주제별 4개 폴더로 재배치
- 정리 규칙 적용: 44개 파일, 508건 치환 (원 출처 표기·연락처·링크·토큰·문서 ID·문서 속성)
- 폴더별 정리 문서(`README.md`) 8개 추가
- 원본 동기화 도구(`tools/`) 추가 — 기준 커밋은 `tools/sources.json`
- 참고: `01-ai-work/claude-for-educators/판서.pptx`의 별도 스택 실습 저장소 링크는 이 폴더의 `stack_visualizer.html`로 연결
