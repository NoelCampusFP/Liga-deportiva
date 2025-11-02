from calendario import partidos
from equipos import equipos, listar_equipos

#Funciones

def registrar_resultado(partidos, equipos):
    """Permite registrar el resultado de un partido pendiente."""
    pendientes = [p for p in partidos if not p["jugado"]]
    if not pendientes:
        print("No hay partidos pendientes.")
        return

    print("\nPartidos pendientes:")
    for p in pendientes:
        local = next((e["nombre"] for e in equipos if e["id"] == p["local_id"]), "?")
        visitante = next((e["nombre"] for e in equipos if e["id"] == p["visitante_id"]), "?")
        print(f"ID {p['id']} | Jornada {p['jornada']} | {local} vs {visitante}")

    try:
        id_partido = int(input("Introduce el ID del partido a registrar: "))
        partido = next((p for p in partidos if p["id"] == id_partido and not p["jugado"]), None)
        if not partido:
            print("ID no válido o partido ya jugado.")
            return
        gL = int(input("Goles equipo local: "))
        gV = int(input("Goles equipo visitante: "))
        if gL < 0 or gV < 0:
            print("Los goles deben ser números no negativos.")
            return
    except ValueError:
        print("Entrada inválida.")
        return

    partido["resultado"] = (gL, gV)
    partido["jugado"] = True
    print("Resultado registrado .")


def calcular_clasificacion(partidos, equipos):
    """Calcula la tabla de posiciones según los partidos jugados."""
    tabla = []
    for eq in equipos:
        if not eq["activo"]:
            continue
        stats = {
            "id": eq["id"],
            "nombre": eq["nombre"],
            "PJ": 0, "G": 0, "E": 0, "P": 0,
            "GF": 0, "GC": 0, "DG": 0, "PTS": 0
        }
        for p in partidos:
            if not p["jugado"] or not p["resultado"]:
                continue
            gL, gV = p["resultado"]
            if p["local_id"] == eq["id"]:
                stats["PJ"] += 1
                stats["GF"] += gL
                stats["GC"] += gV
                if gL > gV:
                    stats["G"] += 1
                    stats["PTS"] += 3
                elif gL == gV:
                    stats["E"] += 1
                    stats["PTS"] += 1
                else:
                    stats["P"] += 1
            elif p["visitante_id"] == eq["id"]:
                stats["PJ"] += 1
                stats["GF"] += gV
                stats["GC"] += gL
                if gV > gL:
                    stats["G"] += 1
                    stats["PTS"] += 3
                elif gV == gL:
                    stats["E"] += 1
                    stats["PTS"] += 1
                else:
                    stats["P"] += 1
        stats["DG"] = stats["GF"] - stats["GC"]
        tabla.append(stats)
    tabla.sort(key=lambda x: (-x["PTS"], -x["DG"], -x["GF"]))
    return tabla

#Funcion clasificacion
def mostrar_clasificacion(tabla):
    """Muestra la tabla formateada."""
    print("\n Clasificacion")
    print("Pos | Equipo               | PJ | G | E | P | GF | GC | DG | PTS")
    for i, eq in enumerate(tabla, 1):
        print(f"{i:>3} | {eq['nombre']:<20} | {eq['PJ']:>2} | {eq['G']:>1} | {eq['E']:>1} | {eq['P']:>1} | {eq['GF']:>2} | {eq['GC']:>2} | {eq['DG']:>3} | {eq['PTS']:>3}")

#Funcion stats
def estadisticas_equipo(equipos, partidos):
    """Muestra resumen de estadísticas de un equipo."""
    listar_equipos(equipos)
    try:
        id_eq = int(input("ID del equipo: "))
    except ValueError:
        print("ID inválido.")
        return
    equipo = next((e for e in equipos if e["id"] == id_eq and e["activo"]), None)
    if not equipo:
        print("Equipo no encontrado o inactivo.")
        return

    tabla = calcular_clasificacion(partidos, equipos)
    stats = next((t for t in tabla if t["id"] == id_eq), None)
    if not stats:
        print("No hay datos aún para este equipo.")
        return
    print(f"\n📊 Estadísticas de {equipo['nombre']}:")
    print(f"PJ: {stats['PJ']}, GF: {stats['GF']}, GC: {stats['GC']}, PTS: {stats['PTS']}")


#Menú

def menu_ranking():
    salir = False
    while not salir:
        print("\n=== MÓDULO 4: Resultados y Clasificación ===")
        print("1 - Registrar resultado")
        print("2 - Ver clasificación")
        print("3 - Ver estadísticas por equipo")
        print("4 - Volver al menú principal")

        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            registrar_resultado(partidos, equipos)
        elif opcion == "2":
            tabla = calcular_clasificacion(partidos, equipos)
            mostrar_clasificacion(tabla)
        elif opcion == "3":
            estadisticas_equipo(equipos, partidos)
        elif opcion == "4":
            salir = True
        else:
            print("Opción no válida.")
