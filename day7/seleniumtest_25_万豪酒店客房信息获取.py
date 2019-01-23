"""
__title__ = ''
__author__ = 'Thompson'
__mtime__ = '2018/12/16'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""

import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

url = 'https://www.marriott.com/default.mi'
#url = 'https://www.marriott.com/reservation/rateListMenu.mi?defaultTab=standard'
browser = webdriver.Chrome() #browser = webdriver.Chrome() #
wait = WebDriverWait(browser,50)
browser.maximize_window()
browser.get(url)
#print(browser.page_source)
print(browser.current_url)
#print(browser.status_code)

time.sleep(5)
try:
    elemkeyword = wait.until(EC.presence_of_element_located((By.NAME,'destinationAddress.destination')))
    print(elemkeyword)
    elemkeyword.send_keys('上海世茂皇家艾美酒店, China, Shanghai, Huangpu, Nanjing Road, Nanjing East Road')
    btnSubmit = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.l-xs-col-4.l-xl-col-4.l-xl-last-col.l-hsearch-find.l-find-top.js-hform-fields > .analytics-click.js-is-roomkey-enabled.m-button.m-button-primary'))) #
    print(btnSubmit)
    btnSubmit.click()
    time.sleep(5)
    # 搜索结果页面
    print(browser.current_url)
    # 查找 继续按钮
    btnContinue = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#property-record-map-SHADW > div > .js-rate-btn-container > div > div > a')))
    print(btnContinue)
    # 点击，进入酒店客房详情页面
    btnContinue.click()
    print(browser.page_source)
    print(browser.current_url)
    time.sleep(5)
    #客房信息提取
    ls = browser.find_elements_by_xpath('.//div[@id="tab0"]/div[@class="l-room-list-container js-initial-room-list"]')
    print(len(ls))
    ls = browser.find_elements_by_xpath('.//div[@id="tab0"]/div[@class="l-room-list-container js-initial-room-list"]//div[@class="room-rate-results rate-type t-box-shadow"]')
    print(len(ls))
    for item in ls:
        print(item.get_attribute('innerHTML'))
        title = item.find_element_by_xpath('.//div[@class="l-l-col-8 l-xl-col-8"]//h3').text
        print('房间：',title)
        prices = item.find_elements_by_xpath('.//div[@class="not-cancellable l-row rph-row widget-container t-border-bottom-lightgrey l-padding-top l-padding-bottom l-pos-relative l-width-max l-rate-inner-container l-clear-both  "]')
        if len(prices)>0:
            price1 = prices[0].find_element_by_xpath('.//div[@class="without-widget-flow t-price l-display-flex "]/div/h2').text.strip()
            print('会员价：', price1)

        if len(prices)>1:
            price2 = prices[1].find_element_by_xpath('.//div[@class="without-widget-flow t-price l-display-flex "]/div/h2').text.strip()
            print('常规费率：', price2)


except Exception as e:
    print('error:',e)


time.sleep(8)
browser.close()