# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class EtaoItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
