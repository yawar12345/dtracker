import requests
import bs4
import json
from urllib import request

url = "https://www.daraz.pk/products/360-degree-water-saving-tap-aerator-diffuser-faucet-nozzel-swivel-head-aerator-clip-fan-faucet-tap-anti-splash-tap-kitchen-shower-splash-i190654494-s1381690489.html?dsource=share&laz_share_info=14382023_100_100_600039546476_13337830_null&laz_token=070de784337c77f760b29a324f9bb42e"

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

stock_count = list()
for skuInfo in skuInfos:
    print(skuInfos[skuInfo]["stock"])
    stock_count.append("SKU " + skuInfo + " --- STOCK : " + str(skuInfos[skuInfo]["stock"]))

with open('data.txt', 'w', encoding="utf-8") as outfile:
    # outfile.write(substring)
    json.dump(substring, outfile)

print(stock_count)

# Send Message
my_string = '\n'.join(map(str, stock_count)) 
print(my_string)
requests.get("https://api.telegram.org/bot1987340011:AAGQVebsO9YguKsrGMWoSolnvI2jRwfJeik/sendMessage?chat_id=1010879813&text="+my_string)

print('Success')
