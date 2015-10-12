#!/usr/bin/env python3
import random

print('between 1 and 0 random float:', random.random())
print('between 1 and 100 random int:', random.randint(0, 100))
print()

values = ['Python', 'C', 'C++', 'Java', 'Ruby']
print('give a random choose in a list:', random.choice(values))
print('give three random choose in a list:', random.sample(values, 3))
print()
print()

print('randomize a list:')
print()
print('Before:', values)
random.shuffle(values)
print('After:', values)
print()
print()

print('50 random numbers:', random.getrandbits(50))
