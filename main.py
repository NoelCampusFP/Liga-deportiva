#Import de todos los demas archivos

import equipos
import jugadores
import calendario
import ranking


def menu_principal():
    salir = False
    while not salir:
        print("\nLIGA DEPORTIVA AMATEUR")
        print("1. Gestión de equipos")
        print("2. Gestión de jugadores")
        print("3. Calendario de partidos")
        print("4. Resultados y clasificación")
        print("5. Salir")

        opcion = input("Selecciona una opción (1-5): ").strip()

        if opcion == "1":
            equipos.menu_equipos()
        elif opcion == "2":
            jugadores.menu_jugadores()
        elif opcion == "3":
            calendario.menu_calendario()
        elif opcion == "4":
            ranking.menu_ranking()
        elif opcion == "5":
            print("Saliendo del programa...")
            salir = True
        else:
            print("Opción no válida. Inténtalo de nuevo.")


if __name__ == "__main__":
    menu_principal()
