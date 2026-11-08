def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Ingrese un número entero válido.")


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numero_nuevo = leer_entero("Ingrese el número que desea agregar: ")
numeros.append(numero_nuevo)

posicion = leer_entero("Ingrese la posición que desea consultar (desde 1): ")
if 1 <= posicion <= len(numeros):
    print(f"Contenido de la posición {posicion}: {numeros[posicion - 1]}")
else:
    print("La posición está fuera del rango de la lista.")

valor_insertar = leer_entero("Ingrese el valor que desea insertar: ")
posicion_insertar = leer_entero(
    "Ingrese la posición donde desea insertarlo (desde 1): "
)
if 1 <= posicion_insertar <= len(numeros) + 1:
    numeros.insert(posicion_insertar - 1, valor_insertar)
else:
    print("La posición de inserción está fuera del rango permitido.")

print("Lista actual:", numeros)

valor_eliminar = leer_entero(
    "Ingrese el valor cuya primera ocurrencia desea eliminar: "
)
if valor_eliminar in numeros:
    numeros.remove(valor_eliminar)
    print(f"Se eliminó la primera ocurrencia de {valor_eliminar}.")
else:
    print(f"El valor {valor_eliminar} no se encuentra en la lista.")

print("Sublista de las posiciones 4 a 6:", numeros[3:6])
print("Tamaño de la lista:", len(numeros))