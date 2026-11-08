def primos_impares():
    for i in range(125, 201):
        contador = 0
        for j in range(2, i):
            if i % j == 0:
                contador += 1
        if contador == 0 and i % 2 == 1:
            print(f'El número {i} es primo e impar')
primos_impares()