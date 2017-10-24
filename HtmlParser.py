""" 
@author:jansonlv
@file: HtmlParser.py 
@time: 2016/8/24
@IDE: PyCharm
@project:spider 
"""

import re

class HtmlParser(object):
    def parser(self, page_url, html_content):
        '''
        用于解析网页内容,抽取url和数据
        :param page_url: 下载页面的url????
        :param html_content: 下载的网页内容
        :return: 返回url和数据
        '''
        if page_url is None or not html_content:
            pass
        new_urls = ''
        new_data = ''
        return new_urls, new_data

    def _get_new_urls(self, page_url, html_content):
        '''
        抽取新的url集合
        :param page_url: 下载页面的url???
        :param html_content: html页面内容
        :return: 返回新的url集合
        '''
        new_urls = set()
        '''
        抽取url地址
        '''
        return new_urls

    def _get_new_data(self, page_url, html_content):
        '''
        抽取有效数据
        :param page_url: 下载页面的url
        :param html_content: html页面内容
        :return: 返回有效数据
        '''
        data = {}
        data['url'] = page_url
        '''
        提取data数据
        '''
        data['title'] = ''
        return data