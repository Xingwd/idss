# -*- coding: UTF-8 -*-
from flask import Flask, make_response, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
# from logging.config import dictConfig
from config import Config

db = SQLAlchemy()


def create_app(config=Config):

    # https://dormousehole.readthedocs.io/en/latest/logging.html#logging
    # dictConfig({
    #     'version': 1,
    #     'formatters': {'default': {
    #         'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    #     }},
    #     'handlers': {'wsgi': {
    #         'class': 'logging.StreamHandler',
    #         'stream': 'ext://flask.logging.wsgi_errors_stream',
    #         'formatter': 'default'
    #     }},
    #     'root': {
    #         'level': 'INFO',
    #         'handlers': ['wsgi']
    #     }
    # })

    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    CORS(app)

    # https://dormousehole.readthedocs.io/en/latest/api.html#flask.Flask.errorhandler
    # https://dormousehole.readthedocs.io/en/latest/errorhandling.html#error-handlers
    @app.errorhandler(404)
    def not_found(error):
        return make_response(jsonify({'msg': 'Not found', 'status_code': 404}), 404)

    @app.errorhandler(400)
    def bad_request(error):
        return make_response(jsonify({'msg': 'Bad request', 'status_code': 400}), 400)

    # 测试接口
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    # Blueprint
    from .stock_overview import bp as stock_overview_bp
    app.register_blueprint(stock_overview_bp, url_prefix='/api/stock/overview')
    from .stock_klines import bp as stock_klines_bp
    app.register_blueprint(stock_klines_bp, url_prefix='/api/stock/klines')
    from .stock_index_component import bp as stock_index_component_bp
    app.register_blueprint(stock_index_component_bp, url_prefix='/api/stock/index_component')
    from .stock_choice import bp as stock_choice_bp
    app.register_blueprint(stock_choice_bp, url_prefix='/api/stock/choice')

    return app
