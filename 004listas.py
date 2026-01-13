my_list = list()
my_other_list = []

my_list = [35, 22, 32, 30, 16]

print(my_list)
print(len(my_list)) #imprime la longitud de la lista

MY_TOEHR_LIST = ["Zhen", "Yang", 19]
print(MY_TOEHR_LIST)
print(type(MY_TOEHR_LIST))

print(MY_TOEHR_LIST[0])
print(MY_TOEHR_LIST[1])
print(MY_TOEHR_LIST[2])
print(MY_TOEHR_LIST[-1])
print(MY_TOEHR_LIST[-2])
print(MY_TOEHR_LIST[-3])

print(MY_TOEHR_LIST.count("Zhen"))
print(MY_TOEHR_LIST.count(19))

name,surname,age = MY_TOEHR_LIST
print(name)
print(surname)
print(age)

name,surname,age = MY_TOEHR_LIST[2],MY_TOEHR_LIST[1],MY_TOEHR_LIST[0]
print(name)
print(surname)
print(age)

print(my_list+MY_TOEHR_LIST)

print(type(my_list))
print(type(my_other_list))


MY_TOEHR_LIST.append("ilerna")
print(MY_TOEHR_LIST)

MY_TOEHR_LIST.insert(1,"azul")
print(MY_TOEHR_LIST)

MY_TOEHR_LIST[1]="Rojo"
print(MY_TOEHR_LIST)

my_list.remove(30)
print(my_list)

print(my_list.pop()) #elimina el ultimo elemento
print(my_list)

print(my_list.pop(2)) #elimina el elemento en la posicion 2
print(my_list)

del my_list[2]
print(my_list)


my_list.clear()
print(my_list)

my_new_list = my_list.copy()
print(my_new_list)


my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)