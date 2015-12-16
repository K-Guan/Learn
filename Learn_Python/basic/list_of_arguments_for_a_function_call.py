#!/usr/bin/env python3
def test(*args):
    if 'test1' in args:
        print('Test1')

    if 'test2' in args:
        print('Test2')

    if 'test3' in args:
        print('Test3')


a = True
b = False
c = True

args = []

if a: args.append('test1')
if b: args.append('test2')
if c: args.append('test3')

test(*args)
