# -*-coding:utf-8-*-


import re
import requests
import os,uuid
from Crypto.Cipher import AES
import m3u8


# des
base_url='https://1258712167.vod2.myqcloud.com/fb8e6c92vodtranscq1258712167/f0a0fd0d5285890804501530799/drm/voddrm.token.dWluPTA7c2tleT07cHNrZXk9O3Bsc2tleT07ZXh0PTtjaWQ9MjczNzMyNTt0ZXJtX2lkPTEwMjg0NDU5ODt2b2RfdHlwZT0w.v.f30742.m3u8?exper=0&sign=f76c60c918f82a7aebddc496abc0f061&t=60ea696e&us=7534938683620818388'
# res=requests.get(url=base_url)
# # print(res.content)
# pay_list=res.text.split('\n')
# print(pay_list)
# print(pay_list[9:-1:3])
# print(pay_list[10:-1:3])
class Demo(object):
    '''
       只需要在download方法中传入一个m3u8url即可
    '''
    # def __init__(self):
    #     #初始化url:(m3u8 url）
    #     # self.base_url=base_url
    #     # 加密方法的正则语句
    #     self.m_re = '#EXT-X-KEY:METHOD=(.*?),'
    #     # 加密url的正则语句
    #     self.url_re='#EXT-X-KEY:METHOD=AES-128,(.*?)\n'

    # def get_ts_url(self,url):
    #
    #
    #
    #     return ts_urls

    # def get_method_key(self, content):
    #     method = re.findall(self.m_re, content)[0]
    #     # 获取加密url
    #     key = re.findall(self.url_re, content)[0]
    #     key_url = key[1:-1]
    #     # 对加密url发起请求
    #     res = requests.get(key_url)
    #     # 获取返回来的加密密钥
    #     key = res.content
    #
    #     return method, key

    def get_filpath(self):
        if not os.path.exists('ts_files'):
            os.system('mkdir ts_files')
        f_path=os.getcwd()+'\\ts_files\\'
        return f_path

    def ts_to_mp4(self):
        path = self.get_filpath()
        mp4_name = str(uuid.uuid1()) + '.mp4'
        merge_cmd = 'copy /b ' + path + '\*.ts ' + path + '\\' + mp4_name
        # del_cmd = 'del ' + path + '\*.ts'

        os.system(merge_cmd)
        # os.system(del_cmd)
        print('转换完成')

    def download_ts(self,url,base_url):
        # 获取初始的ts_urls 和content
        res = requests.get(url=url)
        pay_list = res.text.split('\n')
        ts_urls = pay_list[9:-1:3]

        # 获取加密的方法和密钥
        content=res.text
        method = re.findall('#EXT-X-KEY:METHOD=(.*?),', content)[0]
        # 获取加密url
        key = re.findall('#EXT-X-KEY:METHOD=AES-128,(.*?)\n', content)[0]
        key_url = re.findall('"(.*?)"', key)[0]
        # 对加密url发起请求
        res = requests.get(key_url)
        # 获取返回来的加密密钥
        key = res.content

        cryptor = AES.new(key, AES.MODE_CBC, key)

        for i, p in enumerate(ts_urls):
            ts_url = base_url + p
            res = requests.get(ts_url)
            file_name = str(i).rjust(3,'0') + '.ts'
            file=self.get_filpath()+file_name
            with open(file, 'wb') as f:
                # 对ts文件内容进行解密
                f.write(cryptor.decrypt(res.content))
                print('下载完成')
        self.ts_to_mp4()


if __name__=='__main__':
    url = 'https://1258712167.vod2.myqcloud.com/fb8e6c92vodtranscq1258712167/e9bb3a515285890788236802920/drm/voddrm.token.dWluPTM1MTc4MzU1NDQ7c2tleT1AQklIMFlFYU9SO3Bza2V5PUpPUE44RVUtLXdMUWxqeERZVHUyNEFoa3kqVGh5NGp5clBpbUIzbUJscW9fO3Bsc2tleT0wMDA0MDAwMDc2MTNiOTRmMjA4NmU1NTJjNzhkYzI3NzdhYjQ3NGQxYzZhNGEzN2ZkNTVmMDc4ODZhODFjNDI3MTBmZTA2MTJmN2EwZjFkNzczOTU1OTMyO2V4dD07dWlkX3R5cGU9MDt1aWRfb3JpZ2luX3VpZF90eXBlPTA7Y2lkPTMwNTg1ODt0ZXJtX2lkPTEwMjY5MjcyMjt2b2RfdHlwZT0w.v.f30741.m3u8?exper=0&sign=5fba39b595b47e49acb367bf07635d20&t=60ea99c3&us=6195723431588545335'
    base_url='https://1258712167.vod2.myqcloud.com/fb8e6c92vodtranscq1258712167/e9bb3a515285890788236802920/drm/'
             # 'https://1258712167.vod2.myqcloud.com/fb8e6c92vodtranscq1258712167/f0a0fd0d5285890804501530799/drm/'
    h = Demo()
    h.download_ts(url=url,base_url=base_url)
