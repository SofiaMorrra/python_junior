import requests
from bs4 import BeautifulSoup as BS

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}

eur_yen_link = 'https://www.google.com/search?client=firefox-b-d&q=yen+to+eur'

r = requests.get(eur_yen_link, headers=headers)

soup = BS(r.content, 'html.parser')

match = soup.find('span', class_='DFlfde SwHCTb')
exchange_rate = float(match.text.replace(',', '.'))
# exchange_rate = float(match['data-value']
user_sum = float(input('Please enter amount in EUR: '))
print(user_sum / exchange_rate, 'YEN')
