# Lista de estudiantes con sus calificaciones
estudiantes = [
    {"nombre": "Juan Pérez", "calificacion": 85},
    {"nombre": "Ana Gómez", "calificacion": 45},
    {"nombre": "Luis Martínez", "calificacion": 72},
    {"nombre": "Marta López", "calificacion": 90},
    {"nombre": "Carlos García", "calificacion": 60}
]

# Abrir el archivo 'informe_estudiantes.txt' en modo escritura ('w')
with open('informe_estudiantes.txt', 'w') as file:
    # Iterar sobre cada estudiante
    for estudiante in estudiantes:
        # Obtener el nombre y la calificación del estudiante
        nombre = estudiante["nombre"]
        calificacion = estudiante["calificacion"]

        # Determinar si el estudiante está aprobado o reprobado (nota > 60 es aprobado)
        resultado = "Aprobado" if calificacion > 60 else "Reprobado"

        # Escribir la línea en el archivo con la información formateada
        file.write(f"Nombre: {nombre} | Calificación: {calificacion} | Resultado: {resultado}\n")

# Mensaje para confirmar que se ha escrito el archivo
print("Informe generado exitosamente en 'informe_estudiantes.txt'")
