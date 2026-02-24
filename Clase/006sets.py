my_set = set()
my_other_set = {}


print(type(my_set))
print(type(my_other_set))


my_other_set = {"Zhen", "Yang"}
print(type(my_other_set))


print(len(my_other_set))


my_other_set.add("Yang")
print(my_other_set)


my_other_set = {"Zhen","Yang", 22,"Zhen"} ## aparece dos veces Zhen
print(type(my_other_set))
my_other_set.add("Zhen")
print(my_other_set)


print("Zhen" in my_other_set)
print("Yang" in my_other_set)
print("Pepe" in my_other_set)


my_other_set = {"Python","Zhen" ,"Yang"}
my_other_set.remove("Zhen")
print(my_other_set)


 ## my_other_set,clear() ## elimina todo
 ## print(my_other_set)


##  my_other_set = {"Python","Zhen" ,"Developer"}


## del my_other_set
## print(my_other_set)


my_set = {"Zhen","Yang", 25}
my_list = list(my_set)
print(my_list)
print(my_list[0])




my_other_set = {"Java","php","Python"}
my_new_set = my_set.union(my_other_set)
print(my_new_set)