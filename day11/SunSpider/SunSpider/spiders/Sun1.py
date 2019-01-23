# -*- coding: utf-8 -*-
import scrapy
from SunSpider.items import SunspiderItem

class Sun1Spider(scrapy.Spider):
    name = 'Sun1'
    allowed_domains = ['wz.sun0769.com']
    url = 'http://wz.sun0769.com/index.php/question/questionType?type=4&page='
    offset =0
    start_urls = [url + str(offset)]

    def parse(self, response):
        print('body:',response.body.decode(response.encoding))
        ls = response.xpath("//div[@id='morelist']/div/table[2]/tr/td/table/tr")
        print(len(ls))

        for link in ls:
            item = SunspiderItem()
            number = link.xpath("./td[1]/text()")[0].extract()
            print("number:",number)
            title= link.xpath("./td[2]/a[2]/text()").extract()[0]
            print("title:",title)
            detail_url = link.xpath("./td[2]/a[2]/@href").extract()[0]
            print('detail url:',detail_url)
            user = link.xpath("./td[4]/text()").extract()[0]
            print('user:',user)
            pub_date = link.xpath("./td[5]/text()").extract()[0]
            print('pub_date:',pub_date)
            print("="*60)
            item["number"] = number
            item["title"] = title
            item["url"] = detail_url
            item["user"] = user
            item["pub_date"] = pub_date

            req = scrapy.Request(detail_url,callback=self.parse_content)
            req.meta['item'] = item
            yield req

        #处理翻页
        if self.offset <= 60000:
            self.offset += 30
            page_url = self.url + str(self.offset)
            print('next page url:',page_url)
            yield scrapy.Request(page_url,callback=self.parse)

    def parse_content(self,response):
        print('parse content....')
        item = response.meta['item']
        #投诉内容
        content = response.xpath('//div[@class="wzy1"]/table[2]/tr[1]/td/text()')
        if len(content)>0:
            content = content.extract()
            content = ''.join(content)
        else:
            content = response.xpath('//div[@class="wzy1"]/table[2]/tr[1]/td/div[@class="contentext"]/text()')
            if len(content) > 0:
                #content = content.extract()[0].strip()
                content = ''.join(content)
            else:
                content = '空'
        item['content'] = content
        print("item:",item)
        yield item

