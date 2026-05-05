from typing import List

def leer_consumo(mensaje: str) -> float:
    """
    Prompts the user for a water consumption value in liters.
    
    Args:
        mensaje: The prompt message to display.
        
    Returns:
        The consumption value as a float, or -1.0 to signal termination.
    """
    while True:
        entrada: str = input(mensaje).strip()
        if entrada == "-1":
            return -1.0
        if not entrada:
            print("No ingresaste nada. Intenta de nuevo.")
            continue
        try:
            valor: float = float(entrada)
            if valor <= 0:
                print("El consumo debe ser mayor que cero. Intenta de nuevo (o -1 para terminar).")
                continue
            return valor
        except ValueError:
            print("Por favor ingresa un número válido (ej. 12.5) o -1 para terminar.")

def registrar_consumos() -> List[float]:
    """
    Collects daily water consumption data from the user.
    
    Returns:
        A list of daily consumption values in liters.
    """
    consumos: List[float] = []
    dia: int = 1
    print("Registro de consumo diario de agua")
    print("Escribe -1 cuando quieras terminar el registro.\n")

    while True:
        mensaje: str = f"Ingrese litros consumidos en el día {dia} (o -1 para terminar): "
        valor: float = leer_consumo(mensaje)
        if valor == -1.0:
            break
        consumos.append(valor)
        dia += 1

    return consumos

def generar_informe(consumos: List[float]) -> None:
    """
    Generates and prints a statistical report of water consumption.
    
    Args:
        consumos: List of daily consumption values.
    """
    print("\n--- INFORME DEL MES ---")

    if not consumos:
        print("No se registraron consumos. No hay datos para mostrar.")
        return

    total_dias: int = len(consumos)
    total_litros: float = sum(consumos)
    promedio: float = total_litros / total_dias

    valor_max: float = max(consumos)
    dia_max: int = consumos.index(valor_max) + 1
    valor_min: float = min(consumos)
    dia_min: int = consumos.index(valor_min) + 1

    listado_asc: List[float] = sorted(consumos)

    print(f"Total de días registrados: {total_dias}")
    print(f"Total de litros consumidos: {total_litros:.2f} L")
    print(f"Promedio diario: {promedio:.2f} L/día")
    print(f"Día con mayor consumo: Día {dia_max} -> {valor_max:.2f} L")
    print(f"Día con menor consumo: Día {dia_min} -> {valor_min:.2f} L")
    print("\nListado completo del consumo diario (orden ascendente):")
    for i, v in enumerate(listado_asc, start=1):
        print(f" {i}. {v:.2f} L")
    print("------------------------\n")

def main() -> None:
    """Main entry point for the water consumption tracker."""
    consumos: List[float] = registrar_consumos()
    generar_informe(consumos)

if __name__ == "__main__":
    main()
