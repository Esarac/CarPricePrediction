"""Web scraping script

This script allows the user to scrape data from https://carroya.com using helium and BeautifulSoup. 
For efficiency, this script can run using multiple threads (The number of threads used is defined by 
the constant THREAD_QUANTITY) and uses pandas to export the data obtained on a CSV file.

The script requires the browser Firefox installed on the machine.
"""

from multiprocessing import Pool
from time import sleep
from helium import *
from bs4 import BeautifulSoup
import pandas as pd
import multiprocessing as mp
import requests
import shutil
import os

# --------------------Constants--------------------
COLUMNS_NAME = ['NOMBRE', 'SUBTITULO', 'PRECIO', 'PRECIO MENSUAL', 'KILOMETRAJE', 'ANIO', 'TIPO DE CAJA', 'CILINDRAJE', 'COMBUSTIBLE', 'COLOR', 'ESTADO', 'UBICACIÓN', 'DIRECCIÓN', 'PLACA', 'PUERTAS', 'AIRBAGS', 'ID']
THREAD_QUANTITY = 4 #int(mp.cpu_count() / 2)  # Change to apply a different number of threads
PAGE_QUANTITY = 688 # 688 is the actual number of pages in this website


# --------------------Methods--------------------
def get_data(threadNumber):
    """
    Goes to https://carroya.com and start scraping the information of the cars 
    page by page until the last one. Access the detail page of each car and store 
    the data obtained on a dictionary. Downloads the image of the car calling 
    the function download_img(). Finally, store each dict in a list and returns it.

    Args:
        threadNumber (int): The number of threads that the algorithm is going to use.
    
    Returns:
        list: A list of dict containing the data obtained from the website.
    """
    errors = 0
    browser = start_firefox(headless=True)
    allCars = []

    for x in range(threadNumber, (PAGE_QUANTITY + 1), THREAD_QUANTITY):
        url = 'https://www.carroya.com/resultados/automoviles-y-camionetas?page=' + str(x)

        go_to(url)
        sleep(3)
        soup = BeautifulSoup(browser.page_source, 'html.parser')
        Button('Download').exists
        cars = soup.find_all('div', class_='contentCurrentCard')

        for y in range(3, len(cars)):
            try:
                car = cars[y]
                carTemp = {}

                for g in COLUMNS_NAME:
                    carTemp[g] = ''

                # Data
                carTemp['NOMBRE'] = car.find('h3', class_='h3P titleCard').text
                carTemp['SUBTITULO'] = car.find('h4', class_='subtitleCard').text
                carTemp['PRECIO'] = car.find('h2', class_='h2P priceCard').text
                carTemp['PRECIO MENSUAL'] = car.find('h3', class_='mounthlyPriceCard').text
                carTemp['ID'] = str(x) +"_"+str(y - 2)

                # Car Detail Page
                detailUrl = 'https://www.carroya.com' + car.find('a', href=True)['href']

                go_to(detailUrl)
                sleep(1)
                detail = BeautifulSoup(browser.page_source, 'html.parser')

                features = detail.find('div', class_='features')

                names = features.find_all('h5', class_='name')
                descriptions = features.find_all('h4', class_='description')

                # Data
                carTemp['KILOMETRAJE'] = detail.find('h3', class_='h3P kilometers').text
                carTemp['ANIO'] = detail.find('h3', class_='h3P year').text

                for c in range(len(names)):
                    if names[c].text in set(COLUMNS_NAME):
                        carTemp[names[c].text] = str(descriptions[c].text)

                allCars.append(carTemp)

                # Download Image
                download_img(car.find('img', class_='imageCard')['src'], carTemp['ID'])
                
                # Print
                print("PAG " + str(x) + ", CAR " + str(y - 2))
            except:
                #Print
                print("ERROR - PAG " + str(x) + ", CAR " + str(1 + y))
                errors = errors + 1
    #Print
    print("Thread " + str(threadNumber) + " errors: " + str(errors))

    kill_browser()

    return allCars


def download_img(image, id):
    """
    Downloads an image using the provided URL and the name.

    Args:
        image (str): The url of the image to download.
        id (str): The name of the image.
    """
    try:
        response = requests.get(image)

        file = open('images/' + str(id) + '.jpg', 'wb')
        file.write(response.content)
        response.close()
        file.close()

        #Print
        print("IMG " + str(id))
    except:
        #Print
        print("ERROR - IMG" + str(id))

if __name__ == "__main__":
    # --------------------Logic--------------------
    pool = Pool(THREAD_QUANTITY)

    # CSV & IMG
    shutil.rmtree('images')
    os.mkdir('images')
    cMap = pool.map_async(get_data, range(1, THREAD_QUANTITY + 1))
    carsMatrix = cMap.get()

    allCars = []
    for c in carsMatrix:
        allCars += c

    pd.DataFrame.from_dict(data=allCars, orient='columns').to_csv('carroya_data.csv', header=True)