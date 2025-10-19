
pacientes = []  # cada elemento será un diccionario: {"nombre": ..., "servicio": ...}

while True:  # bucle principal: se repite hasta que el usuario escriba "fin"
    nombre = input("Ingrese el nombre completo (o escriba FIN para terminar): ").strip()
    
    # Si el usuario quiere terminar
    if nombre.lower() == "fin":
        print("Fin del registro.")
        break  # salimos del bucle principal
    
    # Validar que el nombre no esté vacío
    if nombre == "":
        print("El nombre no puede estar vacío. Intente de nuevo.")
        continue  # volvemos a pedir el nombre (misma iteración del bucle principal)
    
    # Mostrar opciones de servicio y pedir que elija una
    print("Servicios disponibles:")
    print("1 - Medicina General")
    print("2 - Exámenes de Laboratorio")
    print("3 - Odontología")
    opcion = input("Elija el número del servicio (1, 2 o 3): ").strip()
    
    # Validar la opción del servicio y asignar el texto correspondiente
    if opcion == "1":
        servicio = "Medicina General"
    elif opcion == "2":
        servicio = "Exámenes de Laboratorio"
    elif opcion == "3":
        servicio = "Odontología"
    else:
        print("Opción de servicio inválida. Se canceló el registro de este paciente.")
        # Podrías usar 'continue' para volver a pedir todo; aquí solo saltamos a la siguiente iteración.
        continue
    
    # Guardar el paciente en la lista
    paciente = {"nombre": nombre, "servicio": servicio}
    pacientes.append(paciente)
    print("Turno registrado:", nombre, "->", servicio)
    print()  # línea en blanco para separar registros

# Al salir del bucle principal, mostrar el resumen
print("=== Resumen de la jornada ===")
total = len(pacientes)
print("Número total de turnos:", total)

if total == 0:
    print("No se registraron pacientes.")
else:
    # Primer y último paciente registrado
    primer = pacientes[0]["nombre"]
    ultimo = pacientes[-1]["nombre"]
    print("Primer paciente registrado:", primer)
    print("Último paciente registrado:", ultimo)
    
    # Listado alfabético de nombres
    nombres = [p["nombre"] for p in pacientes]
    nombres_ordenados = sorted(nombres)
    print("\nListado alfabético de nombres:")
    for n in nombres_ordenados:
        print("-", n)
    
    # Cantidad de turnos por servicio (contar manualmente)
    conteo = {
        "Medicina General": 0,
        "Exámenes de Laboratorio": 0,
        "Odontología": 0
    }
    for p in pacientes:
        s = p["servicio"]
        if s in conteo:
            conteo[s] += 1
    
    print("Cantidad de turnos por servicio:")
    print("Medicina General:", conteo["Medicina General"])
    print("Exámenes de Laboratorio:", conteo["Exámenes de Laboratorio"])
    print("Odontología:", conteo["Odontología"])
