my_tuple = tuple() #forma 1 usando el constructor tuple()
my_other_tuple = () #forma 2 usando parentesis

my_tuple = (35,1.77,"Zhen", "Yang")
print(my_tuple)


print(my_tuple[0]) #primer elemento
print(my_tuple[-1]) #ultimo elemento

 
#print(my_tuple[4]) #indice fuera de rango
#print(my_tuple[-6]) #indice fuera de rango

print(my_tuple.count("Zhen"))

print(my_tuple.index("Zhen"))


#my_tuple[1] = 1.6

print(my_tuple)


my_sum_tuple = my_tuple + my_other_tuple

print(my_sum_tuple)


my_tuple = list(my_tuple)

print(type(my_tuple))

my_tuple[2] = "ilerna"


my_tuple.insert(1, "Azul")

print(my_tuple)

my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))


#del my_tuple[2]  ERROR YA QUE SOLO PERMITE ELIMINAR TODAS.

del my_tuple

my_set = set()#crea un conjunto vació
my_other_set = {} #Crea un diccionario vacío
print(type(my_set))
print(type (my_other_set)) # Inicialmente es un diccionario
my_other_set = {"zhen", "yang", 20} #crea un conjunto
print(type (my_other_set))


print(len(my_other_set))
my_other_set.add("yang")
print(my_other_set)

print("zhen" in my_other_set)
print("hola"in my_other_set)

my_other_set = {"Python", "Geral", "Developer"}
my_other_set.remove("Geral")
print(my_other_set)

my_other_set.clear()
print(my_other_set)

