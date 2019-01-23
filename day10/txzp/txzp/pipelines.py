# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
class TxzpPipeline(object):
    def open_spider(self,item):
        self.con=pymysql.connect(host='localhost',port=3306,user='root',password='root',db='txzp',charset='utf8')
        self.cursor=self.con.cursor()
    def process_item(self, item, spider):
        self.sql='insert into news values (%s,%s,%s,%s,%s,%s,%s)'
        self.cursor.execute(self.sql,(0,item['title'],item['kind'],item['num'],item['addr'],item['times'],item['intro']))
        self.con.commit()
        return item
    def close_spider(self,item):
        self.cursor.close()
        self.con.close()
