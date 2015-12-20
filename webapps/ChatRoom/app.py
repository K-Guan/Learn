#!/usr/bin/env python
from jinja2 import escape
from flask import Flask, render_template, session
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode='eventlet')


@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('start chat', namespace='/chat')
def start_chat(message):
    if message['nickname'] != '':
        session['nickname'] = escape(message['nickname'])
    else:
        session['nickname'] = 'anonymous'

    emit('Joined', {'nickname': session['nickname']}, broadcast=True)


@socketio.on('chating', namespace='/chat')
def send_message(message):
    emit('Chat', {'data': escape(message['data']),
                  'nickname': session['nickname']},  broadcast=True)


if __name__ == '__main__':
    socketio.run(app, debug=True)
