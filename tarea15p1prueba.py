numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros.append(11)
posicion = int(input("Escriba la posición del número que desea mostrar: "))
posicion = posicion - 1
print(numeros[posicion])
numero = int(input("Escriba un número: "))
posicion = int(input("Escriba la posición donde desea insertar el número: "))
posicion = posicion - 1
numeros.insert(posicion, numero)
print(numeros)
eliminar = int(input("Escriba el número que desea eliminar: "))
numeros.remove(eliminar)
sublista = numeros[3:6]
print(len(numeros))