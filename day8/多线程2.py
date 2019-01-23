# 设计多线程爬虫爬取糗事百科
# 1、用三个线程爬取10页页面内容，放入队列
# 2、用三个线程解析队列中的页面内容
# 3、把提取的内容存入json文件


import json
import threading
from queue import Queue

import requests
from lxml import etree
from fake_useragent import UserAgent
ua = UserAgent()


class thread_crawl(threading.Thread):
    '''
    抓取线程类
    '''
    def __init__(self, threadID):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.headers = {
            'User-Agent': ua.random}

    def run(self):
        print("Starting " + self.threadID)
        self.qiushi_spider()
        print("Exiting ", self.threadID)

    def qiushi_spider(self):
        while not page_queue.empty():
            page = page_queue.get()
            url = 'http://www.qiushibaike.com/8hr/page/' + str(page) + '/'
            print('spider:', self.threadID, ',page:', str(page))
            # 多次尝试失败结束、防止死循环
            timeout = 4
            while timeout > 0:
                timeout -= 1
                try:
                    content = requests.get(url, headers=self.headers, timeout=0.5)
                    data_queue.put(content.text)
                    break
                except Exception as e:
                    print('qiushi_spider', e)


class Thread_Parser(threading.Thread):
    '''
    页面解析类；
    '''


    def __init__(self, threadID, file):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.file = file


    def run(self):
        print('starting ', self.threadID)
        while not exitFlag_Parser:
            try:
                '''
                调用队列对象的 get()方法从队头删除并返回一个项目。可选参数为 block，
                默认为 True。
                如果队列为空且 block 为 True，get()就使调用线程暂停，直至有项目可用。
                如果队列为空且 block 为 False，队列将引发 Empty 异常。
                '''
                item = data_queue.get(False)
                if not item:
                    pass
                self.parse_data(item)
                data_queue.task_done()  # 提示线程 join()是否停止阻塞
            except:
                pass
            # print('Exiting ', self.threadID)

    def parse_data(self, item):
        '''
        解析网页函数
        :param item: 网页内容
        :return:
        '''


        try:
            html = etree.HTML(item)# //li[contains(@id,"qiushi_tag")]
            result = html.xpath('//li[contains(@id,"qiushi_tag")]')
            for site in result:
                try:
                    imgUrl = site.xpath('./a/img/@src')[0]
                    print('imgUrl:', imgUrl)
                    title = site.xpath('.//a[@class="recmd-content"]')[0].text.strip()
                    print('title:', title)
                    author = site.xpath('.//span[@class="recmd-name"]/text()')[0]
                    print('author:', author)
                    portrait = site.xpath('.//a[@class="recmd-user"]/img/@src')[0]
                    print('portrait:', portrait)
                    tmp = site.xpath('.//div[@class="recmd-num"]/span')
                    votenum = tmp[0].text
                    print("votenum:", votenum)
                    comments = 0
                    if len(tmp) >= 5:
                        comments = tmp[3].text
                    print('comments:', comments)

                    data = {
                        'author': author,
                        'imgUrl': imgUrl,
                        'title': title,
                        'vote': votenum,
                        'comments': comments,
                    }
                    if mutex.acquire():
                        data = json.dumps(data, ensure_ascii=False)
                        print('save....', data)
                        print("=" * 90)
                        self.file.write(data + "\n")
                        mutex.release()
                except Exception as e:
                    print('site in result', e)
        except Exception as e:
            print('parse_data', e)


def main():
    output = open('data/qiushibaike.json', 'a', encoding='utf-8')
    # 初始化网页页码 page 从 1-10 个页面
    for page in range(1, 11):
        page_queue.put(page)
        # 初始化采集线程
        crawlthreads = []
        crawlList = ["crawl-1", "crawl-2", "crawl-3"]
        print("开始打印第%s页" % page)
        print("*"*60)
        for threadID in crawlList:
            thread = thread_crawl(threadID)
            thread.start()
            crawlthreads.append(thread)
            # 初始化解析线程 parserList
            parserthreads = []
            parserList = ["parser-1", "parser-2", "parser-3"]
            # 分别启动 parserList
            for threadID in parserList:
                threadID = threadID
                thread = Thread_Parser(threadID, output)
                thread.start()
                parserthreads.append(thread)
                # 等待队列清空
                while not page_queue.empty():
                    pass
                # 等待所有线程完成
                for t in crawlthreads:
                    t.join()
                while not data_queue.empty():
                    pass
                # 通知线程是时候退出
                # global exitFlag_Parser
                # exitFlag_Parser = True
                # for t in parserthreads:
                #     t.join()
                #     print("退出主线程")
                #     if mutex.acquire():
                #         output.close()

if __name__ == '__main__':
    data_queue = Queue()
    page_queue = Queue(50)
    exitFlag_Parser = False
    mutex = threading.Lock()
    main()

