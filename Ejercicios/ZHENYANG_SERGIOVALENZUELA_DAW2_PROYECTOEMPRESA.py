# Proyecto Empresa
# SERGIO VALENZUELA
# ZHEN YANG
# Nombre de la empresa: GameJam
# Tipo de tienda: Tienda de videojuegos
# Profesora: Geraldin López

print("Bienvenido a GAMEJAM, tu tienda de videojuegos favorita")

nombre_empresa = "GAMEJAM"
anio_fundacion = 2000
ingresos_mensuales = 2500.50
es_internacional = True

nombre_usu = input("Dime tu nombre: ")
edad_usu = int(input("Dime tu edad: "))
producto_favorito = input("¿Cuál es tu videojuego favorito? ")

edad_doble = edad_usu * 2
edad_div = edad_usu // 2
edad_mod = edad_usu % 3

print(f"Tu edad al doble es {edad_doble}, la mitad es {edad_div} y tu edad % 3 es {edad_mod}")

frase = input("Escribe una frase para analizar: ")

print("Análisis de la cadena introducida por el usuario")
print(f"Número de letras 'a': {frase.count('a')}")
print(f"¿Es numérica?: {frase.isnumeric()}")
print(f"¿Está en mayúsculas?: {frase.isupper()}")
print(f"¿Empieza con 'hola'?: {frase.lower().startswith('hola')}")
print(f"Longitud de la frase: {len(frase)}")
print("Primeros 5 caracteres:", frase[:5])
print("Frase en mayúsculas:", frase.upper())
print("Frase en minúsculas:", frase.lower())
print("Capitalizado:", frase.capitalize())

productos = ["Super Mario Bros", "Sonic Boom", "Minecraft"]
precios = [45, 35, 20]

print("\nProductos disponibles:", productos)
print("Precios:", precios)

productos.append("Halo Infinite")
precios.append(60)

productos.insert(1, "Call of Duty")
precios.insert(1, 70)

productos.remove("Sonic Boom")
precios.pop(1)

productos_copy = productos.copy()
productos_copy.reverse()
productos.sort()

print("\nLista de productos final:", productos)
print("Copia invertida:", productos_copy)

carrito = []
continuar = 1

while continuar != 0:
    prod = input("Dime un producto para añadir a tu carrito: ")
    carrito.append(prod)
    continuar = int(input("Introduce 0 para parar o cualquier número para seguir: "))

if edad_usu >= 18:
    print("Puedes comprar videojuegos para adultos.")
else:
    print("Solo puedes comprar juegos categoría E o T.")

info_empresa = ("GAMEJAM", "Videojuegos", 2000, "España")

print("\nINFORMACIÓN DE LA EMPRESA (Tupla):", info_empresa)
print("La palabra 'España' aparece:", info_empresa.count("España"))
print("Posición del tipo de tienda:", info_empresa.index("Videojuegos"))

lista_empresa = list(info_empresa)
lista_empresa.append("Sucursal Online")

info_empresa = tuple(lista_empresa)

print("Tupla actualizada:", info_empresa)

categorias = {"Acción", "Aventura", "Estrategia"}
nuevas_categoria = {"Deportes", "Aventura"}

categorias.add("RPG")
categorias.remove("Acción")

union_categorias = categorias.union(nuevas_categoria)
diferencia_categorias = categorias.difference(nuevas_categoria)

print("\nCategorías finales:", categorias)
print("Unión:", union_categorias)
print("Diferencia:", diferencia_categorias)
print("¿Existe 'RPG' en las categorías?:", "RPG" in categorias)

print(f"\nGracias por visitar {nombre_empresa}, {nombre_usu}.")
print(f"Elegiste los productos: {carrito}")
print("¡Vuelve pronto!!!")
