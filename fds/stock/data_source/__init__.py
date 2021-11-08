'''
股票数据源
'''
from abc import ABC, abstractmethod


class DataSource(ABC):
    """
    股票数据源基类
    定义每个数据源必须实现的方法
    """

    @property
    @abstractmethod
    def shang_zheng_50(self):
        """
        上证50成分股
        """

    @property
    @abstractmethod
    def hu_shen_300(self):
        """
        沪深300成分股
        """

    @property
    @abstractmethod
    def stock_company_profile(self):
        """
        个股公司简介
        """

    @property
    @abstractmethod
    def stock_concept_theme(self):
        """
        个股概念题材
        """
