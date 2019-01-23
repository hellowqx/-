# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from SunSpider.items import SunspiderItem

class Sun2Spider(CrawlSpider):
    name = 'Sun2'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4']

    # 翻页的链接提取器
    pagelink = LinkExtractor(restrict_xpaths=('//div[@class="pagination"]/a[text()=">"]'))
    # 帖子内容的链接提取器
    contentlink = LinkExtractor(restrict_xpaths=('//a[@class="news14"]'))

    rules = [
        Rule(pagelink,process_links="deal_link",follow=True),
        Rule(contentlink,callback='parse_item')
    ]

    # def parse_start_url(self, response):
    #     print("parse_start_url....")
    #     return CrawlSpider.parse_start_url(self,response)

    def deal_link(self,links):
        for link in links:
            print('link:',link.url)
        return links


    def parse_item(self, response):
        '''
        处理请求到的详情页面
        :param response:
        :return:
        '''
        title  = response.xpath('//div[@class="wzy1"]/table[1]/tr/td[2]/span[1]/text()').extract()[0]
        print('title:',title)
        number = response.xpath('//div[@class="wzy1"]/table[1]/tr/td[2]/span[2]/text()').extract()[0]
        print('number:',number)
