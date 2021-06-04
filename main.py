from selenium import webdriver
from huadong import scroll
import time
from downloadpic import savepic
browser = webdriver.Edge('E:\python\msedgedriver.exe') # 创建一个浏览器对象,这里还可以使用chrome等浏览器
browser.maximize_window()
try:
    for page in range(1,2):
        print("----打开{}网页----".format(page))
        browser.get('https://www.huashi6.com/hot_%s'%page)
        time.sleep(5)
        scroll(browser)
        list1=[]
        imgbq=browser.find_elements_by_xpath('//div[@class="c-work-img"]/img')
        for bq in imgbq:
            imgurl=bq.get_attribute('src')
            list1=imgurl.split('?')
            url=str(list1[0])
            name=url.split('/')[-1]
            savepic(url,name)
    print("第{}页下载成功！".format(page))
finally:
    browser.close()


