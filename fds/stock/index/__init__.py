'''
股票指数数据
'''
import logging
from .csindex import CSIndex

logger = logging.getLogger('fds.stock')


class Index:
    """
    股票指数数据
    """

    def __init__(self, data_source: str = 'csindex') -> None:
        if data_source == 'csindex':
            self.ds = CSIndex()
        else:
            self.ds = CSIndex()

    @property
    def shang_zheng_50(self):
        """
        上证50成分股
        """
        return self.ds.shang_zheng_50

    @property
    def hu_shen_300(self):
        """
        沪深300成分股
        """
        return self.ds.hu_shen_300
