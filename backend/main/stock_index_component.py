# -*- coding: UTF-8 -*-
from flask import Blueprint, request, jsonify
from main.db import select_from_db_pagination, upsert_to_db
from crawler.eastmoney.stock.index_component import (
    get_sh50_component, get_hs300_component)

bp = Blueprint('stock_index_component', __name__)
SH50_COMPONENT = 'stock_index_component_sh50'
HS300_COMPONENT = 'stock_index_component_hs300'
cols = 'code,name'


@bp.route('/sh50', methods=['GET'])
def get_sh50():
    page = request.args.get('page', 1, type=int)
    page_size = request.args.get('page_size', 30, type=int)
    data = select_from_db_pagination(page, page_size, SH50_COMPONENT)
    return jsonify(data)


@bp.route('/sh50', methods=['POST'])
def post_sh50():
    components = get_sh50_component()
    if components:
        upsert_to_db(components, SH50_COMPONENT, cols)
        return jsonify({'msg': 'Synchronization succeeded', 'status_code': 201}), 201
    else:
        return jsonify({'msg': 'Synchronization failed', 'status_code': 500}), 500


@bp.route('/hs300', methods=['GET'])
def get_hs300():
    page = request.args.get('page', 1, type=int)
    page_size = request.args.get('page_size', 30, type=int)
    data = select_from_db_pagination(page, page_size, HS300_COMPONENT)
    return jsonify(data)


@bp.route('/hs300', methods=['POST'])
def post_hs300():
    components = get_hs300_component()
    if components:
        upsert_to_db(components, HS300_COMPONENT, cols)
        return jsonify({'msg': 'Synchronization succeeded', 'status_code': 201}), 201
    else:
        return jsonify({'msg': 'Synchronization failed', 'status_code': 500}), 500
