'''
股票数据
http://data.eastmoney.com/stockdata/600031.html

'''

from selenium.webdriver import Chrome, ChromeOptions
from bs4 import BeautifulSoup


# chromedriver下载地址 https://chromedriver.storage.googleapis.com/index.html
# chromedriver版本需要和本地chrome浏览器版本保持大版本一致。
chrome_driver = '/Users/xingweidong/envs/selenium/webdriver/chrome/88.0.4324.96/chromedriver'
chrome_options = ChromeOptions()
chrome_options.add_argument('headless')  # 启用静默模式，不打开浏览器窗口
url = 'http://data.eastmoney.com/stockdata/{}.html'.format('600031')
with Chrome(executable_path=chrome_driver, options=chrome_options) as driver:
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    tags = soup.find('div', 'hxtc-content').find_all('p')
    for p in tags:
        print(p.b)
