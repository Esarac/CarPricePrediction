from helium import *
from bs4 import BeautifulSoup

url = 'https://www.carroya.com/resultados/automoviles-y-camionetas?page=50'
browser = start_firefox(url, headless = True)
soup = BeautifulSoup(browser.page_source, 'html.parser')
cars = soup.find_all('div', class_='contentCurrentCard')

for car in cars:
    title = car.find('h3', class_='h3P titleCard').text
    subtitle = car.find('h4', class_='subtitleCard').text
    tagsCard = car.find('div', class_='tagsCard').text
    fullPrice = car.find('h2', class_='h2P priceCard').text
    monthlyPrice = car.find('h3', class_='mounthlyPriceCard').text
    #info = [title, subtitle, tagsCard, fullPrice, monthlyPrice]
    #print(info)
    detailUrl = 'https://www.carroya.com' + car.find('a', href = True)['href']
    browserDetail = start_firefox(detailUrl, headless = True)
    detail = BeautifulSoup(browserDetail.page_source, 'html.parser')
    features = detail.find('div', class_='features')
    descriptions = features.find_all('h4', class_='description')