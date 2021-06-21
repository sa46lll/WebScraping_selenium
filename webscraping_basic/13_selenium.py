from selenium import webdriver
import time

# options = webdriver.ChromeOptions()
# options.add_experimental_option("excludeSwitches", ["enable-logging"])
# browser = webdriver.Chrome(options=options) # chromedriver 경로 지정 ("./chromedriver.exe")


browser = webdriver.Chrome("z:/nadoPython/chromedriver")

# 1. 네이버 이동
url = "http://naver.com"
browser.get(url)
time.sleep(3)

# 2. 로그인 버튼 클릭
elem = browser.find_element_by_class_name("link_login")
elem.click()

# 3. id, pw 입력
browser.find_element_by_id("id").send_keys("naver_id")
browser.find_element_by_id("pw").send_keys("password")

# 4. 로그인 버튼 클릭
browser.find_element_by_id("log.login").click()
time.sleep(3)

# 5. id 를 새로 입력
browser.find_element_by_id("id").clear()
browser.find_element_by_id("id").send_keys("my_id")
time.sleep(3)

# 6. html 정보 출력
print(browser.page_source)

# 7. 브라우저 종료
# browser.close() # 현재 탭만 종료
browser.quit() # 전체 브라우저 종료


# while(True):
#     pass

# # 로그인 버튼 클릭하기
# elem = browser.find_element_by_class_name("link_login")
# elem.click()
# browser.back()
# browser.forward()
# browser.refresh()

# # naver 검색하기
# from selenium.webdriver.common.keys import Keys # ENTER
# elem = browser.find_element_by_id("query")
# elem.send_keys("나도코딩")
# elem.send_keys(Keys.ENTER)

# # 모든 elem의 href 속성을 가져옴.
# elem = browser.find_elements_by_tag_name("a") #"a" element를 모두 가져옴
# for e in elem:            
#     e.get_attribute("href")

# # daum 검색하기 : xpath
# browser.get("http://daum.net")
# elem = browser.find_element_by_name("q")
# elem.send_keys("나도코딩")
# elem = browser.find_element_by_xpath("//*[@id='daumSearch']/fieldset/div/div/button[2]")
# elem.click()

# # 종료
# browser.close() # 탭 종료
# browser.quit() # 모든 브라우저 종료