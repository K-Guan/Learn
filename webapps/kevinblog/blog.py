#!/usr/bin/env python3
import datetime
import mysql.connector
from bs4 import BeautifulSoup
from flask import Flask, render_template, redirect, url_for, request, g,\
    session, abort


app = Flask(__name__)

app.config.update(dict(
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))


@app.before_request
def before_request():
    g.conn = mysql.connector.connect(user='root',
                                     password='password',
                                     database='blog')
    g.cur = g.conn.cursor()


@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.conn.close()
        g.cur.close()


def gettime():
    f = '%B %d, %Y at %I:%S %p'
    t = datetime.datetime.now()
    return t.strftime(f)


def shortcut(string):
    soup = BeautifulSoup(string, "html.parser")
    text = soup.get_text()

    if len(text) > 180:
        return text[:180]+' ...'
    else:
        return text


def query_db(query, args=(), one=False):
    g.cur.execute(query, args)
    rv = [dict((g.cur.description[idx][0], value)
               for idx, value in enumerate(row)) for row in g.cur.fetchall()]
    return (rv[0] if rv else None) if one else rv


@app.route('/')
def index():
    return redirect(url_for('pages', page=1))


@app.route('/pages/<int:page>')
def pages(page):
    posts = query_db('select * from posts')
    return render_template('index.html', posts=posts, page=page)


@app.route('/post/<int:postid>')
def posts(postid):
    posts = query_db('select * from posts where ID = (%s)', [int(postid)])
    return render_template('posts.html', posts=posts)


@app.route('/add', methods=['GET', 'POST'])
def add_post():
    if not session.get('logged_in'):
        abort(401)

    if request.method == 'POST':
        g.cur.execute('insert into posts (date, title, body)' +
                      'values (%s, %s, %s)',
                      [gettime(), request.form['title'],
                       request.form['body'].replace('\r', '<br>')])

        g.conn.commit()
        return redirect(url_for('index'))

    else:
        return render_template('add.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            return 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            return 'Invalid password'
        else:
            session['logged_in'] = True
            return redirect(url_for('index'))
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('index'))

app.jinja_env.filters['shortcut'] = shortcut
if __name__ == '__main__':
    app.run(debug=True)
