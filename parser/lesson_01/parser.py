import requests
from bs4 import BeautifulSoup as BS


file = open('test.html', encoding='utf-8')

html = file.read()

soup = BS(html, 'html.parser')
m = soup.find(class_ = 'content-container').find_all('h1', {'class':'title'})
print(m)

for i in m:
    print(i.text.strip())