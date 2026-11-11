import ttkbootstrap as ttkb

import ttkbootstrap as tb

ventana = tb.Window()
#ventana = tb.Window(themename="superhero")

#Imprimir los diferentes tipos de tema.
print(ventana.style.theme_names())
ventana.mainloop()