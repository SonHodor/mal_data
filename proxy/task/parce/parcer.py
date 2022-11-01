from typing import List
from datetime import date 

import psycopg2
import requests
from bs4 import BeautifulSoup

from utility.creds import credentials as creds

PROXY_URL = 'https://free-proxy-list.net/'

PG_CONFIG_TEST = {**creds['pg']}


def get_new_proxys_list():
    s = requests.Session()
    s.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45. 0'})

    html = s.get(PROXY_URL).text

    soup = BeautifulSoup(html, "html.parser")

    proxy_text = soup.find("textarea", attrs={"class": "form-control"}).text
    proxy_list = proxy_text.replace('\n\n', '\n').split('\n')[3:-1]

    return proxy_list


def write_proxy_list_to_pg(new_proxys: List[str], pg_config=PG_CONFIG_TEST) -> None:
    import psycopg2.extras as ex

    tday = str(date.today())
    tuple_values = [
        (proxy, tday) for proxy in new_proxys
    ]

    with psycopg2.connect(**pg_config) as conn:
        with conn.cursor() as cur:

            ex.execute_values(
                cur,
                'INSERT INTO other.proxy_list (ip, processed_dt) VALUES %s ON CONFLICT DO NOTHING',
                tuple_values
            )
        conn.commit()
        print(f'commited {len(tuple_values)} values to other.proxys table')

