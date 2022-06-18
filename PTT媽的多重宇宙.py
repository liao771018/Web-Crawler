from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import os

url = 'https://www.ptt.cc/bbs/movie/M.1651400647.A.B32.html'
r = Request(url)
r.add_header('user-agent', 'Mozilla/5.0')
response = urlopen(r)

html = BeautifulSoup(response)

content = html.find('div', id='main-container')

metas = content.find_all('span', class_='article-meta-value')
name = '作者 : ' + metas[0].text
cls = '看板 : ' + metas[1].text
title = '標題 : ' + metas[2].text
times = '時間 : ' + metas[3].text
head = [name, cls, title, times]

metas = content.find_all('div', class_ = 'article-metaline')
for m in metas:
    m.extract()

metas = content.find_all('div', class_ = 'article-metaline-right')
for m in metas:
    m.extract()

push = 0
pushs = content.find_all('div', class_ = 'push')
for p in pushs:
    if '推' in p.text:
        push += 1
    elif '噓'in p.text:
        push -= 1
    p.extract()

head = '\n'.join(head)
push = '推文: ' + str(push)
content = content.text
doc = head + push + content

dirname = 'PTT/'
if not os.path.exists((dirname)):
    os.mkdir(dirname)

filename = dirname + '媽的多重宇宙.txt'

file = open(filename, 'w', encoding='utf-8')
file.write(doc)
file.close()