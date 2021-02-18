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


def select_from_db_pagination(page, page_size, table):
    data = {}
    cursor = get_db().cursor()
    total = 'select count(*) as total from {}'.format(table)
    cursor.execute(total)
    data['total'] = cursor.fetchone()['total']
    if page_size == -1:
        page = 1
        page_size = data['total']
    records = 'select * from {} limit %s,%s'.format(table)
    cursor.execute(records, ((page - 1) * page_size, page_size))
    data['records'] = cursor.fetchall()
    return data


def upsert_to_db(values, table, cols):
    conn = get_db()
    cursor = conn.cursor()
    place = ','.join(['%s' for i in cols.split(',')])
    sql = 'replace into {}({}) values({})'.format(table, cols, place)
    data = []
    for i in values:
        data.append((i['code'], i['name']))
    cursor.executemany(sql, data)
    conn.commit()
