def calcular_promedio_temperaturas(temperaturas):
    num_ciudades = len(temperaturas)
    num_semanas = len(temperaturas[0])
    num_dias_semana = len(temperaturas[0][0])

    # Lista para almacenar los promedios de temperatura para cada ciudad
    promedios_ciudades = []

    for ciudad in range(num_ciudades):
        suma_temperaturas = 0
        num_dias_totales = 0

        for semana in range(num_semanas):
            # Extraer las temperaturas de la ciudad y semana específicas
            temperaturas_semana = temperaturas[ciudad][semana]
            # Sumar las temperaturas de la semana
            suma_temperaturas += sum(temperaturas_semana)
            num_dias_totales += num_dias_semana

        # Calcular el promedio de temperaturas para la ciudad
        promedio_temperatura = suma_temperaturas / num_dias_totales
        promedios_ciudades.append(promedio_temperatura)

    return promedios_ciudades


# Ejemplo de uso
temperaturas = [
    [  # Ciudad 1
        [15, 16, 17, 18, 19, 20, 21],  # Semana 1
        [16, 17, 18, 19, 20, 21, 22],  # Semana 2
        [17, 18, 19, 20, 21, 22, 23],  # Semana 3
        [18, 19, 20, 21, 22, 23, 24]  # Semana 4
    ],
    [  # Ciudad 2
        [25, 26, 27, 28, 29, 30, 31],  # Semana 1
        [26, 27, 28, 29, 30, 31, 32],  # Semana 2
        [27, 28, 29, 30, 31, 32, 33],  # Semana 3
        [28, 29, 30, 31, 32, 33, 34]  # Semana 4
    ],
    [  # Ciudad 3
        [35, 36, 37, 38, 39, 40, 41],  # Semana 1
        [36, 37, 38, 39, 40, 41, 42],  # Semana 2
        [37, 38, 39, 40, 41, 42, 43],  # Semana 3
        [38, 39, 40, 41, 42, 43, 44]  # Semana 4
    ]
]

promedios = calcular_promedio_temperaturas(temperaturas)

for ciudad, promedio in enumerate(promedios, start=1):
    print(f"Promedio de temperatura para Ciudad {ciudad}: {promedio:.2f}°C")
