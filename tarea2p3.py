import ttkbootstrap as tb

ventana = tb.Window()

datos = tb.Labelframe(ventana, padding=10)
datos.pack(padx=20, pady=10, fill="x")

etiquetaNombre = tb.Label(datos, text="Nombre:")
etiquetaNombre.grid(row=0, column=0, sticky="e")
entradaNombre = tb.Entry(datos, width=28)
entradaNombre.grid(row=0, column=1, padx=5, pady=3)
etiquetaSemestre = tb.Label(datos, text="Semestre:")
etiquetaSemestre.grid(row=1, column=0, sticky="e")
entradaSemestre = tb.Entry(datos, width=28)
entradaSemestre.grid(row=1, column=1, padx=5, pady=3)
etiquetaCarrera = tb.Label(datos, text="Carrera:")
etiquetaCarrera.grid(row=2, column=0, sticky="e")
entradaCarrera = tb.Entry(datos, width=28)
entradaCarrera.grid(row=2, column=1, padx=5, pady=3)

botones = tb.Frame(ventana)
botones.pack(pady=10)

agregar = tb.Button(botones, text="Agregar", width=10, bootstyle="success")
agregar.pack(side="left", padx=5)
limpiar = tb.Button(botones, text="Limpiar", width=10, bootstyle="warning")
limpiar.pack(side="left", padx=5)
salir = tb.Button(ventana, text="Salir", width=10, bootstyle="danger")
salir.pack(pady=10)

ventana.mainloop()