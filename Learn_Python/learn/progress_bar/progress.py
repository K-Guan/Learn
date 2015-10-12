#!/usr/bin/env python3
import time

for i in range(100):
    print('\r{0}\r'.format(i), end='')
    time.sleep(0.2)
