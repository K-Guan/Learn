#!/usr/bin/env python3
import json

d = {'a': 10, 'b': 20, 'c': 30}
t = ('a', 'b', 'c')
l = [10, 20, 30]

jd = json.dumps(d)
jt = json.dumps(t)
jl = json.dumps(l)

fd = json.loads(jd)
ft = json.loads(jt)
fl = json.loads(jl)

print(d, t, l)
print()
print(jd, jt, jl)
print()
print(fd, ft, fl)
