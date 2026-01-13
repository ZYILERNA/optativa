# actividad_listas2.py
# Práctica de creación y manipulación de listas en Python

print("="*60)
print("ACTIVIDAD: CREACIÓN Y MANIPULACIÓN DE LISTAS EN PYTHON")
print("="*60)

# 2. Declarar lista de precios con al menos 6 valores (con repetidos)
precios = [19.99, 35.50, 19.99, 42.00, 28.75, 35.50]
print("\n--- PASO 2: Creación de lista precios ---")
print("Lista precios:", precios)

# 3. Crear lista empleado con 4 datos distintos
empleado = ["Lucía", 29, "Diseñadora", "Barcelona"]
print("\n--- PASO 3: Creación de lista empleado ---")
print("Lista empleado:", empleado)

# 4. Analizar las listas
print("\n--- PASO 4: Análisis de las listas ---")
print("Precios:", precios)
print("Empleado:", empleado)

cantidad_precios = len(precios)
cantidad_empleado = len(empleado)
print("Cantidad de elementos en precios:", cantidad_precios)
print("Cantidad de elementos en empleado:", cantidad_empleado)

tipo_precios = type(precios)
tipo_empleado = type(empleado)
print("Tipo de dato de precios:", tipo_precios)
print("Tipo de dato de empleado:", tipo_empleado)

# 5. Acceder a elementos específicos
print("\n--- PASO 5: Acceso a elementos específicos ---")
primer_elemento = empleado[0]
tercer_elemento = empleado[2]
ultimo_elemento = empleado[-1]
penultimo_elemento = empleado[-2]

print("Primer elemento de empleado:", primer_elemento)
print("Tercer elemento de empleado:", tercer_elemento)
print("Último elemento de empleado:", ultimo_elemento)
print("Penúltimo elemento de empleado:", penultimo_elemento)

# 6. Actualizar información
print("\n--- PASO 6: Actualización de información ---")
empleado[3] = "Madrid"  # Cambiar ciudad
print("Ciudad actualizada:", empleado)

empleado.append("Marketing")  # Agregar departamento
print("Departamento agregado:", empleado)

empleado.insert(1, "EMP-2024-001")  # Insertar número de empleado en posición 1
print("Número de empleado insertado:", empleado)

# 7. Eliminar información
print("\n--- PASO 7: Eliminación de información ---")
precios.remove(19.99)  # Eliminar primer 19.99
print("Precio 19.99 eliminado:", precios)

precio_eliminado = precios.pop()  # Eliminar último precio
print("Último precio eliminado con pop():", precio_eliminado)
print("Lista precios actualizada:", precios)

del empleado[1]  # Eliminar segundo elemento (número de empleado)
print("Segundo elemento eliminado con del:", empleado)

# 8. Combinar listas
print("\n--- PASO 8: Combinación de listas ---")
datos_empresa = empleado + precios
print("Lista combinada datos_empresa:", datos_empresa)

# 9. Aplicar métodos de listas
print("\n--- PASO 9: Aplicación de métodos ---")
conteo = precios.count(35.50)
print("El precio 35.50 aparece", conteo, "veces")

precios_copia = precios.copy()  # Copiar lista
print("Copia de precios:", precios_copia)

precios.clear()  # Vaciar lista original
print("Lista precios después de clear():", precios)
print("Lista precios_copia (sin cambios):", precios_copia)

# 10. Ordenar y reorganizar
print("\n--- PASO 10: Ordenación y reorganización ---")
ventas = [450, 320, 580, 210, 490, 375]
print("Lista ventas original:", ventas)

ventas.sort()  # Ordenar de menor a mayor
print("Ventas ordenadas (menor a mayor):", ventas)

ventas.reverse()  # Invertir orden
print("Ventas invertidas (mayor a menor):", ventas)

# 11. Lista de lenguajes de programación
print("\n--- PASO 11: Lista de lenguajes de programación ---")
lenguajes = ["Python", "JavaScript", "Go", "Rust", "TypeScript"]
print("Lista lenguajes completa:", lenguajes)

primeros_dos = lenguajes[:2]
print("Primeros dos lenguajes (slicing [:2]):", primeros_dos)

lenguajes[1] = "Java"  # Cambiar JavaScript por Java (que ya conoces)
print("Lenguaje cambiado:", lenguajes)

lenguajes.append("Kotlin")  # Agregar nuevo lenguaje al final
print("Nuevo lenguaje agregado:", lenguajes)

del lenguajes[0]  # Eliminar el primero
print("Primer lenguaje eliminado:", lenguajes)

print("\n" + "="*60)
print("ACTIVIDAD COMPLETADA CON ÉXITO")
print("="*60)


