# -*- coding: utf-8 -*-
import scrapy,csv
from scrapy import cmdline
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class QiushibaikeSpider(CrawlSpider):
    name = 'qiushibaike'
    allowed_domains = ['jianshu.com']
    start_urls = ['https://www.qiushibaike.com/8hr/page/1/']

    rules = (
        # Rule(LinkExtractor(restrict_xpaths=r"//div[@class='recmd-right']/a[@class='recmd-content']"), callback='parse_item',follow=True),
        # Rule(LinkExtractor(allow=r"page/\d+/"), callback='parse_item',follow=True),
        Rule(LinkExtractor(restrict_css=r"li:last-child"),callback='parse_item',follow=True),
    )

    def parse_item(self, response):
        print(response.url)
            # title = response.xpath("//div[@class='col1 new-style-col1']/h1[@class='article-title']/text()").extract()[0]
            # link = i.xpath(".//div[@class='recmd-right']/a[@class='recmd-content']/@href").extract()[0]
            # url = base_url + link
            #
            # # 判断评论为空
            # pinglun = i.xpath(".//div[@class='recmd-num']/span[4]/text()").extract()
            # pinglun = pinglun[0] if len(pinglun) > 0 else None
            # zan = i.xpath(".//div[@class='recmd-num']/span[1]/text()").extract()
            # # 判断赞为空
            # zan = zan[0] if len(zan) > 0 else None
            # author = i.xpath(".//a[@class='recmd-user']/span/text()").extract()[0]
            # print(title)
            # with open('data/糗事.csv', 'a+', encoding='utf-8')as f_w:
            #     writer = csv.writer(f_w)
            #     writer.writerow(['作者:', author, '标题:', title, '点赞：', zan, '评论', pinglun, '标题连接:', url])
        yield


if __name__ == '__main__':
    cmd='scrapy crawl qiushibaike'
    cmdline.execute(cmd.split())