작성: Claude Code / 확인: 석정욱

# week09/tools.py 함수 정리

## 개요
- 영화진흥위원회(KOBIS) 오픈 API 로 일별 박스오피스를 조회하는 모듈임
- 함수는 `get_movie_audience` 하나만 있음

## 모듈 상수
- `API_KEY`: 환경변수 `KOBIS_API_KEY` 에서 읽어 옴
- `BASE_URL`: KOBIS 일별 박스오피스 조회 API 주소(`searchDailyBoxOfficeList.json`)임

## get_movie_audience(date, title)
- 역할: 지정 날짜의 박스오피스 순위에서 특정 영화의 관객 수를 돌려줌
- 인자
  - `date`: 조회 날짜 문자열(`YYYYMMDD` 형식, 예: `"20261109"`)임
  - `title`: 찾을 영화 제목임. `movieNm` 과 완전히 같아야 찾음
- 동작 순서
  - `API_KEY` 가 없으면 `RuntimeError` 를 냄
  - `key`, `targetDt` 를 넣어 API 를 GET 호출함(타임아웃 10초)
  - HTTP 오류면 `raise_for_status()` 로 예외를 냄
  - 응답의 `boxOfficeResult.dailyBoxOfficeList` 를 돌면서 제목을 비교함
- 반환값
  - 찾으면 해당 날짜 하루 관객 수(`audiCnt`)를 `"123,456명"` 형식으로 돌려줌
  - 못 찾으면 `"'제목' 은(는) 날짜 순위에 없습니다."` 문자열을 돌려줌
- 참고
  - `audiCnt` 는 누적이 아닌 당일 관객 수임(누적은 `audiAcc`)
  - 일별 순위는 상위 10편만 오므로 순위 밖 영화는 찾지 못함

## 확인할 것
- 제목 비교가 완전 일치라 띄어쓰기·부제가 다르면 못 찾는 점 괜찮은지
- 당일 관객 수(`audiCnt`)를 반환하는 것이 의도와 맞는지(누적 `audiAcc` 필요 여부)
