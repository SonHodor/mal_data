import datetime
import os
from time import sleep

from parcers.sleep import Sleeper

import psycopg2
import requests

# alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789-_'
# print(alphabet[:-2]) # num of 3 symbol alphanum variations = 238328
# print(alphabet) # num of 3 symbol alphanum + '-_' variations  = 262144


# s = requests.Session()
# s.headers.update({
#             'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45. 0'})

# j = s.get('https://myanimelist.net/users.php').json()

# print(j)


ALPHANUMS = 'abcdefghijklmnopqrstuvwxyz0123456789-_'
SECONDS_TO_SLEEP = 2

def play_with_list():
    vow = ['a','e','i','o','u','y']
    comb_list_filtered_1 = [
        f'{a}{b}{c}'
        for a in ALPHANUMS
        for b in ALPHANUMS
        for c in ALPHANUMS 
            if a in vow or b in vow or c in vow
    ]

    comb_list_filtered = [
        f'{a}{b}{c}'
        for a in ALPHANUMS if a in vow
        for b in ALPHANUMS
        for c in ALPHANUMS

    ]
    
    comb_list = [
        f'{a}{b}{c}'
        for a in ALPHANUMS
        for b in ALPHANUMS
        for c in ALPHANUMS
    ]

    print(f'unfiltered list of combinations   - {len(comb_list)}')
    print(f'filtered if any letter is a vowel - {len(comb_list_filtered_1)}')
    print(f'filtered if first symbol is vovel - {len(comb_list_filtered)}')


def get_file_creation_date(
        file_name,
        path_to_csv='/Users/sonhodor/code/py/7_parcers/mal/data/users_raw/'
    ):

    mtime = os.stat(path_to_csv + file_name).st_mtime

    mtime_str = str(datetime.datetime.utcfromtimestamp(mtime)).split('.')[0]

    print(mtime_str)

def test_get_file_creation_date():
    get_file_creation_date('aaa.csv')
    get_file_creation_date('aba.csv')
    get_file_creation_date('aca.csv')
    get_file_creation_date('ada.csv')
    get_file_creation_date('aea.csv')
    get_file_creation_date('afa.csv')
    get_file_creation_date('aga.csv')


def test_psycopg_conn():
    with psycopg2.connect(
        dbname='sonhodor',
        user='root',
        password='root',
        host='192.168.1.84',
        port='5432'
    ) as conn:

        with conn.cursor() as cur:
            cur.execute("SELECT DISTINCT find_combination FROM parcers.mal_users_raw")
            records = [a[0] for a in cur.fetchall()]
            print(records)
            print(len(records))
        # ACTUALLY FUCKIN WORKS o_O


if __name__ == '__main__':
    # test_psycopg_conn()
    s = Sleeper(1)

    while True:
        sleep(0.05)
        print(s.sleep())
        # print(f'sleeped {} sec')
