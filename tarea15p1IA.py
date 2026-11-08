numeros = []

print("Introduce 10 números enteros:")
for i in range(10):
    numeros.append(int(input(f"Número {i + 1}: ")))

print(f"\nLista inicial: {numeros}")

numero = int(input("\nNúmero que deseas agregar: "))
numeros.append(numero)

posicion = int(input("Posición que deseas consultar (empieza en 1): "))
if 1 <= posicion <= len(numeros):
    print(f"Contenido de la posición {posicion}: {numeros[posicion - 1]}")
else:
    print("La posición está fuera del rango de la lista.")

valor = int(input("\nValor que deseas insertar: "))
posicion = int(input(f"Posición donde deseas insertarlo (1-{len(numeros) + 1}): "))
if 1 <= posicion <= len(numeros) + 1:
    numeros.insert(posicion - 1, valor)
else:
    print("La posición está fuera del rango de inserción.")

print(f"\nLista después de la inserción: {numeros}")

valor = int(input("\nValor cuya primera ocurrencia deseas eliminar: "))
if valor in numeros:
    numeros.remove(valor)
    print(f"Se eliminó la primera ocurrencia de {valor}.")
else:
    print(f"El valor {valor} no se encuentra en la lista.")

print(f"\nSublista de las posiciones 4 a 6: {numeros[3:6]}")
print(f"Tamaño de la lista: {len(numeros)}")