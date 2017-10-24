""" 
@author:jansonlv
@file: HtmlDownloader.py 
@time: 2016/8/24
@IDE: PyCharm
@project:spider 
"""

import requests


class HtmlDownloader(object):

    def downlooad(self, url):
        '''
        将url网址下载,并以utf-8格式返回
        :param url:
        :return:
        '''
        if url is None:
            return None
        # 随机获取下载头
        user_agent = ''
        headers = {'User-Agent':user_agent}

        html = requests.get(url, headers=headers)

        if html.status_code == 200:
            html.encoding = 'utf-8'
            return html
        return None
