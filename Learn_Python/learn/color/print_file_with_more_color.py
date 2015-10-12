#!/usr/bin/env python3
import sys
import random

with open(sys.argv[1]) as f:
    for i in f.read():
        color = random.randint(90, 96)
        print('\033[{0}m{1}\033[{0};m'
              .format(color, i), end='', flush=True)

    print()
