#!/usr/bin/env python3
import mysql.connector

conn = mysql.connector.connect(user='root', password='password')
conn.autocommit = True  # set autocommit, then we don't need conn.commit()

cursor = conn.cursor()

# a good function that can simply get data from database as dict object
def query_db(query, args=()):
    cursor.execute(query, args)
    rv = [dict((cursor.description[idx][0], value)
               for idx, value in enumerate(row)) for row in cursor.fetchall()]

    return rv if rv else None

# create a database(if not exists), then use it
cursor.execute('create database if not exists test')
conn.database = 'test'


# let's create a new table(drop the exists) and insert some data into it
cursor.execute('drop table if exists users')
cursor.execute('create table users(uid int auto_increment '
               'primary key, name text)')

cursor.execute('insert into users(name) values(%s)', ['Bob'])
cursor.execute('insert into users(name) values(%s)', ['Kevin'])
cursor.execute('insert into users(name, uid) values(%s, %s)', ['John', '20'])
cursor.execute('insert into users(uid, name) values(%s, %s)', ['50', 'root'])

# oops, seems like that I made a mistake
cursor.execute('update users set name=%s where uid=%s', ['Kevin', '1'])
cursor.execute('update users set name=%s where uid=%s', ['Bob', '2'])

# note that if we didn't set conn.autocommit, then we MUST run this function
## conn.commit()

# okay, let's check the data in users table
users = query_db('select * from users where uid < %s', ['45'])
__import__('pprint').pprint(users)


# because this is a test database, let's drop it!
cursor.execute('drop table users')

# check if there is nothing in that database, then drop it
cursor.execute('select count(*) from information_schema.tables '
               'where table_schema=%s', ['test'])

if cursor.fetchall()[0][0] == 0:
    cursor.execute('drop database test')


# we done, let's close the connection
conn.close()
cursor.close()
