
"""
Getting all League of Legends champions combos to use in another application
Pegando todos os combos dos campeões de league of legends para usar em outra 
aplicação
"""

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

# creat a txt with the names
# with open('champions.txt', 'w') as file:
#     for element in elements:
#         file.write(f'{element.text.strip()}\n')
#         # print(el.text.strip())


# Get the combos using the list
def scraper(champion: str):
    url = f'https://mobalytics.gg/lol/champions/{champion}/combos'
    response = requests.get(url)

# Names like jarvar and nunu are spelled differently,return if not find
    if response.status_code == 404:
        return print(f'404 Not Found {champion}')

    raw_html = response.text
    parsed_html = BeautifulSoup(raw_html, 'html.parser')
    elements = parsed_html.find_all("div", class_="m-1o7d3sk")

    # txt or JSON
    # create a txt file in the same folder
    with open('combos.txt', 'a') as file:
        for element in elements:
            file.write(f'{element.text.strip()}\n')


# running the function with the list created before
# display the list, it may take some time
for i, name in enumerate(all_champions):
    print(f'faltam: {len(all_champions)-i}')
    scraper(name)

print('DONE!!!!!!!!!!!!!!!!!!!!!')
