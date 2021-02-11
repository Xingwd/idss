# -*- coding: UTF-8 -*-
import baostock as bs
from flask import Blueprint, request, jsonify
from main.db import get_db

bp = Blueprint('xuangu', __name__)


# 另一种api写法：https://dormousehole.readthedocs.io/en/latest/views.html#api
@bp.route('/hs300/stocks', methods=['GET'])
def get_hs300_stocks():
    page = request.args.get('page', 1, type=int)
    page_size = request.args.get('page_size', 30, type=int)
    data = []
    cursor = get_db().cursor()
    sql = 'select * from hs300_stocks limit %s,%s'
    cursor.execute(sql, ((page - 1) * page_size, page_size))
    data = cursor.fetchall()
    return jsonify(data)


@bp.route('/hs300/stocks', methods=['POST'])
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
