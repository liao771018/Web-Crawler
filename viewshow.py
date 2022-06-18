import requests
import bs4
import os
from urllib.request import urlopen


url = 'https://www.vscinemas.com.tw/vsweb/film/index.aspx'

response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, params={'p': '1'})

html = bs4.BeautifulSoup(response.text, 'html.parser')

contents = html.find_all('section', class_='infoArea')


for content in contents:

    movie_name = content.find('h2').text

    image = content.parent.find('img').attrs['src'][2:]
    image = 'https://www.vscinemas.com.tw/vsweb' + image

    print(movie_name, image)

    res2 = requests.get(image,headers={'User-Agent': 'Mozilla/5.0'})
    img = res2.content

    dirname = 'viewshow/'
    if not os.path.exists(dirname):
        os.mkdir(dirname)

    # name = dirname + image.split('/')[-1]
    name = dirname + movie_name + '.jpg'
    name = name.replace(':', '_')
    # print(name)

    with open(name, 'wb') as file:
        file.write(img)
