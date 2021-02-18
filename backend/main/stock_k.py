# -*- coding: UTF-8 -*-
import baostock as bs
from flask import Blueprint, request, jsonify
from main.db import get_db

bp = Blueprint('stock_k', __name__)

cols = ','.join(['code', 'date', 'open', 'high', 'low', 'close', 'preclose', 'volume', 'amount', 'adjustflag', 'turn',
                 'tradestatus', 'pctChg', 'peTTM', 'psTTM', 'pcfNcfTTM', 'pbMRQ', 'isST'])


def update_stock_history(code, start_date, end_date, cols=cols, frequency='d', adjustflag='3'):
    # 登录baostock
    bs.login()
    # 获取沪深A股历史K线数据
    rs = bs.query_history_k_data_plus(
            code, cols, start_date=start_date, end_date=end_date,
            frequency=frequency, adjustflag=adjustflag)
    # 获取数据库连接
    conn = get_db()
    cursor = conn.cursor()
    sql = 'replace into stocks({}) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'.format(cols)
    data = []
    while (rs.error_code == '0') & rs.next():
        row = rs.get_row_data()
        data.append(row)
    cursor.executemany(sql, data)
    conn.commit()
    # 登出baostock
    bs.logout()


@bp.route('', methods=['GET'])
def get_stocks():
    page = request.args.get('page', 1, type=int)
    page_size = request.args.get('page_size', 30, type=int)
    data = {}
    cursor = get_db().cursor()
    sql = 'select * from stocks limit %s,%s'
    cursor.execute(sql, ((page - 1) * page_size, page_size))
    data = cursor.fetchall()
    return jsonify(data)


@bp.route('/<code>', methods=['GET'])
def get_stock(code):
    data = {}
    cursor = get_db().cursor()
    sql = 'select * from stocks where code=%s'
    cursor.execute(sql, code)
    data = cursor.fetchall()
    return jsonify(data)


@bp.route('/<code>', methods=['POST'])
def update_stock(code):
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    # TODO: 参数检查
    update_stock_history(code, start_date, end_date)
    return jsonify({'msg': 'Updated success', 'status_code': 201}), 201


@bp.route('', methods=['POST'])
def update_stocks():
    codes = request.args.get('codes')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    for code in codes.split(','):
        update_stock_history(code, start_date, end_date)
    return jsonify({'msg': 'Updated success', 'status_code': 201}), 201
