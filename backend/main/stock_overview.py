# -*- coding: UTF-8 -*-
from flask import Blueprint, request, jsonify, current_app
from main import db
from main.models.stock import Overview
from crawler.eastmoney.stock.data import get_code_hxtc

bp = Blueprint('stock_overview', __name__)


def get_pagination(model, page, page_size):
    pagination = None
    data = {}
    pagination = model.query.order_by(model.code).paginate(
        page=page, per_page=page_size, error_out=False)
    if pagination:
        # 对象属性：https://flask-sqlalchemy.palletsprojects.com/en/2.x/api/#flask_sqlalchemy.Pagination
        data['items'] = [{'code': i.code, 'name': i.name, 'plate': i.plate, 'business_scope': i.business_scope}
                         for i in pagination.items]
        data['page'] = pagination.page
        data['pages'] = pagination.pages
        data['per_page'] = pagination.per_page
        data['total'] = pagination.total
    return data


@bp.route('/', methods=['GET'])
def get_overview_list():
    page = request.args.get('page', 1, type=int)
    page_size = request.args.get('page_size', 15, type=int)
    data = get_pagination(Overview, page, page_size)
    return jsonify(data)


@bp.route('/<code>', methods=['GET'])
def get_overview(code):
    overview = Overview.query.filter(Overview.code == code).all()
    return jsonify(overview)


def upsert_overview(data):
    code = data['code']
    name = data.get('name')
    plate = data.get('plate')
    business_scope = data.get('business_scope')
    current_app.logger.info(f'Upsert <{name}({code})> 的核心题材')
    overview = Overview.query.filter_by(code=code).first()
    if overview:
        overview.name = name
        overview.plate = plate
        overview.business_scope = business_scope
    else:
        overview = Overview(code=code, name=name, plate=plate, business_scope=business_scope)
        db.session.add(overview)
    db.session.commit()


@bp.route('/<code>', methods=['POST', 'PUT'])
def post_or_put_overview(code):
    data = get_code_hxtc(current_app.config['CHROME_DRIVER'], code)
    if data:
        upsert_overview(data)
        return jsonify({'msg': 'Synchronization succeeded', 'status_code': 201}), 201
    else:
        return jsonify({'msg': 'Synchronization failed', 'status_code': 500}), 500
