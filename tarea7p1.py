calificacionUno = float(input("Calificación uno: "))
calificacionDos = float(input("Calificación dos: "))
calificacionTres = float(input("Calificación tres: "))
calificacionCuatro = float(input("Calificación cuatro: "))
calificacionCinco = float(input("Calificación cinco: "))
promedio = (calificacionUno + calificacionDos + calificacionTres + calificacionCuatro + calificacionCinco) / 5
if promedio >= 7:
    print("Aprobado")
else:
    print("Reprobado")