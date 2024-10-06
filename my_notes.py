# Lectura del archivo de texto

# Abrimos el archivo en modo lectura ('r')
file = open('my_notes.txt', 'r')

# Leemos el contenido línea por línea y lo mostramos en consola
for line in file:
    print(line.strip())  # strip() elimina los saltos de línea adicionales

# Cerramos el archivo después de leer
file.close()
