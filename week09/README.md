# week09

## 무엇을 하는 코드인가

영화진흥위원회(KOBIS) 일별 박스오피스 API로 특정 날짜·영화의 **일일 관객 수**를 조회합니다.
`tools.py`의 `get_movie_audience(date, title)`가 조회를 하고, `main.py`는 2026년 8월 24일 기준으로 영화 세 편을 조회해 출력합니다.

## 무엇을 설치해야 하는가

- Python
- `requests` 등 `requirements.txt`에 적힌 패키지
- KOBIS 오픈 API 키 (https://www.kobis.or.kr/kobisopenapi 에서 발급)

```powershell
pip install -r requirements.txt
```

## 어떻게 실행하는가

`main.py`가 `import tools`를 하므로 `week09` 폴더 안에서 실행합니다.

```powershell
cd week09
$env:KOBIS_API_KEY = "발급받은_키"
python main.py
```
