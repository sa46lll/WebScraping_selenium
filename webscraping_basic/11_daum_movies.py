import requests
from bs4 import BeautifulSoup

url = "https://search.daum.net/search?w=tot&q=2020}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"}

res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

images = soup.find_all("img", attrs={"class" : "thumb_img"})

for image in images:
    image_url = image["src"]
    if image_url.startswith("//"): # //로 시작한다면
        image_url = "https:" + image_url
    print(image_url)
