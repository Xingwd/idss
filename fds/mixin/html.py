'''
从网页获取html并处理
'''
from selenium.webdriver import Chrome, ChromeOptions
from bs4 import BeautifulSoup


class GetHtml:
    """
    获取Html
    """

    def _get_html(self, url: str) -> str:
        """
        访问url，获取网页html字符串

        Args:
            url (str): 网页地址

        Returns:
            str: html字符串
        """
        chrome_options = ChromeOptions()
        chrome_options.add_argument('headless')  # 启用静默模式，不打开浏览器窗口
        with Chrome(options=chrome_options) as driver:
            driver.get(url)
            html = driver.page_source
        return html

    def bs4_html(self, url: str) -> BeautifulSoup:
        """
        使用BeautifulSoup解析html字符串

        Args:
            url (str): 网页地址

        Returns:
            BeautifulSoup: html的BeautifulSoup实例
        """
        return BeautifulSoup(self._get_html(url), 'lxml')
