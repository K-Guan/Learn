#!/usr/bin/env python3
import re
import os
files = os.listdir()
for i in files:
    os.renames(i, ' '.join(re.findall('[a-zA-Z]+', os.path.splitext(i)[0])) +
               os.path.splitext(i)[1])
