#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 라이브러리 선언
import bs4,time # 메일 전송 라이브러리, 문자를 안보이게하는 라이브러리
import pandas as pd
from selenium import webdriver
from email.message import EmailMessage
from selenium.webdriver.common.action_chains import ActionChains
# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',}
# data=requests.get(url,headers=headers)

# 크롬드라이버 위치 및 드라이버 생성
driver_loc = "C:/Users/Lenovo/pywork/chromedriver/chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_argument("window-size = 1920x1080")

driver = webdriver.Chrome(driver_loc, options=options)

# 접속할 사이트
url = "http://www.homeplus.co.kr/app.exhibition.main.Main.ghs?paper_no=category"

# driver를 이용해 사이트 접속
driver.get(url)
time.sleep(2)
# print(driver.get_cookies())

# Xpath
mainMenu = '//*[@id="ui-menu-catgnb"]' # 카테고리 창
subMenu = '//*[@id="ui-catlist-tab1"]/ul[1]/li[5]/a' # 정육코너

main = driver.find_element_by_xpath(mainMenu)
sub = driver.find_element_by_xpath(subMenu)
popularList = '//*[@id="bestHotProduct"]'
# 메인 카테고리 창 이동 후 클릭
ActionChains(driver).move_to_element(main).click(sub).perform()
time.sleep(1)
driver.find_element_by_xpath(popularList).click()

time.sleep(3)      # 페이지가 로딩될 때까지 3초기다림 -> 이 부분을 안해주었더니 계속 소스가 짤려서 들어옴

# 페이지 소스를 저장
data = driver.page_source


# 텍스트화된 데이터를 html형태로 추출
bs = bs4.BeautifulSoup(data,'html.parser')
divTags = bs.findAll(name = 'div',
          attrs = {"class":"exh-comtxt w-ty4"})
rows=[]
i = 0
for i in range(0, len(divTags)):
    price = divTags[i].find(name = 'span',
                   attrs = {'class':'unit'}).text.replace("\t","")
    title = divTags[i].find(name = 'a',
                   attrs = {'class':'name'}).text
    rows.append([price,title])
    
result = pd.DataFrame(data = rows, columns=['가격','상품명'])
from datetime import datetime
time = datetime.today().strftime("%Y%m%d")
file = './'+ time +".csv"
result.to_csv(file, encoding = 'ms949', index = False)
driver.close()

