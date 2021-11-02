import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn import metrics

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

"""
This module creates a Decision Tree Regressor model to predict the car prices.
Input: a CSV with the car data. 
The CSV file MUST contain the following labels: Marca, Modelo, Anio, Tipo de carroceria, Tipo de combustible, Color
"""

df = pd.read_csv('full_data_final.csv')

y = df.Precio

# atributos = ['Marca', 'Modelo','Anio', 'Kilometros', 'Color', 'Transmision', 'Tipo de combustible', 'Motor', 'Puertas']
atributos = ['Marca', 'Modelo','Anio', 'Tipo de carroceria', 'Tipo de combustible', 'Color']

X = df[atributos]

X = pd.get_dummies(X)

train_x, val_x, train_y, val_y = train_test_split(X, y, test_size=0.33, random_state=1)

model = DecisionTreeRegressor(random_state=1)
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
plt.savefig('out_modelo1.png')

print(len(val_y))
print(f"MAE: {val_mae}")
print(f"MSE: {val_mse}")
print(f"R^2: {val_r2}")