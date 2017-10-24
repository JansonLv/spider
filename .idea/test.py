""" 
@author:jansonlv
@file: test.py 
@time: 2016/7/24
@IDE: PyCharm
@project:spider 
"""

from bs4 import BeautifulSoup
import lxml
import requests

url = 'http://baike.baidu.com/view/284853.htm'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers={'User-Agent':user_agent}
html = requests.get(url, headers=headers)
# print(html.content)

# with open('aaa.txt', 'w') as f:
#     pass
#
# with open('test.html', 'w', encoding='utf-8') as f:
#     f.write(html.content.decode())
#     print('1')
soup = BeautifulSoup(html.content, 'html.parser', from_encoding='utf-8')
p = soup.select('body > div.body-wrapper > div.content-wrapper > div > div.main-content > div.lemma-summary > div > a')
# p = soup.select('body > div.body-wrapper > div.content-wrapper > div > div.main-content > dl.lemmaWgt-lemmaTitle.lemmaWgt-lemmaTitle- > dd > h1')
# print(p)
for i in p:
    print(i.get_text())
    print(i.get('href'))