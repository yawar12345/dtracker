import requests
import bs4
import json
from urllib import request

url = "https://www.daraz.pk/products/vantime-for-infinix-note-7-case-hard-camera-protect-ring-finger-stand-holder-cover-i204998687-s1406678185.html?spm=a2a0e.searchlist.list.1.3d38419556cwFl&search=1"

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

for skuInfo in skuInfos:
    print(skuInfos[skuInfo]["stock"])




# table=soup.find('table')

# headers=[ heading.text for heading in table.find_all('th')]

# table_rows=[ row for row in table.find_all('tr')]

# results=[{headers[index]:cell.text for index,cell in enumerate(row.find_all("td")) }for row in table_rows]

# print(json.dumps(results))

with open('data.txt', 'w', encoding="utf-8") as outfile:
    # outfile.write(substring)
    json.dump(substring, outfile)


print('Success')
