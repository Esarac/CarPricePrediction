import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn import metrics

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

df = pd.read_csv('full_data.csv')

df = df.fillna('NA')

print(df.info())

y = df.Precio

atributos = ['Marca', 'Modelo','Anio', 'Kilometros', 'Color', 'Transmision', 'Tipo de combustible',
            'Motor', 'Puertas']

X = df[atributos]

X = pd.get_dummies(X)

train_x, val_x, train_y, val_y = train_test_split(X, y, random_state=1)

print(train_x.head())

model = DecisionTreeRegressor(random_state=1)
model.fit(train_x, train_y)

val_pred = model.predict(val_x)
val_mae = metrics.mean_absolute_error(val_pred, val_y)

x1 = list(range(0,90))
y1 = val_pred[:90]
y2 = val_y[:90]

plt.plot(x1, y1)
plt.plot(x1, y2)
plt.show()
plt.savefig('out.png')

print(len(val_y))
print(f"Validation mae: {val_mae}")