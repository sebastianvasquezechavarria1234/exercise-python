import json
import os
from typing import Dict, List, Optional, Any

class OrderSystem:
    """
    Handles orders, menu management, and sales reporting with JSON persistence.
    """
    MENU = {
        "papitas": 3500,
        "helados": 1500,
        "agua": 2300,
        "empanadas": 3400
    }
    DB_FILE = "orders.json"

    def __init__(self):
        self.orders: Dict[str, Dict[str, Any]] = self._load_data()

    def _load_data(self) -> Dict[str, Any]:
        if os.path.exists(self.DB_FILE):
            with open(self.DB_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        return {}

    def _save_data(self) -> None:
        with open(self.DB_FILE, "w", encoding="utf-8") as f:
            json.dump(self.orders, f, indent=4, ensure_ascii=False)

    def add_order(self, order_id: str, client: str, items: Dict[str, int]) -> bool:
        if order_id in self.orders:
            return False
        
        total = sum(self.MENU[prod] * cant for prod, cant in items.items())
        self.orders[order_id] = {
            "cliente": client,
            "items": items,
            "total": total,
            "estado": "activo"
        }
        self._save_data()
        return True

    def cancel_order(self, order_id: str) -> bool:
        if order_id in self.orders and self.orders[order_id]["estado"] == "activo":
            self.orders[order_id]["estado"] = "cancelado"
            self._save_data()
            return True
        return False

    def get_report(self) -> Dict:
        if not self.orders:
            return {}
            
        activos = [o for o in self.orders.values() if o["estado"] == "activo"]
        total_recaudado = sum(o["total"] for o in activos)
        
        return {
            "total_count": len(self.orders),
            "active_count": len(activos),
            "cancelled_count": len(self.orders) - len(activos),
            "revenue": total_recaudado,
            "average": total_recaudado / len(activos) if activos else 0
        }

def main() -> None:
    system = OrderSystem()
    while True:
        print("\n=== SISTEMA DE PEDIDOS (CON PERSISTENCIA) ===")
        print("1 - Registrar pedido")
        print("2 - Cancelar pedido")
        print("3 - Reporte General")
        print("0 - Salir")
        opc = input("Opción: ").strip()
        
        if opc == "1":
            num = input("Número pedido: ")
            cli = input("Cliente: ")
            items = {}
            for prod in system.MENU:
                try:
                    cant = int(input(f"Cantidad {prod} (0 para omitir): ") or 0)
                    if cant > 0: items[prod] = cant
                except ValueError:
                    print("Cantidad inválida, se tomará como 0.")
            
            if items and system.add_order(num, cli, items):
                print(f"Pedido {num} registrado.")
            else:
                print("Error: El pedido ya existe o está vacío.")
        elif opc == "2":
            num = input("Número a cancelar: ")
            if system.cancel_order(num): print("Cancelado.")
            else: print("No encontrado o ya cancelado.")
        elif opc == "3":
            rep = system.get_report()
            if not rep:
                print("No hay datos.")
            else:
                print(f"\n--- Reporte ---")
                print(f"Total pedidos: {rep['total_count']}")
                print(f"Activos: {rep['active_count']}")
                print(f"Ingresos: ${rep['revenue']}")
                print(f"Promedio: ${rep['average']:.2f}")
        elif opc == "0":
            break

if __name__ == "__main__":
    main()
