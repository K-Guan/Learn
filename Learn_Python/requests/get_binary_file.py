#!/usr/bin/env python3
import requests

r = requests.get(str(input('Enter a link of a binary file: ')))
with open('binary_file', 'wb') as f:
    f.write(r.content)
