# -*- coding: utf-8 -*-
import scrapy
from scrapy.spider import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor

class SinaSpider(CrawlSpider):
    name = 'sina'
    allowed_domains = ['blog.sina.com.cn']
    start_urls = ['http://blog.sina.com.cn/s/blog_5af303e30102xdpt.html']



    rules = [
        Rule()
    ]

    def parse(self, response):
        pass
