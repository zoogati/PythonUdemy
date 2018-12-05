import requests
import re
from bs4 import BeautifulSoup

#request = requests.get("https://www.amazon.com/Spigen-Hybrid-Generation-Cushion-Technology/dp/B01M1SCIOV/ref=sr_1_4?s=wireless&ie=UTF8&qid=1507347242&sr=1-4&keywords=iphone+8+case")
#content = request.content

#soup = BeautifulSoup(content, "html.parser")
#element = soup.find("span", {"id": "priceblock_saleprice", "class": "a-size-medium a-color-price"})

# <span id="priceblock_saleprice" class="a-size-medium a-color-price">$11.99</span>

#price_string = element.text.strip()

#price_without_symbol = price_string[1:]

#price = float(price_without_symbol)

#print(price)

request = requests.get("http://web.mta.info/status/serviceStatus.txt")
content = request.content

soup = BeautifulSoup(content, "html.parser")
txt = soup.get_text()
formtxt = ' '.join(re.sub(r'<.+?>', ' ', txt).split())


splitlist = re.split(r'(\d{2,3}/\d{1,2}/\d{4}\s\d{1,2}:\d{1,2}:\d{1,2}\s\w{2}|'r'\d{2}/\d{2}/\d{4}\s\d{1,2}:\d{2}\w{2})', formtxt)

results = {}

# Clean up more broken html
for index, split in enumerate(splitlist):
    splitlist[index] = split.replace('&nbsp;', '').replace('&bull;', '').replace('&mdash;','')
    if index % 2 and index < len(splitlist):
        if split in results.keys():
            results[splitlist[index]].append(splitlist[index+1])
        else:
            results[splitlist[index]] = [splitlist[index+1]]

print(splitlist)