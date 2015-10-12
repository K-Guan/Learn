#!/usr/bin/env python3
from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, this is a test for 404 page'

@app.errorhandler(404)
def page_not_found(error):
    return 'This is not the web page you are looking for.', 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

