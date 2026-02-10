# ==========================================================
# mini_amazon.py
# Gestión de pedidos de comercio electrónico
# Profesora: Zhen Yang
# DAM / DAW
# ==========================================================

# ------------------ DATOS INICIALES ------------------

CATALOGO = {
    "A001": {"nombre": "Teclado Mecánico", "precio": 49.99, "stock": 10, "peso_kg": 0.9},
    "A002": {"nombre": "Ratón Gaming", "precio": 25.50, "stock": 5, "peso_kg": 0.2},
    "A003": {"nombre": "Monitor 24", "precio": 149.00, "stock": 3, "peso_kg": 3.5},
    "A004": {"nombre": "Auriculares", "precio": 35.99, "stock": 0, "peso_kg": 0.4},
    "A005": {"nombre": "Webcam HD", "precio": 39.90, "stock": 7, "peso_kg": 0.3},
}

CODIGOS_PROMO = {
    "ENVIOFREE": {"tipo": "envio", "descuento": 1.0},
    "DESC10": {"tipo": "total", "descuento": 0.10},
}

# ------------------ FUNCIONES ------------------

def mostrar_catalogo(catalogo):
    """Muestra el catálogo de productos"""
    print("\nCATÁLOGO")
    for codigo, datos in catalogo.items():
        print(f"{codigo} - {datos['nombre']} | {datos['precio']} € | Stock: {datos['stock']}")

def validar_codigo_producto(catalogo, codigo):
    """Valida si un código existe usando for-else"""
    for c in catalogo:
        if c == codigo:
            return True
    else:
        return False

def agregar_al_carrito(carrito, catalogo, codigo, cantidad):
    """Añade productos al carrito si hay stock"""
    if catalogo[codigo]["stock"] >= cantidad:
        carrito[codigo] = carrito.get(codigo, 0) + cantidad
        print("Producto añadido al carrito.")
    else:
        print("Stock insuficiente.")

def quitar_del_carrito(carrito, codigo, cantidad):
    """Quita productos del carrito"""
    if codigo in carrito and carrito[codigo] >= cantidad:
        carrito[codigo] -= cantidad
        if carrito[codigo] == 0:
            del carrito[codigo]
        print("Producto eliminado del carrito.")
    else:
        print("No se puede quitar esa cantidad.")

def ver_carrito(carrito, catalogo):
    """Muestra el contenido del carrito"""
    if not carrito:
        print("El carrito está vacío.")
        return

    print("\nCARRITO")
    for codigo, cantidad in carrito.items():
        nombre = catalogo[codigo]["nombre"]
        precio = catalogo[codigo]["precio"]
        print(f"{codigo} - {nombre} x{cantidad} → {precio * cantidad:.2f} €")

def calcular_totales(carrito, catalogo, iva=0.21):
    """Calcula subtotal, IVA, total y peso"""
    subtotal = 0
    peso_total = 0

    for codigo, cantidad in carrito.items():
        subtotal += catalogo[codigo]["precio"] * cantidad
        peso_total += catalogo[codigo]["peso_kg"] * cantidad

    return {
        "subtotal": subtotal,
        "iva": subtotal * iva,
        "total": subtotal * (1 + iva),
        "peso_total": peso_total
    }

def calcular_envio(peso_total, zona="PENINSULA"):
    """Calcula el coste del envío"""
    if peso_total == 0:
        return 0
    if peso_total <= 2:
        return 5
    elif peso_total <= 5:
        return 10
    else:
        return 20

def aplicar_promos(total, envio, *codigos):
    """Aplica códigos promocionales (*args)"""
    for codigo in codigos:
        if codigo in CODIGOS_PROMO:
            promo = CODIGOS_PROMO[codigo]
            if promo["tipo"] == "envio":
                envio = 0
            elif promo["tipo"] == "total":
                total *= (1 - promo["descuento"])
    return total, envio



def main():
    carrito = {}
    pedidos_confirmados = []
    pedidos_cancelados = []
    ventas = {}

    opcion = -1

    while opcion != 0:
        print("\n1. Ver catálogo")
        print("2. Añadir producto al carrito")
        print("3. Quitar producto del carrito")
        print("4. Ver carrito")
        print("5. Confirmar pedido")
        print("0. Salir")

        opcion = int(input("Elige una opción: "))

        if opcion == 1:
            mostrar_catalogo(CATALOGO)

        elif opcion == 2:
            codigo = input("Código del producto: ").upper()
            if not validar_codigo_producto(CATALOGO, codigo):
                print("Código inválido.")
                continue

            cantidad = int(input("Cantidad: "))
            agregar_al_carrito(carrito, CATALOGO, codigo, cantidad)

        elif opcion == 3:
            codigo = input("Código del producto: ").upper()
            cantidad = int(input("Cantidad a quitar: "))
            quitar_del_carrito(carrito, codigo, cantidad)

        elif opcion == 4:
            ver_carrito(carrito, CATALOGO)

        elif opcion == 5:
            if not carrito:
                print("No hay productos en el carrito.")
                continue

            totales = calcular_totales(carrito, CATALOGO)
            envio = calcular_envio(totales["peso_total"])

            promo = input("Código promo (ENTER si no): ").upper()
            total_final, envio = aplicar_promos(totales["total"], envio, promo)

            print("\nRESUMEN")
            print(f"Subtotal: {totales['subtotal']:.2f} €")
            print(f"IVA: {totales['iva']:.2f} €")
            print(f"Envío: {envio:.2f} €")
            print(f"TOTAL: {total_final + envio:.2f} €")

            confirmar = input("¿Confirmar pedido? (s/n): ").lower()

            if confirmar == "s":
                for codigo, cantidad in carrito.items():
                    CATALOGO[codigo]["stock"] -= cantidad
                    ventas[codigo] = ventas.get(codigo, 0) + cantidad
                pedidos_confirmados.append(dict(carrito))
                carrito.clear()
                print("Pedido CONFIRMADO.")
            else:
                pedidos_cancelados.append(dict(carrito))
                carrito.clear()
                print("Pedido CANCELADO.")

        elif opcion == 0:
            break
        else:
            print("Opción no válida.")

    else:
        print("Menú finalizado correctamente.")

    # ------------------ INFORME FINAL ------------------

    print("\nINFORME FINAL")
    print(f"Pedidos confirmados: {len(pedidos_confirmados)}")
    print(f"Pedidos cancelados: {len(pedidos_cancelados)}")

    for codigo, cantidad in ventas.items():
        producto_mas_vendido = max(ventas, key=ventas.get)
        print("Producto más vendido:", CATALOGO[producto_mas_vendido]["nombre"])
        break
    else:
        print("No hubo ventas registradas.")

# ------------------ EJECUCIÓN ------------------

if __name__ == "__main__":
    main()
