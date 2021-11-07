'''
公用模块
'''
import logging

from bs4 import BeautifulSoup
from selenium.webdriver import Chrome, ChromeOptions

logger = logging.getLogger('fds.stock')

def get_bs4_html(chrome_driver, urls):
    """[summary]

    Args:
        chrome_driver ([type]): [description]
        urls ([type]): [description]

    Yields:
        [type]: [description]
    """
    # chromedriver下载地址 https://chromedriver.storage.googleapis.com/index.html
    # chromedriver版本需要和本地chrome浏览器版本保持大版本一致。
    chrome_options = ChromeOptions()
    chrome_options.add_argument('headless')  # 启用静默模式，不打开浏览器窗口
    with Chrome(executable_path=chrome_driver, options=chrome_options) as driver:
        for url in urls:
            logger.info('正在获取%s', url)
            driver.get(url)
            html = driver.page_source
            yield BeautifulSoup(html, 'lxml')
