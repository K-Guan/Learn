#!/usr/bin/env python3
import sys
import difflib

print('Text1: ', flush=True)
a = ''.join(sys.stdin.readlines())
print()

print('Text2: ', flush=True)
b = ''.join(sys.stdin.readlines())
print('\n')

print(''.join(difflib.Differ().compare(a.splitlines(True),
                                       b.splitlines(True))),
      end='')
print()
