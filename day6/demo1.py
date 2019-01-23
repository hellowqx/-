from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument('--headless')
#创建无界面浏览器
chrome = webdriver.Chrome()

chrome.get('http:\\www.baidu.com')
input_box=chrome.find_element_by_id('kw')
input_box.send_keys('wqx')

btn=chrome.find_element_by_id('su')
btn.click()
print()
time.sleep(2)
chrome.execute_script('window.scrollTo(0,document.body.scrollHeight)')
print(chrome.get_cookies())
time.sleep(2)

chrome.save_screenshot('222.png')
chrome.close()
chrome.quit()
