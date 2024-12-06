import matplotlib.pyplot as plt
import numpy as np  

# Crear datos de ejemplo
x = np.linspace(0, 10, 100)  # 100 puntos entre 0 y 10
y = np.sin(x)  # Seno de cada valor de x

# Crear el gráfico
plt.plot(x, y, label='Seno(x)', color='b', linestyle='-', linewidth=2)

# Añadir título y etiquetas
plt.title('Gráfico de la función Seno')
plt.xlabel('x')
plt.ylabel('y')

# Mostrar leyenda
plt.legend()

# Mostrar cuadrícula
plt.grid(True)

# Mostrar el gráfico
plt.show()
