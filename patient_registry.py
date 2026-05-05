from typing import List, Dict

def main() -> None:
    """
    Main entry point for the patient registration system.
    Collects patient information and displays daily statistics.
    """
    pacientes: List[Dict[str, str]] = []  # each element will be a dictionary: {"nombre": ..., "servicio": ...}

    while True:
        nombre: str = input("Ingrese el nombre completo (o escriba FIN para terminar): ").strip()
        
        if nombre.lower() == "fin":
            print("Fin del registro.")
            break
        
        if not nombre:
            print("El nombre no puede estar vacío. Intente de nuevo.")
            continue
        
        print("Servicios disponibles:")
        print("1 - Medicina General")
        print("2 - Exámenes de Laboratorio")
        print("3 - Odontología")
        opcion: str = input("Elija el número del servicio (1, 2 o 3): ").strip()
        
        if opcion == "1":
            servicio = "Medicina General"
        elif opcion == "2":
            servicio = "Exámenes de Laboratorio"
        elif opcion == "3":
            servicio = "Odontología"
        else:
            print("Opción de servicio inválida. Se canceló el registro de este paciente.")
            continue
        
        paciente: Dict[str, str] = {"nombre": nombre, "servicio": servicio}
        pacientes.append(paciente)
        print(f"Turno registrado: {nombre} -> {servicio}\n")

    print("=== Resumen de la jornada ===")
    total: int = len(pacientes)
    print(f"Número total de turnos: {total}")

    if total == 0:
        print("No se registraron pacientes.")
    else:
        primer: str = pacientes[0]["nombre"]
        ultimo: str = pacientes[-1]["nombre"]
        print(f"Primer paciente registrado: {primer}")
        print(f"Último paciente registrado: {ultimo}")
        
        nombres: List[str] = [p["nombre"] for p in pacientes]
        nombres_ordenados: List[str] = sorted(nombres)
        print("\nListado alfabético de nombres:")
        for n in nombres_ordenados:
            print(f"- {n}")
        
        conteo: Dict[str, int] = {
            "Medicina General": 0,
            "Exámenes de Laboratorio": 0,
            "Odontología": 0
        }
        for p in pacientes:
            s: str = p["servicio"]
            if s in conteo:
                conteo[s] += 1
        
        print("\nCantidad de turnos por servicio:")
        for serv, cant in conteo.items():
            print(f"{serv}: {cant}")

if __name__ == "__main__":
    main()
