import time,random
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--headless')
chrome=webdriver.Chrome(options=options)
chrome.get('https://www.jd.com/')
chrome.find_element_by_id('key').send_keys('手机')
chrome.find_element_by_class_name('button').click()

def get_infos(chrome):
    #下拉3次
    for i in range(3):
        chrome.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(3)
    #获取手机信息
    goods_info=chrome.find_elements_by_class_name('gl-item')
    print(len(goods_info))
    for i in goods_info:
        title=i.find_element_by_xpath(".//div[@class='p-name p-name-type-2']/a/em").text.strip()
        price=i.find_element_by_css_selector('.p-price').text.strip()
        print('title:',title)
        print('price:',price)

    #获取下一页
    next_page=chrome.find_elements_by_class_name('pn-next')
    if len(next_page) >0:
        next_page[0].click()
        print('开始采集下一页')
        get_infos(chrome)



if __name__ == '__main__':
    get_infos(chrome)
    chrome.close()
    chrome.quit()



