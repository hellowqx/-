import time

from selenium import webdriver

chrome=webdriver.Chrome()
chrome.get('https://weibo.com/login.php')
print(chrome.page_source)
chrome.find_element_by_id('loginname').send_keys('17637938180')
chrome.find_element_by_name('password').send_keys('2288')