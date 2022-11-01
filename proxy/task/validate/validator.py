import sys

import requests

sys.path.append('/Users/sonhodor/code/py/7_parcers/mal')

from utility.sleep import Sleeper

URL = 'https://myanimelist.net/'
TIMEOUT = 2.5


def test_proxy(sleeper, proxy: str):
    s = requests.Session()
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45. 0'}
    proxies = {"https" : "http://" + proxy}
    spaces = ' '*(25 - len(proxy))

    try:
        html = s.get(URL, headers=header, proxies=proxies, timeout=TIMEOUT).text
        print(f'{proxy + spaces} is ok, len of html = {len(html)}')
        return sleeper.time_since_last_time()
    except requests.HTTPError:
        print(f'{proxy + spaces} timeout')
    except requests.ConnectTimeout:
        print(f'{proxy+ spaces} is http')

