from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

service = Service('/Users/lucasmas/Downloads/chromedriver_mac_arm64(1)/chromedriver')
service.start()
driver = webdriver.Remote(service.service_url)
driver.get('https://www.hltv.org/stats/players/11893/zywoo?startDate=2022-05-10&endDate=2023-05-10')

player_ages = {}

def document_initialised(driver):
    player_soup = BeautifulSoup(driver.page_source, 'html.parser')
    age_div = player_soup.find('div', class_='summaryPlayerAge')
    pseudo_h1 = player_soup.find('h1', class_='summaryNickname text-ellipsis')

    if age_div:
        age = int(age_div.text.strip().split(' ')[0])
        player_ages[pseudo_h1] = age
        print(pseudo_h1, age)

    return driver.find_element(By.CLASS_NAME, 'summaryPlayerAge')


WebDriverWait(driver, 20).until(document_initialised)




# Print the ages
#for player, age in player_ages.items():
    #print(f'{player}: {age}')

driver.quit()