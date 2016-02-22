#!/usr/bin/env python3
from flask import abort
from flask import Flask
app = Flask(__name__)

@app.route('/')
def error():
    abort(401)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)