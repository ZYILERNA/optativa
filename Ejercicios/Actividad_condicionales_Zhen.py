#Zhen Yang DAW

#Ejercicio 1 

horas_trabajo = 8

if horas_trabajo > 0:
    print("Las horas fueron registradas correctamente")

#Ejercicio 2

hora_llegada = 9

empleado_llega = 10

if empleado_llega < hora_llegada:
    print("El empleado llego temprano")
elif empleado_llega == hora_llegada:
    print("El empleado llego a tiempo")
else:
    print("El empleado llego tarde")

#Ejercicio 3 and

horas_trabajada = 20

if horas_trabajada > 0 and horas_trabajada <= 12:
    print("Se ha registrado correctamente las horas trabajadas")
else:
    print("El empleado ha trabajado mas de las horas permitidas")

#Ejercicio 4 elif

minutos_retraso = 10

if minutos_retraso == 0:
    print("El empleado no tiene retrasos")
elif minutos_retraso <= 5:
    print("El empleado tiene un retraso menor a 5 minutos")
elif minutos_retraso <= 10:
    print("El empleado tiene un retraso menor a 10 minutos")
else:
    print("El empleado tiene un retraso mayor a 10 minutos")

#ejercicio 6 Not

hora_salida = 17

if not hora_salida == "":
    print("Se han registrado sus horas de salida")
