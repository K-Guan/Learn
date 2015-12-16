#!/usr/bin/env python3
import os
import sys
import logging
import getpass
from time import sleep

logging.basicConfig(format='%(levelname)s: %(message)s',
                    level=logging.INFO)

if getpass.getuser() != 'root':
    logging.warning("You're not root")
    sleep(2)


logging.info("You're "+getpass.getuser())
sleep(2)
logging.info("You're using "+os.uname().sysname)
sleep(2)
logging.info("Python version is "+str(sys.version_info.major))
sleep(2)

if sys.version_info.major == 3:
    logging.error("You're not using Python 2")
else:
    logging.error("You're not using Python 3")

sleep(2)
logging.info("But don't worry")
sleep(2)

try:
    print(an, error, here)
except:
    logging.critical("We got a problem, " +
                     "please check the log.log for more info.")


[logging.root.removeHandler(handler) for handler in logging.root.handlers[:]]

logging.basicConfig(filename='log.log', filemode='w',
                    format='Time: %(asctime)s\n\
                    Level: %(levelname)s\n\
                    Message: %(message)s\n',
                    datefmt='%Y-%m-%d %I:%M:%S',
                    level=logging.INFO)


logging.warning("This is a test")
logging.warning("So we didn't get a problem")
logging.warning("Enjoy this script")
