#!/usr/bin/env python3


class Number(object):

    def __init__(self, one, two):
        self.one = one
        self.two = two

    def count(self):
        print(self.one + self.two)


o = int(input('Enter the first number: '))
t = int(input('Enter the second number: '))


n = Number(o, t)
n.count()
