# week09/tools.py 함수 설명

## 개요

`week09/tools.py`는 영화진흥위원회(KOBIS) 오픈 API로 일별 박스오피스 정보를 조회하는 모듈입니다.

- `requests` 라이브러리로 HTTP 요청을 보냅니다.
- API 키는 환경변수 `KOBIS_API_KEY`에서 읽어 `API_KEY`에 저장합니다.
- `BASE_URL`은 일별 박스오피스 조회 엔드포인트(`searchDailyBoxOfficeList.json`)입니다.

## 함수 목록

### `get_movie_audience(date, title)`

지정한 날짜의 박스오피스 순위에서 특정 영화의 일일 관객 수를 돌려줍니다.

- **받는 값**
  - `date` (문자열): 8자리 날짜. 예: `"20260824"`
  - `title` (문자열): 영화 제목. 응답의 `movieNm`과 정확히 같아야 합니다.
- **돌려주는 값** (항상 문자열)
  - 찾으면 천 단위 쉼표가 붙은 관객 수. 예: `"123,456명"`
  - 못 찾으면 안내 문장. 예: `"'파묘' 은(는) 20260824 순위에 없습니다."`
- **동작 순서**
  1. `API_KEY`가 없으면 `RuntimeError`를 일으킵니다.
  2. `key`, `targetDt`를 쿼리 파라미터로 `BASE_URL`에 GET 요청을 보냅니다 (타임아웃 10초).
  3. HTTP 오류면 `raise_for_status()`로 예외를 일으킵니다.
  4. 응답 JSON의 `boxOfficeResult.dailyBoxOfficeList`에서 영화 목록을 꺼냅니다.
  5. 목록을 돌며 `movieNm`이 `title`과 같은 영화의 `audiCnt`를 반환합니다.

## 참고

- 함수는 `get_movie_audience` 하나뿐입니다.
- 관객 수와 "순위에 없음" 안내가 모두 문자열이라, 호출하는 쪽에서 둘을 구분하기 어렵습니다.
- 날짜 형식 검증은 하지 않습니다.
