#!/usr/bin/env python3
import itertools
"""
itertools.repeat will make a iterable.
that can repeat the giving element,

in this example 'Test' will be repeated for 5 times.
"""

for i in itertools.repeat('Test', 5):
    print(i)
