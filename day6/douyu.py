import time
from selenium import webdriver


options=webdriver.ChromeOptions()
options.add_argument('--headless')
chrome = webdriver.Chrome(options=options)
chrome.get('https://www.douyu.com/directory/all')

def get_info(chrome):
    room_info=chrome.find_elements_by_xpath("//li/a[@class='play-list-link']/div[@class='mes']")
    print(len(room_info))
    for i in room_info:
        name=i.find_element_by_xpath(".//div[@class='mes-tit']/h3[@class='ellipsis']").text.strip()
        num=i.find_element_by_xpath(".//p/span[@class='dy-num fr']").text.strip()
        print(name,num)


    #下一页
    next_page=chrome.find_elements_by_class_name("shark-pager-next")
    if len(next_page)>0:
        next_page[0].click()
        time.sleep(3)
        print('=='*60)
        print('开始爬取下一页')
        get_info(chrome)

if __name__ == '__main__':
    chrome = webdriver.Chrome(options=options)
    chrome.get('https://www.douyu.com/directory/all')
    get_info(chrome)
    chrome.close()
    chrome.quit()
