import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import re
import random

from sklearn import metrics

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

import xgboost as xgb
from lightgbm import LGBMRegressor

df = pd.read_csv('full_data.csv')
df = df.rename(columns = lambda x:re.sub('[^A-Za-z0-9_]+', '', x))

df['Kilometros'] = df['Kilometros'].fillna('-1')
df['Kilometros'] = df['Kilometros'].astype(int)
df = df[df['Kilometros'] > 0]
df = df.fillna('NA')

df = df[df['Precio'] < 200000000]

df = df[df['Precio'] > 3000000]

print(df.info())

y = df.Precio

y = np.log(y)

# atributos = ['Marca', 'Modelo','Anio', 'Kilometros', 'Color', 'Transmision', 'Tipo de combustible', 'Puertas', 'Motor']

atributos = ['Marca', 'Modelo','Anio', 'Kilometros']

X = df[atributos]

X = pd.get_dummies(X)

X = X.rename(columns = lambda x:re.sub('[^A-Za-z0-9_]+', str(random.randint(0, 1000)), x))

train_x, val_x, train_y, val_y = train_test_split(X, y, test_size = 0.2, random_state=1)

print(train_x.head())

model = LGBMRegressor(learning_rate=0.5, n_estimators=300)
model.fit(train_x, train_y)

val_pred = model.predict(val_x)

val_y = np.exp(val_y)
val_pred = np.exp(val_pred)

val_mae = metrics.mean_absolute_error(val_y, val_pred)
val_mse = metrics.mean_squared_error(val_y, val_pred)
val_r2 = metrics.r2_score(val_y, val_pred)

x1 = list(range(0,90))
y1 = val_pred[:90]
y2 = val_y[:90]

# plt.plot(x1, y1)
# plt.plot(x1, y2)
# plt.show()
# plt.savefig('out.png')

print(len(val_y))
print(f"MAE: {val_mae}")
print(f"MSE: {val_mse}")
print(f"R^2: {val_r2}")