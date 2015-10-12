#!/usr/bin/env python3
import sys
import time

a = 0
while a < 20:
    a = a + 1
    sys.stdout.write('#')
    sys.stdout.flush()
    time.sleep(0.1)

sys.stdout.write('\n')
