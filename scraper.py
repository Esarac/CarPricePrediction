import requests
from bs4 import BeautifulSoup


for year in range(2000, 2010):

    print("###############" + str(year) + "################")

    for num in range(0, 2000, 47):

            print("&&&&&&&&&&&&&&&&&&&&" + str(num) + "&&&&&&&&&&&&&&&&&&&&&&")

            page = requests.get(f"https://carros.tucarro.com.co/{year}/_Desde_{num}")
            soup = BeautifulSoup(page.content, 'html.parser')

            for link in soup.select('a[class="ui-search-result__content ui-search-link"]'):
                
                car_page = requests.get(link['href'])
                car_soup = BeautifulSoup(car_page.content, 'html.parser')

                for title in car_soup.select('h1[class="ui-pdp-title"]'):
                    print(title.text)

                for value in car_soup.select('span[class="andes-table__column--value"]'):
                    print(value.text)

                for price in car_soup.select('span[class="price-tag-fraction"]'):
                    print(price.text)

