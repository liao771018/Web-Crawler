from urllib.request import urlopen, Request
from jieba.analyse import extract_tags
import bs4
import requests
import os

url = 'https://www.ptt.cc/bbs/Gossiping/M.1651397447.A.A8F.html'
# 用內建函式庫的做法
# r = Request(url)
# r.add_header('user-agent', 'Mozilla/5.0')
# response = urlopen(r)
# html = bs4.BeautifulSoup(response)

# 用外部函式庫的作法
# 如果有阻擋,注意可能是自動送 cookies
response = requests.get(url, cookies = {'over18':'1'})
html = bs4.BeautifulSoup(response.text)
# print(html)

# 比對網頁 -> 找出標籤
content = html.find('div', id = 'main-content')
# print(content.text)

metas = content.find_all('span', class_ = 'article-meta-value')
metas_text0 = '作者:' + metas[0].text
metas_text1 = '看板:' + metas[1].text
metas_text2 = '標題:' + metas[2].text
metas_text3 = '時間:' + metas[3].text
metas_text = [metas_text0, metas_text1, metas_text2, metas_text3]

# print('作者:', metas[0].text)
# print('看板:', metas[1].text)
# print('標題:', metas[2].text)
# print('時間:', metas[3].text)

# extract移除不要的標籤
metas = content.find_all('div', class_ = 'article-metaline')
for meta in metas:
    meta.extract()
metas = content.find_all('div', class_ = 'article-metaline-right')
for meta in metas:
    meta.extract()
pushs = content.find_all('div', class_ = 'push')

#計算推噓分數
score = 0
for push in pushs:

    tag = push.find('span', class_ = 'push-tag').text
    if '推' in tag:
        score += 1
    elif '噓' in tag:
        score -= 1

    push.extract()

doc_text = '分數' + str(score) + '\n本文' + content.text
key_words = extract_tags(content.text, 10)
# print(type(key_words))
# print(type(doc_text))
# print(type(metas_text))
# print('分數:', score, '\n本文:' , content.text)
# print('關鍵詞:', extract_tags(content.text, 10))

# 將資訊整理為一個STR
doc = '\n'.join(metas_text) + doc_text + ','.join(key_words)
# 儲存
file = open('PTT.txt', 'w', encoding='utf-8')
file.write(doc)
file.close()
