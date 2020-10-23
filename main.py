import csv
from selenium.webdriver import Safari
from selenium.webdriver.common.by import By

catLinks = []
productLinks = []

with Safari() as driver:
    # driver.get("https://www.tshirt1.ir/all-products")
    # driver.implicitly_wait(2)
    # element = driver.find_element(By.XPATH, '// *[ @ id = "categories_block_left"] / div / ul')
    # elements = element.find_elements(By.TAG_NAME, 'a')
    # for e in elements:
    #     catLinks.append({"name": e.text, "link": e.get_attribute("href")})
    #
    # print(catLinks)

    for i in range(1, 137):
        url = "https://www.tshirt1.ir/all-products?p=" + str(i)
        driver.get(url)
        driver.implicitly_wait(1)

        element = driver.find_element(By.XPATH, '//*[@id="center_column"]/ul')
        elements = element.find_elements(By.TAG_NAME, 'a')
        for e in elements:
            if e.get_attribute("class") == "product_img_link":
                productLinks.append({"name": e.get_attribute("title"), "link": e.get_attribute("href")})

with open('productLinks.csv', 'w') as f1:
    writer = csv.writer(f1, delimiter=',', lineterminator='\n', )
    j = 0
    for key in productLinks:
        row = [j, productLinks[j]["name"], productLinks[j]["link"]]
        writer.writerow(row)
        j += 1

print(productLinks)
