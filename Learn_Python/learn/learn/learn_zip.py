#!/usr/bin/env python3

a = (10, 20, 30)
b = ['ten', 'twenty', 'thirty']

zipped1 = zip(a, b)
zipped2 = zip(a, b)
zipped3 = zip(a, b)

print(*zipped1)
print()

for i in zipped2:
    print(i)

print()

for i, y in zipped3:
    print(i, y)

print()
