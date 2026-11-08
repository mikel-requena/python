def es_primo(n):
        for j in range(2, n):
            if n % j == 0:
                return False
            return True

def es_impar(n):
    return n % 2 == 1

def mostrar_impares_primos(inicio, fin):
    for i in range(inicio, fin + 1):
        if es_primo(i) and es_impar(i):
            print(f'El número {i} es primo e impar')