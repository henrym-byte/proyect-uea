# Crear un diccionario con información personal ficticia
informacion_personal = {
    "nombre": "Juan Pérez",  # Nombre de la persona
    "edad": 28,              # Edad de la persona
    "ciudad": "Quito",       # Ciudad de residencia
    "profesion": "Ingeniero" # Profesión de la persona
}

# Modificar la ciudad
informacion_personal["ciudad"] = "Guayaquil"  # Cambiando la ciudad de Quito a Guayaquil

# Agregar un número de teléfono si no existe
if "telefono" not in informacion_personal:  # Verificar si la clave "telefono" no está presente
    informacion_personal["telefono"] = "0998765432"  # Si no existe, agregar un número de teléfono ficticio

# Eliminar la clave "edad"
del informacion_personal["edad"]  # Eliminar la clave "edad" del diccionario

# Imprimir el diccionario final
print(informacion_personal)  # Mostrar el contenido del diccionario después de las modificaciones
