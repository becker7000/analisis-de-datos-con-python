import matplotlib.pyplot as plt
import numpy as np

amplitud = float(input("Escribe la amplitud: "))
frecuencia = float(input("Escribe la frecuencia: "))

fin = 2*np.pi
x = np.linspace(0, fin ,100)
y = amplitud*np.sin(frecuencia*x) # 2 de amplitud

plt.title("f(x) = sen(x)",color='g')
plt.plot(x,y,color='b')
plt.xlabel('x')
plt.ylabel('y')

plt.grid()
plt.show()