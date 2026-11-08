import tkinter as tk

def calcularEdad():
    edad = int(entrada.get())
    edadActual = 2026 - edad
    resultado.config(text=f"Tienes {edadActual} años")

ventana = tk.Tk()
ventana.geometry("400x200")
ventana.title("Tarea5P2")

pregunta = tk.Label(ventana, text="¿En que año naciste?")
pregunta.pack()
entrada = tk.Entry(ventana, width=25)
entrada.pack()
    
boton = tk.Button(ventana, text="Calcular Edad", command=calcularEdad)
boton.pack()

resultado = tk.Label(ventana, text="", font=("Arial", 14))
resultado.pack()

salir = tk.Button(ventana, text="Salir", command=ventana.destroy, bg="red")
salir.pack()

ventana.mainloop()