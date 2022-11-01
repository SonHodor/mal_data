
from parce.parcer import get_new_proxys_list
from parce.parcer import write_proxy_list_to_pg


def update_proxy_table():
    new_proxys = get_new_proxys_list()
    write_proxy_list_to_pg(new_proxys)


def verify_proxys():
    pass


def main():
    update_proxy_table()


if __name__ == '__main__':
    main()
