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

# # 검색하기
# from selenium.webdriver.common.keys import Keys # ENTER
# elem = browser.find_element_by_id("query")
# elem.send_keys("나도코딩")
# elem.send_keys(Keys.ENTER)