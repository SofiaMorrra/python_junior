import requests
# from requests.exceptions import HTTPError
from bs4 import BeautifulSoup as BS

#  https://xkcd.com/353/
#  200 - success
#  300 - redirect (nabrali odin adres no nas perekinuli na drugoi)
#  400 - client error
#  500 - server error

# r = requests.get('https://xkcd.com/353/', timeout=3)

# r = requests.get('https://imgs.xkcd.com/comics/python.png', timeout=3)
# with open('python_comic.png', 'wb') as file:
#     file.write(r.content)

# print(r)
# print(dir(r))

# print(r.ok)
# print(r.cookies)
# print(r.headers)
# print(r.headers['Server'])

# for url in ['https://api.github.com', 'https://api.github.com/invalid']:
#     try:
#         response = requests.get(url)
#         response.raise_for_status()
#     except HTTPError as http_err:
#         print(f'HTTP error ocured: {http_err}')
#     else:
#         print(response.content)


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}

url = 'https://www.gammatest.net/course/python/'
full_page = requests.get(url)

# soup = BS(full_page.content, 'html.parser')
# # print(soup)
# # print(soup.title.text)
# # print(soup.prettify())
#
# # print(soup.title.name)
# # match = soup.find('div', class_='pagecontent')
# # print(match)
#
# match = soup.find_all('div', class_='col-md-12 col-sm-12')
# print(match.get_attribute_list('class'))

soup = BS(full_page.content, 'html.parser')
# match = soup.find_all('['a', 'table']')

# match = soup.find_all('a', string='Eesti keeles')
# match = soup.find_all('button', type='button')
# for link in match:
#     print()
#     print(link)


# match = soup.find_all('table')
#
# for table in match:
#     row = table.find_all('tr')
#     cells = []
#     for tr in row:
#         cells = tr.find_all('td')
#         row_cells = []
#         for cell in cells:
#             row_cells.append(cell)
#         cells.append(row_cells)
#
#     print(cells)


match = soup.find_all('table')
link = soup.find('a')
print(link)
# print(link.find_parents('div'))
# print(link.find_previous_sibling())
print(link.find_all_previous())