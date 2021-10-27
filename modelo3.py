import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn import metrics

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

import xgboost as xgb

df = pd.read_csv('full_data.csv')

df['Kilometros'] = df['Kilometros'].fillna('-1')
df['Kilometros'] = df['Kilometros'].astype(int)
df = df[df['Kilometros'] > 0]
df = df.fillna('NA')

df = df[df['Precio'] < 200000000]

df['Marca'] = df['Marca'].apply(lambda str : str.upper())
df['Modelo'] = df['Modelo'].apply(lambda str : str.upper())


df = df[df['Precio'] > 3000000]

print(df.info())

y = df.Precio


atributos = ['Marca', 'Modelo','Anio', 'Kilometros', 'Color', 'Transmision', 'Tipo de combustible', 'Puertas', 'Motor']

# atributos = ['Marca', 'Modelo','Anio', 'Kilometros']

X = df[atributos]

X = pd.get_dummies(X)

train_x, val_x, train_y, val_y = train_test_split(X, y, test_size = 0.33, random_state=1)

print(train_x.head())

model = RandomForestRegressor(random_state=1, n_estimators=32, verbose=10)
model.fit(train_x, train_y)

val_pred = model.predict(val_x)

val_mae = metrics.mean_absolute_error(val_y, val_pred)
val_mse = metrics.mean_squared_error(val_y, val_pred)
val_r2 = metrics.r2_score(val_y, val_pred)

x1 = list(range(0,90))
y1 = val_pred[:90]
y2 = val_y[:90]

plt.plot(x1, y1)
plt.plot(x1, y2)
plt.show()
plt.savefig('out.png')

print(len(val_y))
print(f"MAE: {val_mae}")
print(f"MSE: {val_mse}")
print(f"R^2: {val_r2}")