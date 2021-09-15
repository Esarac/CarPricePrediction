from helium import *
from bs4 import BeautifulSoup
import pandas as pd

browser = start_firefox(headless = True)

#columnsname = ['NOMBRE', 'SUBTITULO', 'PRECIO', 'PRECIO MENSUAL', 'KILOMETRAJE', 'ANIO', 'ESTADO', 'UBICACIÓN', 'PLACA', 'TIPO DE CAJA', 'CILINDRAJE', 'COMBUSTIBLE',  'COLOR', 'AIRBAGS', 'DIRECCIÓN', 'CARROCERÍA', 'PUERTAS']
columnsname = ['NOMBRE', 'SUBTITULO', 'PRECIO', 'PRECIO MENSUAL', 'KILOMETRAJE', 'ANIO', 'TIPO DE CAJA', 'CILINDRAJE', 'COMBUSTIBLE', 'COLOR', 'ESTADO', 'UBICACIÓN', 'DIRECCIÓN', 'PLACA', 'PUERTAS', 'AIRBAGS', 'IMAGEN']
allCars = []

for x in range(1, 2):
    url = 'https://www.carroya.com/resultados/automoviles-y-camionetas?page=' + str(x)
    go_to(url)
    soup = BeautifulSoup(browser.page_source, 'html.parser')
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
            print("PAG "+str(x)+", CAR "+str(y-2))
        except AttributeError:
            print("INVALID - PAG "+str(x)+", CAR "+str(1+y))

for c in allCars:
    print(c.keys())

pd.DataFrame.from_dict(data=allCars, orient='columns').to_csv('data.csv', header=True)

kill_browser()

def download_img(x, y, z):
    print(x + '-' + y + '-' + str(z))

def load_img():
    df = pd.read_csv('data.csv')
    for x, y, z in zip(df['NOMBRE'], df['IMAGEN'], df['Unnamed: 0']):
        download_img(x, y, z)