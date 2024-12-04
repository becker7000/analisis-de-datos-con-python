import numpy as np

matriz = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(f"Matriz: \n{matriz}")

print("\nFilas: ")
for fila in matriz:
    print(fila)

print("\n Elementos de la matriz: ")
for i in matriz:
    print("")
    for j in i:
        print(f"\t {j}",end="")