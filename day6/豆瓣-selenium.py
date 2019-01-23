import time
from selenium import webdriver

#设置浏览器
chrome=webdriver.Chrome()
#页面最大化
chrome.maximize_window()
chrome.get('https://www.douban.com/')
chrome.find_element_by_name('form_password').send_keys('1111')
chrome.find_element_by_id('form_email').send_keys('17637938180')

case=input('请输入验证码：')
chrome.find_element_by_id('captcha_field').send_keys(case)
time.sleep(2)
chrome.find_element_by_class_name('bn-submit').click()
time.sleep(5)
chrome.close()
chrome.quit()

