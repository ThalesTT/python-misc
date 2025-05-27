
"""
JSON
Getting all League of Legends champions combos to use in another application
Pegando todos os combos dos campeões de league of legends para usar em outra
aplicação
"""
import json
import requests

from bs4 import BeautifulSoup

url = 'https://www.leagueoflegends.com/en-us/champions/'
response = requests.get(url)
raw_html = response.text
parsed_html = BeautifulSoup(raw_html, 'html.parser')
# print(response.status_code)

# get the name of all the champions
elements = parsed_html.find_all("div", class_="sc-ce9b75fd-0 lmZfRs")

# list of champions names
all_champions = [el.text.strip() for el in elements]
correct_names = []
for name in all_champions:
    if name == 'Nunu & Willump':
        name = 'Nunu'
    if name == 'Renata Glasc':
        name = 'Renata'
    if name == 'Wukong':
        name = 'MonkeyKing'
    correct_names.append(name.replace(
        " ", "").replace("'", "").replace(".", ""))
# print(correct_names)


def scraper(champion: str):
    url = f'https://mobalytics.gg/lol/champions/{champion}/combos'
    response = requests.get(url)
    combos_list: dict[str, list] = dict()
    combos_list[champion] = []

    if response.status_code == 404:
        return print(f'404 Not Found {champion}')

    raw_html = response.text
    parsed_html = BeautifulSoup(raw_html, 'html.parser')
    elements = parsed_html.find_all("div", class_="m-1o7d3sk")

    for element in elements:
        combos_list[champion].append(element.text)
        # print(f'{champion}:{element.text}')
        # print(combos_list)

    return combos_list


# running the function with the list created before
# display the list, it may take some time
combos = []
for i, name in enumerate(correct_names):
    print(f'faltam: {len(correct_names)-i}')
    combos.append(scraper(name))
print('DONE!!!!!!!!!!!!!!!!!!!!!')


# create a JSON in the same folder
with open('combos.json', 'w') as file:
    json.dump(combos, file, indent=4, sort_keys=True)
