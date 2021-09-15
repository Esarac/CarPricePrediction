from multiprocessing import Pool
from time import sleep
from helium import *
from bs4 import BeautifulSoup
import pandas as pd
import multiprocessing as mp
import requests

#--------------------Constants--------------------
THREAD_QUANTITY = int(mp.cpu_count()/2) #Change to apply a different number of threads
PAGE_QUANTITY = 688 #688 is the actual number of pages in this website

#--------------------Methods--------------------
def get_data(columnsname, threadNumber):

    errors = 0
    browser = start_firefox(headless = True)
    allCars = []

    for x in range(threadNumber, (PAGE_QUANTITY + 1), THREAD_QUANTITY):
        url = 'https://www.carroya.com/resultados/automoviles-y-camionetas?page=' + str(x)
        go_to(url)
        soup = BeautifulSoup(browser.page_source, 'html.parser')
        sleep(3)
        cars = soup.find_all('div', class_='contentCurrentCard')

        for y in range(3,len(cars)):
            try:
                car = cars[y]
                carTemp = {}

                for g in columnsname:
                    carTemp[g] = ''

                #Data
                carTemp['NOMBRE'] = car.find('h3', class_='h3P titleCard').text
                carTemp['SUBTITULO'] = car.find('h4', class_='subtitleCard').text
                carTemp['PRECIO'] = car.find('h2', class_='h2P priceCard').text
                carTemp['PRECIO MENSUAL'] = car.find('h3', class_='mounthlyPriceCard').text
                carTemp['IMAGEN'] = car.find('img', class_='imageCard')['src']

                #Car Detail Page
                detailUrl = 'https://www.carroya.com' + car.find('a', href = True)['href']
                go_to(detailUrl)
                detail = BeautifulSoup(browser.page_source, 'html.parser')
                sleep(1)
                features = detail.find('div', class_='features')

                names = features.find_all('h5', class_='name')
                descriptions = features.find_all('h4', class_='description')

                #Data
                carTemp['KILOMETRAJE'] = detail.find('h3', class_='h3P kilometers').text
                carTemp['ANIO'] = detail.find('h3', class_='h3P year').text

                for c in range(len(names)):
                    if names[c].text in set(columnsname):
                        carTemp[names[c].text] = str(descriptions[c].text)

                allCars.append(carTemp)
                print("PAG "+str(x)+", CAR "+str(y-2))#Print actual car
            except AttributeError:
                print("INVALID - PAG "+str(x)+", CAR "+str(1+y))#Print actual cars (invalid)
                errors = errors + 1

    print("Thread "+str(threadNumber)+" errors: "+ str(errors))#Print errors in thread

    kill_browser()

    return allCars

def download_img(name, image, index):#Deberiamos Quitar el nombre
    print(str(index) + '_' + name)
    response = requests.get(image)
    
    file = open('images/' + str(index) + '_' + name + '.jpg', 'wb')
    file.write(response.content)
    response.close()
    file.close()

def load_img(threadNumber):
    df = pd.read_csv('carroya_data.csv')
    for x in range(threadNumber, len(df), THREAD_QUANTITY):
        download_img(df['NOMBRE'].values[x], df['IMAGEN'].values[x], df['Unnamed: 0'].values[x])
    # for x, y, z in zip(df['NOMBRE'], df['IMAGEN'], df['Unnamed: 0']):
    #     download_img(x, y, z)

if __name__ == "__main__":
    #--------------------Logic--------------------
    pool = Pool(THREAD_QUANTITY)

    #CSV
    columnsname = ['NOMBRE', 'SUBTITULO', 'PRECIO', 'PRECIO MENSUAL', 'KILOMETRAJE', 'ANIO', 'TIPO DE CAJA', 'CILINDRAJE', 'COMBUSTIBLE', 'COLOR', 'ESTADO', 'UBICACIÓN', 'DIRECCIÓN', 'PLACA', 'PUERTAS', 'AIRBAGS', 'IMAGEN']
    
    tuples = []
    for t in range(1, THREAD_QUANTITY + 1):
        tuples.append((columnsname, t))

    carsMatrix = pool.starmap(get_data, tuples)
    allCars = []
    for c in carsMatrix:
        allCars += c
    
    pd.DataFrame.from_dict(data=allCars, orient='columns').to_csv('carroya_data.csv', header=True)

    #IMG
    with pool as p:
        p.map(load_img, range(1, THREAD_QUANTITY + 1))