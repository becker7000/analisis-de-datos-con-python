import numpy as np

# Unidimensional
arreglo_inicial = np.array([1,2,3,4,5,6,7,8])

# (filas, columnas) bidimensional
arreglo_redimen = arreglo_inicial.reshape(2,4)

print(f" Arreglo inicial: {arreglo_inicial}")

print(f" Arreglo redimensionado:\n{arreglo_redimen} ")
