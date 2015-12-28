#!/usr/bin/env python3
"""
A simple script which shows how useful of Python list comprehension!
"""

# create a list in 'normal way'
foo = []
for i in ('10', '20'):
    foo.append(int(i))

# use list comprehension, clear and simple
bar = [int(i) for i in ('10', '20')]

print(foo, bar)
