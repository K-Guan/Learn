#!/usr/bin/env python3
a = []
for i in ('10', '20'):
    a.append(int(i))

b = [int(i) for i in ('10', '20')]

print(a, b)
