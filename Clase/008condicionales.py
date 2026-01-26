# Ejemplo de uso de condicionales en Python

# Condicional simple: if
my_condition = True  # Definimos una condición verdadera

if my_condition:
    print("Se ejecuta la condición del primer if")

print("La ejecución continúa después del primer if\n")


# Comparación con números
my_condition = 5 * 3  # Resultado 15

if my_condition == 11:
    print("Se ejecuta la condición del segundo if (igual a 11)")

# como my_condition es 15, el print no se ejecutará


# Comparación correcta con if
if my_condition == 15:
    print("Se ejecuta la condición del segundo if correctamente (igual a 15)")

# Uso de if-else
if my_condition > 10:
    print("Es mayor que 10")
else:
    print("Es menor o igual que 10")

print("La ejecución continúa después del if-else\n")


# Uso de operadores lógicos: and
if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y menor que 20")
else:
    print("No cumple las dos condiciones al mismo tiempo\n")


# Uso de elif
if my_condition > 20:
    print("Es mayor que 20")
elif my_condition == 15:
    print("Es exactamente 15")
else:
    print("Es menor o igual que 10 o mayor o igual que 20")

print("La ejecución continúa después del if-elif-else\n")

# Valores que Python considera False
# Algunas cosas se consideran automáticamente False:
# - Cadena vacía: ""
# - Número 0
# - Lista, tupla o set vacíos
# - None

my_string = ""  # Cadena vacía

if not my_string:  # not invierte el valor booleano
    print("La cadena de texto está vacía")

my_string = "Hola Python"

if my_string:  # ahora la cadena no está vacía, se considera True
    print("La cadena de texto no está vacía:", my_string)
