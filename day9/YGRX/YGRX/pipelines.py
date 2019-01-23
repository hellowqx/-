# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv,codecs

class YgrxPipeline(object):
    def __init__(self):
        self.file=codecs.open('data/YGRX.csv','a',encoding='utf-8')
        self.wr=csv.writer(self.file)
        # 第一条标题行
        self.wr.writerow(['编号', '标题','状态','网友','时间'])
    def process_item(self, item, spider):
        self.wr.writerow([item['num'], item['title'], item['status'], item['name'], item['times']])
        return item
