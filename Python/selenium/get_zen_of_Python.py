#!/usr/bin/env python3
import os
from selenium import webdriver

driver = webdriver.PhantomJS(service_log_path=os.path.devnull)
driver.get('https://www.python.org/dev/peps/pep-0020/')

print(driver.title)
print()
print(__import__('textwrap').dedent(
    driver.find_elements_by_tag_name('pre')[1].text))

driver.close()