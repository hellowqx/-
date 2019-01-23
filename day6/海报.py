from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC







def login(chrome):
    # chrome.find_element_by_link_text('我有海报账号').click()
    time.sleep(1)
    # chrome.find_element_by_name('username').send_keys('17637938180')
    a=chrome.find_elements_by_xpath("//input[@class='placeIpt ico_ipt']")
    print(a)
    a[0].send_keys('17637938180')
    print(len(a))
    b=chrome.find_elements_by_name('password')
    print(len(b))
    b[0].send_keys('222888')
    # chrome.find_element_by_class_name('login_btn red_btn js_hb_login').click()
    time.sleep(5)

    return chrome



# try:
#     element=WebDriverWait(chrome,10).until(
#         EC.presence_of_element_located((By.LINK_TEXT,'浏览更多美图 '))
#     )
#
# except:
#     print('加载异常')





if __name__ == '__main__':
    chrome = webdriver.Chrome()
    chrome.get("http://user.haibao.com/login.html")
    chrome.implicitly_wait(5)
    chrome=login(chrome)
    chrome.get('http://pic.haibao.com/hotimage/')
    imgs = chrome.find_elements_by_xpath("//div[contains(@class,'pageli jsImageContainer jsImageInfo')]")
    print(len(imgs))
    # for i in imgs:
    #     img = i.find_element_by_xpath(
    #         ".//div[@class='pagelibox']/table/tbody/tr/td/a/img[@class='lazys jsInit']").get_attribute('src')
    #     print(img)