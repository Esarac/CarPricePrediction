import json
import urllib
import requests

import pandas as pd

url = 'https://parseapi.back4app.com/classes/Carmodels_Car_Model_List?limit=10000'
headers = {
    'X-Parse-Application-Id': 'g9wD2krxQHnVy58PPyPLalkd95NBNmpjbCkTbXKt', # This is your app's application id
    'X-Parse-REST-API-Key': 'EUiBIVtXZojVmsrhEwQXInTP5oEGvIWzZNN4JmWv' # This is your app's REST API key
}
data = json.loads(requests.get(url, headers=headers).content.decode('utf-8')) # Here you have the data that you need
print(json.dumps(data, indent=2))

print(data)
print("###########################################")

x = data['results']

for item in x:
    print(item['Make'])

df = pd.DataFrame(x)

print(df.head())

df.to_csv('model_data.csv', sep=';')

# print(data['results'])