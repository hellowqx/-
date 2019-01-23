# -*- coding: utf-8 -*-
import scrapy
import random,time


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/top250?start=0&filter=']

    def parse(self, response):
        item = dict()
        allinfo = response.xpath("//ol[@class='grid_view']/li")
        print(len(allinfo))
        for i in allinfo:

            title = i.xpath("./div[@class='item']/div[@class='info']/div[@class='hd']/a/span[@class='title'][1]/text()").extract()[0]
            link = i.xpath("./div[@class='item']/div[@class='info']/div[@class='hd']/a/@href").extract()[0]
            doc = i.xpath(".//div[@class='item']/div[@class='info']/div[@class='bd']/p[1]/text()").extract()[0]
            star = i.xpath(".//div[@class='item']/div[@class='info']/div[@class='bd']/div[@class='star']/span[@class='rating_num']/text()").extract()[0]
            item['title'] = title
            item['star'] = star
            item['link'] = link
            item['doc'] = doc.strip()
            time.sleep(1)

            yield response.follow(link,self.get_info,meta={'item':item})
        # 下一页
        print('==' * 60)
        base_url='https://movie.douban.com/top250'
        next_page = response.xpath("//div[@class='paginator']/span[@class='next']/a[text()='后页>']/@href").extract()
        if len(next_page) > 0:
            next_url=base_url+next_page[0]
            print(next_url)
            time.sleep(random.random() * 5)
            yield response.follow(next_url, self.parse)
        else:
            print('下载完毕')

    def get_info(self,response):
        item=response.meta['item']
        intro=response.xpath("//div[@id='link-report']/span[1]")
        intro=intro.xpath('string(.)').extract_first().strip()
        item['intro']=intro
        print(item)
        yield item



if __name__ == '__main__':
    from scrapy import cmdline

    command = 'scrapy crawl douban'
    cmdline.execute(command.split())