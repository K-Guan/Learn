#!/usr/bin/env python3
from fractions import Fraction

a = Fraction(1, 2)
b = Fraction(3, 10)

text1 = "{a} minus {b} is {num}.\n"
text2 = "{b}'s numerator is {numerator}\n"\
"{b}'s denominator is {denominator}"

print(text1.format(a=a, b=b, num=(a - b)))
print(text2.format(b=b,
                   numerator=b.numerator,
                   denominator=b.denominator))
