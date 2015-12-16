#!/usr/bin/env python3
with open('/tmp/file', 'w+') as f:
    f.write('0123456789')  # write these text into file
    f.seek(0)              # seek to the file start(0)

    print(f.read(4))       # print 4 characters
    f.seek(2, 1)           # now we at 4 + 2 == 6!

    f.write('text')        # write text after 6
    f.seek(0, 2)           # seek to the file end

    f.write('abc')         # write abc into that file
    f.seek(0)              # seek to the file start again

    f.write('xyz')         # write xtz at the file start
    f.seek(0)              # again...

    print(f.read())        # print the whole file
