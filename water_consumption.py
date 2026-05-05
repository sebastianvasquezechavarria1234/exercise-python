# consumo_agua.py
# Registro sencillo del consumo diario de agua (estilo principiante)

def leer_consumo(mensaje):
    """
    Pide al usuario un valor de consumo en litros.
    - Si el usuario escribe '-1' devuelve -1 (señal de terminar).
    - Si ingresa un número mayor que 0 lo devuelve como float.
    - Repite hasta recibir una entrada válida.
    """
    while True:
        entrada = input(mensaje).strip()
        if entrada == "-1":
            return -1
        if entrada == "":
            print("No ingresaste nada. Intenta de nuevo.")
            continue
        try:
            valor = float(entrada)
        except ValueError:
            print("Por favor ingresa un número (ej. 12.5) o -1 para terminar.")
            continue
        if valor <= 0:
            print("El consumo debe ser mayor que cero. Intenta de nuevo (o -1 para terminar).")
            continue
        return valor


def registrar_consumos():
    """
    Registra consumos diarios hasta que el usuario escriba -1.
    Devuelve la lista de consumos (en litros).
    """
    consumos = []
    dia = 1
    print("Registro de consumo diario de agua")
    print("Escribe -1 cuando quieras terminar el registro.\n")

    while True:
        mensaje = f"Ingrese litros consumidos en el día {dia} (o -1 para terminar): "
        valor = leer_consumo(mensaje)
        if valor == -1:
            break
        consumos.append(valor)
        dia += 1

    return consumos


def generar_informe(consumos):
    """
    Genera e imprime el informe estadístico:
    - Total de días registrados
    - Promedio de consumo
    - Día con mayor consumo
    - Día con menor consumo
    - Listado completo en orden ascendente
    """
    print("\n--- INFORME DEL MES ---")

    if not consumos:
        print("No se registraron consumos. No hay datos para mostrar.")
        return

    total_dias = len(consumos)
    total_litros = sum(consumos)
    promedio = total_litros / total_dias

    # Día con mayor y menor consumo (se muestra el primer día en caso de empate)
    valor_max = max(consumos)
    dia_max = consumos.index(valor_max) + 1  # +1 para contar días desde 1
    valor_min = min(consumos)
    dia_min = consumos.index(valor_min) + 1

    # Listado ascendente
    listado_asc = sorted(consumos)

    # Imprimir resultados con formato legible
    print(f"Total de días registrados: {total_dias}")
    print(f"Total de litros consumidos: {total_litros:.2f} L")
    print(f"Promedio diario: {promedio:.2f} L/día")
    print(f"Día con mayor consumo: Día {dia_max} -> {valor_max:.2f} L")
    print(f"Día con menor consumo: Día {dia_min} -> {valor_min:.2f} L")
    print("\nListado completo del consumo diario (orden ascendente):")
    for i, v in enumerate(listado_asc, start=1):
        print(f" {i}. {v:.2f} L")
    print("------------------------\n")


def main():
    consumos = registrar_consumos()
    generar_informe(consumos)


if __name__ == "__main__":
    main()
