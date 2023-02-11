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


def get_post_data(html):
    soup = BS(html, "html.parser")
    details_header = soup.find('div', {'class':'details-header'})
    title = details_header.find('div', {'class':'left'})\
        .find('h1').text.strip()
    price = details_header.find('div', {'class':'price-dollar'}).text.strip()
    address = details_header.find('div', {'class':'address'}).text.strip()
    number = soup.find('div', {'class': 'number'}).text.strip()
    lat = soup.find('div', {'class': 'map-wrapper'}).find('div', {'id':'map2gis'}).get('data-lat')
    lon = soup.find('div', {'class': 'map-wrapper'}).find('div', {'id':'map2gis'}).get('data-lon')

    infos = soup.find('div', {'class':'details-main'}).find_all('div', {'class':'info-row'})
    add_info = {}
    for info in infos:
        key = info.find('div', {'class':'label'}).text.strip()
        value = info.find('div', {'class':'info'}).text.strip()
        add_info.update({key:value})
    print(title)
    print(address)
    print(price)
    print(number)
    print(f'широта - {lat}')
    print(f'довгота - {lon}')
    print(add_info['Дом'])
    print('--------------')



def main():
    html = get_html(URL)
    links = get_post_links(html)
    for link in links:
        detail_html = get_html(link)
        get_post_data(detail_html)


if __name__ == '__main__':
    main()
