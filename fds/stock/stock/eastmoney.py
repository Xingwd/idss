'''
东方财富网数据源
'''
import logging
from fds.mixin.web import WebDriver
from .source import StockSource


logger = logging.getLogger('fds.stock')
BASE_URL = 'https://data.eastmoney.com/'


class EastMoney(StockSource, WebDriver):
    """
    东方财富网数据源
    """

    def __init__(self) -> None:
        pass

    @property
    def stock_company_profile(self):
        """
        个股公司简介
        """
        pass

    @property
    def stock_concept_theme(self):
        """
        个股概念题材
        """
        pass
