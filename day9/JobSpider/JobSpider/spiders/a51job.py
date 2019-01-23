# -*- coding: utf-8 -*-
import scrapy


class A51jobSpider(scrapy.Spider):
    name = '51job'
    allowed_domains = ['51job.com']
    start_urls = ['http://51job.com/']

    def parse(self, response):
        print(dir(response))
        item=dict()
        item['name']='name'
        item['name']='city'
        yield item
