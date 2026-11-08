import tkinter as tk

ventana = tk.Tk()
ventana.geometry("500x500")
nombre = tk.Label(ventana, text="Nombre: Mikel Requena Ortiz", fg="green").pack()
especialidad = tk.Label(ventana, text="Especialidad: Programación", fg="orange").pack()
gradoGrupo = tk.Label(ventana, text="Grado y Grupo: 3°A", fg="purple").pack()

ventana.mainloop()