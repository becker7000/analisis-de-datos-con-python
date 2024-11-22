# Abrir el archivo de texto 'ventas.txt' en modo lectura ('r')
with open('ventas.txt', 'r') as file:
    # Leer todas las líneas del archivo y guardarlas en la variable 'lineas'
    lineas = file.readlines()

"""
with <expresión> as <variable>:
# Código que usa <variable>
"""

# Inicializar un diccionario vacío para almacenar los resultados
# El diccionario tendrá la estructura {producto: {'total': total_ventas, 'fechas': lista_de_fechas}}
ventas_por_producto = {}

# Iterar sobre cada línea del archivo
for linea in lineas:
    # Dividir la línea en partes separadas por el delimitador '|'
    partes = linea.split('|')

    # Extraer el nombre del producto (el valor después de 'Producto: ')
    producto = partes[0].split(':')[1].strip()  # El .strip() elimina los espacios innecesarios

    # Extraer la fecha (el valor después de 'Fecha: ')
    fecha = partes[1].split(':')[1].strip()

    # Extraer el precio (el valor después de 'Precio: ') y convertirlo a float (número con decimales)
    precio = float(partes[2].split(':')[1].strip())

    # Extraer la cantidad de unidades (el valor después de 'Unidades: ') y convertirlo a entero (número entero)
    unidades = int(partes[3].split(':')[1].strip())

    # Calcular el total de ventas para esta transacción (precio * unidades)
    total_venta = precio * unidades

    # Verificar si el producto ya existe en el diccionario
    if producto not in ventas_por_producto:
        # Si no existe, inicializamos una entrada con el total de ventas en 0 y una lista vacía de fechas
        ventas_por_producto[producto] = {'total': 0, 'fechas': []}

    # Actualizar el total de ventas del producto (sumar el total de la venta actual)
    ventas_por_producto[producto]['total'] += total_venta

    # Añadir la fecha de la venta a la lista de fechas del producto
    ventas_por_producto[producto]['fechas'].append(fecha)

# Imprimir el resultado final
# Iteramos sobre los productos y mostramos la información recopilada
for producto, datos in ventas_por_producto.items():
    # Imprimir el nombre del producto
    print(f"Producto: {producto}")

    # Imprimir el total de ventas (formateado a dos decimales)
    print(f"Total de ventas: ${datos['total']:.2f}")

    # Imprimir las fechas en las que se realizó la venta (las fechas están en una lista, la unimos con ', ')
    print(f"Fechas de venta: {', '.join(datos['fechas'])}")

    # Separador entre los productos
    print('-' * 30)
