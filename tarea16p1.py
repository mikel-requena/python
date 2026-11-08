numeros = (1, 2, 3, 4, 5)
numero = 3
print(f"Posicion de numero cualquiera: {numeros.index(numero)}")
print(f"Numero que esta en la posicion 3: {numeros[3]}")
suma = 0
print("iteracion de la tupla:")
for t in numeros:
    print(t)
    suma = suma + t
print(f"La suma de los numeros es: {suma}")
print(f"El numero {numeros[2]} se repite {numeros.count(numeros[2])} veces")