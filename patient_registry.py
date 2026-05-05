from typing import List, Dict
from collections import Counter

class PatientRegistry:
    """
    Manages patient registration and generates service statistics.
    """
    SERVICES = {
        "1": "Medicina General",
        "2": "Exámenes de Laboratorio",
        "3": "Odontología"
    }

    def __init__(self):
        self.patients: List[Dict[str, str]] = []

    def register_patient(self, name: str, service_code: str) -> bool:
        """
        Registers a new patient with a specific service.
        """
        service = self.SERVICES.get(service_code)
        if not service:
            return False
        
        self.patients.append({"nombre": name, "servicio": service})
        return True

    def get_summary(self) -> Dict:
        """
        Calculates and returns a summary of the registration session.
        """
        if not self.patients:
            return {}

        nombres = [p["nombre"] for p in self.patients]
        servicios = [p["servicio"] for p in self.patients]
        
        return {
            "total": len(self.patients),
            "primer": self.patients[0]["nombre"],
            "ultimo": self.patients[-1]["nombre"],
            "nombres_ordenados": sorted(nombres),
            "conteo_servicios": Counter(servicios)
        }

def main() -> None:
    registry = PatientRegistry()
    
    while True:
        nombre = input("Ingrese el nombre completo (o escriba FIN para terminar): ").strip()
        if nombre.lower() == "fin":
            break
        if not nombre:
            print("El nombre no puede estar vacío.")
            continue
        
        print("\nServicios disponibles:")
        for code, name in registry.SERVICES.items():
            print(f"{code} - {name}")
            
        opcion = input("Elija el número del servicio: ").strip()
        
        if registry.register_patient(nombre, opcion):
            print(f"Turno registrado correctamente.\n")
        else:
            print("Opción de servicio inválida. Registro cancelado.\n")

    summary = registry.get_summary()
    print("\n=== Resumen de la jornada ===")
    if not summary:
        print("No se registraron pacientes.")
        return

    print(f"Número total de turnos: {summary['total']}")
    print(f"Primer paciente: {summary['primer']}")
    print(f"Último paciente: {summary['ultimo']}")
    
    print("\nListado alfabético:")
    for n in summary['nombres_ordenados']:
        print(f"- {n}")
        
    print("\nCantidad de turnos por servicio:")
    for serv, cant in summary['conteo_servicios'].items():
        print(f"{serv}: {cant}")

if __name__ == "__main__":
    main()
