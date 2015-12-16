#!/usr/bin/env python3
import os
import urllib
import requests

keyword = input('Enter the keyword: ')
num = int(input('Enter the numbers: '))

files = 1
links = []

images_dir = keyword.replace(' ', '_')

if not os.path.exists(images_dir):
    os.mkdir(images_dir)

os.chdir(images_dir)


for start in range(0, num, 8):
    r = requests.get(
        'http://ajax.googleapis.com/ajax/services/search/images?v=1.0&'
        'q={keyword}&rsz=8&start={start}'.format(
            keyword=urllib.parse.quote(keyword),
            start=start)).json()['responseData']['results']

    links.extend(i['url'] for i in r)

for link in links[:num]:

    image = requests.get(link, timeout=1)
    filename = link.rsplit('/', 1)[1]

    while os.path.exists(filename):
        filename = ('_'+str(files)).join(os.path.splitext(filename))
        files += 1
    else:
        files = 1

    with open(filename, 'wb') as f:
        f.write(image.content)
