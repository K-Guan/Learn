#!/usr/bin/env python3
import sys
import random
color = [color for color in range(91, 97)]
with open(sys.argv[1], 'r') as f:
    for i in f:
        for w in i.rstrip().split(' '):
            if w.strip():
                print('\033[{0}m{1}\033[{0};m'
                      .format(random.choice(color), w), end='')
            print(' ', end='')
        print()
