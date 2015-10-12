#!/usr/bin/env python3
import os
import sqlite3
from flask import Flask, render_template, redirect, url_for, request, g, \
    make_response, abort

app = Flask(__name__)

DATABASE = 'sqlite.db'


@app.before_request
def before_request():
    g.db = sqlite3.connect(DATABASE)


@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()



@app.route('/', methods=['GET', 'POST'])
def add_entry():
    if request.method == 'POST':
        g.db.execute('insert into entries (code) values (?)',
                     [request.form['code']])

        g.db.commit()
        cur = g.db.execute('select mainid from entries where code is (?)',
                           [request.form['code']])

        for mainid in [row[0] for row in cur.fetchall()]:
            return redirect(url_for('show_entries', mainid=mainid))

    else:
        return render_template('index.html')


@app.route('/<int:mainid>')
def show_entries(mainid):
    cur = g.db.execute('select code from entries where mainid is (?)',
                           [mainid])

    entries = [dict(code=row[0]) for row in cur.fetchall()]
    if entries == []:
        abort(404)

    resp = make_response(render_template('show.html', entries=entries))
    resp.headers['Content-Type'] = 'text/plain; charset=utf-8'
    return resp



@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
