# pip install pandas openpyxl

import pandas as pd
from datetime import datetime

# Datos de ejemplo
ventas = [
    {"Producto": "Televisor", "Cantidad": 5, "Precio Unitario": 300, "Fecha": "2024-11-21"},
    {"Producto": "Laptop", "Cantidad": 2, "Precio Unitario": 1200, "Fecha": "2024-11-20"},
    {"Producto": "Teléfono", "Cantidad": 10, "Precio Unitario": 500, "Fecha": "2024-11-19"},
    {"Producto": "Audífonos", "Cantidad": 15, "Precio Unitario": 50, "Fecha": "2024-11-18"},
    {"Producto": "Cámara", "Cantidad": 3, "Precio Unitario": 800, "Fecha": "2024-11-17"}
]

# Crear un DataFrame de pandas con los datos
df = pd.DataFrame(ventas)

# Calcular el total de cada venta (Cantidad * Precio Unitario)
df['Total'] = df['Cantidad'] * df['Precio Unitario']

# Convertir la columna 'Fecha' a tipo datetime para un formato adecuado
df['Fecha'] = pd.to_datetime(df['Fecha'], format='%Y-%m-%d')

# Guardar el DataFrame en un archivo Excel
archivo_excel = 'ventas.xlsx'
df.to_excel(archivo_excel, index=False, engine='openpyxl')

# Agregar una hoja con un resumen (opcional)
with pd.ExcelWriter(archivo_excel, engine='openpyxl', mode='a') as writer:
    resumen = pd.DataFrame({
        "Fecha de Reporte": [datetime.now().strftime('%Y-%m-%d %H:%M:%S')],
        "Total de Ventas": [df['Total'].sum()],
        "Productos Vendidos": [df['Producto'].nunique()]
    })
    resumen.to_excel(writer, sheet_name='Resumen', index=False)

print(f"Archivo Excel '{archivo_excel}' generado exitosamente.")
