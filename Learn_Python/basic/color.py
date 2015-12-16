#!/usr/bin/env python3
for i in range(0, 10):
    print('\033[{0}m{0}: This is a test\033[{0};m'.format(i))

for i in range(30, 48):
    print('\033[{0}m{0}: This is a test\033[{0};m'.format(i))

for i in range(90, 108):
    print('\033[{0}m{0}: This is a test\033[{0};m'.format(i))
