""" 
@author:jansonlv
@file: HtmlParser.py 
@time: 2016/8/24
@IDE: PyCharm
@project:spider 
"""

# import re
import math
from bs4 import BeautifulSoup
import lxml

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
        soup = BeautifulSoup(html_content, 'html.parser', from_encoding='utf-8')

        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

    def _get_new_urls(self, page_url, soup):
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
        links = soup.select('body > div.body-wrapper > div.content-wrapper > div > div.main-content > div.lemma-summary > div > a')
        # print(p)
        for link in links:
            url = link.get('href')
            new_urls.add('https://baike.baidu.com' + url)


        return new_urls

    def _get_new_data(self, page_url, soup):
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
        title = soup.select('body > div.body-wrapper > div.content-wrapper > div > div.main-content > dl.lemmaWgt-lemmaTitle.lemmaWgt-lemmaTitle- > dd > h1')[0].get_text()


        data['title'] = title
        return data
'''

    body > div.body-wrapper > div.content-wrapper > div > div.main-content > div.lemma-summary > div:nth-child(1) > a
    body > div.body-wrapper > div.content-wrapper > div > div.main-content > div.lemma-summary > div:nth-child(2) > a:nth-child(1)
    body > div.body - wrapper > div.content - wrapper > div > div.main - content > div.lemma - summary > div > a.xh - highlight
'''
