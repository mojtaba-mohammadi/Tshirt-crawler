import pandas as pd
import csv
from selenium.webdriver import Safari
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


productLinks = pd.read_csv(r'productLinks.csv')

productInfo = []

with Safari() as driver:
    for i in range(len(productLinks['link'])):
        url = productLinks["link"][i]
        driver.get(url)
        driver.implicitly_wait(1)
        element = driver.find_element(By.ID, 'bigpic')
        pic1 = element.get_attribute("src")
        if pic1[26:27] == "-":
            pic2 = pic1[0:23] + str(int(pic1[23:26]) + 1) + pic1[26:]
        else:
            pic2 = pic1[0:23] + str(int(pic1[23:27]) + 1) + pic1[27:]

        try:
            category = driver.find_element(By.XPATH, '//*[@id="columns"]/div[1]/span[2]/li[1]/a').get_attribute('title')
        except:
            category = "none"

        productInfo.append({"category": category, "name": productLinks["name"][i],
                            "link": productLinks["link"][i], "pic1": pic1, "pic2": pic2})

with open('productInfo.csv', 'w') as f1:
    writer = csv.writer(f1, delimiter=',', lineterminator='\n', )
    j = 0
    for key in productInfo:
        row = [j, productInfo[j]["category"], productInfo[j]["name"], productInfo[j]["link"],
               productInfo[j]["pic1"], productInfo[j]["pic2"]]
        writer.writerow(row)
        j += 1

print(productInfo)
