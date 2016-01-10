#!/usr/bin/env python3
import re
import requests
from urllib import parse

roomid = 1
text = parse.quote(input('Please enter the text: '))

cookies = {'acct': input('Enter the content of cookies "acct": ')}
headers = {'content-type': 'application/x-www-form-urlencoded',
           'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
           '(KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36'}

fkey = re.search(
    '<input id="fkey" name="fkey" type="hidden" value="(.+?)" />',
     requests.get('http://chat.stackoverflow.com/rooms/1',
                  headers=headers, cookies=cookies).text).group(1)

print(cookies)
print(fkey)
print(text)

r = requests.post('http://chat.stackoverflow.com/chats/{id}/messages/new'
                  .format(id=roomid),
                  'text={text}&fkey={fkey}'
                  .format(text=text, fkey=fkey),
                  headers=headers, cookies=cookies)

print(r.text)
