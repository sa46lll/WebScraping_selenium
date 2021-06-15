import csv
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

# csv 파일 저장
filename = "시가총액1-200.csv"
f = open(filename, "w", encoding="utf8", newline="") # 한글이 깨질때 encoding="utf-8-sig"
writer = csv.writer(f)

# column 이름
title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split("/t")
writer.writerow(title)

for page in range(1, 5):
    res = requests.get(url + str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    data_rows = soup.find("table", attrs={"class":"type_2"}). find("tbody"). find_all("tr")
    for row in data_rows:
        columns = row.find_all("td")
        if len(columns) <= 1: # 의미없는 데이터는 skip
            continue
        data = [column.get_text().strip() for column in columns] # strip : 공백 삭제
        print(data)
        writer.writerow(data)

