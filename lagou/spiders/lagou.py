import json
import scrapy
from ..items import LagouItem
from .ua import UA
from random import choice
class lagou_sprider(scrapy.Spider):
    name = 'lagou'
    headers = {
        'User-Agent': choice(UA),
        'Host':  "www.lagou.com",
        'Origin': "https://www.lagou.com",
        'Referer': 'https://www.lagou.com/jobs/list_%E7%88%AC%E8%99%AB?labelWords=&fromSearch=true&suginput='
    }
    def start_requests(self):
        return [scrapy.FormRequest('https://www.lagou.com/jobs/positionAjax.json?city=%E4%B8%8A%E6%B5%B7&needAddtionalResult=false',
                                  formdata={'first':'true','pn':'1','kd':'爬虫'},
                                   meta={'pn':1},
                                   headers=self.headers,
                                  callback=self.anlyze)]
    def anlyze(self,response):
        try:
            companys=json.loads(response.text)['content']["positionResult"]['result']
        except Exception as e:
            print(e)
            return
        pn=response.meta['pn']+1
        if companys!=[]:
            item=LagouItem(company=companys)
            yield item
        else:
            print('空')
            return
        print(pn-1)
        yield scrapy.FormRequest('https://www.lagou.com/jobs/positionAjax.json?city=%E4%B8%8A%E6%B5%B7&needAddtionalResult=false',
                                  formdata={'first':'true','pn':str(pn),'kd':'爬虫'},
                                   meta={'pn':pn},
                                   headers=self.headers,
                                  callback=self.anlyze,
                                dont_filter=True)