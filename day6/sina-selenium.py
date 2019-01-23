import time
from selenium import webdriver

#设置浏览器
chrome=webdriver.Chrome()
#页面最大化
chrome.maximize_window()
# chrome.get('https://weibo.com/login.php')
chrome.get('https://login.sina.com.cn/signup/signin.php?entry=sso')
p=input('请输入密码')
pwd=chrome.find_element_by_name('password').send_keys(p)
chrome.find_element_by_id('username').send_keys('17637938180')
chrome.find_element_by_xpath("//input[@value='登 录']").click()
#s设置超时
# chrome.set_page_load_timeout(10)
# chrome.set_script_timeout(5)

# chrome.execute_script('window.stop()')

#设置浏览器cookie
# cookiess=chrome.get_cookies()
# chrome.add_cookie(cookiess)
time.sleep(3)
#登陆后打开新页面
chrome.execute_script('window.open()')
#切换空白标签
chrome.switch_to_window(chrome.window_handles[1])
#打开新的网页
chrome.get('https://weibo.com/809083621?is_all=1')



def get_info(chrome):
    #下拉3次
    for i in range(3):
        chrome.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(5)


    infos=chrome.find_elements_by_xpath("//div[@class='WB_cardwrap WB_feed_type S_bg2 WB_feed_like ']")
    print(len(infos))
    for i in infos:
        title=i.find_element_by_xpath(".//div[@class='WB_feed_detail clearfix']/div[@class='WB_detail']/div[@class='WB_text W_f14']").text.strip()
        times=i.find_element_by_xpath(".//div[@class='WB_detail']/div[@class='WB_from S_txt2']/a[@class='S_txt2'][1]").text.strip()
        print(times,title)

    #下一页
    next_page=chrome.find_elements_by_link_text("下一页")
    print(len(next_page))
    if len(next_page)>0:
        next_page[0].click()
        time.sleep(3)
        get_info(chrome)

if __name__ == '__main__':
    get_info(chrome)
    chrome.close()
    chrome.quit()

