
language = input("Ingresa una palabra: ")
letra = input("Ingresa una letra a contar: ")

print("1. Primera letra en mayúscula:", language.capitalize())
print("2. En mayúsculas:", language.upper())
print("3. Veces que aparece la letra en la palabra:", language.count(letra))
print("4. ¿La palabra está formada solo por números?:", language.isnumeric())
print("5. Comprobación numérica con '1':", "1".isnumeric())
print("6. En minúsculas:", language.lower())
print("7. ¿La palabra está completamente en mayúsculas?:", language.isupper())
print("8. ¿La palabra comienza con 'py'?:", language.startswith("py"))