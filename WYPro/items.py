# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WyproItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    head = scrapy.Field()
    url = scrapy.Field()
    imageUrl = scrapy.Field()
    tag = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()