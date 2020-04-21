# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import post_api
import codecs

import pymongo
from scrapy.exceptions import DropItem


class SseinfoPipeline(object):
    collection_name = 'aa'
    seq_name = '_counters'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.first = False

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'items')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

        if not self.db[self.collection_name].count():
            self.first = True

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        condition = {"item_id": item['item_id']}
        result = self.db[self.collection_name].find_one(condition)
        if result:
            # 增量更新
            if not self.first:
                self.db[self.seq_name].update(condition, dict(item))
            raise DropItem("Duplicate item found: %s" % item)
        else:
            item_type = '11'
            rs = self.db[self.seq_name].find_and_modify({"type": item_type}, {"$inc": {"row_version": 1}}, upsert=True)
            if rs:
                item['row_version'] = rs['row_version']
                self.db[self.collection_name].insert_one(dict(item))

                return item

# 本地测试用，可在 settings 里替换
# class JsonPipeline(object):
#
#     def open_spider(self, spider):
#         self.file = open('items.json', 'w')
#
#     def close_spider(self, spider):
#         self.file.close()
#
#     def process_item(self, item, spider):
#         line = json.dumps(dict(item)) + "\n"
#         self.file.write(line)
#         return item
