import ttkbootstrap as ttkb

def mostrar():
    nombre = entradaNombre.get()
    genero = generoSeleccion.get()
    pasatiempos = []
    if deporte.get():
        pasatiempos.append("Hacer deporte")
    if videojuegos.get():
        pasatiempos.append("Jugar videojuegos")
    if musica.get():
        pasatiempos.append("Escuchar música")
    resultado.config(text=f"Nombre: {nombre}\nGenero: {genero}\nPasatiempos: {pasatiempos}")

ventana = ttkb.Window(themename="superhero")
ventana.title("Tarea7P2")
ventana.geometry("550x400")

etiqueta = ttkb.Label(ventana, text="Emplea Frameworks para el desarrollo de Software", font=("Arial", 14))
etiqueta.pack()

mensajeNombre = ttkb.Label(ventana, text="Escriba su nombre:", bootstyle="info")
mensajeNombre.pack()
entradaNombre = ttkb.Entry(ventana, width=25)
entradaNombre.pack()

mensajeSexo = ttkb.Label(ventana, text="Seleccione su sexo:", bootstyle="info")
mensajeSexo.pack()
generoSeleccion = ttkb.StringVar()
hombre = ttkb.Radiobutton(ventana, text="Hombre", value="Hombre", variable=generoSeleccion)
hombre.pack()
mujer = ttkb.Radiobutton(ventana, text="Mujer", value="Mujer", variable=generoSeleccion)
mujer.pack()

deporte = ttkb.BooleanVar()
videojuegos = ttkb.BooleanVar()
musica = ttkb.BooleanVar()

mensajePasatiempos = ttkb.Label(ventana, text="Selecciona tus pasatiempos:", bootstyle="info")
mensajePasatiempos.pack()
casillaDeporte = ttkb.Checkbutton(ventana, text="Hacer deporte", variable=deporte)
casillaDeporte.pack()
casillaVideojuegos = ttkb.Checkbutton(ventana, text="Jugar videojuegos", variable=videojuegos)
casillaVideojuegos.pack()
casillaMusica = ttkb.Checkbutton(ventana, text="Escuchar música", variable=musica)
casillaMusica.pack()

boton = ttkb.Button(ventana, text="Mostrar datos", bootstyle="success", command=mostrar)
boton.pack()
    
resultado = ttkb.Label(ventana, text="", font=("Arial", 12))
resultado.pack()

ventana.mainloop()