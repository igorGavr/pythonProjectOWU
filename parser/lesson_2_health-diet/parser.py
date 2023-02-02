# pip install beautifulsoup4 requests lxml

import requests
from bs4 import BeautifulSoup
import json
import csv

# url = "https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie"
url2 = 'https://calorizator.ru/product'
#
#
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}
# req = requests.get(url, headers=headers)
# req = requests.get(url2)
# src = req.text
# print(src)
#
# with open("index.html", 'w') as file:
#     file.write(src)

# відкриваємо файл та зберігаємо код в зміну
# with open('index.html') as file:
#     src = file.read()
#
# soup = BeautifulSoup(src, 'lxml')
#
# all_products_hrefs = soup.find_all(class_ = "product")
# # print(len(all_products_hrefs))
# # print(all_products_hrefs)
#
#
# all_categories_dict = {}
#
# for item in all_products_hrefs:
#     # print(item)  # виводимо ul з класом product
#     links = item.find_all('a')
#     for a in links:
#         # print(a)
#         item_text = a.text
#         item_href = 'https://calorizator.ru/' + a.get('href')
#         # print(f'{item_text} *** {item_href}')
#
#         all_categories_dict[item_text] = item_href
#     # print(links)
# #     lis = item.find('li')
# #     for li in lis:
# #         print(li)

# print(all_categories_dict)
#
# with open("all_categories_dict.json", "w") as file:
#     json.dump(all_categories_dict, file, indent=4, ensure_ascii=False)
#
#
with open("all_categories_dict.json") as file:
    all_categories = json.load(file)
#
count = 0
for category_name, category_href in all_categories.items():
    if count == 0:
        req = requests.get(url=category_href, headers=headers)
        src = req.text

        # category = 'prod'+category_href.split('/')[-1]
        # print(category)
        # print(f'{category_name} -- {category_href}')

        with open(f'data/{count}_{category_name}.html', 'w') as file:
            file.write(src)

        with open(f'data/{count}_{category_name}.html') as file:
            src = file.read()

        soup = BeautifulSoup(src, "lxml")

        # збираємо заголовки таблиці
        table_head = soup.find(class_ = "views-table").find('tr').find_all('th')
        product = table_head[1].text
        proteins = table_head[2].text
        fats = table_head[3].text
        carbohydrates = table_head[4].text
        calories = table_head[5].text
        # print(calories)

        with open(f'data/{count}_{category_name}.csv', 'w', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(
                (
                    product,
                    proteins,
                    fats,
                    carbohydrates,
                    calories,
                )
            )

        # збираємо дані таблиці
        products_data = soup.find(class_ = "views-table").find('tbody').find_all('tr')

        for item in products_data:
            products_tds = item.find_all('td')

            # title = products_tds[0].find('a').find('img').get('title')
            title = products_tds[1].find('a').text
            proteins = products_tds[2].text
            fats = products_tds[3].text
            carbohydrates = products_tds[4].text
            calories = products_tds[5].text
            print(title)

            with open(f'data/{count}_{category_name}.csv', 'a', encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(
                    (
                        title,
                        proteins,
                        fats,
                        carbohydrates,
                        calories,
                    )
                )

        count += 1








