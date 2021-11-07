'''
东方财富网数据
'''
import logging
import requests
from fds.common import get_bs4_html

logger = logging.getLogger('fds.stock')

class EastMoney:
    def __init__(self) -> None:
        pass

    def get_index_component(self, pn=1, fields='f12,f14', **kwargs):
        params = '&'.join(['{}={}'.format(k, v) for k, v in kwargs.items()])
        url = f'http://push2.eastmoney.com/api/qt/clist/get?pn={pn}&fields={fields}&{params}'
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

    def get_codes_hxtc(chrome_driver, codes):
        urls = [f'http://data.eastmoney.com/stockdata/{code}.html' for code in codes]
        soups = get_bs4_html(chrome_driver, urls)
        for idx, soup in enumerate(soups):
            logging.info(f'正在分析{urls[idx]}')
            name = soup.find(id='name').contents[0]
            tags = soup.find('div', 'hxtc-content').find_all('p')[:2]
            yield {'code': codes[idx], 'name': name, 'plate': tags[0].contents[2], 'business_scope': tags[1].contents[2]}


    def get_code_hxtc(chrome_driver, code):
        url = f'http://data.eastmoney.com/stockdata/{code}.html'
        soup = get_bs4_html(chrome_driver, [url])[0]
        logging.info(f'正在分析{url}')
        name = soup.find(id='name').contents[0]
        tags = soup.find('div', 'hxtc-content').find_all('p')[:2]
        return {'code': code, 'name': name, 'plate': tags[0].contents[2], 'business_scope': tags[1].contents[2]}
