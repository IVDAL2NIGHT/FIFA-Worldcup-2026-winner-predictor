from bs4 import BeautifulSoup
import requests
import pandas as pd

# datos para "scraper" 1930-2018
years = [1930, 1934, 1938, 1950, 1954, 1958, 1962, 1966, 1970, 1974,
         1978, 1982, 1986, 1990, 1994, 1998, 2002, 2006, 2010, 2014,
         2018,2022]

web = 'https://en.wikipedia.org/wiki/2014_FIFA_World_Cup'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def get_matches(year):
  	
    web = f'https://en.wikipedia.org/wiki/{year}_FIFA_World_Cup'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(web, headers=headers)
    content = response.text
    soup = BeautifulSoup(content, 'lxml')

    matches = soup.find_all('div', class_='footballbox') # Encuentra todos los divs con la clase 'footballbox', find_all devuelve una lista

    home = []
    score = []
    away = []

    for match in matches:
        home.append(match.find('th', class_='fhome').get_text())  # equipo local
        score.append(match.find('th', class_='fscore').get_text()) # marcador
        away.append(match.find('th', class_='faway').get_text())  # equipo visitante

    dict_football = {'Local': home, 'Resultado': score, 'Visitante': away} 

    df_football = pd.DataFrame(dict_football)
    df_football['Año'] = year

    return df_football

# datos históricos
fifa = [get_matches(year) for year in years]
df_fifa = pd.concat(fifa, ignore_index=True)
df_fifa.to_csv('Mundiales_FIFA_registro_historico', index=False)

# fixture 2026
df_fixture = get_matches('2026')
df_fixture.to_csv('Mundiales_FIFA_fixture', index=False)






