import sys

import psycopg2
import requests

sys.path.append('/Users/sonhodor/code/py/7_parcers/mal')

from utility.sleep import Sleeper
from utility.creds import credentials as creds

URL = 'https://myanimelist.net/'
TIMEOUT = 5

PG_CONFIG_TEST = {**creds['pg']}


def test_proxy(sleeper: Sleeper, proxy: str):
    s = requests.Session()
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45. 0'}
    proxies = {
        "https" : "http://" + proxy 
    }
    sleeper.time_since_last_time()
    try:
        s.get(URL, headers=header, proxies=proxies, timeout=TIMEOUT).text
        return [proxy, 'nice', sleeper.time_since_last_time(True)]
    except requests.ConnectTimeout:
        return [proxy, 'ConnectTimeout', sleeper.time_since_last_time(True)]
    except requests.ReadTimeout:
        return [proxy, 'ReadTimeout', sleeper.time_since_last_time(True)]
    except requests.ConnectionError:
        return [proxy, 'ConnectionError', sleeper.time_since_last_time(True)]
    except requests.HTTPError:
        return [proxy, 'HTTPError', sleeper.time_since_last_time(True)]


def validate():
    sleeper = Sleeper(TIMEOUT)
    with psycopg2.connect(**PG_CONFIG_TEST) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT ip FROM other.proxy_list")
            proxy_list_to_test = [i[0] for i in cur.fetchall()]

    for proxy in proxy_list_to_test:
        status = test_proxy(sleeper, proxy)
        print(*status[::-1], sep='\t')

if __name__ == '__main__':
    validate()

