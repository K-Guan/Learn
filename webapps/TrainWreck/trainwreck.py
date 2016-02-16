#!/usr/bin/env python3
import os
import random
from flask import Flask, send_file

app = Flask(__name__)


@app.route('/')
def trainwreck():
    return send_file(os.path.join('images',
                                  random.choice(os.listdir('images'))))


if __name__ == '__main__':
    app.run(debug=True)
