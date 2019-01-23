import time
from selenium import webdriver


def get_info(chrome):

    infos = chrome.find_elements_by_xpath("//div[contains(@class,'l-row t-bg-white property-record-item l-display-inline-m')]")
    print(len(infos))

    for i in infos:
        name = i.find_element_by_class_name('l-property-name').text
        addr = i.find_element_by_xpath(
            ".//div[@class='l-s-col-4 l-m-col-8 l-l-col-12 l-m-col-last l-s-col-last t-font-s t-line-height-m m-hotel-address t-color-extradarkgrey']").text
        print(name, addr)
        print('=='*60)
        #酒店详情连接
        link=i.find_elements_by_xpath(".//div[contains(@class,'js-button-text-wrapper l-float-right')]/a[1]")
        if len(link) ==1:
            link=link[0].get_attribute('href')
        else:
            continue
        print(link,111111111111111111111111)
        chrome.execute_script('window.open()')
        chrome.switch_to_window(chrome.window_handles[1])
        chrome.get(link)
        time.sleep(2)
        #内部页面的房间数
        rooms=chrome.find_elements_by_xpath("//div[contains(@class,'room-rate-results rate-type t-box-shadow')]")
        print(len(rooms),'房间数')
        for j in rooms:
            intro=j.find_element_by_xpath(".//div[@class='l-l-col-8 l-xl-col-8']/h3").text.strip()
            prices=j.find_elements_by_xpath(".//div[contains(@class,'without-widget-flow t-price l-display-flex')]//h2")
            print(len(prices))
            if len(prices) > 1:
                huiyuan=prices[0].text.strip()
                yuanjia=prices[1].text.strip()
            else:
                huiyuan='无'
                yuanjia=prices[0]
            print(intro,huiyuan,yuanjia)
        chrome.close()
        chrome.switch_to_window(chrome.window_handles[0])




if __name__ == '__main__':
    options=webdriver.ChromeOptions()
    options.add_argument('--headless')
    chrome = webdriver.Chrome()
    chrome.get('https://www.marriott.com/default.mi')
    chrome.implicitly_wait(10)
    input=chrome.find_element_by_xpath("//div[@class='l-display-flex']//input").send_keys('上海世茂皇家艾美酒店')
    chrome.find_element_by_xpath("//div[@class='l-xs-col-4 l-xl-col-4 l-xl-last-col l-hsearch-find l-find-top js-hform-fields']/button[@class='analytics-click js-is-roomkey-enabled m-button m-button-primary']").click()
    time.sleep(5)
    get_info(chrome)


