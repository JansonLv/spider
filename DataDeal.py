""" 
@author:jansonlv
@file: DataDeal.py 
@time: 2016/8/24
@IDE: PyCharm
@project:spider 
"""
import codecs
class DataDeal(object):
    def __init__(self):
        self.datas = []

    def store_data(self, data):
        '''
        将数据存储在内存中
        :param data:
        :return:
        '''
        if data is None:
            return
        self.datas.append(data)

        # 调用,保存文件中

    def _output_data(self):
        '''
        将数据保存在文件中
        :return:
        '''
        pass