#!/usr/bin/env python3
import os
import sys

with open(sys.argv[1], 'r') as f:
    text = f.read()
    text = text.replace('PyQt4', 'PySide')

os.remove(sys.argv[1])

with open(sys.argv[1], 'w') as f:
    f.write(text)
