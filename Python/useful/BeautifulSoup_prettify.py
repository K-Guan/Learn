#!/usr/bin/env python3
import sys
import requests
from bs4 import BeautifulSoup

r = requests.get(sys.argv[1])
soup = BeautifulSoup(r.text, "html.parser")

print(soup.prettify())
