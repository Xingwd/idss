# -*- coding: UTF-8 -*-
from flask import Blueprint, request, jsonify, current_app
from main import db
from main.models.stock import IndexComponentSH50, IndexComponentHS300, Overview
from crawler.eastmoney.stock.index_component import get_sh50_component, get_hs300_component
from crawler.eastmoney.stock.data import get_code_hxtc
from main.stock_overview import upsert_overview

bp = Blueprint('stock_index_component', __name__)


def get_pagination(model, page, page_size):
    pagination = None
    data = {}
    # 对象属性：https://flask-sqlalchemy.palletsprojects.com/en/2.x/api/#flask_sqlalchemy.Pagination
    pagination = db.session.query(model, Overview).outerjoin(
        Overview, model.code == Overview.code).order_by(
        model.id).paginate(page=page, per_page=page_size, error_out=False)
    if pagination:
        items = []
        for i in pagination.items:
            item = {
                'id': i[0].id,
                'code': i[0].code,
                'name': None,
                'plate': None,
                'business_scope': None,
                'sync_time': i[0].sync_time.strftime('%Y-%m-%d %H:%M:%S')
            }
            if i[1]:
                item['name'] = i[1].name
                item['plate'] = i[1].plate
                item['business_scope'] = i[1].business_scope
            items.append(item)

        # data['items'] = [{'code': i[0].code, 'sync_time': i[0].sync_time.strftime('%Y-%m-%d %H:%M:%S')}
        #     for i in pagination.items]
        data['items'] = items
        data['page'] = pagination.page
        data['pages'] = pagination.pages
        data['per_page'] = pagination.per_page
        data['total'] = pagination.total
    return data


def update_components(components, model):
    if components:
        current_app.logger.info(f'更新数据表：{model.__tablename__}')
        db.session.execute(f'truncate table {model.__tablename__}')
        db.session.add_all([model(id=idx + 1, code=i['code']) for idx, i in enumerate(components)])
        db.session.commit()
        update_components_overview(components)
        return jsonify({'msg': 'Synchronization succeeded', 'status_code': 201}), 201
    else:
        return jsonify({'msg': 'Synchronization failed', 'status_code': 500}), 500


def update_components_overview(components):
    for i in components:
        hxtc = get_code_hxtc(current_app.config['CHROME_DRIVER'], i['code'])
        upsert_overview(hxtc)
    current_app.logger.info(f'本次共更新 {len(components)} 只股票的核心题材到数据库')


@bp.route('/sh50', methods=['GET'])
def get_sh50():
    page = request.args.get('page', 1, type=int)
    page_size = request.args.get('page_size', 15, type=int)
    data = get_pagination(IndexComponentSH50, page, page_size)
    return jsonify(data)


@bp.route('/sh50', methods=['PUT', 'POST'])
def put_or_post_sh50():
    return update_components(get_sh50_component(), IndexComponentSH50)


@bp.route('/hs300', methods=['GET'])
def get_hs300():
    page = request.args.get('page', 1, type=int)
    page_size = request.args.get('page_size', 15, type=int)
    data = get_pagination(IndexComponentHS300, page, page_size)
    return jsonify(data)


@bp.route('/hs300', methods=['PUT', 'POST'])
def put_or_post_hs300():
    return update_components(get_hs300_component(), IndexComponentHS300)
