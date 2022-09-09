
import requests

from ..parcers.sleep import Sleeper

URL = 'https://myanimelist.net/'
TIMEOUT = 10


def test_proxy(sleeper, proxy: str):
    s = requests.Session()
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45. 0'}
    proxies = {
        "https" : "http://" + proxy 
    }

    try:
        s.get(URL, headers=header, proxies=proxies, timeout=TIMEOUT-1).text
        print(proxy)
    except Exception:
        if sleeper.sleep() < 1:
            print(f'{proxy} timeout')
        else:
            print(f'{proxy} not https')

def main():
    sleeper = Sleeper(TIMEOUT)
    with open('data/proxy_list.csv', 'r', encoding='utf-8') as f:
        proxy_list_to_test = [line[:-1] for line in f.readlines()]
    
    for proxy in proxy_list_to_test:
        test_proxy(sleeper, proxy)

if __name__ == '__main__':
    main()

