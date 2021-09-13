from helium import *
from bs4 import BeautifulSoup

browser = start_firefox(headless = True)

columnsname = ['NOMBRE', 'SUBTITULO', 'PRECIO', 'PRECIO MENSUAL', 'ESTADO', 'KILOMETRAJE', 'ANIO', 'UBICACION', 'PLACA', 'TIPO DE CAJA', 'CILINDRAJE', 'COMBUSTIBLE',  'COLOR', 'AIRBAGS', 'DIRECCION']

for x in range(1, 3):
    url = 'https://www.carroya.com/resultados/automoviles-y-camionetas?page=' + str(x)
    print(url)
    go_to(url)
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    cars = soup.find_all('div', class_='contentCurrentCard')

    for y in range(4, 6):
        car = cars[y]
        carTemp = {}

        for g in columnsname:
            carTemp[g] = ''

        #Data
        carTemp['NOMBRE'] = car.find('h3', class_='h3P titleCard').text
        carTemp['SUBTITULO'] = car.find('h4', class_='subtitleCard').text
        carTemp['PRECIO'] = car.find('h2', class_='h2P priceCard').text
        carTemp['PRECIO MENSUAL'] = car.find('h3', class_='mounthlyPriceCard').text

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
            carTemp[names[c].text] = descriptions[c].text
        
        print(carTemp.values())
        
kill_browser()