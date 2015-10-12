#!/usr/bin/env python3
import itertools
"""
itertools.cycle will make a iterable.
And that can repeat the giving elements again again again...
"""

a = itertools.cycle('ABC')
num = 0

while num < 10:
    num = num + 1
    print(next(a))
