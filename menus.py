from funciones import *


# Las funciones con las diferentes capas de menu


########################
# Primera capa de menu #
########################


def menu_principal() -> str:
    menu = (
        "\n╔" + "═"*48 + "╗\n"
        "║" + " PANEL DE CONTROL - GESTIÓN DE LABORATORIO ".center(48, "░") + "║\n"
        "╠" + "═"*48 + "╣\n"
        "║ [1] -> Gestión de Almacenes (Inventarios)      ║\n"
        "║ [2] -> Control de Equipamiento Técnico         ║\n"
        "║ [3] -> Entrada de Consumibles y Reactivos      ║\n"
        "║ [4] -> Sesiones de Trabajo Activas             ║\n"
        "║                                                ║\n"
        "║ [0] -> Salir de la Aplicación                  ║\n"
        "╚" + "═"*48 + "╝"
    )
    print(menu)
    # Pide una opción
    return pedir_num(" Seleccione una opción: ")


####################################################
# A partir de aquí estaría la segunda capa de menu #
####################################################


def menu_almacen() -> str:
    # Se podrá crear nuevos almacenes, ver los existentes, juntarlos o eliminarlos
    menu = (
            "\n┌" + "─" * 44 + "┐\n"
            f"│{'  SECCIÓN: GESTIÓN DE ALMACENES ':.^44}│\n"
            "├" + "─" * 44 + "┤\n"
            "│ [1] - Crear nuevo almacén                  │\n"
            "│ [2] - Acceder y consultar existencias      │\n"
            "│ [3] - Fusionar almacenes (Suma de ítems)   │\n"
            "│ [4] - Eliminar almacén del sistema         │\n"
            "│ [5] - Limpiar almacenes (Filtro caducados) │\n"
            "│                                            │\n"
            "│ [0] - Volver al Menú Principal             │\n"
            "└" + "─" * 44 + "┘"
    )
    print(menu)
    # Pedir la instrucción
    return pedir_num(" Instrucción: ")

def menu_equipamiento() -> str:
    # Se podrá traer nuevo equipamiento, moverlo o tirarlo
    menu = (
            "\n┌" + "─" * 44 + "┐\n"
            f"│{'  SECCIÓN: CONTROL DE EQUIPOS ':.^44}│\n"
            "├" + "─" * 44 + "┤\n"
            "│ [1] - Registrar e importar nuevo equipo    │\n"
            "│ [2] - Transferir equipo entre almacenes    │\n"
            "│                                            │\n"
            "│ [0] - Volver al Menú Principal             │\n"
            "└" + "─" * 44 + "┘"
    )
    print(menu)
    # Pedir la instrucción
    return pedir_num(" Instrucción: ")

def menu_consumibles():

    # Los consumibles van por lotes, por lo que si tiramos un consumible de un lote A,
    # también se tiran los demás consumibles del lote A.

    menu = (
        "\n┌" + "─"*44 + "┐\n"
        f"│{'  SECCIÓN: GESTIÓN DE CONSUMIBLES ':.^44}│\n"
        "├" + "─"*44 + "┤\n"
        "│ [1] - Definir un nuevo lote de reactivos   │\n"
        "│ [2] - Reimportar lote histórico definido   │\n"
        "│                                            │\n"
        "│ [0] - Volver atrás / Menú Principal        │\n"
        "└" + "─"*44 + "┘"
    )
    print(menu)

    # Pedir la instrucción
    return pedir_num('\nAcceder a: ')


def menu_sesiones() -> str:
    menu = (
        "\n┌" + "─"*44 + "┐\n"
        f"│{'  SECCIÓN: SESIONES DE LABORATORIO ':.^44}│\n"
        "├" + "─"*44 + "┤\n"
        "│ [1] - Abrir nueva sesión de trabajo        │\n"
        "│ [2] - Consultar sesiones abiertas          │\n"
        "│ [3] - Finalizar sesión y evaluar retorno   │\n"
        "│                                            │\n"
        "│ [0] - Volver al Menú Principal             │\n"
        "└" + "─"*44 + "┘"
    )
    print(menu)
    return pedir_num(" Instrucción: ")


####################################################
# A partir de aquí estaría la tercera capa de menu #
####################################################


def menu_traer_equipamiento() -> str:
    menu = (
        "\n\t┌" + "─"*40 + "┐\n"
        "\t│" + " ¿Qué tipo de equipo desea registrar? ".center(40, "░") + "│\n"
        "\t├" + "─"*40 + "┤\n"
        "\t│ [1] -> Equipo Genérico                 │\n"
        "\t│ [2] -> Centrifugadora                  │\n"
        "\t│ [3] -> Equipo de Medida                │\n"
        "\t│ [4] -> Equipo Térmico                  │\n"
        "\t│ [5] -> Reutilizar del Catálogo Base    │\n"
        "\t│                                        │\n"
        "\t│ [0] -> Volver al menú anterior         │\n"
        "\t└" + "─"*40 + "┘"
    )
    print(menu)
    return pedir_num("\t Selección: ")
