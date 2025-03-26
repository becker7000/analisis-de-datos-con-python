import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargamos el CSV
file_path = '2024-11.csv'
df = pd.read_csv(file_path)

# print(df)

# Transformación de los datos (EDA):
df['Fecha_Retiro'] = pd.to_datetime(df['Fecha_Retiro']+' '+df['Hora_Retiro'],format='%d/%m/%Y %H:%M:%S')
df['Fecha_Arribo'] = pd.to_datetime(df['Fecha_Arribo']+' '+df['Hora_Arribo'],format='%d/%m/%Y %H:%M:%S')

# Resumen estadistico:
print(df['Edad_Usuario'].describe())

# Análisis de la distribución de géneros de los usuarios:
gender_counts = df['Genero_Usuario'].value_counts().reset_index()
gender_counts.columns = ['Genero_Usuario','count']

# print(gender_counts)

# Análisis de la distribución de género...
plt.figure(figsize=(6,4))
sns.barplot(x='Genero_Usuario', y='count', data = gender_counts)
plt.title('Distribución de género de los usuarios de Ecobici en noviembre 2024')
plt.xlabel('Género')
plt.ylabel('Número de usuarios')
plt.show()

# Obteniendo las bicicletas más usadas:
top_bikes = df['Bici'].value_counts().head(75).reset_index()
top_bikes.columns = ['Bici','count']

plt.figure(figsize=(10,6))
sns.barplot(x='Bici',y='count',data=top_bikes, palette='Set1')
plt.title('Top 75 bicicletas más usadas en Ecobici en noviembre 2024')
plt.xlabel('Bici')
plt.ylabel('Cantidad de uso')
plt.xticks(rotation=60) # Inclinamos las etiquetas
plt.show()







