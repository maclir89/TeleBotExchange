import requests
from bs4 import BeautifulSoup as bs
# Решил адаптировать проект под свои нужды. Часто меняю деньги в DemirBank. API запросов у них не нашел,
# поэтому распарсил курс с их сайта.

url = 'https://www.demirbank.kg/ru/retail/home'

a = []                  # Список для добавления всех нужных элементов
exchange_rate = {}      # Словарь для приведения полученных данных к нужной структуре

sours = requests.get(url)
text = bs(sours.content, "html.parser")

table = text.find("table", class_ = "table")
tr = table.findAll("tr")

for i  in tr:       # Привоим данные в формат(валюта, курс покупки, курс продажи): [['EUR', '93.5', '94.5'], ...]
    a.append(i.text.strip().split('\n'))

a.pop(0)

for f, g, h in a:
    exchange_rate[f] = [g, h]
exchange_rate.update(KGS = ['1', '1'])# Добавляем к нашему словарю валюту банка, для проведения всех операций вычисления