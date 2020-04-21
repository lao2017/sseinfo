# -*- coding: utf-8 -*-
import scrapy
import re

# import sys
# sys.setdefaultencoding('utf-8')
from sseinfo.items import SseinfoItem


class SnsSpider(scrapy.Spider):
   #爬虫名
    name = 'sns'
   #爬取域范围，允许爬虫在这个域名下进行爬取（可选）
    allowed_domains = ['sns.sseinfo.com']
   #爬虫执行后第一批请求，将从这个列表里获取
    baseURL = "http://sns.sseinfo.com/ajax/feeds.do?type=11&pageSize=10&lastid=-1&show=1&page="

    #起始页为1
    offset = 1
    start_urls = [baseURL + str(offset)]
    matchObj = False

    def parse(self, response):

        node_list = response.xpath("//div[@class='m_feed_item']")
        print(node_list.extract())
        #存储所有的item字段
        for node in node_list:

            item = SseinfoItem()

            # 通过xpath获取需要的内容（list）
            id_attr = node.xpath("./@id")

            questioner_path = node.xpath("./div[@class='m_feed_detail m_qa_detail']/div[@class='m_feed_face']/p/text()")
            ask_who_path = node.xpath("./div[@class='m_feed_detail m_qa_detail']/div[2]/div[@class='m_feed_txt']/a/text()")
            question_path = node.xpath("./div[@class='m_feed_detail m_qa_detail']/div[2]/div[@class='m_feed_txt']/text()[2]")
            question_time_path = node.xpath("./div[@class='m_feed_detail m_qa_detail']/div[2]/div[@class='m_feed_func']/div[1]/span/text()")

            answerer_path = node.xpath("./div[@class='m_feed_detail m_qa']/div[@class='m_feed_face']/p/text()")
            answer_path = node.xpath("./div[@class='m_feed_detail m_qa']/div[@class='m_feed_cnt']/div[@class='m_feed_txt']/text()")
            answer_time_path = node.xpath("./div[@class='m_feed_detail m_qa']/div[@class='m_feed_func top10']/div[@class='m_feed_from']/span/text()")

            # 从获得的list中拿到数据
            id_attr = id_attr.extract()[0]
            id_attr = id_attr.split('-')
            item_id = id_attr[1]

            questioner = questioner_path.extract()[0] if len(questioner_path) else ""
            ask_who = ask_who_path.extract()[0] if len(ask_who_path) else ""
            question = question_path.extract()[0] if len(question_path) else ""

            question_time = question_time_path.extract()[0] if len(question_time_path) else ""

            answerer = answerer_path.extract()[0] if len(answerer_path) else ""
            answer = answer_path.extract()[0] if len(answer_path) else ""
            answer_time = answer_time_path.extract()[0] if len(answer_time_path) else ""
            ask_who.encode('utf-8')

            # 将数据添加到字典中
            item['item_id'] = item_id

            item['questioner'] = questioner
            item['ask_who'] = ask_who
            print(question)
            item['question'] = question.replace('\n\t\t\t\t\t\t\t\t','')

            item['question_time'] = question_time

            item['answerer'] = answerer
            item['answer'] = answer.replace('\n\t\t\t\t\t\t\t','').replace('\n\t\t\t\t\t\t','')
            item['answer_time'] = answer_time



            #python2需要加上encode('utf-8')，python3不需要加encode('utf-8')
            #self.matchObj = re.search("月", item['answer_time'].encode('utf-8'), re.M | re.I)
            # 若部署SpiderKeeper中的Args填写 increment=False|True 取消下面一行注释
            if self.increment is True:
            # 未采集历史数据则注释下面三行，则后续采集取消注释
             self.matchObj = re.search("月", item['answer_time'], re.M|re.I)
             if self.matchObj:
                break

            yield item

        # 如果没有找到对应的class则表明还有下一页
        if not response.xpath("//a[@class ='m_feed_note']") and not self.matchObj:
        # if node_list and not matchObj:
            self.offset += 1
            next_url = self.baseURL + str(self.offset)
            yield scrapy.Request(next_url, callback=self.parse)
        else:
            print("采集完成")




# 第一种方法，在命令行用crawl控制spider爬取的时候，加上 - a选项，例如:
#scrapy crawl sns -a increment=True|False



