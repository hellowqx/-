# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WeiboItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class User_info(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    avatar = scrapy.Field()
    gender = scrapy.Field()
    local = scrapy.Field()
    description = scrapy.Field()
    certification = scrapy.Field()
    fans_count = scrapy.Field()
    follows_count = scrapy.Field()
    weibos_count = scrapy.Field()
    person_url = scrapy.Field()
    level = scrapy.Field()


class UserRelationItem(scrapy.Item):
    id = scrapy.Field()
    follows = scrapy.Field()
    fans = scrapy.Field()