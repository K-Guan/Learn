#!/usr/bin/env python3

print(sorted([1, 20, 3, 22, -54, 21, 44, 97, 48]))
# use the normal mode of sorted.

print(sorted(map(abs, [1, 20, 3, 22, -54, 21, 44, 97, 48])))
# use sorted with map(abs, *iterables).

print(sorted([1, 20, 3, 22, -54, 21, 44, 97, 48], key=abs))
# use sorted(iterable, key=abs)
