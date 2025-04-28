import matplotlib.pyplot as plt
import numpy as np
from seaborn import color_palette

autos = np.array(["WRX","Civic","CX-50","RAV4","Forester"])
ventas = np.array([4,12,14,28,17])
paleta = ['red','blue','green','yellow']

# barh para volverla horizontal
plt.bar(autos,ventas,color=paleta)
plt.show()

