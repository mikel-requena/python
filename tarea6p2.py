import tkinter as tk

def sumar():
    numeroUno = int(primerNumero.get())
    numeroDos = int(segundoNumero.get())
    resultado.config(text=f"SUMA\n{primerNumero.get()} + {numeroDos} = {numeroUno + numeroDos}")

def resta():
    numeroUno = int(primerNumero.get())
    numeroDos = int(segundoNumero.get())
    resultado.config(text=f"RESTA\n{numeroUno} - {numeroDos} = {numeroUno - numeroDos}")

def multiplicacion():
    numeroUno = int(primerNumero.get())
    numeroDos = int(segundoNumero.get())
    resultado.config(text=f"MULTIPLICACIÓN\n{numeroUno} X {numeroDos} = {numeroUno * numeroDos}")

def division():
    numeroUno = int(primerNumero.get())
    numeroDos = int(segundoNumero.get())
    resultado.config(text=f"DIVISIÓN\n{numeroUno} / {numeroDos} = {numeroUno / numeroDos}")

ventana = tk.Tk()
ventana.geometry("400x300")

eleccion = tk.StringVar()

primerNumero = tk.Label(ventana, text="Escriba el primer número:").pack()
primerNumero = tk.Entry(ventana, width=25)
primerNumero.pack()

segundoNumero= tk.Label(ventana, text="Escriba el segundo número:").pack()
segundoNumero = tk.Entry(ventana, width=25)
segundoNumero.pack()

opcionSumar = tk.Radiobutton(ventana, text="Sumar", variable=eleccion, value="Sumar", command=sumar)
opcionSumar.pack()
opcionRestar = tk.Radiobutton(ventana, text="Restar", variable=eleccion, value="Restar", command=resta)
opcionRestar.pack()
opcionMultiplicar = tk.Radiobutton(ventana, text="Multiplicar", variable=eleccion, value="Multiplicar", command=multiplicacion)
opcionMultiplicar.pack()
opcionDividir = tk.Radiobutton(ventana, text="Dividir", variable=eleccion, value="Dividir", command=division)
opcionDividir.pack()

resultado = tk.Label(ventana, text="", font=("Arial", 14))
resultado.pack()

ventana.mainloop()