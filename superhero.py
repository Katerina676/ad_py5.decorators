import requests
from log2 import log_path


url = 'https://superheroapi.com/api/2619421814940190/search/'


@log_path('logger2.txt')
def find_super_hero(hero_list):
    for hero in hero_list:
        res = requests.get(url + hero['name'])
        hero['intelligence'] = int(res.json()['results'][0]['powerstats']['intelligence'])
    super_int = max(hero_list, key = lambda k: k['intelligence'])
    message = f'{super_int["name"]} самый сильный супергерой! Его мощность составляет - {super_int["intelligence"]}'
    return message


if __name__ == '__main__':
    print(find_super_hero([{'name' : 'Hulk'}, {'name' : 'Captain America'}, {'name' : 'Thanos'}]))