# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo as pymongo

class BarkBusinessPipeline(object):
    def process_item(self, item, spider):
        return item

class MongoPipeline(object):

    def __init__(self, mongo_uri, mongo_db, stats):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.stats = stats

    @classmethod
    def from_crawler(cls, crawler):
        ## pull in information from settings.py
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE'),
            stats=crawler.stats
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db['England'].insert(item)
        return item
