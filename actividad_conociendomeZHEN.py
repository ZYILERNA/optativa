"""
Crea tres variables para guardar:
Tu nombre completo (tipo str)
Tu edad (tipo int)
Si eres estudiante o no (tipo bool)
Muestra la información en pantalla con frases personalizadas.
Usa la función type() para mostrar el tipo de dato de cada variable.
Cambia el valor de una de las variables y muestra nuevamente el resultado.
"""

nombre = "zhenyang"

edad = 19

estudiante = True

print("mi nombre es" + nombre + "tengo " + str(edad) + "años" + "soy estudiante?" + str(estudiante))


"""
Parte 2 – Gustos personales
Pide al usuario tres cosas que le gusten (por ejemplo: leer, música, viajar).
Guarda esas respuestas en una lista llamada gustos.
Muestra la lista completa en pantalla.
Usa la función len() para mostrar cuántos elementos tiene la lista.
Crea una nueva lista llamada gustos_modificados que repita los gustos dos veces (usando gustos * 2).
Muestra el resultado y explica en un comentario qué observas.
"""

print("¿Qué te gusta leer?")
leer = input()
print("¿Qué música te gusta?")
musica = input()
print("¿Dónde te gustaría viajar?")
viajar = input()

gustos = [leer, musica, viajar]

print("Tus gustos son:", gustos)

print("La lista tiene", len(gustos), "elementos.")

gustos_modificados = gustos * 2

print("Lista modificada:", gustos_modificados)

"""
Bueno, hemos visto que para pedir al usuario se utiliza input() que tambien se le puede poner en vez de print, pues poniendo el texto dentro del input
osea input("¿Qué te gusta leer?").

para guardar en una lista, tan oslo tneemos que coger las variables introducidas por el usuario y guardarla en formato lista
gustos = [leer, musica, viajar], y si ahora imprimimos la variable lista, nos muestra en formato: 
Tus gustos son: ['lirbos', 'pop', 'caribe']

el len() sirve para mostrar la cantidad de variables que tiene almacenado, en este caso 3, y si lo guardamos en una nueva variable *2.
veremos que mostrara la misma lista, pero más larga. Qué sería algo como.['lirbos', 'pop', 'caribe','lirbos', 'pop', 'caribe']
"""


"""
Parte 3 – Comidas favoritas
Crea una tupla llamada comidas_favoritas con tres comidas que te gusten mucho.
Muestra la tupla completa.
Intenta cambiar uno de los valores de la tupla (solo como experimento).
Escribe en un comentario qué sucede y por qué.
Usa len() para contar cuántas comidas hay en la tupla.

"""
comidas_favoritas = ("pizza", "tacos", "helado")

print("Mis comidas favoritas son:", comidas_favoritas)

"""
Intentamos cambiar uno de los valores de la tupla (solo como experimento)
comidas_favoritas[0] = "sushi"  # <-- Esto dará un error

Las tuplas son inmutables, es decir, **no se puede cambiar un elemento una vez creada**.
Si descomentas la línea de arriba, Python lanzará un TypeError.

Usamos len() para contar cuántas comidas hay en la tupla
"""

print("La tupla tiene", len(comidas_favoritas), "comidas.")


"""
Parte 4 – Conjunto de números
Crea un conjunto (set) llamado numeros con algunos números repetidos, por ejemplo:
numeros = {1, 2, 2, 3, 4, 4, 5}
Muestra el conjunto en pantalla y observa qué sucede con los valores duplicados.
Agrega otro número al conjunto reescribiendo la variable, por ejemplo:
numeros = numeros | {6}
Muestra nuevamente el conjunto y observa el cambio.
Escribe un comentario explicando por qué los valores repetidos no aparecen más de una vez.
"""

numeros = {1, 2, 2, 3, 4, 4, 5}

print("Conjunto inicial:", numeros)


"""
Como no permiten valores repetidos, 2 4 en este caso aparecerán solo una vez.
"""

'Agregamos otro número usando la unión de conjuntos'
numeros = numeros | {6}

print("Conjunto después de agregar 6:", numeros)

"""
los duplicados se eliminan igual, al sumar un nuevo numero que no existía entonces se le agregará.
"""



"""
Parte 5 – Tipos de datos y resumen
Usa la función type() para mostrar el tipo de dato de:
Tu variable nombre
La lista gustos
La tupla comidas_favoritas
El conjunto numeros
Crea una nueva lista llamada resumen que contenga las tres estructuras principales:
resumen = [gustos, comidas_favoritas, numeros]
Muestra el contenido de resumen y comenta qué observas al combinar diferentes tipos de datos en una lista.
"""

print("Tipo de 'nombre':", type(nombre))
print("Tipo de 'gustos':", type(gustos))
print("Tipo de 'comidas_favoritas':", type(comidas_favoritas))
print("Tipo de 'numeros':", type(numeros))

resumen = [gustos, comidas_favoritas, numeros]

print("Resumen combinado:", resumen)


"""
Podemos combinar diferentes tipos de datos dentro de una lista.
Aquí, 'resumen' contiene una lista, una tupla y un conjunto.
Python permite mezclar tipos de datos en la misma lista sin problema,
pero cada elemento sigue conservando su tipo original.
Tipo de 'nombre': <class 'str'>
Tipo de 'gustos': <class 'list'>
Tipo de 'comidas_favoritas': <class 'tuple'>
Tipo de 'numeros': <class 'set'>
Resumen combinado: [['pap"', 'papa', 'pepe'], ('pizza', 'tacos', 'helado'), {1, 2, 3, 4, 5, 6}]
"""


"""
Parte 6 – Reto de lógica
Usa la edad que guardaste en la parte 1.
Escribe un bloque de código que imprima un mensaje diferente según la edad:
Si la edad es menor de 18: muestra “Eres menor de edad”.
Si la edad es entre 18 y 30: muestra “Eres joven”.
Si es mayor de 30: muestra “Eres adulto”.
Usa operadores lógicos (and, or) para combinar condiciones.
Explica en un comentario qué hace tu código y por qué.
 Pista: Recuerda que puedes usar la estructura if, elif y else.
Ejemplo :
if edad < 18:
    print("Eres menor de edad.")
elif edad >= 18 and edad <= 30:
    print("Eres joven.")
else:
    print("Eres adulto.")
"""

if edad < 18:
    print("Eres menor de edad")
elif edad >=18 and edad <= 30:
    print("Eres joven")
else:
    print("Eres adulto")

"""
Estamos comparando con la variable del ejercicio 1, a la que es un if, donde si la variable edad es menor de 18 <18,
pondra eres menor de edad, si eres mayor o igual que 18 y menor o igual a 30 pues eres joven.
pondra eres adulta si no coincides con los ifs. que es en este caso mayor de 18 y superando los 30 osea 31.
Como en el ejercicio anterior puse 19, pues me imprime en la consola Eres joven.
"""

"""
Parte 7 – Reflexiona
Responde en tu documento:
¿Qué tipo de dato devuelve la función input()?

Siempre será texto, si quieres usarlo en numero o float que es el numero con decimales, pues hay que utilizar int() a la variable o float().

¿Por qué el conjunto no muestra los valores duplicados?

Porque los sets en Python no permiten elementos duplicados.
Al crear un conjunto, automáticamente elimina cualquier repetido.

¿Cuál es la diferencia entre una lista y una tupla?

Lista: puedes modificar, agregar o eliminar elementos.

Tupla: no puedes cambiar sus elementos una vez creada.

¿Qué sucede si cambias el orden de los elementos en un conjunto?

El set no está ordenado, Python puede mostrarlos en cualquier orden.

Los sets se enfocan en que no repitan los número, no en el orden.

¿Por qué las listas permiten modificaciones y las tuplas no?

Las listas son diseñadas para colecciones dinámicas.

Las tuplas son inmutables para garantizar seguridad y eficiencia, especialmente al usarlas como claves de diccionarios o en estructuras donde no se quiere que cambien.

¿Qué ventajas tiene usar conjuntos en un programa?

Evitan duplicados automáticamente.

Permiten operaciones rápidas de unión, intersección y diferencia.

Son útiles para filtrar elementos únicos o hacer comparaciones entre grupos.

En el bloque de lógica, ¿por qué crees que se usan condiciones en orden (if, elif, else) y no todas a la vez?

Porque Python evalúa las condiciones de arriba hacia abajo.

Usar elif evita que se ejecuten múltiples bloques cuando solo queremos una acción por caso.

Esto hace el programa más eficiente y lógico, ya que cada situación se maneja de forma exclusiva.

"""