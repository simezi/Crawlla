# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawllaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    pass


class Song(scrapy.Item):
    title = scrapy.Field()
    bpm = scrapy.Field()
    time = scrapy.Field()
    type = scrapy.Field()
    category = scrapy.Field()
    start = scrapy.Field() # 実装日
    difficulties = scrapy.Field()

class Difficulty(scrapy.Item):
    rank = scrapy.Field()
    level = scrapy.Field()
    stamina = scrapy.Field()
    notes = scrapy.Field()
    density = scrapy.Field()