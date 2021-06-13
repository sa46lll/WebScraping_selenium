import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
print(soup.title)
print(soup.title.get_text()) #get_text()
print(soup.a) # soup 객체에서 처음 발견되는 a
print(soup.a.attrs) # attrs : 속성 (딕셔너리 형태)
print(soup.a["href"]) # a의 href 속성의 '값' 출력

print(soup.find("a", attrs = {"class":"Nbtn_upload"})) # class = "Nbtn_upload"인 a element 를 찾아줘
# print(soup.find(attrs = {"class":"Nbtn_upload"})) # class = "Nbtn_upload" 인 어떤 element 를 찾아줘

# print(soup.find("li", attrs = {"class":"rank01"}))
rank1 = soup.find("li", attrs = {"class":"rank01"}) # li(class:rank01) 하위의 a element 를 찾아줘
print(rank1.a)

