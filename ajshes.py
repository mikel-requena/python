tupla = (4, 7, 4, 9, 4)

# Imprime la posición (índice) de uno de los elementos.
elemento = 9
print(f"El elemento {elemento} esta en la posicion {tupla.index(elemento)}")

# Los índices de las tuplas comienzan en 0.
print(f"El valor en la posicion 3 es {tupla[3]}")

# Recorre la tupla y suma sus valores de manera tradicional.
suma = 0
print("Elementos de la tupla:")
for valor in tupla:
    print(valor)
    suma += valor

print(f"La suma de los valores es {suma}")

# Cuenta cuántas veces aparece el elemento de la posición 2.
elemento_posicion_2 = tupla[2]
print(
    f"El elemento {elemento_posicion_2} de la posicion 2 "
    f"se repite {tupla.count(elemento_posicion_2)} veces"
)