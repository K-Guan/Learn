#!/usr/bin/env python3
import difflib


def check_diff(a, b):
    diff = [i[0] for i in difflib.ndiff(a, b) if i[0] != ' ']
    nums = abs(diff.count('+') - diff.count('-'))
    return (nums if nums != 0 else diff.count('+'))


if __name__ == '__main__':
    a = input('Text1: ')
    b = input('Text2: ')
    print(list(difflib.ndiff(a, b)))
    print(check_diff(a, b))
