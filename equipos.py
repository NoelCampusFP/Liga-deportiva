# Lista de diccionarios
equipos = []
{
    "id": 1,
    "nombre": "Leones",
    "ciudad": "Leganes",
    "activo": True
}
# Funciones 

def generar_id(equipos):
    if equipos:
        return max(equipo["id"] for equipo in equipos) + 1
    return 1

def crear_equipo(equipos):
    nombre = input("nombre: ").strip()
    ciudad = input("Ciudad. ").strip()
    if nombre != "" and ciudad != "":
        nuevo = {
            "id": generar_id(equipos),
            "nombre": nombre,
            "ciudad": ciudad,
            "activo": True
        }
        equipos.append(nuevo)
        print("Equipo creado")
    else:
        print("Nombre y ciudad no pueden estar vacios")

def listar_equipos(equipos):
    if len(equipos) ==0:
        print("No hay equipos")
    else:
        print("\n LISTA DE EQUIPOS")
        for equipo in equipos:
            estado = "activo" if equipo["activo"] else "inactivo"
            print(f"{equipo['id']}. {equipo['nombre']} - {equipo['ciudad']} ({estado})")

def actualizar_equipo(equipos):
    try:
        id_equipo = int(input("id del equipo que quieres actualizar: "))
    except ValueError:
        print("id invalido")
        return 
    
    encontrado = False

    for equipo in equipos:
        if equipo["id"] == id_equipo:
             print(f"\nEditando equipo: {equipo['nombre']} - {equipo['ciudad']}")
            
    nuevo_nombre = input(f"Nuevo nombre (actual: {equipo['nombre']}): ").strip()
    nueva_ciudad = input(f"Nueva ciudad (actual: {equipo['ciudad']}): ").strip()
    nuevo_estado = input(f"¿Activo? (s/n) [actual: {'s' if equipo['activo'] else 'n'}]: ").lower()

    if nuevo_nombre != "":
        equipo["nombre"] = nuevo_nombre
    if nueva_ciudad != "":
        equipo["ciudad"] = nueva_ciudad
    if nuevo_estado != "":
        equipo["estado"] = nuevo_estado

def eliminar_equipo(equipos):
    try:
        id_borrar = int(input("id a desactivar"))
    except ValueError:
        print("id no valido")
        return
    encontrado = False
    for equipo in equipos:
        if equipo["id"] == id_borrar:
            equipo["activo"] = False
            print("equipo desactivado")
            encontrado = True
    if not encontrado:
        print("Equipo no encontrado")

# Menú de equipo        

def menu_equipos():
    equipos = []
    salir = False

    while not salir:
        print("\nMENÚ DE EQUIPOS")
        print("1 - Crear nuevo equipo")
        print("2 - Listar equipos")
        print("3 - Buscar equipo por ID")
        print("4 - Actualizar datos de un equipo")
        print("5 - Desactivar (eliminar) equipo")
        print("6- Salir del módulo")