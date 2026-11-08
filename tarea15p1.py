numeros = []
for i in range(10):
    numeros.append(int(input("Introduce un número: ")))

numeros.append(int(input("Escriba el número para agregar: ")))
posicion = int(input("Escriba la posición del número que quiere mostrar: "))
print(numeros[posicion])
posicion = int(input("Escriba la posición donde quiere insertar el número: "))
numeroInsertar = int(input("Escriba el número que quiere insertar: "))
numeros.insert(posicion, numeroInsertar)
print(numeros)
numeros.remove(int(input("Escriba la ocurrencia que quiere eliminar: ")))
sublista = numeros[4:7]
print(sublista)

print(len(numeros))