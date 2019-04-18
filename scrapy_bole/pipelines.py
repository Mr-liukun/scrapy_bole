# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class ScrapyBolePipeline(object):
    def __init__(self):
        #self.conn = pymysql.connect("172.17.0.2", "root", "root", "onedb")
        self.conn = pymysql.connect("localhost", "root", "123", "onedb")
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        sql = "insert into bole (url,title, type,tag,content, time) values('%s','%s','%s','%s','%s','%s')" \
              % (item["url"], item["title"], item["type"], item["tag"], item["content"], item["time"])
        self.cursor.execute(sql)
        self.conn.commit()


    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()
