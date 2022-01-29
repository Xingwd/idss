'''
web相关工具类
'''
from selenium.webdriver import Chrome, ChromeOptions


class WebDriver:
    """
    获取WebDriver能力
    """

    def __init__(self) -> None:
        self.driver = self.get_chrome_driver()

    def __quit__(self) -> None:
        self.driver.quit()

    def get_chrome_driver(self) -> Chrome:
        """
        Chrome Driver

        Returns:
            Chrome: Chrome实例
        """
        chrome_options = ChromeOptions()
        # 启用静默模式，不打开浏览器窗口
        chrome_options.add_argument('headless')
        return Chrome(options=chrome_options)
