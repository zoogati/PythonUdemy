import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.amazon.com/Spigen-Hybrid-Generation-Cushion-Technology/dp/B01M1SCIOV/ref=sr_1_4?s=wireless&ie=UTF8&qid=1507347242&sr=1-4&keywords=iphone+8+case")
content = request.content

soup = BeautifulSoup(content, "html.parser")
element = soup.find("span", {"id": "priceblock_saleprice", "class": "a-size-medium a-color-price"})

# <span id="priceblock_saleprice" class="a-size-medium a-color-price">$11.99</span>

price_string = element.text.strip()
price_without_symbol = price_string[1:]

price = float(price_without_symbol)

print(price)
