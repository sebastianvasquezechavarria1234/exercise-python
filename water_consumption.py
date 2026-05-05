import json
import os
from typing import List, Dict

class WaterTracker:
    """
    Tracks daily water consumption with persistence and analysis.
    """
    DB_FILE = "water_data.json"

    def __init__(self):
        self.consumos: List[float] = self._load_data()

    def _load_data(self) -> List[float]:
        if os.path.exists(self.DB_FILE):
            with open(self.DB_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        return []

    def _save_data(self) -> None:
        with open(self.DB_FILE, "w", encoding="utf-8") as f:
            json.dump(self.consumos, f, indent=4)

    def add_consumption(self, value: float) -> None:
        if value > 0:
            self.consumos.append(value)
            self._save_data()

    def get_analysis(self) -> Dict:
        if not self.consumos:
            return {}
        
        total = sum(self.consumos)
        count = len(self.consumos)
        v_max = max(self.consumos)
        v_min = min(self.consumos)
        
        return {
            "total_days": count,
            "total_liters": total,
            "average": total / count,
            "max": {"value": v_max, "day": self.consumos.index(v_max) + 1},
            "min": {"value": v_min, "day": self.consumos.index(v_min) + 1},
            "sorted_list": sorted(self.consumos)
        }

def main() -> None:
    tracker = WaterTracker()
    print("=== MONITOR DE CONSUMO DE AGUA ===")
    print("Escriba -1 para terminar de ingresar datos.\n")

    while True:
        dia = len(tracker.consumos) + 1
        try:
            entrada = input(f"Día {dia} - Litros: ").strip()
            if entrada == "-1": break
            val = float(entrada)
            if val <= 0:
                print("El valor debe ser positivo.")
                continue
            tracker.add_consumption(val)
        except ValueError:
            print("Entrada inválida.")

    analysis = tracker.get_analysis()
    if not analysis:
        print("No hay datos registrados.")
        return

    print("\n--- INFORME ESTADÍSTICO ---")
    print(f"Días registrados: {analysis['total_days']}")
    print(f"Total consumido: {analysis['total_liters']:.2f} L")
    print(f"Promedio diario: {analysis['average']:.2f} L/día")
    print(f"Máximo: {analysis['max']['value']:.2f} L (Día {analysis['max']['day']})")
    print(f"Mínimo: {analysis['min']['value']:.2f} L (Día {analysis['min']['day']})")

if __name__ == "__main__":
    main()
