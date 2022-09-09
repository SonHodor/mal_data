import os
from typing import List
from collections import defaultdict

PATH_TO_CSV = '/Users/sonhodor/code/py/7_parcers/mal/data/users_raw/'

def all_csv_to_list() -> List[str]:
    nick_list = []

    for _, _, files in os.walk(PATH_TO_CSV):
        for name in files:
            with open(PATH_TO_CSV + name, 'r', encoding='utf-8') as f:
                for line in f.readlines():
                    nick_list.extend(line[:-1].split(','))    

    return nick_list

def main():
    print(len(set(all_csv_to_list())))


if __name__ == '__main__':
    main()