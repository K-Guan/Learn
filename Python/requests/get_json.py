#!/usr/bin/env python3
import requests

r = requests.get('https://github.com/timeline.json')
print(r.json())
