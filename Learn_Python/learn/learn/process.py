#!/usr/bin/env python3
from multiprocessing import Process, Queue
import time
import sys


def write(q):
    q.put("Hello")
    time.sleep(5)

    q.put('True')


def read(q):
    print(q.get())
    while True:
        if q.get() == 'True':
            print('\nFinish')
            sys.exit()

q = Queue()
Process(target=write, args=(q,)).start()
Process(target=read, args=(q,)).start()
