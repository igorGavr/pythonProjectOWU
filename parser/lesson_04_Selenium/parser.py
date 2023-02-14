import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

ser = Service(r"C:\chromedriver.exe")
op = webdriver.ChromeOptions()
s = webdriver.Chrome(service=ser, options=op)

url = 'https://www.house.kg/'
s.get(url)
time.sleep(1)

button = s.find_element(By.XPATH, '//*[@id="homepage"]/header/div/div[2]/ul/li[2]/a')
button.click()


# search = s.find_element(By.XPATH, '//*[@id="quick-search-fake-form"]/div[1]/input')
# text = input('Input some text: ')
# search.send_keys(text)
# search.submit()

option = s.find_element(By.XPATH, '//*[@id="homepage"]/div[7]/div[2]/div[1]/div[6]/div[1]/div/div[2]/div[1]/div[1]/p/a')

posts = s.find_elements(By.CLASS_NAME, 'listing')
for post in posts:
    title = post.find_element(By.CLASS_NAME, 'title')
    print(title.text)

time.sleep(1)

s.close()
