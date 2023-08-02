import requests
from bs4 import BeautifulSoup as BS

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}

url = "https://www.ilmateenistus.ee/ilm/ilmavaatlused/vaatlusandmed/oopaevaandmed/"

r = requests.get(url, headers=headers)

soup = BS(r.content, 'html.parser')

table = soup.find('div', class_="float-thead-table-container")
# print(table)

name_all = table.find('thead')
# print(name_all)

name = name_all.find_all('th')
# print(name)

for th in name:
     row = table.find_all('tr')
     #print(row)

# ilm = table.find_all('th', colspan="2")
# print(ilm)



