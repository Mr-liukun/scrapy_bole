# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyBoleItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class ItemsBole(scrapy.Item):

    title = scrapy.Field()   # 标题

    type = scrapy.Field()    # 类型

    url = scrapy.Field()     # 链接

    time = scrapy.Field()    # 时间

    content = scrapy.Field() # 内容
