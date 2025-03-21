import matplotlib.pyplot as plt
import seaborn as sns # Modulo para la visualización de datos

dataframe_flores = sns.load_dataset('iris')

# print(dataframe_flores)

# Mostrando solamente las 5 primeras filas:
print(dataframe_flores.head())

# Mostrando información acerca de un conjunto:
# Metadatos del dataframe
dataframe_flores.info()

# Descripción estadistica:
print(dataframe_flores.describe())

# Recolectando y contando los valores que son nulos:
print(dataframe_flores.isnull().sum())

# Generando un histograma sobre las distribuciones de los datos
dataframe_flores.hist(figsize=(10,8),bins=20)
plt.suptitle('Distribución de las variables numéricas')
plt.show()

# Boxplot para detectar valores dificiles de analizar
# Ver la pelicula: BigShort
sns.boxplot(data=dataframe_flores, orient="h")
plt.title('Boxplot de las variables númericas')
plt.show()

# Matriz para las correalaciones entre las variables
correlacion_matriz = dataframe_flores.select_dtypes(include=['float64','int64']).corr()
#print(correlacion_matriz)
plt.figure(figsize=(8,6))
sns.heatmap(correlacion_matriz,annot=True,cmap='coolwarm',fmt='.2f')
plt.title('Matriz de correlación')
plt.show()

# Análisis de una distribución de las especies:
sns.countplot(x='species',data=dataframe_flores)
plt.title('Distribución de las especies de las flores')
plt.show()

"""
El analisis exploratorio de datos (EDA)
Obtener estadisticas o datos clave (indicadores) acerca de conjuntos de datos

Tarea: Generar un analisis de datos exploratorio 
         para un conjunto de datos...

"""