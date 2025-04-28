import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Datos iniciales
marcas = ['Nissan', 'GM', 'VW', 'Toyota', 'Kia']
ventas_2024_mexico = [255116, 205045, 138181, 121968, 104384]
colores = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0']

# Crear figura y ejes
fig, ax = plt.subplots(figsize=(8, 8))
plt.subplots_adjust(left=0.3, bottom=0.4)  # espacio para sliders

# Dibujar gráfico de pastel inicial
wedges, texts, autotexts = ax.pie(ventas_2024_mexico, labels=marcas, colors=colores, autopct='%1.1f%%', startangle=140)
ax.set_title('Distribución de ventas por marca en México - 2024')

# Crear sliders
sliders = []
for i in range(len(marcas)):
    ax_slider = plt.axes([0.3, 0.3 - i*0.05, 0.6, 0.03])
    # Ajustamos el rango del slider para cubrir el rango de ventas real
    slider = Slider(
        ax_slider,
        label=marcas[i],
        valmin=50000,
        valmax=300000,
        valinit=ventas_2024_mexico[i],
        valstep=1000
    )
    sliders.append(slider)

# Función de actualización
def actualizar(val):
    nuevas_ventas = [slider.val for slider in sliders]
    ax.clear()
    ax.pie(nuevas_ventas, labels=marcas, colors=colores, autopct='%1.1f%%', startangle=140)
    ax.set_title('Distribución de ventas por marca en México - 2024')
    fig.canvas.draw_idle()

# Conectar los sliders con la función
for slider in sliders:
    slider.on_changed(actualizar)

plt.show()
