# -*- coding: utf-8 -*-
import scrapy


class BilibiliSpider(scrapy.Spider):
    name = 'Bilibili'
    allowed_domains = ['bilibili.com']
    start_urls = ['https://www.bilibili.com/ranking#!/all/0/0/7/',]

    def parse(self, response):
        item=dict()
        allinfo=response.xpath("//li[@class='rank-item']")
        print(type(allinfo))
        print(len(allinfo))
        for i in allinfo:
            title=i.xpath(".//div[@class='content']/div[@class='info']/a[@class='title']/text()").extract()[0]
            link=i.xpath(".//div[@class='content']/div[@class='info']/a[@class='title']/@href").extract()[0]
            num=i.xpath(".//div[@class='num']/text()").extract()[0]
            score=i.xpath("./div[@class='content']/div[@class='info']/div[@class='pts']/div/text()").extract()[0]
            author=i.xpath("./div[@class='content']/div[@class='info']/div[@class='detail']/a/span[@class='data-box']/text()").extract()[0]
            item['title']=title
            item['num']=num
            item['link']=link
            item['score']=score
            item['author']=author
            print(item)
            yield item

