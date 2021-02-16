# -*- coding: UTF-8 -*-
import baostock as bs
from flask import Blueprint, request, jsonify
from main.db import get_db

bp = Blueprint('xuangu', __name__)
TABLE_NAME = 'hs300_stocks'


# 另一种api写法：https://dormousehole.readthedocs.io/en/latest/views.html#api
@bp.route('/hs300', methods=['GET'])
def get_hs300_stocks():
    page = request.args.get('page', 1, type=int)
    page_size = request.args.get('page_size', 30, type=int)
    data = {}
    cursor = get_db().cursor()
    total = 'select count(*) as total from {}'.format(TABLE_NAME)
    cursor.execute(total)
    data['total'] = cursor.fetchone()['total']
    if page_size == -1:
        page = 1
        page_size = data['total']
    records = 'select * from {} limit %s,%s'.format(TABLE_NAME)
    cursor.execute(records, ((page - 1) * page_size, page_size))
    data['records'] = cursor.fetchall()
    return jsonify(data)


@bp.route('/hs300', methods=['POST'])
def update_hs300_stocks():
    # 登录baostock
    bs.login()
    # 获取沪深300成分股
    rs = bs.query_hs300_stocks()
    # 获取数据库连接
    conn = get_db()
    cursor = conn.cursor()
    sql = 'replace into hs300_stocks(id,code,name,update_date) values(%s,%s,%s,%s)'
    id = 1
    data = []
    while (rs.error_code == '0') & rs.next():
        row = rs.get_row_data()
        data.append((id, row[1], row[2], row[0]))
        id += 1
    cursor.executemany(sql, data)
    conn.commit()
    # 登出baostock
    bs.logout()
    return jsonify({'msg': 'Updated success', 'status_code': 201}), 201
