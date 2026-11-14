import ttkbootstrap as tb

def mostrar():
    resultado.config(text=f"Nombre: {nombre.get()}\nTurno: {turno.get()}\nSemestre: {semestre.get()}\nGrupo: {grupo.get()}\nEspecialidad: {especialidad.get()}")


ventana = tb.Window(themename='one-light')
ventana.geometry("400x600")

mensajeNombre = tb.Label(ventana, text="Nombre:", bootstyle="info")
mensajeNombre.pack()
nombre = tb.Entry(ventana, width=25)
nombre.pack()

mensajeTurno = tb.Label(ventana, text="Turno:", bootstyle="info").pack()
turno = tb.StringVar()
matutino = tb.Radiobutton(ventana, text="Matutino", value="Matutino", variable=turno).pack()
vespertino = tb.Radiobutton(ventana, text="Vespertino", value="Vespertino", variable=turno).pack()

mensajeSemestre = tb.Label(ventana, text="Semestre:", bootstyle="info").pack()
lista = ["Semestre 1", "Semestre 2", "Semestre 3", "Semestre 4", "Semestre 5", "Semestre 6"]
semestre = tb.Combobox(ventana, values=lista, state="readonly", width=20)
semestre.current(0)
semestre.pack()

mensajeGrupo = tb.Label(ventana, text="Grupo:", bootstyle="info").pack()
grupo = tb.Entry(ventana, width=20).pack()

mensajeEspecialidad = tb.Label(ventana, text="Especialidad:", bootstyle="info").pack()
especialidad = tb.Entry(ventana, width=20).pack()

boton = tb.Button(ventana, text="Mensaje", command=mostrar).pack()
resultado = tb.Label(ventana, text="", font=("Arial", 15)).pack()

salir = tb.Button(ventana, text="Salir", command=ventana.destroy, bootstyle="danger").pack()

ventana.mainloop()