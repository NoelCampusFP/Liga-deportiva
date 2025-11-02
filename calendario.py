from equipos import equipos, listar_equipos

partidos = []

#Funciones

def generar_id(partidos):
    if partidos:
        return max(partido["id"] for partido in partidos) + 1
    return 1

def buscar_equipo(equipos, id_equipo):
    for equipo in equipos:
        if equipo["id"] == id_equipo:
            return equipo
    return None

def crear_partido(partidos, equipos):
    try:
        jornada = int(input("Jornada: "))
        local_id = int(input("ID equipo local: "))
        visitante_id = int(input("ID equipo visitante: "))
    except ValueError:
        print("Error: valores numéricos inválidos.")
        return

    if jornada < 1:
        print("La jornada debe ser mayor o igual a 1.")
        return
    if local_id == visitante_id:
        print("El equipo local y visitante deben ser diferentes.")
        return

    equipo_local = buscar_equipo(equipos, local_id)
    equipo_visitante = buscar_equipo(equipos, visitante_id)

    if not equipo_local or not equipo_visitante:
        print("Uno de los equipos no existe.")
        return
    if not equipo_local["activo"] or not equipo_visitante["activo"]:
        print("Ambos equipos deben estar activos.")
        return

    # Evitar duplicado mismo enfrentamiento en la misma jornada
    for partido in partidos:
        if partido["jornada"] == jornada and (
            (partido["local_id"] == local_id and partido["visitante_id"] == visitante_id)
            or (partido["local_id"] == visitante_id and partido["visitante_id"] == local_id)
        ):
            print("Ya existe un partido entre estos equipos en esta jornada.")
            return

    fecha = input("Fecha (YYYY-MM-DD): ")
    hora = input("Hora (HH:MM): ")

    nuevo_partido = {
        "id": generar_id(partidos),
        "jornada": jornada,
        "local_id": local_id,
        "visitante_id": visitante_id,
        "fecha": fecha,
        "hora": hora,
        "jugado": False,
        "resultado": None
    }

    partidos.append(nuevo_partido)
    print(" Partido creado .")

def listar_partidos(partidos, equipos):
    if not partidos:
        print("No hay partidos registrados.")
        return

    opcion = input("¿Deseas listar todos (T) o por jornada (J)? ").lower()
    if opcion == "j":
        try:
            jornada = int(input("Introduce número de jornada: "))
        except ValueError:
            print("Jornada inválida.")
            return
        lista_filtrada = [partido for partido in partidos if partido["jornada"] == jornada]
    else:
        lista_filtrada = partidos

    if not lista_filtrada:
        print("No hay partidos en esa jornada.")
        return

    print("\n Calendario de partidos:")
    for partido in lista_filtrada:
        equipo_local = buscar_equipo(equipos, partido["local_id"])
        equipo_visitante = buscar_equipo(equipos, partido["visitante_id"])
        nombre_local = equipo_local["nombre"] if equipo_local else "?"
        nombre_visitante = equipo_visitante["nombre"] if equipo_visitante else "?"
        estado = "Jugado" if partido["jugado"] else "Pendiente"
        print(f"ID {partido['id']} | Jornada {partido['jornada']} | {nombre_local} VS {nombre_visitante}")
        print(f"   Fecha: {partido['fecha']}  Hora: {partido['hora']}  Estado: {estado}")
        if partido["jugado"] and partido["resultado"]:
            print(f"   Resultado: {partido['resultado'][0]} - {partido['resultado'][1]}")

def reprogramar_partido(partidos):
    try:
        id_partido = int(input("id del partido a reprogramar: "))
    except ValueError:
        print("ID inválido.")
        return

    for partido in partidos:
        if partido["id"] == id_partido:
            if partido["jugado"]:
                print("No se puede reprogramar un partido ya jugado.")
                return
            nueva_fecha = input("Nueva fecha (YYYY-MM-DD): ")
            nueva_hora = input("Nueva hora (HH:MM): ")
            partido["fecha"] = nueva_fecha
            partido["hora"] = nueva_hora
            print("Partido reprogramado .")
            return
    print("Partido no encontrado.")

def eliminar_partido(partidos):
    try:
        id_partido = int(input("ID del partido a eliminar: "))
    except ValueError:
        print("ID inválido.")
        return

    for partido in partidos:
        if partido["id"] == id_partido:
            if partido["jugado"]:
                print("No se puede eliminar un partido jugado.")
                return
            partidos.remove(partido)
            print("❌ Partido eliminado.")
            return
    print("Partido no encontrado.")

#Menú

def menu_partidos():
    salir = False
    while not salir:
        print("\n Menú de partido")
        print("1 - Crear partido")
        print("2 - Listar partidos")
        print("3 - Reprogramar partido")
        print("4 - Eliminar partido")
        print("5 - Volver al menú principal")

        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            listar_equipos(equipos)
            crear_partido(partidos, equipos)
        elif opcion == "2":
            listar_partidos(partidos, equipos)
        elif opcion == "3":
            reprogramar_partido(partidos)
        elif opcion == "4":
            eliminar_partido(partidos)
        elif opcion == "5":
            salir = True
        else:
            print("Opción no válida.")
