""" 
@author:jansonlv
@file: spider.py 
@time: 2016/8/24
@IDE: PyCharm
@project:spider 
"""

from DataDeal import DataDeal
from HtmlDownloader import HtmlDownloader
from HtmlParser import HtmlParser
from URLManager import UrlManager


class Spider(object):
    def __init__(self):
        self.url_manager = UrlManager()
        self.html_parser = HtmlParser()
        self.html_downloader = HtmlDownloader()
        self.data_save = DataDeal()

    def crawl(self, start_url):
        '''
        爬虫执行程序
        :param start_url: 爬虫开始地址
        :return: 无
        '''
        # 添加爬虫开始地址
        self.url_manager.add_new_url(start_url)
        # 如果还有url未爬取则不会停
        while self.url_manager.has_new_url():

            try:
                # 获取url
                new_url = self.url_manager.get_new_url()
                # 放入下载器
                html = self.html_downloader.downlooad(new_url)
                # 分析数据获取url和data
                urls, data = self.html_parser.parser(new_url, html)
                # url加入new_urls
                self.url_manager.add_new_urls(urls)
                # data放入内存,写入文件
                self.data_save.store_data(data)
                # 统计文件
                print("已经爬取{}个网页数据".format(str(self.url_manager.old_urls_len())))
            except Exception as error:
                print('crawl failed:', new_url, error)
        else:
            print('new_urls is null')

def main():
    spider1 = Spider()
    spider1.crawl('https://baike.baidu.com/item/%E8%9C%98%E8%9B%9B/8135707')


if __name__ == '__main__':
    main()
