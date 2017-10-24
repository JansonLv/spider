"""
@author:jansonlv
@file: URLManager.py 
@time: 2016/8/24
@IDE: PyCharm
@project:spider 
"""


class UrlManager(object):

    def __init__(self):
        # 未爬取的url集合
        self.new_urls = set()
        # 已爬取的url集合
        self.old_urls = set()

    def has_new_url(self):
        '''
        判断是否含有未爬取的url
        :return:
        '''
        if self.new_urls_len():
            # print(self.new_urls)
            # print(self.new_urls_len())
            return True
        else:
            return False

    def new_urls_len(self):
        '''
        未爬取的url集合长度
        :return:
        '''
        return len(self.new_urls)

    def old_urls_len(self):
        '''
        已爬取的url集合长度
        :return:
        '''
        return len(self.old_urls)

    def get_new_url(self):
        '''
        获取一个新的(未爬取)url地址
        :return: 未爬取的url
        '''
        # 获取一个新的url
        new_url = self.new_urls.pop()
        # 将新的url返回给已爬取的url集合
        self.old_urls.add(new_url)
        return new_url

    def add_new_url(self, url):
        '''
        将新爬取的url添加到未爬取的url集合中
        :param url: 单个未爬取的url
        :return:
        '''
        if not url:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        '''
        将新的urls集合添加到未爬取的uel集合中
        :param urls:
        :return:
        '''
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.new_urls.add(url)

















