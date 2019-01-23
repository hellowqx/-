import time
from selenium import webdriver


def get_info(chrome):
    global n
    n += 1
    infos = chrome.find_elements_by_xpath("//ul[@id='news-flow-content']/li")
    print(len(infos))
    for i in infos:
        title = i.find_element_by_css_selector('.bigsize a').text.strip()
        content = i.find_element_by_css_selector('.newsDigest p').text.strip()
        times = i.find_element_by_css_selector('.sourceDate').text.strip()
        print(times, title, content)

    # 下一页
    print(n,'===================================')
    next_page = chrome.find_elements_by_link_text(str(n))
    #todo  两个
    print(len(next_page))

    if len(next_page) > 0:
        next_page[0].click()
        time.sleep(2)
        print('=='*60)
        get_info(chrome)


if __name__ == '__main__':
    n = 1
    chrome = webdriver.Chrome()
    chrome.get('http://tech.163.com/')
    try:
        while True:
            height = chrome.execute_script('return document.body.scrollHeight')
            chrome.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(2)
            new_height = chrome.execute_script('return document.body.scrollHeight')
            if new_height == height:
                break
            height = new_height
    except:
        print('加载失败')

    # 加载全部
    chrome.find_element_by_class_name('load_more_tip').click()
    time.sleep(3)
    # 切换空白标签
    chrome.switch_to_window(chrome.window_handles[1])
    get_info(chrome)
