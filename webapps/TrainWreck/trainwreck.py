#!/usr/bin/env python3
import os
import random
import string
from flask import Flask, send_file

app = Flask(__name__)


@app.route('/')
def trainwreck():
    return send_file(os.path.join('trainwreck',
                                  random.choice(os.listdir('trainwreck'))))


if __name__ == '__main__':
    app.run(debug=True)
