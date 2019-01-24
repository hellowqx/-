# -*- coding: utf-8 -*-
import scrapy,time,random
from scrapy_redis.spiders import RedisSpider
from YGRX.items import YgrxItem


class YgSpiderSpider(RedisSpider):
    name = 'Yg_spider'
    # allowed_domains = ['sun0769.com']
    # start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4']
    redis_key='Yg_spider:start_urls'

    def __init__(self, *args, **kwargs):
        # Dynamically define the allowed domains list.
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(YgSpiderSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        item=YgrxItem()
        allinfo=response.xpath("//div[@class='greyframe']//table[2]//tr/td/table//tr")
        print(len(allinfo))
        for i in allinfo:
            num=i.xpath("./td[1]/text()").extract()[0]
            title=i.xpath('.//td[2]/a[2]/text()').extract()[0]
            status=i.xpath(".//td[@class='t12h'][1]/span/text()").extract()[0]
            name=i.xpath(".//td[@class='t12h'][2]/text()").extract()[0]
            times=i.xpath(".//td[@class='t12wh']/text()").extract()[0]
            # print(title,status,name,time)
            item['num']=num
            item['title']=title
            item['status']=status
            item['name']=name
            item['times']=times
            self.log(item)
            yield item
        #下一页
        print('=='*60)
        next_page=response.xpath("//div[@class='pagination']/a[text()='>']/@href").extract()
        if len(next_page) >0:
            print(next_page)
            next_page=next_page[0]
            time.sleep(random.random()*5)
            yield response.follow(next_page,self.parse)




