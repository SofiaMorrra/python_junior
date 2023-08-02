import requests
from bs4 import BeautifulSoup as BS

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}

eur_btc_link = 'https://www.google.com/search?q=eur+to+btc&oq=eur+to+btc&aqs=chrome..69i57j0i512j0i22i30l8.10261j0j7&sourceid=chrome&ie=UTF-8'

r = requests.get(eur_btc_link, headers=headers)

soup = BS(r.content, 'html.parser')

match = soup.find('span', class_="pclqee")
print(match)

exchange_rate = float(match.text.replace(',', '.'))

user_sum = float(input('Please enter amount in EUR: '))
print(user_sum * exchange_rate, 'BTC')
user_sum = float(input('Please enter amount in BTC: '))
print(user_sum / exchange_rate, 'EUR')