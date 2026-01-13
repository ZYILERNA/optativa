#operadores logicos
#()
#not
#and
#or

print(3 < 4 and not ("Hola" > "hola"))

print(5 == 5 or "adios" < "hola")

print(82<2 or 5>2)

print(5>2 and not 5<2)

print(4 == 4 or("Python" == "Python" and 4==2))
print(3> 4 and("Hola" < "Python" and 3>2))
print(3> 4 or("Hola" < "Python" and 3>2))


#Ejemplos con not

print(not(3>2)) #False porque 3 es mayor que 2

print(not(3<2)) #True porque 3 no es menor que 2

print(not(3==3)) #False porque 3 es igual a 3

print(not(3!=3)) #True porque 3 no es diferente de 3

print(not("hola"=="adadadad")) #True porque "hola" no es igual a "adadadad"