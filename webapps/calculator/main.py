#!/usr/bin/env python3
from flask import Flask, flash, redirect, render_template, \
     request, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        number1 = int(request.form['number1'])
        number2 = int(request.form['number2'])
        finish = number1 * number2

        return render_template('finish.html',
                               number1=number1,
                               number2=number2,
                               finish=finish)
    else:
        return render_template('index.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html')

@app.errorhandler(500)
def wrong_input(error):
    return redirect(url_for('main'))

@app.errorhandler(502)
def wrong_input(error):
    return redirect(url_for('main'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
