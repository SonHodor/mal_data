import os
from typing import List
from collections import defaultdict, Counter
from matplotlib import pyplot as plt

PATH_TO_CSV = '/Users/sonhodor/code/py/7_parcers/mal/data/users_raw/'

def get_dict_comb_user() -> defaultdict:
    """
    returns 
        {
            'aaa': [
                'user1', 'user2'
            ], 
            'aab': [
                'user1', 'user2'
            ]
        }
    """
    d = defaultdict(list)
    for _, _, files in os.walk(PATH_TO_CSV):
        for name in files:
            with open(PATH_TO_CSV + name, 'r', encoding='utf-8') as f:
                for line in f.readlines():
                    d[name.split('.')[0]].extend(line[:-1].split(','))
    return d

def print_top_req_comb() -> None:
    d = get_dict_comb_user()

    sorted_counted_list =  sorted([
        [k, len(v) // 24] 
            for k, v in d.items()], 
        key=lambda a: a[1])

    [print(f'{elem[0]} - {elem[1]}') for elem in sorted_counted_list]


def show_num_of_users_per_comb() -> None:
    d = get_dict_comb_user()

    sorted_counted_list = list(map(
        lambda elem: elem[1],
        sorted([
            [k, len(v) // 24] 
                for k, v in d.items()], 
            key=lambda a: a[1])
    ))
    
    plt.plot(
        range(len(sorted_counted_list)),
        sorted_counted_list)
    plt.show()


def show_num_of_lines_per_comb():
    d = get_dict_comb_user()
    for key in d:
        d[key] = (len(d[key]) // 24) // 100
    
    lengths = d.values()
    c = sorted(Counter(lengths).items(), key=lambda a: a[0])
    
    plt.style.use('seaborn-whitegrid')

    plt.plot(
        [a[0] for a in c],
        [a[1] for a in c],
        'o', 
        markersize=2,
        color='black'
        )
    plt.show()
    
    


def main():
    # show_num_of_users_per_comb()
    show_num_of_lines_per_comb()
    # print_top_req_comb()

if __name__ == '__main__':
    main()
