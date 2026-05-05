from typing import Dict, List, Optional, Any

MENU: Dict[str, int] = {
    "papitas": 3500,
    "helados": 1500,
    "agua": 2300,
    "empanadas": 3400
}

# In-memory storage for orders: key = order_number (string)
pedidos: Dict[str, Dict[str, Any]] = {}

def leer_entero(mensaje: str) -> int:
    """
    Prompts the user for an integer until a valid one is provided.
    
    Args:
        mensaje: The prompt message to display.
        
    Returns:
        The valid integer entered by the user.
    """
    while True:
        entrada: str = input(mensaje).strip()
        if not entrada:
            print("No ingresaste nada. Intenta de nuevo.")
            continue
        try:
            return int(entrada)
        except ValueError:
            print("Por favor ingresa un número entero válido.")

def mostrar_menu() -> None:
    """Displays the menu with prices."""
    print("\n--- MENÚ ---")
    for nombre, precio in MENU.items():
        print(f"{nombre} -> ${precio}")
    print("------------\n")

def registrar_pedido() -> None:
    """Registers a new order with validations."""
    print("\nRegistrar nuevo pedido")
    numero: str = input("Número de pedido: ").strip()
    if not numero:
        print("El número de pedido no puede estar vacío.")
        return

    if numero in pedidos:
        print("Ese número de pedido ya existe. Usa otro número.")
        return

    cliente: str = input("Nombre del cliente: ").strip()
    if not cliente:
        print("El nombre del cliente no puede estar vacío.")
        return

    mostrar_menu()

    items: Dict[str, int] = {}
    total_cantidades: int = 0
    for producto in MENU:
        cantidad: int = leer_entero(f"Cantidad de {producto} (0 si no desea): ")
        if cantidad < 0:
            print("No se permiten cantidades negativas. Registro cancelado.")
            return
        items[producto] = cantidad
        total_cantidades += cantidad

    if total_cantidades == 0:
        print("El pedido debe contener al menos un ítem. No se registró el pedido.")
        return

    total: int = sum(MENU[prod] * cant for prod, cant in items.items())

    pedidos[numero] = {
        "cliente": cliente,
        "items": items,
        "total": total,
        "estado": "activo"   # "activo" or "cancelado"
    }

    print(f"Pedido registrado correctamente. Total a pagar: ${total}")

def consultar_pedido() -> None:
    """Consults an order by its number and displays it."""
    print("\nConsultar pedido")
    numero: str = input("Número de pedido a consultar: ").strip()
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

def cancelar_pedido() -> None:
    """Cancels an order by changing its state to 'cancelado'."""
    print("\nCancelar pedido")
    numero: str = input("Número de pedido a cancelar: ").strip()
    if numero not in pedidos:
        print("Pedido no encontrado.")
        return
    if pedidos[numero]["estado"] == "cancelado":
        print("El pedido ya está cancelado.")
        return
    pedidos[numero]["estado"] = "cancelado"
    print("Pedido cancelado correctamente.")

def ver_todos_los_pedidos() -> None:
    """Displays a list of all registered orders."""
    print("\nTodos los pedidos:")
    if not pedidos:
        print("No hay pedidos registrados.")
        return
    for numero, p in pedidos.items():
        print(f"- Nº {numero} | Cliente: {p['cliente']} | Total: ${p['total']} | Estado: {p['estado']}")
    print("")

def generar_reporte_dia() -> None:
    """Generates and displays a daily sales report."""
    print("\nReporte del día")
    total_pedidos: int = len(pedidos)
    if total_pedidos == 0:
        print("No hay pedidos para reportar.")
        return

    activos: List[Dict[str, Any]] = [p for p in pedidos.values() if p["estado"] == "activo"]
    cancelados: List[Dict[str, Any]] = [p for p in pedidos.values() if p["estado"] == "cancelado"]

    total_recaudado: int = sum(p["total"] for p in activos)
    cantidad_activos: int = len(activos)
    cantidad_cancelados: int = len(cancelados)

    if cantidad_activos > 0:
        promedio: float = total_recaudado / cantidad_activos
        pedido_mayor = max(activos, key=lambda x: x["total"])
        numero_mayor: Optional[str] = next((num for num, p in pedidos.items() if p is pedido_mayor), None)
    else:
        promedio = 0.0
        pedido_mayor = None
        numero_mayor = None

    print(f"Total de pedidos registrados: {total_pedidos}")
    print(f" - Pedidos activos: {cantidad_activos}")
    print(f" - Pedidos cancelados: {cantidad_cancelados}")
    print(f"Total recaudado (solo activos): ${total_recaudado}")
    print(f"Promedio por pedido (activos): ${promedio:.2f}")
    if numero_mayor:
        print(f"Pedido con valor más alto: Nº {numero_mayor} | Cliente: {pedido_mayor['cliente']} | Total: ${pedido_mayor['total']}")
    print("")

def menu_principal() -> None:
    """Main menu to control the program flow."""
    while True:
        print("=== SISTEMA DE PEDIDOS ===")
        print("1 - Registrar pedido")
        print("2 - Consultar pedido por número")
        print("3 - Cancelar pedido")
        print("4 - Ver todos los pedidos")
        print("5 - Generar reporte del día")
        print("0 - Salir")
        opcion: str = input("Elige una opción: ").strip()

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

if __name__ == "__main__":
    menu_principal()
