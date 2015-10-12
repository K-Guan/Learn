#!/usr/bin/env python3
import requests

r = requests.get(str(input('Enter a link: ')))
with open('webpage.html', 'w') as f:
    f.write(r.text)
