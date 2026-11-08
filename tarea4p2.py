import tkinter as tk

def leerNombre():
    nombre = entradaNombre.get()
    return nombre

def leerEspecialidad():
    especialidad = entradaEspecialidad.get()
    return especialidad

def saludar():
    nombre = leerNombre()
    especialidad = leerEspecialidad()
    resultado.config(text=f"{nombre} estudia {especialidad}")

def limpiar():
    entradaNombre.delete(0, tk.END)
    entradaEspecialidad.delete(0, tk.END)
    resultado.config(text="")

ventana = tk.Tk()
ventana.geometry("500x300")

mensajeNombre = tk.Label(ventana, text="Nombre:").pack()
entradaNombre = tk.Entry(ventana, width=30)
entradaNombre.pack()

mensajeEspecialidad = tk.Label(ventana, text="Especialidad:").pack()
entradaEspecialidad = tk.Entry(ventana, width=30)
entradaEspecialidad.pack()

mensaje = tk.Button(ventana, text="Mensaje", command=saludar)
mensaje.pack()

borrar = tk.Button(ventana, text="Limpiar", command=limpiar)
borrar.pack()

salir = tk.Button(ventana, text="Salir", command=ventana.destroy, bg="red").pack()

resultado = tk.Label(ventana, text="", font=("Arial", 14))
resultado.pack()

ventana.mainloop()