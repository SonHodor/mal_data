from time import sleep, time
from typing import List

import requests
from bs4 import BeautifulSoup

from sleep import Sleeper


ALPHANUMS = 'abcdefghijklmnopqrstuvwxyz0123456789-_'
SECONDS_TO_SLEEP = 1

sleeper = Sleeper(SECONDS_TO_SLEEP)

def get_users_from_url(s: requests.Session, url: str) -> List[str]:
    html = s.get(url).text
    soup = BeautifulSoup(html, "html.parser")

    users = soup.find_all("td", attrs={"class": "borderClass"})

    links = [user.find_all("a")[0]['href'] for user in users]
    nicks = [link.split('/')[-1] for link in links]

    users_total = int(url.split('=')[-1])
    iterations = users_total // 24
    current_combination = url.split('&')[-2][-3:]
    print(f"{current_combination}\t{iterations}\t{users_total}\t\t{url}")

    return nicks


def iterate_url(url: str) -> str:
    next_num = int(url.split('=')[-1]) + 24
    new_url = '='.join(url.split('=')[:-1]) + '=' + str(next_num)

    return new_url


def write_users(combination: str, users_on_page: str) -> None:
    with open(f'data/users_raw/{combination}.csv', 'a', encoding='utf-8') as f:
        f.write(','.join(users_on_page) + '\n')


def write_iter_time_to_log(iter_time: float) -> None:
    with open('./logs/iteration_time.log', 'a', encoding='utf-8') as f:
        f.write(str(iter_time) + '\n')


def pagination_write(s: requests.Session, combination: str, url: str) -> None:
    global sleeper

    while True:
        users_on_page = get_users_from_url(s, url)

        if len(users_on_page) == 0:
            break
        else:
            write_users(combination, users_on_page)
            url = iterate_url(url)

        iteration_time = sleeper.sleep_for_time()
        write_iter_time_to_log(iteration_time)
       


def parce_users_from_combinations(combinations: List[str]) -> None:
    url_main = 'https://myanimelist.net/users.php?cat=user&'

    s = requests.Session()
    s.headers.update({
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45. 0'})

    for combination in combinations:
        url = url_main + f'q={combination}&show=0'
        pagination_write(s, combination, url)


def main():
    comb_list: List[str] = [
        f'{a}{b}{c}'
        for a in ALPHANUMS if a in ['a','e','i','o']
        for b in ALPHANUMS
        for c in ALPHANUMS
    ]
    where_begin = comb_list.index('a-3')
    parce_users_from_combinations(comb_list[where_begin:])


if __name__ == '__main__':
    main()