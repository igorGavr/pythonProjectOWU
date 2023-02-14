import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd
# pip install pandas openpyxl selenium

ser = Service(r"C:\chromedriver.exe")
op = webdriver.ChromeOptions()
s = webdriver.Chrome(service=ser, options=op)

url = 'https://www.mashina.kg/search/all/'
s.get(url)
time.sleep(5)
posts = s.find_elements(By.CLASS_NAME, 'list-item')
posts_data = []
for post in posts:
    name = post.find_element(By.CLASS_NAME, 'name')
    price = post.find_element(By.CLASS_NAME, 'price').find_element(By.TAG_NAME, 'p')
    info = post.find_element(By.CLASS_NAME, 'year-miles')
    posts_data.append(
        (name.text, price.text, info.text)
    )
headers = ['Title', 'Price', 'Add. info']
data_frame = pd.DataFrame(posts_data, columns=headers)
with pd.ExcelWriter('mashina_kg.xlsx') as writer:
    data_frame.to_excel(writer)


time.sleep(1)
