#!/usr/bin/env python3
import sys
from itertools import cycle
color = cycle([91, 93, 92, 96, 94, 95])

with open(sys.argv[1]) as f:
    for i in f.read():
       print('\033[{0}m{1}\033[{0};m'
             .format(next(color), i),
             end='', flush=True)

    else:
        print()
