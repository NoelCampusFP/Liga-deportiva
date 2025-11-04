# Lista de diccionarios
equipos = [
    {
        "id": 1,
        "nombre": "Leones",
        "ciudad": "Leganes",
        "activo": True
    }
]

# Funciones
def generar_id(equipos):
    if equipos:
        return max(equipo["id"] for equipo in equipos) + 1
    return 1

def crear_equipo(equipos):
    nombre = input("Nombre: ").strip()
    ciudad = input("Ciudad: ").strip()
    if nombre and ciudad:
        nuevo = {
            "id": generar_id(equipos),
            "nombre": nombre,
            "ciudad": ciudad,
            "activo": True
        }
        equipos.append(nuevo)
        print("Equipo creado correctamente.")
    else:
        print("Nombre y ciudad no pueden estar vacíos.")

def listar_equipos(equipos):
    if not equipos:
        print("No hay equipos registrados.")
    else:
        print("\nLISTA DE EQUIPOS:")
        for equipo in equipos:
            estado = "Activo" if equipo["activo"] else "Inactivo"
            print(f"{equipo['id']}. {equipo['nombre']} - {equipo['ciudad']} ({estado})")

def actualizar_equipo(equipos):
    try:
        id_equipo = int(input("ID del equipo que quieres actualizar: "))
    except ValueError:
        print("ID inválido.")
        return

    for equipo in equipos:
        if equipo["id"] == id_equipo:
            print(f"\nEditando equipo: {equipo['nombre']} - {equipo['ciudad']}")
            nuevo_nombre = input(f"Nuevo nombre (actual: {equipo['nombre']}): ").strip()
            nueva_ciudad = input(f"Nueva ciudad (actual: {equipo['ciudad']}): ").strip()
            nuevo_estado = input(f"¿Activo? (s/n) [actual: {'s' if equipo['activo'] else 'n'}]: ").lower()

            if nuevo_nombre:
                equipo["nombre"] = nuevo_nombre
            if nueva_ciudad:
                equipo["ciudad"] = nueva_ciudad
            if nuevo_estado in ["s", "n"]:
                equipo["activo"] = (nuevo_estado == "s")

            print("Equipo actualizado correctamente.")
            return
    print("Equipo no encontrado.")

def eliminar_equipo(equipos):
    try:
        id_borrar = int(input("ID del equipo a desactivar: "))
    except ValueError:
        print("ID no válido.")
        return

    for equipo in equipos:
        if equipo["id"] == id_borrar:
            equipo["activo"] = False
            print("Equipo desactivado correctamente.")
            return
    print("Equipo no encontrado.")

# Menú de equipos
def menu_equipos():
    salir = False
    while not salir:
        print("\nMENÚ DE EQUIPOS")
        print("1 - Crear nuevo equipo")
        print("2 - Listar equipos")
        print("3 - Actualizar datos de un equipo")
        print("4 - Desactivar equipo")
        print("5 - Volver al menú principal")

        opcion = input("Selecciona una opción (1-5): ").strip()

        if opcion == "1":
            crear_equipo(equipos)
        elif opcion == "2":
            listar_equipos(equipos)
        elif opcion == "3":
            actualizar_equipo(equipos)
        elif opcion == "4":
            eliminar_equipo(equipos)
        elif opcion == "5":
            print("Volviendo al menú principal...")
            salir = True
        else:
            print("Opción no válida. Inténtalo de nuevo.")
