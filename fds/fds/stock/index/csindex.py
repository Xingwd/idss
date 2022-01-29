'''
中证指数
https://www.csindex.com.cn/#/
'''
import logging
import pandas as pd
from fds.mixin.web import WebDriver
from .source import IndexSource


logger = logging.getLogger('fds.stock')


class CSIndex(IndexSource, WebDriver):
    """
    中证指数
    """

    def __init__(self) -> None:
        super().__init__()

    def __quit__(self) -> None:
        return super().__quit__()

    def get_index_component(self, index_code):
        url = f'https://www.csindex.com.cn/#/indices/family/detail?indexCode={index_code}'
        self.driver.get(url)
        elem = self.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/div[2]/div/div[2]/div/div[1]/div[2]/div[2]/div[3]/a')
        dl_url = elem.get_property('href')
        df = pd.read_excel(dl_url, usecols=[4, 5, 9], names=[
                           'code', 'name', 'weight'], dtype={'code': str})
        # df = pd.read_excel(dl_url, dtype={'code': str})
        return df

    @property
    def shang_zheng_50(self):
        """
        上证50成分股
        """
        return self.get_index_component('000016')

    @property
    def hu_shen_300(self):
        """
        沪深300成分股
        """
        return self.get_index_component('000300')
