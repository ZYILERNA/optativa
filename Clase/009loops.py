my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2

else:
    print("Mi condicion es mayor o igual que 10")

print("La ejecucon continua")


my_condition = 0

while my_condition < 10:
    print(my_condition)

    my_condition += 2

    if my_condition == 10:
        print("mi condicion es igual a 10")
    else:
        print("mi condiciones es mayor o igual que 10")

print("La ejecucion continua")

while my_condition < 20:
    my_condition += 1

    if my_condition == 15:
        print("mi condiciones es 15")

        print("La ejecucion continua")

# Detener con break

while my_condition < 20:
    my_condition += 1

    if my_condition == 15:
        print("se detiene la ejecucion del bucle")
        break

    print(my_condition)

print("La ejecucion continua")

# Bucle for -> este se ejecuta un numero determinado de veces, permite reccorree set, listas, tuplas, diccionarios

my_list = [35, 24, 62, 52, 12]
for element in my_list:
    print(element)

my_set = {"Zhen", "Yang", 25}
for element in my_set:
    print(element)

my_tuple = (25,1.70, "Zhen", "Yang")
for element in my_tuple:
    print(element)

# Los diccionarios solo imprimen las claves no los valores

my_dict = {
    "Nombre": "Zhen",
    "Apellido": "Yang",
    "Edad": 25
}

for element in my_dict:
    print(element)

for element in my_dict.values():
    print(element)
else:
    print("Se han recorrido todos los elementos del diccionario")

    
for key, value in my_dict.items():
    print(f"Clave: {key} - Valor: {value}")

for element in my_dict:
    print(element)

    if element == "Edad":
     continue
else:
    print("El bule for para diccionarios ha finalizado")