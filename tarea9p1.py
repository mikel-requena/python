promedio = 0
repeticion = 0
calificaciones = 0
while repeticion < 50:
    repeticion += 1
    print(f"Alumno número: {repeticion}")
    calificacionUno = float(input("Calificación materia uno: "))
    calificacionDos = float(input("Calificación materia dos: "))
    calificacionTres = float(input("Calificación materia tres: "))
    calificacionCuatro = float(input("Calificación materia cuatro: "))
    calificacionCinco = float(input("Calificación materia cinco: "))
    totalAlumno = calificacionUno + calificacionDos + calificacionTres + calificacionCuatro + calificacionCinco
    promedio += totalAlumno
promedioGrupal = promedio / 250
print (f"El promedio del grupo es de: {promedioGrupal:.2f}")