import tkinter as tk

def mensaje():
    print("Hola Mundo")

ventana = tk.Tk()
ventana.geometry("300x500")

boton = tk.Button(ventana, text="Mensaje", command=mensaje).pack()
salir = tk.Button(ventana, text="Salir", command=ventana.destroy, bg="red").pack()

ventana.mainloop()