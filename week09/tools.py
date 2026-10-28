import os
import requests

API_KEY = os.getenv("KOBIS_API_KEY")
BASE_URL = "https://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"


def get_movie_audience(date, title):
    """해당 날짜 박스오피스 순위에서 영화 관객 수를 반환합니다."""
    if not API_KEY:
        raise RuntimeError("KOBIS_API_KEY 환경변수를 설정하세요.")
    params = {"key": API_KEY, "targetDt": date}
    response = requests.get(BASE_URL, params=params, timeout=10)
    response.raise_for_status()
    movies = response.json()["boxOfficeResult"]["dailyBoxOfficeList"]

    for movie in movies:
        if movie["movieNm"] == title:
            return f"{int(movie['audiCnt']):,}명"
    return f"'{title}' 은(는) {date} 순위에 없습니다."
