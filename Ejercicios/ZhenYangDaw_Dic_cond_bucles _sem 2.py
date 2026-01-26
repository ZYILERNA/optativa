# Programa de gestión de alumnos
# Profesora: Zhen Yang
# DAM2

# ----------------------
# Parte 1: Crear alumnos
# ----------------------
alumnos = {
    "Ana": {
        "Edad": 19,
        "Curso": "DAM2",
        "Lenguajes": {"Python", "Java"},
        "Nota media": 7.5
    },
    "Luis": {
        "Edad": 20,
        "Curso": "DAM1",
        "Lenguajes": {"C++", "Python"},
        "Nota media": 8.2
    },
    "Marta": {
        "Edad": 18,
        "Curso": "DAM2",
        "Lenguajes": {"JavaScript", "HTML", "CSS"},
        "Nota media": 6.8
    }
}

# ----------------------
# Función para mostrar alumnos
# ----------------------
def mostrar_alumnos(filtrar=False):
    """Muestra todos los alumnos o solo los que cumplen condiciones."""
    for nombre, info in alumnos.items():
        if filtrar:
            # Parte 4: Filtrar alumnos mayores de 18 y nota >= 7
            if info["Edad"] <= 18 or info["Nota media"] < 7:
                continue
        print(f"Alumno: {nombre}")
        print(f"Edad: {info['Edad']}")
        print(f"Curso: {info['Curso']}")
        print(f"Lenguajes: {', '.join(info['Lenguajes'])}")
        # Parte 3: Condicionales sobre notas
        nota = info["Nota media"]
        if nota < 5:
            estado = "Suspenso"
        elif nota < 7:
            estado = "Aprobado"
        elif nota < 9:
            estado = "Notable"
        else:
            estado = "Sobresaliente"
        print(f"Nota media: {nota} ({estado})")
        print("-" * 30)

# ----------------------
# Función para buscar alumno
# ----------------------
def buscar_alumno():
    nombre = input("Introduce el nombre del alumno a buscar: ").strip()
    alumno = alumnos.get(nombre)
    if alumno:
        print(f"Alumno: {nombre}")
        print(f"Edad: {alumno['Edad']}")
        print(f"Curso: {alumno['Curso']}")
        print(f"Lenguajes: {', '.join(alumno['Lenguajes'])}")
        print(f"Nota media: {alumno['Nota media']}")
    else:
        print("Alumno no encontrado")
    print("-" * 30)

# ----------------------
# Función para añadir alumno
# ----------------------
def añadir_alumno():
    nombre = input("Nombre del alumno (o 'salir' para cancelar): ").strip()
    if nombre.lower() == "salir":
        return  # Parte 8: volver al menú sin añadir
    if nombre in alumnos:
        print("El alumno ya existe.")
        return
    
    try:
        edad = int(input("Edad: "))
        curso = input("Curso: ").strip()
        lenguajes = input("Lenguajes (separados por comas): ").strip().split(",")
        lenguajes_set = set([l.strip() for l in lenguajes])
        nota = float(input("Nota media: "))
    except ValueError:
        print("Datos inválidos. Inténtalo de nuevo.")
        return
    
    # Guardar alumno en el diccionario
    alumnos[nombre] = {
        "Edad": edad,
        "Curso": curso,
        "Lenguajes": lenguajes_set,
        "Nota media": nota
    }
    print(f"Alumno {nombre} añadido correctamente.")
    print("-" * 30)

# ----------------------
# Función para calcular media general
# ----------------------
def media_general():
    if not alumnos:
        return 0
    total = sum(info["Nota media"] for info in alumnos.values())
    return total / len(alumnos)

# ----------------------
# Parte 5: Menú con bucle while
# ----------------------
while True:
    print("\n--- MENÚ DE ALUMNOS ---")
    print("1. Mostrar todos los alumnos")
    print("2. Buscar alumno")
    print("3. Añadir alumno")
    print("4. Mostrar alumnos filtrados (Edad>18 y Nota>=7)")
    print("5. Salir")
    
    opcion = input("Elige una opción: ").strip()
    
    if opcion == "1":
        mostrar_alumnos()
    elif opcion == "2":
        buscar_alumno()
    elif opcion == "3":
        añadir_alumno()
    elif opcion == "4":
        mostrar_alumnos(filtrar=True)
    elif opcion == "5":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Inténtalo de nuevo.")

# Reto final: Mostrar media de notas
print(f"\nMedia de notas de todos los alumnos: {media_general():.2f}")
