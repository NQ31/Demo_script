from pymongo import MongoClient

class Handle_Mongo(object):

    def __init__(self,client,db,colle):
        # self.client = MongoClient('192.168.3.85', 27017)
        # self.db = self.client.popular_industry
        # self.collections = self.db.hxq_simple_zj_data
        self.client=client
        self.db=db
        self.collections=colle

    def inser_data(self, item,**kwargs):
        content_url = item['content_url']
        if self.collections.find_one({'content_url': content_url}):
            print('数据已经存在')
            return '数据已存在'
        else:
            self.collections.insert_one(item)
            return '插入成功'

    def update_data(self,item,**kwargs):
        '''
        update_one第一个参数｛｝是筛选条件
                  第二个参数｛｝是修改字段
        批量修改：updateMany,参数跟update_one一致
        '''
        res=self.collections.update_one({'content_url': content_url}, {"$set": {'job_information_list': new_job_list}})
        return res

    def delete_data(self):
        pass
