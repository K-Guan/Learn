#!/usr/bin/env python3
"""
A simple demo about what does file.seek() function do
"""

with open('/tmp/file', 'w+') as f:
    f.write('0123456789')  # write the string into the file
    f.seek(0)              # seek to the file start (so it's `0`)

    print(f.read(4))       # read the first 4 characters
    f.seek(2, 1)           # now we at the index `4 + 2` == `6`.

    f.write('text')        # write text after index 6
    f.seek(0, 2)           # seek to the file end

    f.write('abc')         # write 'abc' into the file
    f.seek(0)              # seek to the file start again

    f.write('xyz')         # write 'xtz' at the file start
    f.seek(0)              # seek again

    print(f.read())        # print the whole file
