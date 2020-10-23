import os
import requests
import pandas as pd

productInfo = pd.read_csv(r'productInfo.csv')

for i in range(len(productInfo['name'])):

    directory = productInfo["category"][i].replace(" ", "-")
    if not os.path.exists(directory):
        os.makedirs(directory)

    url = productInfo["pic1"][i]
    name = productInfo["name"][i].replace(" ", "-")
    name = name.replace("/", "-")
    r = requests.get(url, allow_redirects=True)
    path = directory + '/' + str(i) + '-' + name + '-1.jpg'
    open(path, 'wb').write(r.content)

    url = productInfo["pic2"][i]
    r = requests.get(url, allow_redirects=True)
    path = directory + '/' + str(i) + '-' + name + '-2.jpg'
    open(path, 'wb').write(r.content)

    print(i)

print('hi')