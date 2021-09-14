import requests
from bs4 import BeautifulSoup

page = requests.get("https://carros.tucarro.com.co/_Desde_145")

soup = BeautifulSoup(page.content, 'html.parser')

[x.extract() for x in soup.findAll('script')]

print(page)
print(soup.prettify())

for link in soup.select('a[class="ui-search-result__content ui-search-link"]'):
    print(link['href'])
    
    car_page = requests.get(link['href'])
    car_soup = BeautifulSoup(car_page.content, 'html.parser')
    [x.extract() for x in car_soup.findAll('script')]
    print(car_soup.prettify() + "######################")

    for value in car_soup.select('span[class="andes-table__column--value"]'):
        print(value.text)

    break
