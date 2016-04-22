#!/usr/bin/env python3
import os
import sys
import requests
from bs4 import BeautifulSoup


def url_generater(path):
    song = os.path.realpath(path).split('/')

    name = os.path.splitext(song[-1])[0]
    if '. ' in name:
        name = name.split('. ')[-1]

    name = name.lower().replace(' ', '')

    artist = song[5].lower().replace(' ', '')
    return 'http://www.azlyrics.com/lyrics/{}/{}.html'.format(artist, name)


headers = {'user-agent': 'Mozilla/5.0 (X11 Linux x86_64) AppleWebKit/537.36 '
           '(KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36'}

r = requests.get(url_generater(sys.argv[1]), headers=headers)


soup = BeautifulSoup(r.text, "html.parser")
print(soup.find('span', {'id': 'cf_text_top'}).find_next('div').text.strip())
