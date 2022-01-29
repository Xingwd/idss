'''
股票数据源
'''
import logging
from .eastmoney import EastMoney


logger = logging.getLogger('fds.stock')


class Stock:
    """
    股票数据
    """

    def __init__(self, data_source: str = 'eastmoney') -> None:
        if data_source == 'eastmoney':
            self.data_source = EastMoney()
        else:
            self.data_source = EastMoney()

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
