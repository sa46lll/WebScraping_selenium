# User-Agent 방식 (크롬/익스플로러 에서 보는 것과 같은 내용을 불러옴)

import requests
url = "http://nadocoding.tistory.com"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"}
res = requests.get(url, headers)
res.raise_for_status()

with open("nadocoding.html", "w", encoding="utf8") as f:
    f.write(res.text)


# User-Agent 아닌 방식

# import requests
# url = "http://nadocoding.tistory.com"
# res = requests.get(url)
# # res.raise_for_status() #웹 스크래핑을 위해서 코드를 올바르게 가져왔다. 문제가 있으면 종료.

# with open("nadocoding.html", "w", encoding="utf8") as f:
#     f.write(res.text)