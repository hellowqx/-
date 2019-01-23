# -*- coding: utf-8 -*-
import scrapy,json
from scrapy import cmdline
import time,random,re
from jdspider.items import JdspiderItem

num = 0


class JdshopSpider(scrapy.Spider):

    name = 'jdshop'
    allowed_domains = ['jd.com']
    start_urls = ['https://search.jd.com/s_new.php?keyword=%E7%AC%94%E8%AE%B0%E6%9C%AC%E7%94%B5%E8%84%91&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E7%AC%94%E8%AE%B0%E6%9C%AC%E7%94%B5%E8%84%91&page=0&s=163&click=0']

    def parse(self, response):
        global num
        allinfos = response.xpath('//li[@class="gl-item"]')
        #获取页面商品id
        goods_ids = response.xpath('//li[@class="gl-item"]//strong/@class').extract()
        goods_ids=''.join(goods_ids)
        goods_ids=re.sub(r'(J_)',',',goods_ids)[1:]
        #评论的连接包含商品id
        pinglun_url='https://club.jd.com/comment/productCommentSummaries.action?referenceIds='+goods_ids+'&callback=jQuery450465&_=1548078886455'
        print(pinglun_url,222222222222222222)
        # res=scrapy.Request(pinglun_url,callback=None,method='get')
        # print(res,111111111111111111)

        # print(goods_ids)
        # goods_ids = goods_ids[2:]
        print(len(allinfos))
        for i in allinfos:
            price=i.xpath(".//strong/i/text()").extract()[0]
            goods_id=i.xpath(".//strong/@class").extract()[0]
            goods_id=goods_ids[2:]
            intro=i.xpath(".//div[@class='p-name p-name-type-2']")
            intro=intro.xpath('string(.)').extract()[0].strip()
            # print(price,goods_ids,pinglun,intro)
            item=JdspiderItem(price=price,intro=intro)
            # yield response.follow(pinglun_url,self.pinglun,meta={'item':item})
            yield scrapy.Request(pinglun_url,self.pinglun,meta={'item':item})


        num += 1
        if num < 101:
            next_page = 'https://search.jd.com/s_new.php?keyword=%E7%AC%94%E8%AE%B0%E6%9C%AC%E7%94%B5%E8%84%91&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E7%AC%94%E8%AE%B0%E6%9C%AC%E7%94%B5%E8%84%91&page='+str(num)+'&s=163&click=0'
            time.sleep(random.random() * 5)

            yield response.follow(next_page,self.parse)
    def pinglun(self,response):
        # print(type(response))
        a=json.loads(response.text)
        print(a,333333333333333333333)
        # item=response['item']
        # pinlun=1


if __name__ == '__main__':
    cmd = 'scrapy crawl jdshop'
    cmdline.execute(cmd.split())
