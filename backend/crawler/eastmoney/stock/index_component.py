'''
指数成分
http://quote.eastmoney.com/center/gridlist.html#index_components

经过分析东方财富网站，发现获取指数成分数据的接口如下：
http://push2.eastmoney.com/api/qt/clist/get?pn=1&pz=20&po=1&np=1&fltt=2&invt=2&fid=f3&fs=b:BK0611+f:!50&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152,f45
url参数说明
pn=分页,pz=分页大小,po,np,fltt,invt,fid=指定排序列,fs=指数代号(分析网站获取),fields=数据域
fields说明
f1,f2=最新价,f3=涨跌幅,f4=涨跌额,f5=成交量(手),f6=成交额,f7=振幅,f8=换手率,f9=市盈率(动态),f10=量比,f12=代码,f13,
f14=名称,f15=最高,f16=最低,f17=今开,f18=昨收,f20,f21,f23=市净率,f24,f25,f22,f11,f62,f128,f136,f115,f152,f45
'''

import requests


# 获取新浪财经指数最新成分股
def get_index_component(pn=1, fields='f12,f14', **kwargs):
    url = 'http://push2.eastmoney.com/api/qt/clist/get?pn={}&fields={}&{}'.format(
        pn, fields, '&'.join(['{}={}'.format(k, v) for k, v in kwargs.items()]))
    r = requests.get(url)
    data = r.json()['data']['diff']
    components = []
    for v in data.values():
        item = {}
        for k, v in v.items():
            if k == 'f12':
                item['code'] = v
            elif k == 'f14':
                item['name'] = v
            else:
                item[k] = v
        components.append(item)
    return components


# 获取上证50指数最新成分股
def get_sh50_component():
    return get_index_component(pz=50, fs='b:BK0611+f:!50')


# 获取沪深300指数成分股
def get_hs300_component():
    return get_index_component(pz=300, fs='b:BK0500+f:!50')
