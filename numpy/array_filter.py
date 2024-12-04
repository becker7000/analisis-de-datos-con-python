import numpy as np

ventas_autos = np.array([5,7,3,11,7,4,6,8,10,12])

# Filtro de ventas:
arreglo_filtrado = ventas_autos[ventas_autos>=5]
print(f" Ventas mayores o iguales que 5: {arreglo_filtrado}")

arreglo_filtrado_2 = ventas_autos[ventas_autos%2==1]
arreglo_filtrado_3 = arreglo_filtrado_2[arreglo_filtrado_2>4]
print(f" Ventas impares mayores que 4: {arreglo_filtrado_3}")

"""
    Filtrar las ventas que fueron un número impar mayor a 4
    Termina a las 8:10 PM
"""