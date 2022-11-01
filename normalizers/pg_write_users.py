import datetime
import os
from typing import List

from utility.creds import credentials as creds

import psycopg2


PATH_TO_CSV = '/Users/sonhodor/code/py/7_parcers/mal/data/users_raw/'
DB_TABLE_NAME = 'parcers.mal_users_raw'

TRANSACTION_SIZE = 1000
# size 200      execution time 5m 31s   block I/O 6k        trans/p/s 30   tuples_in 6k
# size 500      execution time 3m 46s   block I/O 10k       trans/p/s 19   tuples_in 9k
# size 1000     execution time 3m 10s   block I/O 10.5k     trans/p/s 11   tuples_in 10k

def get_pg_conn():
    return psycopg2.connect(**creds['pg'])

def get_file_modify_datetime(path: str) -> str:
    mtime = os.stat(path).st_mtime
    return str(datetime.datetime.utcfromtimestamp(mtime)).split('.')[0]

def get_all_users_from_csv(path: str) -> List[str]:
    all_users = []
    with open(path, 'r', encoding='utf-8') as f:
        for row in f.readlines():
            all_users.extend(row[:-1].split(','))
    return all_users

def get_all_file_paths():
    filenames = [filename for _, _, filename in os.walk(PATH_TO_CSV)][0]
    filepaths = [PATH_TO_CSV + name for name in filenames]
    return filepaths


def insert_all_users_from_all_files() -> None:
    import psycopg2.extras as ex
    conn = get_pg_conn()
    cur = conn.cursor()

    cur.execute("SELECT DISTINCT find_combination FROM parcers.mal_users_raw")
    all_written_combinations = [a[0] for a in cur.fetchall()]

    for filepath in get_all_file_paths():
        comb_name = filepath.split('/')[-1][:3]
        if comb_name in all_written_combinations:
            print(f'\tskipping {comb_name}.csv')
            continue

        users_from_file = get_all_users_from_csv(filepath)
        file_modify_date = get_file_modify_datetime(filepath)

        list_of_tuples = [
            (user, comb_name, file_modify_date)
            for user in users_from_file
        ]

        chunked_tuples = [
            list_of_tuples[i:i+TRANSACTION_SIZE]
            for i in range(0, len(list_of_tuples), TRANSACTION_SIZE)
        ]
        
        for i, chunk in enumerate(chunked_tuples):
            ex.execute_values(
                cur,
                'INSERT INTO parcers.mal_users_raw (username, find_combination, parce_dt) VALUES %s',
                chunk
            )
            conn.commit()
            print(f'commited chunk {i}')
        print(f'done writing {comb_name}')

    cur.close()
    conn.close()


def main():
    insert_all_users_from_all_files()


if __name__ == '__main__':
    main()