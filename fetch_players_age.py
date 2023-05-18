import undetected_chromedriver as uc
from bs4 import BeautifulSoup
import pickle

browser = uc.Chrome()
browser.get('https://www.hltv.org/stats/players?startDate=2022-05-10&endDate=2023-05-10&rankingFilter=Top50')

soup = BeautifulSoup(browser.page_source, 'html.parser')
players = soup.find_all('td', class_='playerCol')

players_age = {}

for player in players:
    link = player.find('a')
    player_url = 'https://www.hltv.org' + link['href']

    browser.get(player_url)
    browser.implicitly_wait(5)
    player_soup = BeautifulSoup(browser.page_source, 'html.parser')

    age_div = player_soup.find('div', class_='summaryPlayerAge')
    pseudo_h1 = player_soup.find('h1', class_='summaryNickname text-ellipsis')

    if age_div:
        age = int(age_div.text.strip().split(' ')[0])
        pseudo = pseudo_h1.text.strip()
        players_age[pseudo] = age
        print(pseudo, age)

with open('data/players_age.pkl', 'wb') as file:
    pickle.dump(players_age, file)

