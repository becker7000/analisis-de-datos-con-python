import matplotlib.pyplot as plt
import numpy as np

# Solicitamos la pendiente y la ordenada al origen:
m = float(input("\n\t Escribe la pendiente (m): "))
b = float(input("\n\t Escribe la ordenada al origen (b): "))

# Generando un arreglo con 180 datos entre -10 y 20
x = np.linspace(-10, 20, 180)

# Calculamos los valores de y usando la ecuación cónica de la recta:
y = m * x + b  # 180 valores también

# Crear la gráfica:
# Estilos de línea: - (continua), : (punteada), -. (combinada), -- (guionada)
# Colores: r (rojo), g (verde), b (azul)
line1, = plt.plot(x, y, label=f'y = {m}x + {b}', color='#4c801a', linestyle='-', linewidth=4) # Color verde

# Modificamos la recta
y = 0.5*x + b
line2, = plt.plot(x, y, label=f'y = {m / 2}x + {b / 2}', color='#b4b4b4', linestyle='-', linewidth=4) # Color gris

plt.legend()

# Añadimos título y etiquetas:
plt.title("Gráfica de una línea recta")
plt.xlabel('x')
plt.ylabel('y')

# Añadimos la leyenda, asegurando que los colores coincidan con las líneas
# plt.legend(handles=[line1, line2])

# Activamos la cuadrícula
plt.grid(True)

# Mostramos la gráfica
plt.show()
