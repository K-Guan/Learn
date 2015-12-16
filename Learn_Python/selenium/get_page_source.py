#!/usr/bin/env python3
from selenium import webdriver
driver = webdriver.PhantomJS()

driver.get('https://www.google.com/')
print(driver.page_source)

driver.close()
