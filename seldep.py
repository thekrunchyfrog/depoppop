import urllib.request
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep


base_url = "https://www.depop.com/surfingskeletons/"

options = Options()
# options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=options)

driver.get(base_url)

i = 0
while i < 100:
    driver.execute_script("window.scrollBy(0, 2000);")
    sleep(.5)
    i = i + 1

items = driver.find_elements(By.CSS_SELECTOR, "a[data-testid='product__item']")

for item in items:
    newDriver = webdriver.Chrome(chrome_options=options)
    newDriver.get(item.get_attribute('href'))
    newDriver.execute_script("window.scrollBy(0, 2000);")

    username = newDriver.find_element(By.CSS_SELECTOR, "a[data-testid='bio__username']").get_attribute('text')

    print(username)

    sleep(1)
    item_pics = newDriver.find_elements(By.CSS_SELECTOR, "div[data-testid='product__images'] img[data-testid='lazyLoadImage__img']")

    if not os.path.exists(username):
        os.makedirs(username)

    for item_pic in item_pics:
        urllib.request.urlretrieve(item_pic.get_attribute('src'), username + "/" + item_pic.get_attribute('alt').replace('/', ' ') + ".jpg")

    newDriver.close()

driver.close()
