# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SseinfoItem(scrapy.Item):
    # define the fields for your item here like:
    # id
    item_id = scrapy.Field()
    # 自增 ID
    row_version = scrapy.Field()
    # 提问者
    questioner = scrapy.Field()
    # 向谁提问
    ask_who = scrapy.Field()
    # 问题描述
    question = scrapy.Field()
    # 提问时间
    question_time = scrapy.Field()

    # 回答者
    answerer = scrapy.Field()
    # 回答描述
    answer = scrapy.Field()
    # 回答时间
    answer_time = scrapy.Field()
