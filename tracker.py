import requests
import bs4
import json
from urllib import request

url = "https://www.daraz.pk/products/360-degree-water-saving-tap-aerator-diffuser-faucet-nozzel-swivel-head-aerator-clip-fan-faucet-tap-anti-splash-tap-kitchen-shower-splash-i190654494-s1381690489.html?dsource=share&laz_share_info=14382023_100_100_600039546476_13337830_null&laz_token=070de784337c77f760b29a324f9bb42e"

response = request.urlopen(url)
page_source = response.read()

str = page_source.decode('utf-8')

startIndex = str.find('{"data"')
endIndex = str.find('["module_popups"]}}}')

substring = str[startIndex:endIndex+20]

# print(substring)

jsonObj = json.loads(substring)

# print(y["data"]["root"]["fields"]["skuInfos"])

skuInfos = jsonObj["data"]["root"]["fields"]["skuInfos"]

stock_count = list()
for skuInfo in skuInfos:
    print(skuInfos[skuInfo]["stock"])
    # stock_count.append("SKU " + str(skuInfo) + " --- STOCK : " + str(skuInfos[skuInfo]["stock"]))

with open('data.txt', 'w', encoding="utf-8") as outfile:
    # outfile.write(substring)
    json.dump(substring, outfile)

print(stock_count)


print('Success')
