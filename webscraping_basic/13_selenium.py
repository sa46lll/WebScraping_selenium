from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(options=options) # chromedriver 경로 지정 ("./chromedriver.exe")

url = "http://naver.com"
browser.get(url)
while(True):
    pass 

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