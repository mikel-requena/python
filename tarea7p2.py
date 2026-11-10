import tkinter as tk

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

ventana = tk.Tk()
ventana.title("Tarea7P2")
ventana.geometry("500x350")

etiqueta = tk.Label(ventana, text="Emplea Freamworks para el desarrollo de Software", font=("Arial", 14), fg="purple")
etiqueta.pack()

mensajeNombre = tk.Label(ventana, text="Escriba su nombre:").pack()
entradaNombre = tk.Entry(ventana, width=25)
entradaNombre.pack()

mensajeSexo = tk.Label(ventana, text="Seleccione su sexo:")
mensajeSexo.pack()
generoSeleccion = tk.StringVar()
hombre = tk.Radiobutton(ventana, text="Hombre", value="Hombre", variable=generoSeleccion)
hombre.pack()
mujer = tk.Radiobutton(ventana, text="Mujer", value="Mujer", variable=generoSeleccion)
mujer.pack()

deporte = tk.BooleanVar()
videojuegos = tk.BooleanVar()
musica = tk.BooleanVar()

mensajePasatiempos = tk.Label(ventana, text="Selecciona tus pasatiempos:")
mensajePasatiempos.pack()
casillaDeporte = tk.Checkbutton(ventana, text="Hacer deporte", fg="blue", variable=deporte)
casillaDeporte.pack()
casillaVideojuegos = tk.Checkbutton(ventana, text="Jugar videojuegos", fg="blue", variable=videojuegos)
casillaVideojuegos.pack()
casillaMusica = tk.Checkbutton(ventana, text="Escuchar música", fg="blue", variable=musica)
casillaMusica.pack()

boton = tk.Button(ventana, text="Mostrar datos", bg="green", command=mostrar)
boton.pack()
    
resultado = tk.Label(ventana, text="", font=("Arial", 12))
resultado.pack()

ventana.mainloop()