'''
股票数据
http://data.eastmoney.com/stockdata/600031.html

'''
import logging
from . import get_bs4_html


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
