def rectangulo(base, altura):
    area = base * altura
    return area
base = float(input("Escriba la medida de la base del rectángulo: "))
altura = float(input("Escriba la medida de la altura del rectángulo: "))
print(f"El área del rectángulo es: {rectangulo(base, altura)}")