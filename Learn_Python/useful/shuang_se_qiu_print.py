#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup


url = 'http://www.touzhuzhan.com/toolset/index.php/'+\
    'History/ssqiu/rangqi/100/page/1/startqi/0/endqi/0/'

headers = ({'user-agent': 'Mozilla/5.0 (X11; Linux x86_64)'+
                          'AppleWebKit/537.36 (KHTML, like Gecko)'+
                          'Chrome/45.0.2454.85 Safari/537.36'})

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, "html.parser")

a = soup.find_all('tr', {'class', "tr4"})
for i in a:
    data = i.text.strip().split('\n')
    rb = data[2].split()
    print('日期：', data[0])
    print('期号：', data[1])
    print('红号1：', rb[0])
    print('红号2：', rb[1])
    print('红号3：', rb[2])
    print('红号4：', rb[3])
    print('红号5：', rb[4])
    print('红号6：', rb[5])
    print('蓝号：', data[4])
    print('\n')
