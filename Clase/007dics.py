# -----------------------------
# Crear diccionarios en Python
# -----------------------------

# Usando el constructor dict()
my_dict = dict()
print(type(my_dict))  # <class 'dict'>

# Usando {} podemos crear diccionarios con varios elementos
# Nota: si ponemos varios elementos sin clave se crea un set, no un dict

# Python permite usar claves de distintos tipos
my_other_dict = {
    "Nombre": "Zhen",
    "Apellido": "Yang",
    "Edad": 25,
    1: "Python"  # clave numérica
}

# En un diccionario los valores pueden ser cualquier tipo de datos, incluso sets
my_dict = {
    "Nombre": "Zhen",
    "Apellido": "Yang",
    "Edad": 25,
    "Lenguajes": {"Python", "Java", "JavaScript"}
}

print(my_other_dict)
print(my_dict)

# len() cuenta cuántas claves tiene el diccionario
print(len(my_other_dict))  # 4
print(len(my_dict))        # 4

# Acceder a un valor usando la clave
print(my_dict["Nombre"])  # Zhen

# Modificar un valor en un diccionario
my_dict["Nombre"] = "Zhenyi"
print(my_dict["Nombre"])  # Zhenyi

# Añadir una nueva clave con su valor
my_dict["Calle"] = "Calle Dragon"
print(my_dict)

# Eliminar un elemento concreto del diccionario
del my_dict["Calle"]

# Verificar si una clave o valor existe en el diccionario
print("Zhen" in my_dict)       # False, porque cambiamos el nombre a Zhenyi
print("Nombre" in my_dict)     # True

# Métodos útiles de diccionarios
print(my_dict.items())   # Devuelve pares clave-valor
print(my_dict.keys())    # Devuelve solo las claves
print(my_dict.values())  # Devuelve solo los valores

# Uso de fromkeys()
# Crea un nuevo diccionario con las claves indicadas y valor None
my_new_dict = my_other_dict.fromkeys(("Nombre", 1))
print(my_new_dict)

# fromkeys() también puede generar un diccionario usando todas las claves de otro dict
my_new_dict = dict.fromkeys(my_dict)
print(my_new_dict)

# Asignando un valor específico a todas las claves
my_new_dict = dict.fromkeys(my_dict, "Valor por defecto")
print(my_new_dict)
