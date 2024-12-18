# Importamos las bibliotecas necesarias
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Cargar el CSV en un DataFrame de Pandas
file_path = '2024-10.csv'  # Reemplaza con la ruta de tu archivo CSV
df = pd.read_csv(file_path)  # Cargamos el archivo CSV

# 2. Transformación de datos:
# Convertimos las columnas 'Fecha_Retiro' y 'Hora_Retiro' a un único objeto datetime
df['Fecha_Retiro'] = pd.to_datetime(df['Fecha_Retiro'] + ' ' + df['Hora_Retiro'], format='%d/%m/%Y %H:%M:%S')
df['Fecha_Arribo'] = pd.to_datetime(df['Fecha_Arribo'] + ' ' + df['Hora_Arribo'], format='%d/%m/%Y %H:%M:%S')

# 3. Manejo de valores faltantes (si los hay):
# Eliminamos filas donde faltan los valores de 'Edad_Usuario', 'Genero_Usuario' y 'Bici'
df = df.dropna(subset=['Edad_Usuario', 'Genero_Usuario', 'Bici'])

# 4. Codificar variables categóricas:
# Usamos LabelEncoder para convertir las categorías de 'Genero_Usuario' en números
label_encoder = LabelEncoder()
df['Genero_Usuario'] = label_encoder.fit_transform(df['Genero_Usuario'])

# 5. Crear nuevas características:
# Calculamos la duración del viaje en minutos
df['Duracion_Viaje'] = (df['Fecha_Arribo'] - df['Fecha_Retiro']).dt.total_seconds() / 60

# 6. Selección de características (X) y la variable objetivo (y)
X = df[['Genero_Usuario', 'Duracion_Viaje']]  # Características: género y duración del viaje
y = df['Edad_Usuario']  # Variable objetivo: edad del usuario

# 7. División de los datos en conjunto de entrenamiento y conjunto de prueba (80% - 20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 8. Entrenar y evaluar modelos:

# Modelo 1: Regresión Lineal
linear_model = LinearRegression()  # Creamos un modelo de regresión lineal
linear_model.fit(X_train, y_train)  # Entrenamos el modelo con los datos de entrenamiento

# Predicciones con el modelo de Regresión Lineal
y_pred_linear = linear_model.predict(X_test)

# Evaluación del modelo de Regresión Lineal
mse_linear = mean_squared_error(y_test, y_pred_linear)  # Error cuadrático medio
r2_linear = r2_score(y_test, y_pred_linear)  # Coeficiente de determinación R²

print(f"Regresión Lineal - MSE: {mse_linear:.2f}, R²: {r2_linear:.2f}")

# Modelo 2: Árbol de Decisión
tree_model = DecisionTreeRegressor(random_state=42)  # Creamos un modelo de Árbol de Decisión
tree_model.fit(X_train, y_train)  # Entrenamos el modelo con los datos de entrenamiento

# Predicciones con el modelo de Árbol de Decisión
y_pred_tree = tree_model.predict(X_test)

# Evaluación del modelo de Árbol de Decisión
mse_tree = mean_squared_error(y_test, y_pred_tree)  # Error cuadrático medio
r2_tree = r2_score(y_test, y_pred_tree)  # Coeficiente de determinación R²

print(f"Árbol de Decisión - MSE: {mse_tree:.2f}, R²: {r2_tree:.2f}")

# 9. Comparación de los modelos:
# Graficamos la comparación entre los valores reales y las predicciones

plt.figure(figsize=(10, 6))

# Gráfica de comparación para el modelo de Regresión Lineal
plt.scatter(y_test, y_pred_linear, color='blue', label='Regresión Lineal', alpha=0.6)

# Gráfica de comparación para el modelo de Árbol de Decisión
plt.scatter(y_test, y_pred_tree, color='green', label='Árbol de Decisión', alpha=0.6)

# Línea diagonal que representa las predicciones perfectas
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', linestyle='--')

# Etiquetas y título
plt.xlabel('Edad Real')
plt.ylabel('Edad Predicha')
plt.title('Comparación entre modelos de Regresión Lineal y Árbol de Decisión')

# Leyenda
plt.legend()

# Mostrar el gráfico
plt.show()
