import matplotlib.pyplot as plt
import numpy as np

# Solicitar la pendiente y la ordenada al origen
m = float(input("Introduce la pendiente (m): "))
b = float(input("Introduce la ordenada al origen (b): "))

# Generar un rango de valores de x
x = np.linspace(-10, 10, 100)  # Rango de x de -10 a 10 con 100 puntos

# Calcular los valores de y usando la ecuación de la recta
y = m * x + b

# Crear la gráfica
plt.plot(x, y, label=f'y = {m}x + {b}', color='r', linestyle='-', linewidth=2)

# Añadir título y etiquetas
plt.title('Gráfica de la Línea Recta')
plt.xlabel('x')
plt.ylabel('y')

# Mostrar leyenda
plt.legend()

# Mostrar cuadrícula
plt.grid(True)

# Mostrar el gráfico
plt.show()
