#!/usr/bin/env python3
import time
from flask import Flask

app = Flask(__name__)

@app.route('/')
def dateandtime():
    return '<h1>'+time.strftime('%Y-%m-%d %H:%M:%S')+'</h1>'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
