#!/usr/bin/env python3
from selenium import webdriver

driver = webdriver.PhantomJS()
driver.maximize_window()

driver.get(input('Link: '))

for i in [i/100 for i in range(10, 999)]:
    driver.execute_script("scroll(0, document.body.scrollHeight/{0});"
                          .format(i))

driver.save_screenshot(input('File name: '))
