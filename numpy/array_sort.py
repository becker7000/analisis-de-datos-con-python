import numpy as np

grupos = np.array([7,3,11,5,8,6,2])
grupos_2d = np.array([[7,4,9],[5,0,3]])

print(f"\n\t Grupos ordenados: {np.sort(grupos)}")
print(f"\n\t Matriz ordenada: \n{np.sort(grupos_2d)}")

enteros = np.array([7,2,9,11,0,-3,6,12])

# Suponemos que el primero es el menor y mayor
menor = enteros[0]
mayor = enteros[0]

for ent in enteros:
    if menor>ent:
        menor=ent
    if mayor<ent:
        mayor=ent

print(f"\n\t Enteros: {enteros}")
print(f"\n\t Elemento menor: {menor}")
print(f"\n\t Elemento mayor: {mayor}")

"""
    Generar un arreglo con al menos 5 elementos
    Y mostrar, cual el menor y mayor elemento...
    Termina: 8:55 PM
"""
