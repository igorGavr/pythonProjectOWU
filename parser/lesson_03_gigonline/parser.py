import requests
from bs4 import BeautifulSoup
from bs4.dammit import EncodingDetector
from time import sleep
import pandas as pd

url = 'https://gidonline.io/rating/'

resp = requests.get(url)
http_encoding = resp.encoding if 'charset' in resp.headers.get('content-type', '').lower() else None
html_encoding = EncodingDetector.find_declared_encoding(resp.content, is_html=True)
encoding = html_encoding or http_encoding
soup = BeautifulSoup(resp.content, 'lxml', from_encoding=encoding)

data = []
for p in range(2, 5):
    print(f'page - {p}')
    url = f'https://gidonline.io/rating/page/{p}/'
    resp = requests.get(url)
    sleep(2)
    soup = BeautifulSoup(resp.content, 'lxml', from_encoding=encoding)

    films = soup.find('div', {'id': 'posts'}).find_all('a')
    for film in films:
        title = film.find('span').text
        year = film.find('div', {'class': 'mqn'}).text
        img_href = f'https://gidonline.io' + film.find('img').get('src')
        data.append([title, year, img_href])

header = ['title', 'year', 'img_href']
df = pd.DataFrame(data, columns=header)
df.to_csv(r'C:\Users\User\Desktop\gigonline_data.csv', sep=';')

print(len(data))
