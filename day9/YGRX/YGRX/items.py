# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YgrxItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    num=scrapy.Field()
    title=scrapy.Field()
    name=scrapy.Field()
    times=scrapy.Field()
    status=scrapy.Field()