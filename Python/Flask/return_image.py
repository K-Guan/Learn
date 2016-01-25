#!/usr/bin/env python3
from flask import Flask
from flask import send_file

app = Flask(__name__)

@app.route('/')
def return_image():
    return send_file(str(input('Enter a image path: ')))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
