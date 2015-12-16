#!/usr/bin/env python3
import re

text = '((2+3) + (4+5))'
test1 = re.findall(r'\(.*\)', text)
test2 = re.findall(r'\([^\(].+?\)', text)

for i in test1:
    print(i, end='')
else:
    print()

for i in test2:
    print(i, end='')
else:
    print()
