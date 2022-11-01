import json

import requests
from bs4 import BeautifulSoup

"""
# https://myanimelist.net/animelist/EcchiGodMamster/load.json?offset=300&status=7

# https://myanimelist.net/profile/OP_Rider
#   - recommendations: 7

# https://myanimelist.net/profile/EcchiGodMamster
#   - recommendations: 0
#   - friends: 2022
#   - fav anime: 20
#   - fav manga: 20
#   - fav character: 20
#   - anime list: 3596
#   - manga list: 205
"""

def get_info_from_main_page():
    d = {}

    d['username'] = ''
    d['last_online'] = ''
    d['gender'] = ''
    d['birthday'] = ''
    d['location'] = ''
    d['joined'] = ''

    d['reviews'] = ''
    d['recomendations'] = ''
    d['friends'] = ''

    d['a_now'] = ''
    d['a_completed'] = ''
    d['a_pause'] = ''
    d['a_dropped'] = ''
    d['a_plan'] = ''

    d['a_entries'] = ''
    d['a_rewatched'] = ''
    d['a_episodes'] = ''

    d['m_now'] = ''
    d['m_completed'] = ''
    d['m_pause'] = ''
    d['m_dropped'] = ''
    d['m_plan'] = ''

    d['m_entries'] = ''
    d['m_reread'] = ''
    d['m_chapters'] = ''
    d['m_volumes'] = ''

    d['fav_anime'] = ''
    d['fav_manga'] = ''
    d['fav_chracter'] = ''
    d['fav_people'] = ''


def get_anime_list():
    pass


def get_info_from_user(username):


    main_info = get_info_from_main_page(username)

    anime_list = get_anime_list(username)



    pass

def get_dict_from_url(s: requests.Session, url: str) -> dict:
    d = s.get(url).json()
    print(type(d))
    return d


def read_json():
    with open('data/big_file.json', 'r', encoding='utf-8') as f:
        return json.load(f)


def process_user_anime_list(username: str):
    
    pass


def test():
    d = read_json()

    arr = []
    for elem in d:
        if len(elem['demographics']) != 0:
            arr.extend(elem['demographics'])
    
    print(set([e['id'] for e in arr]))
    print(set([e['name'] for e in arr]))





def main():

    # names = ['Hotaaru__','M_I_K_U__S_I_M_P','Shoku__','Kiru__','u__u','jordu__','Guu____H','wakuuu__','otaku__SEA','Kurizu__','Pichiru__','Nepu__','Bru__na','Lu__','dhanu__ningrat','Fu__','Otaku__Life','Natsu__Sempaiii','KuraRisu__','__kaAatsuUu__','Chaitu__0','Otaku__Multiuso','otaku__girlsss','Otaku__Disease']
    names = ['Hotaaru__']
    url = 'https://myanimelist.net/animelist/%s/load.json'
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45. 0'})

    dict_arr = []
    for name in names:
        dict_arr.extend(get_dict_from_url(session, url % name))
    
    print(dict_arr)

    test()



if __name__ == '__main__':
    main()
