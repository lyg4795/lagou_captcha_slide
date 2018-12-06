# -*- coding: utf-8 -*-

import logging
# from scrapy.utils.log import configure_logging
#
# configure_logging(install_root_handler=False)
# logging.basicConfig(
#     filename='log.txt',
#     format='%(levelname)s: %(message)s',
#     level=logging.INFO
# )
# logger=logging.getLogger()
# logger.error('da')
import pymongo

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class LagouPipeline(object):
    def __init__(self):
        self.connect=pymongo.MongoClient(host='localhost',port=27017)
        self.db=self.connect.sprider
        self.collection=self.db.lagou
    def process_item(self, item, spider):
        # for i in item['company']:
        #     filename=i["createTime"].split()[0]
        #     filename='C:/Users/yglin/PycharmProjects/sprider/lagou/company/'+filename
        #     with open(filename+'.json','a',encoding='utf8')as f:
        #         # 加ensure_ascii可转换中文，不然是Unicode格式
        #         f.write(json.dumps(i,ensure_ascii=False)+'\n')
        postItem=dict(item)
        dup_num=0

        try:
            for i in postItem['company']:
                self.collection.insert_one(i)
        except Exception as e:
            if ('duplicate key error') in str(e):
                dup_num+=1
            else:
                with open('log.txt','a',encoding='utf8')as f:
                    f.write(str(e)+'\n')
        with open('log.txt', 'a', encoding='utf8')as f:
            f.write(str(dup_num)+'\n')
        return item
