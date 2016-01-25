#!/usr/bin/env python3
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.google.com/')

driver.get_screenshot_as_file('google.png')
driver.close()
