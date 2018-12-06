import pymongo
import json
import logging
connect=pymongo.MongoClient(host='localhost',port=27017)
db=connect.sprider
collection=db.lagou
# 去重
# al=collection.aggregate([{'$group':{'_id':{'createTime':'$createTime',
#                                         'companyShortName':'$companyShortName'},
#                                  'count':{'$sum':1},
#                                  'dups':{'$addToSet':'$_id'}
#                                  }
#                           },
#                          { '$match':{'count':{'$gt':1}}
#                            }
#                       ])
# with open('company/2018-10-15.json','r',encoding='utf8')as f:
#     doc=f.readline()
# doc=json.loads(doc)
# try:
#     collection.insert_one(doc)
# except Exception as e:
#     if ('duplicate key error') in str(e):
#         print('duplicate key error')
#     else:
#         print(1)

logging.basicConfig(filename='log.txt',level=logging.DEBUG)
logging.warning(0)