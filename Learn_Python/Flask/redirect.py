#!/usr/bin/env python3
from flask import Flask
from flask import redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('hello'))

@app.route('/hello')
def hello():
    return '<h1>Look! Here is "/hello"!</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
