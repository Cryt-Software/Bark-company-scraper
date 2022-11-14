# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BarkBusinessItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    desc = scrapy.Field()
    name = scrapy.Field()
    list_of_services = scrapy.Field()
    address = scrapy.Field()
    url = scrapy.Field()
    links = scrapy.Field()
    facebook = scrapy.Field()
    tel = scrapy.Field()
    website = scrapy.Field()
    email = scrapy.Field()
