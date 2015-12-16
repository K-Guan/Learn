#!/usr/bin/env python3
import functools
def num(num1, num2):
    print(num1 + num2)

num2 = functools.partial(num, 2)

num(10, 20)
num2(10)
