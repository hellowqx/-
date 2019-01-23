# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random
import requests
import hashlib
import scrapy
import time
# from .settings import IPPOOL
from .settings import UAPOOL
from scrapy.contrib.downloadermiddleware.httpproxy import HttpProxyMiddleware
from scrapy.contrib.downloadermiddleware.useragent import UserAgentMiddleware


# class ProxyMiddleWare(object):
#     """docstring for ProxyMiddleWare"""
#     def process_request(self,request, spider):
#         '''对request对象加上proxy'''
#         proxy = self.get_random_proxy()
#         print("this is request ip:"+proxy)
#         request.meta['proxy'] = proxy
#
#
#     def process_response(self, request, response, spider):
#         '''对返回的response处理'''
#         # 如果返回的response状态不是200，重新生成当前request对象
#         if response.status != 200:
#             proxy = self.get_random_proxy()
#             print("this is response ip:"+proxy)
#             # 对当前reque加上代理
#             request.meta['proxy'] = proxy
#             return request
#         return response
#
#     def get_random_proxy(self):
#         '''随机从文件中读取proxy'''
#         while 1:
#             with open('E:\Project\Tools\proxies.txt', 'r') as f:
#                 proxies = f.readlines()
#             if proxies:
#                 break
#             else:
#                 time.sleep(1)
#         proxy = random.choice(proxies).strip()
#         return proxy

#
import pymysql

class ProxyIpPool:
    def __init__(self):
        #self.ua = UserAgent()
        host = 'localhost'
        port = 3306
        dbname = 'dbproxyip'
        user = 'root'
        pwd = 'root'
        self.driver = None
        try:
            self.conn = pymysql.connect(host=host,port=port,user=user,password=pwd,db=dbname,charset='utf8')
            self.cur = self.conn.cursor()
            self.id_list = []
            self.get_from_db()
        except Exception as e:
            print('init:',e)
            #self.close()
        # 使用谷歌浏览器
        # self.driver = webdriver.Chrome()

    def get_from_db(self):
        '''
        从数据库中读取已有的代理ip，并检验其有效性
        :return:
        '''
        strsql = "select * from proxyippool"
        self.cur.execute(strsql)
        results = self.cur.fetchall()
        for item in results:
            id = item[1]
            ip = item[2]
            port = item[3]
            proxy = ip + ":" + port
            if self.check_ip(proxy):
                self.id_list.append(id)
                item = dict()
                lists = list()
                item['ipaddr'] = ip + ':' + port
                lists.append(item)
            else:
                self.delRecord(id)
            time.sleep(2)

        return lists
    def check_ip(self,ip):
        '''
        检验ip是否有效
        :param ip:
        :return:
        '''
        #headers = {'User-Agent': self.ua.random}  # 定制请求头
        headers = {'User-Agent': 'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)'}
        proxies = {"http": "http://" + ip, "https": "http://" + ip}  # 代理ip
        try:
            print('check:', ip)
            url = "http://ip.27399.com/"
            url = "http://www.ip138.com/"
            code = requests.get(url=url, proxies=proxies, headers=headers, timeout=5).status_code
            if code == 200:
                return True
            else:
                return False
        except:
            return False

    def save(self,ip,port):
        '''
        代理ip存储到数据库
        :param ip:
        :param port:
        :return:
        '''
        print('begin save...')
        proxy = ip + ":" + port
        h = hashlib.md5()
        h.update(proxy.encode())
        id = h.hexdigest()
        if id not in self.id_list:
            try:
                strsql='insert into proxyippool VALUES(0,%s,%s,%s)'
                params = (id,ip,port)
                result = self.cur.execute(strsql,params)
                self.conn.commit()
                self.id_list.append(id)
                print('save:', proxy)
            except Exception as e:
                print('save:',e)
                self.close()

    def get_proxy(self):
        '''
        随机提取可用的代理ip
        :return:
        '''
        if len(self.id_list)<=0:
            return None
        id = random.choice(self.id_list)
        strsql='select * from proxyippool where id="'+id +'"'
        self.cur.execute(strsql)
        result = self.cur.fetchone()
        if result != None:
            ip = result[1]
            port = result[2]
            proxy = ip + ":"+port
            if self.check_ip(proxy):
                return proxy
            else:
                self.delRecord(id)
                self.get_proxy()
        else:
            self.get_proxy()

    def delRecord(self,id):
        '''
        删除指定的记录
        :param self:
        :param id:
        :return:
        '''
        strsql = 'delete from proxyippool where id="' + id + '"'
        self.cur.execute(strsql)
        self.conn.commit()
        print('del proxy:',id)

    # def close(self):
    #     try:
    #         if self.driver:
    #             self.driver.close()
    #         self.cur.close()
    #         self.conn.close()
    #     except Exception as e:
    #         print(e)


class IPPOOLS(HttpProxyMiddleware):

    def __init__(self, ip=''):
        self.ip = ip

    def process_request(self, request, spider):
        IPPOOL = ProxyIpPool()
        IPPOOLss = IPPOOL.get_from_db()
        thisip = random.choice(IPPOOLss)
        print('当前使用IP为:'+ thisip['ipaddr'])
        request.meta['proxy'] = 'http://' + thisip['ipaddr']


class Uamid(UserAgentMiddleware):
    def __init__(self, user_agent=''):
        self.user_agent = user_agent

    def process_request(self, request, spider):
        thisua = random.choice(UAPOOL)
        print('当前使用的User_Agent是:' + thisua)
        request.headers.setdefault('User-Agent', thisua)


class WeiboSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class WeiboDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
