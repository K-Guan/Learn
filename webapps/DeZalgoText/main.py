#!/usr/bin/env python3
import string
from flask import Flask, jsonify, render_template, request
app = Flask(__name__)


@app.route('/_dezalgo')
def dezalgo():
    text = request.args.get('text', '')
    return jsonify(result=''.join(i for i in text if i in string.printable)
                   .strip())


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
