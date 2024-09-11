# Definir el número de ciudades, días de la semana y semanas
num_ciudades = 3  # Por ejemplo, 3 ciudades
num_dias_semana = 7  # Lunes a Domingo
num_semanas = 4  # Ejemplo: 4 semanas

# Crear una matriz 3D con temperaturas de ejemplo
temperaturas = [
    [  # Ciudad 1
        [15, 16, 17, 18, 19, 20, 21],  # Semana 1
        [16, 17, 18, 19, 20, 21, 22],  # Semana 2
        [17, 18, 19, 20, 21, 22, 23],  # Semana 3
        [18, 19, 20, 21, 22, 23, 24]   # Semana 4
    ],
    [  # Ciudad 2
        [25, 26, 27, 28, 29, 30, 31],  # Semana 1
        [26, 27, 28, 29, 30, 31, 32],  # Semana 2
        [27, 28, 29, 30, 31, 32, 33],  # Semana 3
        [28, 29, 30, 31, 32, 33, 34]   # Semana 4
    ],
    [  # Ciudad 3
        [35, 36, 37, 38, 39, 40, 41],  # Semana 1
        [36, 37, 38, 39, 40, 41, 42],  # Semana 2
        [37, 38, 39, 40, 41, 42, 43],  # Semana 3
        [38, 39, 40, 41, 42, 43, 44]   # Semana 4
    ]
]

# Calcular y mostrar el promedio de temperaturas para cada ciudad por semana
for ciudad in range(num_ciudades):
    print(f"\nCiudad {ciudad + 1}:")
    for semana in range(num_semanas):
        # Extraer las temperaturas de la ciudad y semana específicas
        temperaturas_semana = temperaturas[ciudad][semana]
        # Calcular el promedio
        promedio_temperatura = sum(temperaturas_semana) / num_dias_semana
        print(f"Promedio de temperaturas en la semana {semana + 1}: {promedio_temperatura:.2f}°C")
