import matplotlib.pyplot as plt
import numpy as np

corredores = np.array([35,22,10,4])
distancias = np.array(["5K","10K","21K","42K"])
paleta = ["#b89e37","#328f28","#539cb0","#8c70c2"]

plt.title("Distancias que puede correr el grupo A")
plt.pie(corredores,labels=distancias,colors=paleta,explode=[0.1,0.1,0.1,0.1],shadow=True)
plt.legend(title="Colores",loc='upper right')
plt.show()