from typing import Dict, List, Optional, Any

class OrderSystem:
    """
    Handles orders, menu management, and sales reporting.
    """
    MENU = {
        "papitas": 3500,
        "helados": 1500,
        "agua": 2300,
        "empanadas": 3400
    }

    def __init__(self):
        self.orders: Dict[str, Dict[str, Any]] = {}

    def add_order(self, order_id: str, client: str, items: Dict[str, int]) -> bool:
        """Adds a new order to the system."""
        if order_id in self.orders:
            return False
        
        total = sum(self.MENU[prod] * cant for prod, cant in items.items())
        self.orders[order_id] = {
            "cliente": client,
            "items": items,
            "total": total,
            "estado": "activo"
        }
        return True

    def cancel_order(self, order_id: str) -> bool:
        """Marks an order as cancelled."""
        if order_id in self.orders and self.orders[order_id]["estado"] == "activo":
            self.orders[order_id]["estado"] = "cancelado"
            return True
        return False

    def get_active_orders(self) -> List[Dict]:
        return [o for o in self.orders.values() if o["estado"] == "activo"]

    def get_report(self) -> Dict:
        """Generates statistical data for all orders."""
        if not self.orders:
            return {}
            
        activos = self.get_active_orders()
        total_recaudado = sum(o["total"] for o in activos)
        
        return {
            "total_count": len(self.orders),
            "active_count": len(activos),
            "cancelled_count": len(self.orders) - len(activos),
            "revenue": total_recaudado,
            "average": total_recaudado / len(activos) if activos else 0
        }

# Logic for the CLI remains separate to maintain clean separation of concerns
def main() -> None:
    system = OrderSystem()
    while True:
        print("\n=== SISTEMA DE PEDIDOS ===")
        print("1 - Registrar pedido")
        print("2 - Cancelar pedido")
        print("3 - Reporte")
        print("0 - Salir")
        opc = input("Opción: ").strip()
        
        if opc == "1":
            num = input("Número pedido: ")
            cli = input("Cliente: ")
            items = {}
            for prod in system.MENU:
                cant = int(input(f"Cantidad {prod}: ") or 0)
                if cant > 0: items[prod] = cant
            if items and system.add_order(num, cli, items):
                print("Registrado.")
            else:
                print("Error en registro.")
        elif opc == "2":
            num = input("Número a cancelar: ")
            if system.cancel_order(num): print("Cancelado.")
            else: print("No encontrado o ya cancelado.")
        elif opc == "3":
            rep = system.get_report()
            print(f"Reporte: {rep}")
        elif opc == "0":
            break

if __name__ == "__main__":
    main()
