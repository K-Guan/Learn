#!/usr/bin/env python3
import string

s = slice(3, 20, 3)
t = [t for t in range(100)]

print('slice start at: {0}, {1}'.format(s.start, t[s.start]))
print('slice stop at: {0}, {1}'.format(s.stop, t[s.stop]))
print('slice step is: {0}'.format(s.step))
print()
print(t[s])
