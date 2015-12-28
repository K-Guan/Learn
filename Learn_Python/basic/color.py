#!/usr/bin/env python3
"""
A small script which could print a test string
in all available color, format of the console (works on NT and Unix)

To let you know how to print text 'prettily'.
"""

formats = []

for i in range(0, 10):
    formats.append(i)
for i in range(30, 48):
    formats.append(i)
for i in range(90, 108):
    formats.append(i)

print('Demo:'+'\n')
for i in formats:
    # `fn` means `format_number` here
    print('\033[{fn}m   The demo of format "{fn}"   \033[{fn};m'
          .format(fn=i))
