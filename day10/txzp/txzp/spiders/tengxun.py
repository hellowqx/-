# -*- coding: utf-8 -*-
import scrapy
import time,re,random
from items import TxzpItem


class TengxunSpider(scrapy.Spider):
    name = 'tengxun'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['http://hr.tencent.com/position.php?&start=0#a']

    def parse(self, response):
        item = TxzpItem()
        allinfo = response.xpath("//table[@class='tablelist']//tr")
        allinfo=allinfo[1:-1]
        print(len(allinfo))
        for i in allinfo:
            title = i.xpath(".//td[@class='l square']/a/text()").extract()[0]
            link = i.xpath(".//td[@class='l square']/a/@href").extract()[0]
            try:
                kind = i.xpath(".//td[2]/text()").extract()[0]
            except:
                kind='未分类'

            num = i.xpath(".//td[3]/text()").extract()[0]
            addr = i.xpath(".//td[4]/text()").extract()[0]
            times = i.xpath(".//td[5]/text()").extract()[0]

            item['title'] = title
            item['kind'] = kind
            item['num'] = num
            item['addr'] = addr
            item['times'] = times
            # print(item)
            time.sleep(0)
            yield response.follow(link, self.get_info, meta={'item': item})
    #     # 下一页
        print('==' * 60)
        base_url = 'https://hr.tencent.com/'
        next_page = response.xpath("//div[@class='right']/div[@class='pagenav']/a[@id='next']/@href").extract()
        if len(next_page) > 0:
            next_url = base_url + next_page[0]
            print(next_url,'----------------'*5)
            time.sleep(random.random() * 5)
            yield response.follow(next_url, self.parse)
        else:
            print('下载完毕')

    def get_info(self, response):
        item = response.meta['item']
        intro = response.xpath("//ul[contains(@class,'squareli')]/li")
        intro = intro.xpath('string(.)').extract()
        intro=''.join(intro)
        item['intro'] = intro
        print(item)
        yield item

if __name__ == '__main__':
    from scrapy import cmdline
    cmd='scrapy crawl tengxun'
    cmdline.execute(cmd.split())