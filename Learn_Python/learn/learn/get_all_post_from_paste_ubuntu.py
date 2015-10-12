#!/usr/bin/env python3
import requests
import itertools
from bs4 import BeautifulSoup

a = itertools.count(1)

for i in a:

    r = requests.get('http://paste.ubuntu.com/'+str(i)+'/')
    soup = BeautifulSoup(r.text, "html.parser")

    try:
        with open(str(i), 'w') as f:
            f.write(soup.find('td', {'class', "code"}).text.strip()+'\n')
    except:
        pass
