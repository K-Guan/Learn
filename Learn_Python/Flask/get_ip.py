#!/usr/bin/env python3
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def get_ip():
    return request.remote_addr

if __name__ == '__main__':
    app.run()
