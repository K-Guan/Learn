#!/usr/bin/env python3
import requests
import mysql.connector
from bs4 import BeautifulSoup


conn = mysql.connector.connect(user=str(input('Enter username: ')),
                               password=str(input('Enter password: ')),
                               database='ssq')

cursor = conn.cursor()
cursor.execute('create table log(' +
               'Date date,' +
               'number int,' +
               'r1 int,' +
               'r2 int,' +
               'r3 int,' +
               'r4 int,' +
               'r5 int,' +
               'r6 int,' +
               'blue int)')

for url in ['http://www.touzhuzhan.com/toolset/index.php/' +
            'History/ssqiu/rangqi/100/page/1/startqi/0/endqi/0/',
            'http://www.touzhuzhan.com/toolset/index.php/' +
            'History/ssqiu/rangqi/100/page/2/startqi/0/endqi/0/']:

    headers = ({'user-agent': 'Mozilla/5.0 (X11; Linux x86_64)' +
                              'AppleWebKit/537.36 (KHTML, like Gecko)' +
                              'Chrome/45.0.2454.85 Safari/537.36'})

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")

    a = soup.find_all('tr', {'class', "tr4"})
    for i in a:
        data = i.text.strip().split('\n')
        rb = data[2].split()
        cursor.execute('insert into log values' +
                       '(%s, %s, %s, %s, %s, %s, %s, %s, %s)',
                       [data[0], data[1], rb[0], rb[1], rb[2],
                        rb[3], rb[4], rb[5], data[4]])

conn.commit()
cursor.close()
conn.close()
