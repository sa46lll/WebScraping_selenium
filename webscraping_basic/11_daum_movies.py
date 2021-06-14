import requests
from bs4 import BeautifulSoup

# 2015-2020 상위 영화 5개 이미지 저장
for year in range(2015, 2021):
    url = "https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(year)

    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    images = soup.find_all("img", attrs={"class" : "thumb_img"})

    for idx, image in enumerate(images): # enumerate : index를 줌
        image_url = image["src"]
        if image_url.startswith("//"): # //로 시작한다면
            image_url = "https:" + image_url
        print(image_url)

        image_res = requests.get(image_url)
        image_res.raise_for_status()

        with open("movie_{}_{}.jpg".format(year, idx+1), "wb") as f:
            f.write(image_res.content)

        # 싱위 5개 이미지까지만 다운로드
        if idx >= 4:
            break