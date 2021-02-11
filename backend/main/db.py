import pymysql
from flask import g


def get_db():
    if 'db' not in g:
        g.db = pymysql.connect(host='localhost',
                               user='xingweidong',
                               password='xingweidong&123',
                               database='seer',
                               cursorclass=pymysql.cursors.DictCursor)
    return g.db


def close_db():
    db = g.pop('db', None)
    if db is not None:
        db.close()

