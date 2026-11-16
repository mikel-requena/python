import ttkbootstrap as tb

def mostrar():
    resultado.config(text=f"Nombre: {nombre.get()}\nTurno: {turno.get()}\nSemestre: {semestre.get()}\nGrupo: {grupo.get()}\nEspecialidad: {especialidad.get()}")


ventana = tb.Window(themename='one-light')
ventana.geometry("350x600")

mensajeNombre = tb.Label(ventana, text="Nombre:", bootstyle="info")
mensajeNombre.grid(row=0, column=0, sticky="e", padx=5, pady=5)
nombre = tb.Entry(ventana, width=25)
nombre.grid(row=0, column=1, padx=5, pady=5)

mensajeTurno = tb.Label(ventana, text="Turno:", bootstyle="info")
mensajeTurno.grid(row=1, column=0, sticky="e", padx=5, pady=5)
turno = tb.StringVar()
matutino = tb.Radiobutton(ventana, text="Matutino", value="Matutino", variable=turno)
matutino.grid(row=1, column=1, sticky="w", padx=5, pady=5)
vespertino = tb.Radiobutton(ventana, text="Vespertino", value="Vespertino", variable=turno)
vespertino.grid(row=2, column=1, sticky="w", padx=5, pady=5)

mensajeSemestre = tb.Label(ventana, text="Semestre:", bootstyle="info")
mensajeSemestre.grid(row=3, column=0, sticky="e", padx=5, pady=5)
lista = ["Semestre 1", "Semestre 2", "Semestre 3", "Semestre 4", "Semestre 5", "Semestre 6"]
semestre = tb.Combobox(ventana, values=lista, state="readonly", width=20)
semestre.current(0)
semestre.grid(row=3, column=1, padx=5, pady=5)

mensajeGrupo = tb.Label(ventana, text="Grupo:", bootstyle="info")
mensajeGrupo.grid(row=4, column=0, sticky="e", padx=5, pady=5)
grupo = tb.Entry(ventana, width=20)
grupo.grid(row=4, column=1, padx=5, pady=5)

mensajeEspecialidad = tb.Label(ventana, text="Especialidad:", bootstyle="info")
mensajeEspecialidad.grid(row=5, column=0, sticky="e", padx=5, pady=5)
especialidad = tb.Entry(ventana, width=20)
especialidad.grid(row=5, column=1, padx=5, pady=5)

boton = tb.Button(ventana, text="Mensaje", command=mostrar)
boton.grid(row=6, column=0, columnspan=2, pady=10)
resultado = tb.Label(ventana, text="", font=("Arial", 15))
resultado.grid(row=7, column=0, columnspan=2, pady=10)

salir = tb.Button(ventana, text="Salir", command=ventana.destroy, bootstyle="danger")
salir.grid(row=8, column=0, columnspan=2, pady=10)

ventana.mainloop()