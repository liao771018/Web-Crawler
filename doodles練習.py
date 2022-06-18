import urllib.request
from urllib.request import urlopen
import json
import os

for i in range(4):
    url = 'https://www.google.com/doodles/json/2022/' + str(i+1) + '?hl=zh-TW'
    response = urlopen(url)
    # response.read()
    # break

    #json讀出串列資料
    doodles = json.load(response)

    #doodles -> list -> dict
    for doodle in doodles:
        #url提取出來
        url = 'https:' + doodle['url']
        print(f'現在處理{i + 1}月中')
        print(doodle['title'], url)
        #讀取圖片資料
        response = urlopen(url)
        img = response.read()
        #準備存取路徑
        dirname = 'doodles/' + str(i + 1) + '/'
        if not os.path.exists(dirname):
            os.mkdir(dirname)

        name = dirname + url.split('/')[-1]
        #開始存取
        file = open(name, 'wb')
        file.write(img)
        file.close()

print('已下載完成')