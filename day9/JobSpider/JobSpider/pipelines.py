# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import codecs,csv
class JobspiderPipeline(object):
    def __init__(self):
        self.file=codecs.open('51job.csv','a+',encoding='utf-8')
        self.wr=csv.writer(self.file)
        #第一条标题行
        self.wr.writerow(['name','city'])

    def process_item(self, item, spider):
        self.wr.writerow([item['name'],item['city']])
        return item
