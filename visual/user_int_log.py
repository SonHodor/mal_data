import os
from typing import List
from collections import Counter
from matplotlib import pyplot as plt

PATH_TO_LOG = '/Users/sonhodor/code/py/7_parcers/mal/logs/iteration_time.log'

def get_list_iterations():
    with open(PATH_TO_LOG, 'r', encoding='utf-8') as f:
        return [float(line[:3]) for line in f.readlines()]

def show_num_of_users_per_comb() -> None:
    iterations = get_list_iterations()
    c = Counter(iterations).items()
    c = sorted(c, key=lambda a: a[0])

    # print(c.keys)
    # print(c.values)
    
    plt.plot(
        [a[0] for a in c],
        [a[1] for a in c])
    plt.show()


def main():
    show_num_of_users_per_comb()
    # print_top_req_comb()

if __name__ == '__main__':
    main()
