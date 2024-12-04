import numpy as np

gastos = np.array([3400,6800,2400,7300,1500,2900,4500,3500])
# 6900 -> 3450

# Media aritmetica
print(f" Media aritmetica: $ {np.mean(gastos):.3f} ")

# Mediana
print(f" Mediana: $ {np.median(gastos)} ")

# Desviación estandar
print(f" Desviación estandar: $ {np.std(gastos):.3f}")
