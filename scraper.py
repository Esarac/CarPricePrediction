import requests
import csv

from bs4 import BeautifulSoup
from multiprocessing import Pool

def car_scraper(year_start, year_end):

    data = []

    for year in range(year_start, year_end):

        print("###############" + str(year) + "################")

        for num in range(0, 2000, 47):

            print("&&&&&&&&&&&&&&&&&&&&" + str(num) + "&&&&&&&&&&&&&&&&&&&&&&")

            page = requests.get(f"https://carros.tucarro.com.co/{year}/_Desde_{num}")
            soup = BeautifulSoup(page.content, 'html.parser')

            links = soup.select('a[class="ui-search-result__content ui-search-link"]')

            if not links:
                break

            for link in links:
                
                car_page = requests.get(link['href'])
                car_soup = BeautifulSoup(car_page.content, 'html.parser')

                car_data = []

                for title in car_soup.select('h1[class="ui-pdp-title"]'):
                    car_data.append(title.text)

                for value in car_soup.select('span[class="andes-table__column--value"]'):
                    car_data.append(value.text)

                for price in car_soup.select('span[class="price-tag-fraction"]'):
                    car_data.append(price.text)

                data.append(car_data)
    
    return data

def create_csv():
    pool = Pool(4)

    result = pool.starmap(car_scraper, [(1938, 1958), (1958, 1978), (1978, 1998), (1998, 2008), (2008, 2014), (2014, 2018), (2018, 2022)])

    with open('data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        
        for item in result:
            writer.writerows(item)
        
create_csv()