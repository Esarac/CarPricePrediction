import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn import metrics

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

import xgboost as xgb

df = pd.read_csv('full_data.csv')

df = df.fillna('NA')

print(df.info())

df = df[df['Precio'] < 100000000]

y = df.Precio


atributos = ['Marca', 'Modelo','Anio', 'Kilometros', 'Color', 'Transmision', 'Tipo de combustible',
            'Motor', 'Puertas']

X = df[atributos]

X = pd.get_dummies(X)

train_x, val_x, train_y, val_y = train_test_split(X, y, test_size = 0.33, random_state=1)

print(train_x.head())

xgbr = xgb.XGBRegressor()
print(xgbr)

xgbr.fit(train_x, train_y)

score = xgbr.score(train_x, train_y)

print(f"Training score: {score}")

val_pred = xgbr.predict(val_x)
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