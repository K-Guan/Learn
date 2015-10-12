#!/usr/bin/env python3
import sys

# this will redirect stdout to file 'stdout.log'
sys.stderr = open('stdout.log', 'w')
# this will redirect stderr to file 'stderr.log'
sys.stdout = open('stderr.log', 'w')


# make some stdout
print('Hello, this is a test')
print('A test')

# make a stderr
this_is_a_not_defined_name
