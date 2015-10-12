#!/usr/bin/env python3
import sys
import requests

url = 'http://paste.ubuntu.com/'
headers = ({'user-agent': 'Mozilla/5.0 (X11; Linux x86_64)'+
                          'AppleWebKit/537.36 (KHTML, like Gecko)'+
                          'Chrome/45.0.2454.85 Safari/537.36'})

name = input('Enter your name: ')
syntax = input('Enter the syntax: ')

with open(sys.argv[1], 'r') as f:
    text = f.read()

post = {'poster': name,
        'content': text,
        'syntax': syntax,}

r = requests.post(url, data=post, headers=headers)
print('\nYour text has been post on: '+r.url)
