from collections import defaultdict
import json
from typing import List

import requests
from bs4 import BeautifulSoup

url = 'https://free-proxy-list.net/'

def get_proxy_list():
    s = requests.Session()
    s.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45. 0'})

    html = s.get(url).text

    soup = BeautifulSoup(html, "html.parser")

    proxy_text = soup.find("textarea", attrs={"class": "form-control"}).text
    proxy_list = proxy_text.replace('\n\n', '\n').split('\n')[3:-1]

    return proxy_list

def write_list_to_csv(arr: list):
    with open('data/proxy_list.csv', 'w', encoding='utf-8') as f:
        for elem in arr:
            f.write(elem + '\n')

if __name__ == '__main__':
    write_list_to_csv(get_proxy_list())