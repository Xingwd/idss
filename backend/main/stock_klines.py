# -*- coding: UTF-8 -*-
from datetime import datetime, timedelta
from flask import Blueprint, request, jsonify
from main import db
from main.models.stock import KLinesDay
from crawler.eastmoney.stock.klines import get_klines_day

bp = Blueprint('stock_klines', __name__)


@bp.route('/day/<code>', methods=['GET'])
def get_day_klines(code):
    today = datetime.today()
    last_month_date = today - timedelta(30)
    begin_date = request.args.get('begin_date', last_month_date.strftime('%Y-%m-%d'))
    end_date = request.args.get('end_date', today.strftime('%Y-%m-%d'))
    klines_day = KLinesDay.query.filter(
        KLinesDay.code == code and KLinesDay.date >= begin_date and KLinesDay.date <= end_date).order_by(
        KLinesDay.date).all()
    data = {'code': code, 'klines': []}
    for i in klines_day:
        data['klines'].append({
            'date': i.date, 'open': i.open, 'close': i.close, 'high': i.high, 'low': i.low, 'volume': i.volume,
            'amount': i.amount, 'amplitude': i.amplitude, 'pct_chg': i.pct_chg, 'chg': i.chg, 'turn': i.turn})
    return jsonify(data)


@bp.route('/day/<code>', methods=['POST'])
def post_day_klines(code):
    begin_date = request.json.get('begin_date', 0)
    end_date = request.json.get('end_date', 20500000)
    data = get_klines_day(code, beg=begin_date, end=end_date)
    if data:
        c = 0
        records = []
        for i in data['klines']:
            if KLinesDay.query.filter(KLinesDay.code == code and KLinesDay.date == i['date']).first():
                pass
            else:
                i = i.split(',')
                records.append(
                    KLinesDay(code=code, date=i[0], open=i[1], close=i[2], high=i[3], low=i[4], volume=i[5],
                              amount=i[6], amplitude=i[7], pct_chg=i[8], chg=i[9], turn=i[10]))
                c += 1
                if c >= 5000:
                    db.session.add_all(records)
                    db.session.commit()
                    c = 0
        if c > 0:
            db.session.add_all(records)
            db.session.commit()
        return jsonify({'msg': 'Synchronization succeeded', 'status_code': 201}), 201
    else:
        return jsonify({'msg': 'Synchronization failed', 'status_code': 500}), 500
