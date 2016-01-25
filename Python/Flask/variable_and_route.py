#!/usr/bin/env python3
from flask import Flask
app = Flask(__name__)

@app.route('/')
def main():
    return '<h2>Try access to  "/number1/number2"  \
        for some interesting things</h2>'

@app.route('/<int:number1>/<int:number2>')
def plus(number1, number2):
    text = """<h1><font color="red">
    "number1({0}) * number2({1})" = "{2}"
    </font></h1>""".format(number1, number2, number1 * number2)

    return text


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
