import requests

# URL de la Fake Store API
url = "https://fakestoreapi.com/products"

# Realizamos un solicitud con mé_todo HTTP GET
response = requests.get(url)

# Verificamos si la respuesta del request fue exitosa
if response.status_code==200:
    productos = response.json() # Transforma un JSON a un diccionario de Python

    for producto in productos:
        nombre = producto['title']
        categoria = producto['category']
        precio = producto['price']
        print(f"\n\t Producto: {nombre} | Categoria: {categoria} | Precio: $ {precio:.2f}")
else:
    print(f"\n\t Error al obtener los datos, status:{response.status_code} ")

