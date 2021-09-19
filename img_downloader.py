import pandas as pd
import os
import urllib.request

from multiprocessing import Pool

"""
This module contains all the tools needed to download images from csv files
"""

def download_image(name, url):

    """
    Dowloads a single image and saves it as a JPG file with the given name

    Parameters:
    name (str): The name that the image will be saved as
    url (str): The url that contains the image to be saved 
    """
    urllib.request.urlretrieve(url, f'img/{name}.jpg')
    print(f"downloaded {name}")

def download_csv_imgs(filepath):

    """
    Downloads the images in parallel from the csv specified.

    Parameters:
    filepath (str): The filepath to the data file (must be a csv file)

    NOTE: The csv file must have a column named 'Img' with the links to the images 
    """

    df = pd.read_csv(filepath)
    print(df.head())

    print(df['Img'].size)

    if not os.path.exists('img'):
        os.mkdir('img')

    img_urls = []

    for i in range(0, df['Img'].size):
        img_urls.append( (i, df['Img'][i]) )

    pool = Pool(4)

    result = pool.starmap(download_image, img_urls)

if __name__ == '__main__':
    download_csv_imgs('tucarro_data.csv')
