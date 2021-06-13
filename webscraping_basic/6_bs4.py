import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# print(soup.title)
# print(soup.title.get_text()) #get_text()
# print(soup.a) # soup 객체에서 처음 발견되는 a
# print(soup.a.attrs) # attrs : 속성 (딕셔너리 형태)
# print(soup.a["href"]) # a의 href 속성의 '값' 출력

# print(soup.find("a", attrs = {"class":"Nbtn_upload"})) # class = "Nbtn_upload"인 a element 를 찾아줘
# print(soup.find(attrs = {"class":"Nbtn_upload"})) # class = "Nbtn_upload" 인 어떤 element 를 찾아줘

# print(soup.find("li", attrs = {"class":"rank01"}))
rank1 = soup.find("li", attrs = {"class":"rank01"}) # li(class:rank01) 하위의 a element 를 찾아줘
# print(rank1.a.get_text())
# print(rank1.next_sibling)
# rank2 = rank1.next_sibling.next_sibling # next_sibling : 다음 sibling 찾기
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.a.get_text())
# rank2 = rank3.previous_sibling.previous_sibling # previous_sibling
# print(rank2.a.get_text())
# print(rank1.parent)

# rank2 = rank1.find_next_sibling("li") # find_next_sibling : 다음 li sibling 찾기
# print(rank2.a.get_text())
# rank3 = rank2.find_next_sibling("li")
# print(rank3.a.get_text())
# rank2 = rank3.find_previous_sibling("li") # find_previous_sibling
# print(rank2.a.get_text())

print(rank1.find_next_siblings("li")) # find_next_siblings : rank1의 모든 li sibling 찾기

webtoon = soup.find("a", text = "독립일기-99화 영양제")
print(webtoon)
