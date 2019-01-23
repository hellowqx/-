from fake_useragent import UserAgent
import requests, chardet, csv
from lxml import etree, html
import threading, time


def get_html(url):
    global count
    while count <= int(10):
        print(threading.current_thread().getName(), '爬取了一个页面', count)
        count += 1
        time.sleep(2)
        headers = {'User-Agent': ua.random}
        response = requests.get(url, headers=headers)
        response.encoding = 'utf-8'
        htmls = response.text
        # 返回换成符合 HTML 规则的结构化数据对象
        docs = etree.HTML(htmls)
        # docs=etree.HTML(htmls)
        page_list.append(docs)
        print(page_list)

    else:
        print(threading.current_thread().getName(), '没有页面了')


def save_img():
    pass

def get_info(docs):
    global num
    while num <=len(page_list) :
        allinfo = docs.xpath("//div[@class='recommend-article']/ul/li")
        for i in allinfo:
            a = i.xpath(".//div[@class='recmd-right']/a/text()")
            if len(a) == 0:
                continue
            title = i.xpath(".//div[@class='recmd-right']/a/text()")[0]
            link = i.xpath(".//div[@class='recmd-right']/a[@class='recmd-content']/@href")[0]
            url = base_url + link
            save_img()
            # 判断评论为空
            pinglun = i.xpath(".//div[@class='recmd-num']/span[4]/text()")
            pinglun = pinglun[0] if len(pinglun) > 0 else None
            zan = i.xpath(".//div[@class='recmd-num']/span[1]/text()")[0]
            # 判断赞为空
            zan = zan[0] if len(zan) > 0 else None
            author = i.xpath(".//a[@class='recmd-user']/span/text()")[0]
            # with open('data/糗事.csv', 'a+', encoding='utf-8')as f_w:
            #     writer = csv.writer(f_w)
            #     writer.writerow(['作者:', author, '标题:', title, '点赞：', zan, '评论', pinglun, '标题连接:', url])
        print(threading.current_thread().getName(), '解析了一个页面', num)
        num+=1
        time.sleep(2)
    else:
        print(threading.current_thread().getName(), '没有任务了')

if __name__ == '__main__':
    ua = UserAgent()
    count = 1
    n=input('请输入爬取的页面数:')
    page_list = list()
    base_url = 'https://www.qiushibaike.com'
    url = 'https://www.qiushibaike.com/8hr/page/' + str(count)
    t1 = threading.Thread(name='爬虫1', target=get_html,args=(url,n))
    t2 = threading.Thread(name='爬虫2', target=get_html,args=(url,n))
    t3 = threading.Thread(name='爬虫3', target=get_html,args=(url,n))
    print(page_list)
    num = 1
    docs=page_list[num]
    t4 = threading.Thread(name='爬虫4', target=get_info,args=(docs,))
    t5 = threading.Thread(name='爬虫5', target=get_info,args=(docs,))
    t6 = threading.Thread(name='爬虫6', target=get_info,args=(docs,))
    t1.start()
    t1.join()
    t2.start()
    t2.join()
    t3.start()
    t3.join()
    t4.start()
    t4.join()
    t5.start()
    t5.join()
    t6.start()
    t6.join()


    # docs=get_html('https://www.qiushibaike.com/8hr/page/1/')

    #
