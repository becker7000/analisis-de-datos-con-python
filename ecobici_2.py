import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el CSV en un DataFrame de Pandas:
file_path = '2024-10.csv'
df = pd.read_csv(file_path)

# Transformación de datos:
df['Fecha_Retiro'] = pd.to_datetime(df['Fecha_Retiro'] + ' ' + df['Hora_Retiro'], format='%d/%m/%Y %H:%M:%S')
df['Fecha_Arribo'] = pd.to_datetime(df['Fecha_Arribo'] + ' ' + df['Hora_Arribo'], format='%d/%m/%Y %H:%M:%S')

# Resumen estadístico de la columna 'Edad_Usuario':
print(df['Edad_Usuario'].describe())

# Análisis de distribución de géneros:
gender_counts = df['Genero_Usuario'].value_counts().reset_index()
gender_counts.columns = ['Genero_Usuario', 'count']

plt.figure(figsize=(6,4))
sns.barplot(x='Genero_Usuario', y='count', data=gender_counts, palette='Set2')
plt.title('Distribución de género de los usuarios')
plt.xlabel('Género')
plt.ylabel('Número de usuarios')
plt.show()

# Obteniendo las bicicletas más utilizadas:
top_bikes = df['Bici'].value_counts().head(50).reset_index()
top_bikes.columns = ['Bici', 'count']

plt.figure(figsize=(10,6))
sns.barplot(x='Bici', y='count', data=top_bikes, palette='Set1')
plt.title('Top 50 bicicletas más utilizadas de Ecobici en octubre 2024 CDMX')
plt.xlabel('ID Bicicleta')
plt.ylabel('Cantidad de uso')
plt.xticks(rotation=60)  # Rotamos 60° las etiquetas (IDs)
plt.show()
