# -*- coding: UTF-8 -*-
from datetime import datetime
from flask import Blueprint, request, jsonify
from main import db
from main.models.stock import IndexComponentSH50, IndexComponentHS300
from crawler.eastmoney.stock.index_component import (
    get_sh50_component, get_hs300_component)

bp = Blueprint('stock_index_component', __name__)


def get_pagination(model, page, page_size):
    pagination = None
    data = {}
    pagination = model.query.order_by(model.id).paginate(
        page=page, per_page=page_size, error_out=False)
    if pagination:
        # 对象属性：https://flask-sqlalchemy.palletsprojects.com/en/2.x/api/#flask_sqlalchemy.Pagination
        data['items'] = [
            {'id': i.id, 'code': i.code, 'name': i.name, 'sync_time': i.sync_time.strftime('%Y-%m-%d %H:%M:%S')}
            for i in pagination.items]
        data['page'] = pagination.page
        data['pages'] = pagination.pages
        data['per_page'] = pagination.per_page
        data['total'] = pagination.total
        print(data['items'])
    return data


def update(components, model):
    if components:
        db.session.execute('truncate table {}'.format(model.__tablename__))
        db.session.add_all([model(id=idx + 1, code=i['code'], name=i['name']) for idx, i in enumerate(components)])
        db.session.commit()
        return jsonify({'msg': 'Synchronization succeeded', 'status_code': 201}), 201
    else:
        return jsonify({'msg': 'Synchronization failed', 'status_code': 500}), 500


@bp.route('/sh50', methods=['GET'])
def get_sh50():
    page = request.args.get('page', 1, type=int)
    page_size = request.args.get('page_size', 30, type=int)
    data = get_pagination(IndexComponentSH50, page, page_size)
    return jsonify(data)


@bp.route('/sh50', methods=['POST'])
def post_sh50():
    return update(get_sh50_component(), IndexComponentSH50)


@bp.route('/hs300', methods=['GET'])
def get_hs300():
    page = request.args.get('page', 1, type=int)
    page_size = request.args.get('page_size', 30, type=int)
    data = get_pagination(IndexComponentHS300, page, page_size)
    return jsonify(data)


@bp.route('/hs300', methods=['POST'])
def post_hs300():
    return update(get_hs300_component(), IndexComponentHS300)
