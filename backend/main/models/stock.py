from datetime import datetime
from main import db


class Overview(db.Model):
    __tablename__ = 'overview'
    code = db.Column(db.String(20), primary_key=True, comment='股票代码')
    name = db.Column(db.String(50), comment='股票名称')

    def __repr__(self):
        return '<Stock {}[{}]>'.format(self.name, self.code)


class KLinesDay(db.Model):
    __tablename__ = 'klines_day'
    code = db.Column(db.String(20), primary_key=True, comment='股票代码')
    date = db.Column(db.String(10), primary_key=True, comment='交易日期')
    open = db.Column(db.Float, comment='开盘价')
    close = db.Column(db.Float, comment='收盘价')
    high = db.Column(db.Float, comment='最高价')
    low = db.Column(db.Float, comment='最低价')
    volume = db.Column(db.Integer, comment='成交量')
    amount = db.Column(db.Float, comment='成交额')
    amplitude = db.Column(db.String(8), comment='振幅')
    pct_chg = db.Column(db.String(8), comment='涨跌幅')
    chg = db.Column(db.Float, comment='涨跌额')
    turn = db.Column(db.String(8), comment='换手率')

    def __repr__(self):
        return '<Stock {} {}>'.format(self.code, self.date)


class IndexComponentSH50(db.Model):
    __tablename__ = 'index_compnent_sh50'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    code = db.Column(db.String(20))
    name = db.Column(db.String(50))
    sync_time = db.Column(db.DateTime, nullable=False, default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    def __repr__(self):
        return '<Stock {}[{}]>'.format(self.name, self.code)


class IndexComponentHS300(db.Model):
    __tablename__ = 'index_compnent_hs300'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    code = db.Column(db.String(20))
    name = db.Column(db.String(50))
    sync_time = db.Column(db.DateTime, nullable=False, default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    def __repr__(self):
        return '<Stock {}[{}]>'.format(self.name, self.code)

# schemas迁移工具
# https://docs.sqlalchemy.org/en/13/core/metadata.html#altering-schemas-through-migrations
