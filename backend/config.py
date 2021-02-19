# -*- coding: UTF-8 -*-

# https://dormousehole.readthedocs.io/en/latest/config.html#config
class Config(object):
    SECRET_KEY = 'e9d37baf44de4b11a76159c50820468f'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://xingweidong:xingweidong&123@localhost/seer_stock'  # 股票数据库，默认
    SQLALCHEMY_BINDS = {
        'fund':        'mysql+pymysql://xingweidong:xingweidong&123@localhost/seer_fund'  # 基金数据库
    }
