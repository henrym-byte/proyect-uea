def calcular_descuento(monto_total, porcentaje_descuento=10):
    # Calcula el descuento multiplicando el monto total por el porcentaje de descuento
    return (monto_total * porcentaje_descuento) / 100

# Programa principal
# Primer ejemplo: monto total de 200
monto1 = 200
# Llama a la función para calcular el descuento
descuento1 = calcular_descuento(monto1)
# Calcula el monto final a pagar restando el descuento del monto total
monto_final1 = monto1 - descuento1
# Imprime los resultados
print(f"Monto total: ${monto1:.2f}, Descuento: ${descuento1:.2f}, Monto a pagar: ${monto_final1:.2f}")

# Segundo ejemplo: monto total de 150 y un porcentaje de descuento del 20%
monto2 = 150
porcentaje2 = 20
# Llama a la función con ambos parámetros
descuento2 = calcular_descuento(monto2, porcentaje2)
# Calcula el monto final a pagar
monto_final2 = monto2 - descuento2
# Imprime los resultados
print(f"Monto total: ${monto2:.2f}, Descuento: ${descuento2:.2f}, Monto a pagar: ${monto_final2:.2f}")
