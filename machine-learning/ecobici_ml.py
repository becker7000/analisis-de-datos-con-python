import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Cargamos el CSV
file_path = '2024-11.csv'
df = pd.read_csv(file_path)

# Transformación de los datos (EDA):
df['Fecha_Retiro'] = pd.to_datetime(df['Fecha_Retiro']+' '+df['Hora_Retiro'],format='%d/%m/%Y %H:%M:%S')
df['Fecha_Arribo'] = pd.to_datetime(df['Fecha_Arribo']+' '+df['Hora_Arribo'],format='%d/%m/%Y %H:%M:%S')

# Limpieza de datos:
df = df.dropna(subset=['Edad_Usuario','Genero_Usuario','Bici'])

label_encoder = LabelEncoder()
df['Genero_Usuario'] = label_encoder.fit_transform(df['Genero_Usuario'])

# Calculamos la duración de los viajes:
df['Duracion_Viaje'] = (df['Fecha_Arribo']-df['Fecha_Retiro']).dt.total_seconds()/60

# Selección de caracteristicas (X) y variables objetivo (y)
X = df[['Genero_Usuario','Duracion_Viaje']]
y = df['Edad_Usuario']

# 80% entrenamiento y 20% prueba
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

# Entrenamos y evaluamos los modelos:
linear_model = LinearRegression()
linear_model.fit(X_train,y_train)

# Predicción con el modelo de regresión lineal
y_pred_linear = linear_model.predict(X_test)

#Evaluando:
mse_linear = mean_squared_error(y_test,y_pred_linear) # Error cuadratico medio
r2_linear = r2_score(y_test,y_pred_linear) # Coeficiente de determinación R²

# windows + .
print(f"Regresion lineal MSE: {mse_linear:.2f}, R²: {r2_linear:.2f}")

plt.figure(figsize=(10,6))
plt.scatter(y_test,y_pred_linear,color='blue',label='Regresión lineal', alpha=0.6)

plt.plot([y_test.min(),y_test.max()],[y_test.min(),y_test.max()],color='red',linestyle='--')

plt.title('Comparación entre el modelo de regresión lineal y ...')
plt.xlabel('Edad real')
plt.xlabel('Edad predicha')

plt.legend()
plt.show()