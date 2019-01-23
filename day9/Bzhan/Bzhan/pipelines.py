# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import codecs,csv
import pymysql
class BzhanPipeline(object):
    # def __init__(self):
    #     self.file = codecs.open('data/bili.csv','a',encoding='utf-8')
    #     self.wr = csv.writer(self.file)
    #     # 第一条标题行
    #     self.wr.writerow(['编号', '标题', '链接', '得分', '作者'])
    #
    # def process_item(self, item, spider):
    #     self.wr.writerow([item['num'], item['title'], item['link'], item['score'], item['author']])
    #     return item

    def open_spider(self,item):
        self.connect=pymysql.connect(host='localhost',port=3306,user='root',password='root',
                                     db='spiders_1',charset='utf8')
        self.cursor=self.connect.cursor()


    def close_spider(self,item):
        self.connect.commit()
        self.cursor.close()
        self.connect.close()

    def process_item(self, item, spider):
        sql = 'insert into bili values (%s,%s,%s,%s,%s,%s)'
        self.cursor.execute(sql,(0,item['num'], item['title'], item['link'], item['score'], item['author']))
        self.connect.commit()

        return item

