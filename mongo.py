# -*-coding:utf-8-*-
import re
from pymongo import MongoClient
'''
mongo数据修改脚本
'''
client = MongoClient('192.168.3.85', 27017)
db = client.popular_industry
collections = db.hxq_gangwei_data
total = 0

for item in collections.find({'sub_category': '数字文化服务产业', 'information_categories': '招聘资源'}):
    xueli = item.get('job_information_list')[4].get('学历要求')
    if xueli:
        if re.search('\d+', xueli) or '若干' in xueli:

            job_list = item.get('job_information_list')

            new_job_list = job_list
            new_job_list[4]['学历要求'] = None

            content_url = item.get('content_url')
            # print(content_url)
            collections.update_one({'content_url': content_url}, {"$set": {'job_information_list': new_job_list}})
            total = total + 1
    else:
        print(item.get('job_information_list'))



print(total)
