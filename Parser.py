import requests
from bs4 import BeautifulSoup as bs


url = 'https://www.demirbank.kg/ru/retail/home'

a = []
exchange_rate = {}
sours = requests.get(url)
text = bs(sours.content, "html.parser")

table = text.find("table", class_ = "table")
tr = table.findAll("tr")

for i  in tr:
    a.append(i.text.strip().split('\n'))

a.pop(0)

for f, g, h in a:
    exchange_rate[f] = [g, h]
exchange_rate.update(KGS = ['1', '1'])