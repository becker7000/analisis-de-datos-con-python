# 1. Creación de arreglos con NumPy
import numpy as np

# Crear un arreglo unidimensional
arr = np.array([1, 2, 3, 4, 5])
print("Arreglo unidimensional:", arr)

# Crear un arreglo bidimensional (matriz)
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("Arreglo bidimensional:\n", arr_2d)

# 2. Operaciones elementales con arreglos
arr = np.array([1, 2, 3])

# Sumar un valor a cada elemento
arr_sum = arr + 2
print("Suma de 2 a cada elemento:", arr_sum)

# Multiplicar cada elemento por un escalar
arr_prod = arr * 3
print("Multiplicación por 3:", arr_prod)

# 3. Generación de arreglos con funciones de NumPy
# Crear un arreglo con números secuenciales (0 a 9)
arr = np.arange(10)
print("Arreglo con arange:", arr)

# Crear un arreglo con números igualmente espaciados
arr_lin = np.linspace(0, 1, 5)  # 5 números entre 0 y 1
print("Arreglo con linspace:", arr_lin)

# 4. Manejo de dimensiones y formas de los arreglos
arr = np.array([1, 2, 3, 4, 5])

# Cambiar la forma de un arreglo
arr_reshaped = arr.reshape((5, 1))
print("Arreglo reconfigurado:\n", arr_reshaped)

# Obtener la forma del arreglo
print("Forma del arreglo:", arr_reshaped.shape)

# 5. Indexación y segmentación de arreglos
arr = np.array([1, 2, 3, 4, 5])

# Acceder a un elemento específico
print("Elemento en índice 2:", arr[2])

# Slicing: Obtener una porción del arreglo
print("Porción del arreglo (índices 1 a 3):", arr[1:4])

# 6. Funciones estadísticas de NumPy
arr = np.array([1, 2, 3, 4, 5])

# Calcular la media, la mediana y la desviación estándar
print("Media:", np.mean(arr))
print("Mediana:", np.median(arr))
print("Desviación estándar:", np.std(arr))

# 7. Operaciones con matrices (producto de matrices)
# Crear matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Producto de matrices
C = np.dot(A, B)
print("Producto de matrices:\n", C)

# 8. Operaciones lógicas con NumPy
arr = np.array([1, 2, 3, 4, 5])

# Comparación y operaciones booleanas
print("¿Es mayor que 2?", arr > 2)

# Filtrar elementos que cumplen una condición
filtered_arr = arr[arr > 2]
print("Elementos mayores que 2:", filtered_arr)

# 9. Generación de números aleatorios
# Crear un arreglo de números aleatorios entre 0 y 1
arr_rand = np.random.rand(3, 3)
print("Matriz de números aleatorios:\n", arr_rand)

# Crear un arreglo de números enteros aleatorios
arr_rand_int = np.random.randint(1, 10, size=(3, 3))
print("Matriz de números enteros aleatorios:\n", arr_rand_int)

# 10. Manejo de valores nulos (NaN)
arr = np.array([1, 2, np.nan, 4, 5])

# Verificar si un elemento es NaN
print("¿Es NaN el tercer elemento?", np.isnan(arr))

# Reemplazar NaN por un valor específico (por ejemplo, 0)
arr[np.isnan(arr)] = 0
print("Arreglo después de reemplazar NaN:", arr)
