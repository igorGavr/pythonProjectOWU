import requests
from bs4 import BeautifulSoup as BS
from datetime import datetime
import xlsxwriter
from multiprocessing import Pool

URL = 'https://www.house.kg/snyat-kvartiru?region=1&town=2&sort_by=upped_at+desc'
array = []


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
        links.append(full_link)
    return links


def get_post_data(html):
    soup = BS(html, "html.parser")
    details_header = soup.find('div', {'class': 'details-header'})
    title = details_header.find('div', {'class': 'left'}) \
        .find('h1').text.strip()
    price = details_header.find('div', {'class': 'price-dollar'}).text.strip()
    address = details_header.find('div', {'class': 'address'}).text.strip()
    number = soup.find('div', {'class': 'number'}).text.strip()
    lat = soup.find('div', {'class': 'map-wrapper'}).find('div', {'id': 'map2gis'}).get('data-lat')
    lon = soup.find('div', {'class': 'map-wrapper'}).find('div', {'id': 'map2gis'}).get('data-lon')

    infos = soup.find('div', {'class': 'details-main'}).find_all('div', {'class': 'info-row'})
    add_info = {}
    for info in infos:
        key = info.find('div', {'class': 'label'}).text.strip()
        value = info.find('div', {'class': 'info'}).text.strip()
        add_info.update({key: value})
    # print(title)
    # print(address)
    # print(price)

    # array.append(number)
    # print(f'широта - {lat}')
    # print(f'довгота - {lon}')
    # print(add_info['Дом'])
    data = {
        "number": number,
        "lat": lat,
        "lon": lon,
    }
    return data


def get_last_page(html):
    soup = BS(html, "html.parser")
    ul_pagination = soup.find('ul', {'class': 'pagination'})
    list_li = ul_pagination.find_all('li', {'class': 'page-item'})
    last_btn = list_li[-1]
    last_page_number = int(last_btn.find('a').get('data-page'))
    return last_page_number


def write_excel(data, row_number):
    # workbook = xlsxwriter.Workbook('house_kg.xlsx', {'in_memory':True})
    # worksheet = workbook.add_worksheet()
    # col = 0
    # for value in data.values():
    #     worksheet.write(row_number, col, value)
    #     col += 1
    # workbook.close()
    pass



def parse_page(page_number):
    row_number = 0
    URL = 'https://www.house.kg/snyat-kvartiru?region=1&town=2&sort_by=upped_at+desc'
    page_url = URL + f'&page{page_number}'
    print(page_url)
    html = get_html(page_url)
    links = get_post_links(html)
    for link in links:
        detail_html = get_html(link)
        data = get_post_data(detail_html)
        write_excel(data=data, row_number=row_number)
        row_number += 1


def main():
    time_start = datetime.now()
    URL = 'https://www.house.kg/snyat-kvartiru?region=1&town=2&sort_by=upped_at+desc'
    last_page_number = get_last_page(get_html(URL))

    with Pool(10) as p:
        p.map(parse_page, range(1, 21))

    time_end = datetime.now()
    print(time_end - time_start)


if __name__ == '__main__':
    main()

# print(array)
