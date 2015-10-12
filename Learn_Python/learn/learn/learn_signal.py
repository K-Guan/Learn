#!/usr/bin/env python3
import time
import signal

def text(signum, frame):
    print("Now exit the program.")
    exit()

signal.signal(signal.SIGALRM, text)
signal.alarm(5)

while True:
    print('Print some text...')
    time.sleep(1)
