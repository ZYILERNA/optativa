my_string = "Hola Mundo"
my_string2 = "ADIOS"
my_stringconsalto = "texto\nconsalto"
tab = "texto\tcon\ttabulador"


print(my_string)
print(my_string2)
print(len(my_string))
print(len(my_string2))
print(my_string + " " + my_string2)
print(my_string + my_string2)
print(my_string + my_stringconsalto)
print(tab)


name,surname,age = "zhen", "yang", 19
print("mi nombre es: "+name+" " +surname+" y tengo "+str(age)+" años")

# %s para strings
# %d para enteros
# %f para float

print("mi nombre es: %s %s y tengo %d años" % (name,surname,age))

print("mi nombre es: {} {} y tengo {} años".format(name,surname,age))


language = "python"
a,b,c,d,e,f = language
print(a)#muestra p  
print(b)#muestra y
print(c)#muestra t
print(d)#muestra h
print(e)#muestra o
print(f)#muestra n

language = "python"
language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2:]
print(language_slice)

reverse_language = language[::-1]
print(reverse_language)


print(language.capitalize()) # 1. primera letra en mayúscula
print(language.upper()) # 2. todas las letras en mayúscula
print(language.lower()) # 3. todas las letras en minúscula
print(language.count("o")) # 4. cuenta las letras
print(language.isnumeric()) # 5. verifica si es numérico
print("1".isnumeric()) # 6. verifica si es numérico
print(language.upper().isupper()) # 7. verifica si es mayúscula
print(language.startswith("py")) # 8. verifica si empieza con py


