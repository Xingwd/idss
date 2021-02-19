'''
股票k线数据

经过分析东方财富网站，发现获取股票数据的接口如下：
http://push2his.eastmoney.com/api/qt/stock/kline/get?secid=1.600028&klt=101&fqt=0&beg=0&end=20500101&fields1=f1,f2,f3,f4,f5,f6&fields2=f51,f52,f53,f54,f55,f56,f57,f58,f59,f60,f61
url参数说明
secid: 股票代码。上证股票添加前缀1.，深证股票添加前缀0.。例如 1.600028，0.000333
klt: 周期。101=日线，102=周线，103=月线
fqt: 复权。0=不复权，1=前复权，2=后复权。

beg: 开始日期。格式示例20210101
end: 结束日期。格式示例20210118
beg=0&end=20500000，获取股票全部历史数据。
beg=20210118&end20210118，表示获取2021年1月1日的数据。

fields1说明
f1=code(代码),f2=market,f3=name(名称),f4=decimal(精度),f5=dktotal,f6=preKPrice,f7=prePrice,f8=qtMiscType,f9,f10,f11,f12,f13
fields2说明
f51=交易日期,f52=开盘价,f53=收盘价,f54=最高价,f55=最低价,f56=成交量,f57=成交额,f58=振幅,f59=涨跌幅,f60=涨跌额,f61=换手率
'''

import requests


# 获取k线数据
def get_klines(secid, klt=101, fqt=0, beg=0, end=20500000, fields1='f1,f2,f3,f4,f5,f6,f7,f8',
               fields2='f51,f52,f53,f54,f55,f56,f57,f58,f59,f60,f61'):
    params = {
        'secid': secid,
        'klt': klt,
        'fqt': fqt,
        'beg': beg,
        'end': end,
        'fields1': fields1,
        'fields2': fields2
    }
    url = 'http://push2his.eastmoney.com/api/qt/stock/kline/get?{}'.format(
        '&'.join(['{}={}'.format(k, v) for k, v in params.items()]))
    r = requests.get(url)
    data = r.json()['data']
    return data


# 获取日k数据
def get_klines_day(secid, fqt=0, beg=0, end=20500000, fields1='f1',
                   fields2='f51,f52,f53,f54,f55,f56,f57,f58,f59,f60,f61'):
    return get_klines(secid, fqt=fqt, beg=beg, end=end, fields1=fields1, fields2=fields2)
