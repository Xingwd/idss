'''
东方财富网数据源
'''
import logging
from fds.stock.data_source import DataSource
from fds.mixin.html import GetHtml


logger = logging.getLogger('fds.stock')
BASE_URL = 'https://data.eastmoney.com/'


class EastMoney(DataSource, GetHtml):
    """
    东方财富网数据源
    """

    def __init__(self) -> None:
        pass

    @property
    def shang_zheng_50(self):
        """
        上证50成分股
        """
        url = '50'
        return self.bs4_html(url)

    @property
    def hu_shen_300(self):
        """
        沪深300成分股
        """
        url = '300'
        return self.bs4_html(url)

    @property
    def stock_company_profile(self):
        """
        个股公司简介
        """
        url = 'cp'
        return self.bs4_html(url)

    @property
    def stock_concept_theme(self):
        """
        个股概念题材
        """
        url = 'ct'
        return self.bs4_html(url)

    # def stock(chrome_driver, code):
    #     url = f'http://data.eastmoney.com/stockdata/{code}.html'
    #     soup = get_bs4_html(chrome_driver, [url])[0]
    #     logging.info(f'正在分析{url}')
    #     name = soup.find(id='name').contents[0]
    #     tags = soup.find('div', 'hxtc-content').find_all('p')[:2]
    #     return {'code': code, 'name': name, 'plate': tags[0].contents[2], 'business_scope': tags[1].contents[2]}
