my_set = set()
my_other_set = {}


print(type(my_set))
print(type(my_other_set))


my_other_set = {"Aaron", "Evangelista"}
print(type(my_other_set))


print(len(my_other_set))


my_other_set.add("Mendez")
print(my_other_set)


my_other_set = {"Aaron","Evangelista", 22,"Aaron"} ## aparece dos veces Aaron
print(type(my_other_set))
my_other_set.add("Aaron")
print(my_other_set)


print("Aaron" in my_other_set)
print("Evangelista" in my_other_set)
print("Pepe" in my_other_set)


my_other_set = {"Python","Aaron" ,"Evangelista"}
my_other_set.remove("Aaron")
print(my_other_set)


 ## my_other_set,clear() ## elimina todo
 ## print(my_other_set)


##  my_other_set = {"Python","Aaron" ,"Developer"}


## del my_other_set
## print(my_other_set)


my_set = {"Azael","Mendez", 35}
my_list = list(my_set)
print(my_list)
print(my_list[0])




my_other_set = {"Java","php","Python"}
my_new_set = my_set.union(my_other_set)
print(my_new_set)