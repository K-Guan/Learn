#!/usr/bin/env python3
import os
import sqlite3
from flask import Flask, render_template, redirect, url_for, request, g

app = Flask(__name__)

DATABASE = 'sqlite.db'


@app.before_request
def before_request():
    g.db = sqlite3.connect(DATABASE)

@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()



@app.route('/')
def show_entries():
    cur = g.db.execute('select * from entries')
    entries = [dict(ID=row[0],
                    title=row[1],
                    body=row[2]) for row in cur.fetchall()]

    return render_template('index.html', entries=entries)


@app.route('/add', methods=['GET', 'POST'])
def add_entry():
    if request.method == 'POST':
        g.db.execute('insert into entries (title, body) values (?, ?)',
                     [request.form['title'], request.form['body']])

        g.db.commit()
        return redirect(url_for('show_entries'))

    else:
        return render_template('add.html')


@app.route('/remove', methods=['GET', 'POST'])
def remove_entry():
    if request.method == 'POST':
        g.db.execute('delete from entries where id=(?)',
                     [request.form['id']])

        g.db.commit()

    cur = g.db.execute('select * from entries')
    entries = [dict(ID=row[0]) for row in cur.fetchall()]
    return render_template('remove.html', entries=entries)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
