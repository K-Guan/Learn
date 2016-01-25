#!/usr/bin/env python3
import requests

r = requests.get('https://wiki.archlinux.org/index.php/Special:Random')
print(r.url)
