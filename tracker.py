import requests
import bs4
import json
from urllib import request

# url = "https://www.daraz.pk/products/best-quality-peel-off-nail-paints-or-polish-pack-of-100-artificial-nails-with-glue-false-nails-acrylic-nails-kit-french-nails-multicolor-pack-of-6-nail-paints-i220983176-s1434986421.html?dsource=share&laz_share_info=14391127_100_100_600039546476_13346934_null&laz_token=e5c97959d297e728a1eb33ada9874271"


# Using readlines()
file1 = open('urls.txt', 'r')
Lines = file1.readlines()
 
count = 0
# Strips the newline character
for url in Lines:
    count += 1
    print("Line{}: {}".format(count, url.strip())) 
    response = request.urlopen(url)
    page_source = response.read()
    strSource = page_source.decode('utf-8')

    startIndex = strSource.find('{"data"')
    endIndex = strSource.find('["module_popups"]}}}')

    substring = strSource[startIndex:endIndex+20]

    # print(substring)

    jsonObj = json.loads(substring)

    # print(y["data"]["root"]["fields"]["skuInfos"])

    skuInfos = jsonObj["data"]["root"]["fields"]["skuInfos"]
    specs = jsonObj["data"]["root"]["fields"]["specifications"]
    store_name = jsonObj["data"]["root"]["fields"]["seller"]["name"].replace('&', 'n')
    #store_name = jsonObj["data"]["root"]["fields"]["seller"]["name"].replace('!', 'n')
    
    stock_count = list()
    stock_count.append(store_name)
    stock_count.append('\n')
    stock_count.append(jsonObj["data"]["root"]["fields"]["product"]["title"])
    i = 0
    for skuInfo in skuInfos:
        i += 1
        name = ''
        if skuInfo in specs:
            name = specs[skuInfo]["boxContent"]
            print(name)
        print(skuInfos[skuInfo]["stock"])
        stock_count.append(name + "\nSKU " + skuInfo + " --- STOCK : " + str(skuInfos[skuInfo]["stock"]))

    with open('data.txt', 'w', encoding="utf-8") as outfile:
        # outfile.write(substring)
        json.dump(substring, outfile)

    print(stock_count)

    # Send Message
    my_string = '\n'.join(map(str, stock_count)) 
    print(my_string)
    requests.get("https://api.telegram.org/bot1987340011:AAGQVebsO9YguKsrGMWoSolnvI2jRwfJeik/sendMessage?chat_id=447905121&text="+my_string)

    print('Success')
