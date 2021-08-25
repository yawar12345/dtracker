import requests
import bs4
import json
from urllib import request

url = "https://www.daraz.pk/products/best-quality-mini-hair-straightener-and-straightner-travel-mini-hair-flat-iron-ceramic-plate-hair-straightener-best-for-traveling-gifts-outing-i221047490-s1435161574.html?spm=a2a0e.searchlist.list.9.424dbfbewter4p&search=1"

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
