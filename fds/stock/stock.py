'''
获取股票数据
'''
import logging

from .data_source import eastmoney

logger = logging.getLogger('fds.stock')


class Stock:
    """
    股票数据
    """

    def __init__(self, data_source: str = 'eastmoney') -> None:
        if data_source == 'eastmoney':
            self.data_source = eastmoney.EastMoney()
        else:
            self.data_source = eastmoney.EastMoney()

    @property
    def shang_zheng_50(self):
        """
        上证50成分股
        """

    @property
    def hu_shen_300(self):
        """
        沪深300成分股
        """

    @property
    def stock_company_profile(self):
        """
        个股公司简介
        """

    @property
    def stock_concept_theme(self):
        """
        个股概念题材
        """
