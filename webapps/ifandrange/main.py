#!/usr/bin/env python3
from flask import Flask, flash, redirect, render_template, \
     request, url_for

app = Flask(__name__)

@app.route('/<text>')
def main(text):
    try:
        text = int(text)
        if text > 10000 or text < -10000:
            text = 10000

    except ValueError:
        pass


    return render_template('index.html', text=text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
