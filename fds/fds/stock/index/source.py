'''
股票指数数据源
'''
from abc import ABC, abstractmethod


class IndexSource(ABC):
    """
    股票指数数据源基类
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
