#!/usr/bin/env python3
import os
import sys
import argparse
from fnmatch import fnmatch


class Main(object):

    def __init__(self):
        self.argparser()
        for i in self.args.files:
            if os.path.isdir(i):
                for root, dirs, files in os.walk(i):
                    for name in files:
                        if fnmatch(root, i+'/.*'):
                            pass
                        elif name[0] == '.':
                            pass
                        else:
                            if not self.shebang:
                                if os.path.splitext(name)[1] == '.py':
                                    self.shebang = '#!/usr/bin/env python3'
                                elif fnmatch(os.path.splitext(name)[1], '.*sh'):
                                    self.shebang = '#!/bin/bash'
                                else:
                                    continue
                            self.checkshebang(os.path.join(root, name))

            else:
                if not self.shebang:
                    if os.path.splitext(i)[1] == '.py':
                        self.shebang = '#!/usr/bin/env python3'
                    elif fnmatch(os.path.splitext(i)[1], '.*sh'):
                        self.shebang = '#!/bin/bash'
                    else:
                        continue
                self.checkshebang(i)

    def argparser(self):
        parser = argparse.ArgumentParser(description="Auto change the script" +
                                         " SheBang and permission.")

        group = parser.add_mutually_exclusive_group()
        group.add_argument(
            "-a", "--auto",
            help="auto check the file type(By default, will use the extension)",
            action="store_true")

        group.add_argument("-b", "--bash",
                           help="The file type is 'bash', all files!",
                           action="store_true")

        group.add_argument("-p", "--python",
                           help="The file type is 'python', all files!",
                           action="store_true")

        parser.add_argument('files', nargs='+',
                            help="The files that you want to" +
                            "change the SheBang and permission")

        self.args = parser.parse_args()
        if self.args.bash:
            self.shebang = '#!/bin/bash'
        elif self.args.python:
            self.shebang = '#!/usr/bin/env python3'
        else:
            self.shebang = False

    def checkshebang(self, file):
        with open(file, 'r') as f:
            text = f.readline()
            if text[:2] != '#!':
                with open(file, 'w') as e:
                    e.write(self.shebang+'\n'+text+f.read())

            else:
                with open(file, 'w') as e:
                    e.write(self.shebang+'\n'+f.read())

            os.chmod(file, 493)

if __name__ == '__main__':
    Main()
