from equipos import equipos, listar_equipos

#Lista diccionarios
jugadores = []

#Funciones

def generar_id(jugadores):
    if jugadores:
        return max(jugador["id"] for jugador in jugadores) + 1
    return 1

def buscar_id_equipo(equipos, id_equipo):
    for equipo in equipos:
        if equipo["id"] == id_equipo:
            return equipo
        return None
    
def buscar_id_jugador(jugadores,id_jugador):
    for jugador in jugadores:
        if jugador["id"] == id_jugador:
            return jugador
        return None
    
def crear_jugador(jugadores, equipos):
    nombre = input("Nombre del jugador: ")
    posicion = input("Posicion")
    try:
        equipo_id = int(input("id del equipo al que pertenece"))
    except ValueError:
        print("id no valido")
        return
    
    equipo = buscar_id_equipo(equipos, equipo_id)
    if not equipo:
        print("El equipo no existe")
        return
    if not equipo["activo"]:
        print("El equipo no esta activo, no se puede agregar al jugador")
        return
    
    nuevo_jugador = {
        "id": generar_id(jugadores),
        "nombre": nombre,
        "posicion": posicion,
        "equipo_id": equipo_id,
        "activo": True
    }
    jugadores.append(nuevo_jugador)
    print(f"Jugador {nombre} añadido al equipo{equipo['nombre']}.")
    
def listar_jugadores(jugadores, equipos):
    if not jugadores:
        print("No hay jugadores registrados.")
        return

    print("\n¿Deseas listar todos los jugadores o solo los de un equipo?")
    print("1 - Todos")
    print("2 - Por equipo")
    opcion = input("Opción: ")

    jugadores_filtrados = jugadores
    if opcion == "2":
        try:
            equipo_id = int(input("Introduce el ID del equipo: "))
        except ValueError:
            print("ID inválido.")
            return
        jugadores_filtrados = [jugador for jugador in jugadores if jugador["equipo_id"] == equipo_id]

    if not jugadores_filtrados:
        print("No hay jugadores para mostrar.")
        return

    print("\nLISTA DE JUGADORES:")
    for jugador in jugadores_filtrados:
        equipo = buscar_id_equipo(equipos, jugador["equipo_id"])
        nombre_equipo = equipo["nombre"] if equipo else "Equipo desconocido"
        estado = "Activo" if jugador["activo"] else "Inactivo"
        print(f"{jugador['id']}. {jugador['nombre']} - {jugador['posicion']} ({nombre_equipo}) [{estado}]")

def buscar_jugador(jugadores, equipos):
    try:
        id_jugador = int(input("ID del jugador: "))
    except ValueError:
        print("ID inválido.")
        return

    jugador = buscar_id_jugador(jugadores, id_jugador)
    if not jugador:
        print("Jugador no encontrado.")
        return

    equipo = buscar_id_equipo(equipos, jugador["equipo_id"])
    nombre_equipo = equipo["nombre"] if equipo else "Equipo desconocido"

    print("\nFICHA DEL JUGADOR")
    print(f"ID: {jugador['id']}")
    print(f"Nombre: {jugador['nombre']}")
    print(f"Posición: {jugador['posicion']}")
    print(f"Equipo: {nombre_equipo}")
    print(f"Activo: {'Sí' if jugador['activo'] else 'No'}")

def actualizar_jugador(jugadores, equipos):
    try:
        id_jugador = int(input("ID del jugador a actualizar: "))
    except ValueError:
        print("ID inválido.")
        return

    jugador = buscar_id_jugador(jugadores, id_jugador)
    if not jugador:
        print("Jugador no encontrado.")
        return

    print(f"\nEditando jugador {jugador['nombre']} ({jugador['posicion']})")

    nuevo_nombre = input(f"Nuevo nombre (actual: {jugador['nombre']}): ").strip()
    nueva_posicion = input(f"Nueva posición (actual: {jugador['posicion']}): ").strip()

    try:
        nuevo_equipo_id = input(f"Nuevo equipo ID (actual: {jugador['equipo_id']}): ").strip()
        nuevo_equipo_id = int(nuevo_equipo_id) if nuevo_equipo_id != "" else jugador["equipo_id"]
    except ValueError:
        print("ID de equipo inválido.")
        return

    equipo = buscar_id_equipo(equipos, nuevo_equipo_id)
    if not equipo or not equipo["activo"]:
        print("El nuevo equipo no existe o está inactivo.")
        return

    if nuevo_nombre:
        jugador["nombre"] = nuevo_nombre
    if nueva_posicion:
        jugador["posicion"] = nueva_posicion
    jugador["equipo_id"] = nuevo_equipo_id

    print("Jugador actualizado correctamente.")

def eliminar_jugador(jugadores):
    try:
        id_jugador = int(input("ID del jugador a desactivar: "))
    except ValueError:
        print("ID inválido.")
        return

    jugador = buscar_id_jugador(jugadores, id_jugador)
    if not jugador:
        print("Jugador no encontrado.")
        return

    jugador["activo"] = False
    print(f"Jugador {jugador['nombre']} desactivado.")

    #Menú jugadores

def menu_jugadores():
    salir = False
    while not salir:
        print("\nMENÚ DE JUGADORES")
        print("1 - Alta de jugador")
        print("2 - Listar jugadores")
        print("3 - Buscar jugador por ID")
        print("4 - Actualizar jugador")
        print("5 - Eliminar (desactivar) jugador")
        print("6 - Volver al menú principal")

        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            crear_jugador(jugadores, equipos)
        elif opcion == "2":
            listar_jugadores(jugadores, equipos)
        elif opcion == "3":
            buscar_jugador(jugadores, equipos)
        elif opcion == "4":
            actualizar_jugador(jugadores, equipos)
        elif opcion == "5":
            eliminar_jugador(jugadores)
        elif opcion == "6":
            salir = True
        else:
            print("Opción no válida.")