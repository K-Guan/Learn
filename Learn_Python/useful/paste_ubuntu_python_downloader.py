#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup

r = requests.get(str(input('Enter the link: ')))
file = str(input('Enter the filename: '))
print('\n')

soup = BeautifulSoup(r.text, "html.parser")

with open(file, 'w') as f:
    f.write(soup.find('td', {'class', "code"})
            .text.strip()+'\n')

for i in soup.find_all('h1'):
    print(i.text)

for i in soup.find('pre'):
    line = i

print('\nLine: '+line.split('\n')[-1] +
      '\nFilename: '+file)
