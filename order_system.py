# pedidos.py
# Sistema sencillo de pedidos (estilo principiante, fácil de leer)

MENU = {
    "papitas": 3500,
    "helados": 1500,
    "agua": 2300,
    "empanadas": 3400
}

# Aquí guardamos los pedidos: clave = numero_pedido (string)
pedidos = {}


def leer_entero(mensaje):
    """
    Pide un entero al usuario. Repite hasta que el usuario ponga un entero válido.
    Es una función auxiliar para evitar errores con int().
    """
    while True:
        entrada = input(mensaje).strip()
        if entrada == "":
            print("No ingresaste nada. Intenta de nuevo.")
            continue
        try:
            valor = int(entrada)
            return valor
        except ValueError:
            print("Por favor ingresa un número entero válido.")


def mostrar_menu():
    """Muestra el menú con precios."""
    print("\n--- MENÚ ---")
    for nombre, precio in MENU.items():
        print(f"{nombre} -> ${precio}")
    print("------------\n")


def registrar_pedido():
    """Registra un nuevo pedido con validaciones."""
    print("\nRegistrar nuevo pedido")
    numero = input("Número de pedido: ").strip()
    if numero == "":
        print("El número de pedido no puede estar vacío.")
        return

    if numero in pedidos:
        print("Ese número de pedido ya existe. Usa otro número.")
        return

    cliente = input("Nombre del cliente: ").strip()
    if cliente == "":
        print("El nombre del cliente no puede estar vacío.")
        return

    mostrar_menu()

    # Pedir cantidades por cada producto
    items = {}
    total_cantidades = 0
    for producto in MENU:
        cantidad = leer_entero(f"Cantidad de {producto} (0 si no desea): ")
        if cantidad < 0:
            print("No se permiten cantidades negativas. Registro cancelado.")
            return
        items[producto] = cantidad
        total_cantidades += cantidad

    if total_cantidades == 0:
        print("El pedido debe contener al menos un ítem. No se registró el pedido.")
        return

    # Calcular total automáticamente
    total = 0
    for producto, cantidad in items.items():
        precio = MENU[producto]
        total += precio * cantidad

    # Guardar pedido
    pedidos[numero] = {
        "cliente": cliente,
        "items": items,
        "total": total,
        "estado": "activo"   # puede ser "activo" o "cancelado"
    }

    print(f"Pedido registrado correctamente. Total a pagar: ${total}")


def consultar_pedido():
    """Consulta un pedido por su número y lo muestra."""
    print("\nConsultar pedido")
    numero = input("Número de pedido a consultar: ").strip()
    if numero not in pedidos:
        print("Pedido no encontrado.")
        return
    p = pedidos[numero]
    print(f"\nPedido Nº {numero}")
    print(f"Cliente: {p['cliente']}")
    print(f"Estado: {p['estado']}")
    print("Items:")
    for producto, cantidad in p["items"].items():
        if cantidad > 0:
            precio = MENU[producto]
            subtotal = precio * cantidad
            print(f" - {producto}: {cantidad} x ${precio} = ${subtotal}")
    print(f"Total: ${p['total']}\n")


def cancelar_pedido():
    """Cancela un pedido (cambia su estado a 'cancelado')."""
    print("\nCancelar pedido")
    numero = input("Número de pedido a cancelar: ").strip()
    if numero not in pedidos:
        print("Pedido no encontrado.")
        return
    if pedidos[numero]["estado"] == "cancelado":
        print("El pedido ya está cancelado.")
        return
    pedidos[numero]["estado"] = "cancelado"
    print("Pedido cancelado correctamente.")


def ver_todos_los_pedidos():
    """Muestra una lista simple con todos los pedidos."""
    print("\nTodos los pedidos:")
    if not pedidos:
        print("No hay pedidos registrados.")
        return
    for numero, p in pedidos.items():
        print(f"- Nº {numero} | Cliente: {p['cliente']} | Total: ${p['total']} | Estado: {p['estado']}")
    print("")  # línea en blanco


def generar_reporte_dia():
    """
    Genera el reporte del día:
    - Total de pedidos registrados
    - Pedidos activos y cancelados
    - Total recaudado (solo activos)
    - Promedio por pedido (sobre pedidos activos)
    - Pedido con valor más alto (entre activos)
    """
    print("\nReporte del día")
    total_pedidos = len(pedidos)
    if total_pedidos == 0:
        print("No hay pedidos para reportar.")
        return

    activos = [p for p in pedidos.values() if p["estado"] == "activo"]
    cancelados = [p for p in pedidos.values() if p["estado"] == "cancelado"]

    total_recaudado = sum(p["total"] for p in activos)
    cantidad_activos = len(activos)
    cantidad_cancelados = len(cancelados)

    if cantidad_activos > 0:
        promedio = total_recaudado // cantidad_activos  # promedio en pesos, entero
        pedido_mayor = max(activos, key=lambda x: x["total"])
        # buscar el número del pedido mayor
        numero_mayor = None
        for num, p in pedidos.items():
            if p is pedido_mayor:
                numero_mayor = num
                break
    else:
        promedio = 0
        pedido_mayor = None
        numero_mayor = None

    print(f"Total de pedidos registrados: {total_pedidos}")
    print(f" - Pedidos activos: {cantidad_activos}")
    print(f" - Pedidos cancelados: {cantidad_cancelados}")
    print(f"Total recaudado (solo activos): ${total_recaudado}")
    print(f"Promedio por pedido (activos): ${promedio}")
    if pedido_mayor:
        print(f"Pedido con valor más alto: Nº {numero_mayor} | Cliente: {pedido_mayor['cliente']} | Total: ${pedido_mayor['total']}")
    else:
        print("No hay pedidos activos para determinar el pedido más alto.")
    print("")


def menu_principal():
    """Menú principal que controla el flujo del programa."""
    while True:
        print("=== SISTEMA DE PEDIDOS ===")
        print("1 - Registrar pedido")
        print("2 - Consultar pedido por número")
        print("3 - Cancelar pedido")
        print("4 - Ver todos los pedidos")
        print("5 - Generar reporte del día")
        print("0 - Salir")
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            registrar_pedido()
        elif opcion == "2":
            consultar_pedido()
        elif opcion == "3":
            cancelar_pedido()
        elif opcion == "4":
            ver_todos_los_pedidos()
        elif opcion == "5":
            generar_reporte_dia()
        elif opcion == "0":
            print("Saliendo... hasta luego.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


# Punto de entrada
if __name__ == "__main__":
    menu_principal()
