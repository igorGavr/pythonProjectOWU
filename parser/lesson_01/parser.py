import requests
from bs4 import BeautifulSoup as BS

URL = 'https://www.house.kg/snyat-kvartiru?region=1&town=2&sort_by=upped_at+desc'


def get_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return None

def get_post_links(html):
    links = []
    soup = BS(html, 'html.parser')
    container = soup.find('div', {"class": "listings-wrapper"})
    posts = container.find_all('div', {'class': 'listing'})
    for post in posts:
        p = post.find('p', {'class': 'title'}).find('a').get('href')
        full_link = 'https://www.house.kg' + p
        # print(full_link)
        links.append(full_link)
    return links


def main():
    html = get_html(URL)
    links = get_post_links(html)
    for link in links:
        detail_html = get_html(link)

if __name__ == '__main__':
    main()