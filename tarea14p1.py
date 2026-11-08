def par(numero):
    if numero % 2 == 0:
        print("El número es par.")

def multiplo(numero):
    if numero % 7 == 0:
        print("El número es múltiplo de 7.")

numero = int(input("Escriba un número: "))
par(numero)
multiplo(numero)