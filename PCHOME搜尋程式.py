# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XUN_uzxU88Z_8VSFiAtXRJDHakjmhqJP
"""

from json.decoder import JSONDecodeError
import requests
import json
import prettytable

url = 'https://ecshweb.pchome.com.tw/search/v3.3/all/results'

page = 1
q = input('關鍵字: ')

try:

  while True:  

    response = requests.get(url, 
                            params = {
                                      'q' : q,
                                      'page' : page,
                                      'sort' : 'sale/dc'
                                      }
                            )

    ret = json.loads(response.text)

    # print(ret)
    # print(type(ret))  # dict

    prods = ret['prods']
    # print(prods)
    # print(type(prods))  # list

    p1 = prettytable.PrettyTable(['名稱', '價格'], )
    p1.align['名稱'] = 'l'
    p1.align['價格'] = 'c'

    for prod in prods:
      p1.add_row([prod['name'], prod['price']])

    print(p1)
    page = int(input('前往頁碼: '))

except KeyError:
  print('找不到與' + q  + '有關的產品')

except JSONDecodeError:
  print('頁碼超過範圍!')