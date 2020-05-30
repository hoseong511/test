#!/usr/bin/env python
# coding: utf-8

# In[2]:


import bs4,requests
import pandas as pd
from selenium import webdriver


driver_loc = "C:/Users/Lenovo/pywork/chromedriver/chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_argument("window-size = 1920x1080")
driver = webdriver.Chrome(driver_loc, options=options)


driver.get("https://sparkkorea.com/")
import time
time.sleep(3)
quizMenuXpath = '//*[@id="menu-item-382"]/a'

driver.find_element_by_xpath(quizMenuXpath).click()
curentUrl = driver.current_url
data = driver.page_source


bs = bs4.BeautifulSoup(data,'html.parser')
divTag = bs.find(name = "div",
                 attrs = {"class" : "class_spark_quiz"})

aTags = divTag.findAll(name = "a")
aTagsLen = len(aTags)
row = []
for i in range(0, aTagsLen):
    eachLink = aTags[i].attrs["href"]
    eachText = aTags[i].text
    row.append([eachLink, eachText])
result = pd.DataFrame(data = row, columns=["링크","타이틀"])
result.to_csv("./test.csv",encoding = 'ms949',index = False)


# In[ ]:




