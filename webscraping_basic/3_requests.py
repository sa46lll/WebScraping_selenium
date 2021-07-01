import requests
res = requests.get("http://google.com")
# res = requests.get("http://nadocoding.tistory.com")
res.raise_for_status() #웹 스크래핑을 위해서 코드를 올바르게 가져왔다. 문제가 있으면 종료.

# print("응답코드 :", res.status_code) # 200이면 정상

# if res.status_code == requests.codes.ok:
#     print("정상입니다.")
# else :
#     print("문제가 생겼습니다. [에러코드 ",res.status_code, "]")

print(len(res.text))
print(res.text)

with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)

# match() : 처음부터 일치하는지
# search() : 일치하는게 있는지
# findall() : 일치하는 것 모두 리스트로