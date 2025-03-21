import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargamos el conjunto de datos:
dataframe_titanic = sns.load_dataset('titanic')

# Mostramos el dataframe:
# print(dataframe_titanic)

# Conteo de sobrevivientes:
sns.countplot(x='survived', data = dataframe_titanic)
plt.title('Conteo de sobrevivientes (0=No, 1=Sí)')
plt.show()

# Distribución de la edad:
sns.histplot(dataframe_titanic['age'].dropna(),kde=True,bins=30)
plt.title('Distribución de las edades')
plt.show()

# Relación entre la clase y la supervivencia:
sns.countplot(x='class',hue='survived', data=dataframe_titanic)
plt.title('Sobrevivientes por clase de Titanic')
plt.show()

# Relación entre el género y sobrevivientes:
sns.countplot(x='sex',hue='survived', data=dataframe_titanic)
plt.title('Sobrevivientes por género')
plt.show()

"""

Otro sets de seaborn:
tips, flights, diamonds, penguins, exercise, car crashes, planets

Hacer EDA de los sets anteriores...
Truquito es imprimirlo primero para dar un vistazo general...

"""