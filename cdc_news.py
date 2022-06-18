import requests
import bs4

for page in range(2, 10):

    url = 'https://www.cdc.gov.tw/Bulletin/List/MmgtpeidAR5Ooai4-fgHzQ'

    response = requests.get(url, headers={'user-agent': 'Mozilla/5.0'}, params={'page': page})

    # print(response) # get
    html = bs4.BeautifulSoup(response.text, 'html.parser')

    contents = html.find_all('div', class_="content-boxes-v3")
    # print(contents)


    for content in contents:

        u = content.find('a')

        ps = content.find_all('p')
        p_list = []
        for p in ps:
            p_list.append(p.text + ' ')

        p = ''.join(p_list)
        print(p, end='\n')

        u = 'https://www.cdc.gov.tw' + u.attrs['href']
        print(u)

        res2 = requests.get(u, headers={'user-agent': 'Mozilla/5.0'})

        html2 = bs4.BeautifulSoup(res2.text, 'html.parser')
        content2 = html2.find('div', class_='text-right')

        print(content2.parent.text)

        filename = 'cdc_news/' + p + '.txt'
        with open(filename, 'w', encoding='utf-8') as file:

            file.write(p + '\n' + u + '\n\n' + content2.parent.text)
