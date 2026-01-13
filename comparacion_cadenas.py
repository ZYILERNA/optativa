print("Hola" > "Python")#False  
print("Hola" < "Python")#True
print("Hola" >= "Hola")#True
print("Hola" <= "Python")#False
print("Hola" == "Hola")#True
print("Hola" != "Python")#True

#Preguntas de análisis
#1. ¿Qué resultado obtuviste en cada comparación?

#obtube True False True False True True

#2. ¿Por qué "Hola" < "Python" devuelve True y "Hola" > "Python" devuelve False?

#porque Python es mayor que Hola

#3. ¿Qué sucede si cambias "Hola" por "hola" (con minúscula)?

#sucede que "hola" es menor que "Python"

#4. ¿Por qué "Hola" == "hola" da False aunque parecen iguales?

#porque Python distingue entre mayusculas y minusculas

#5. ¿Qué crees que hace Python internamente para comparar dos textos?

#Python compara los caracteres de las cadenas de texto uno por uno

#6. Escribe en el intérprete lo siguiente y anota el resultado:

#7. print(ord("H"))

print(ord("H"))

#8. print(ord("P"))

print(ord("P"))

#¿Qué representan esos números?

#representan el valor de los caracteres en la tabla ASCII

#9. Cambia las palabras y prueba con ejemplos como:

print("a" < "b")
print("Z" < "a")
print("Casa" > "casa")
print("Python" > "Py")

#Explica en tus palabras por qué se obtienen esos resultados.

#Porque Python compara cadenas por sus códigos Unicode:
#carácter a carácter, distinguiendo mayúsculas de minúsculas (case-sensitive),
#y, si dos cadenas comparten el mismo prefijo, la más larga es mayor.
