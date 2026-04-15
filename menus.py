from funciones import *


# Las funciones con las diferentes capas de menu


########################
# Primera capa de menu #
########################


def menu_principal():


    print(
        f'\n\t[1] -\tAlmacen\n'
        f'\t[2] -\tEquipamiento\n'
        f'\t[3] -\tConsumibles\n'
        f'\t[4] -\tSesiones\n'
        f'\t[0] -\tSalir programa\n'
    )

    # Pedir la instrucción
    return pedir_num('\nAcceder a: ')


####################################################
# A partir de aquí estaría la segunda capa de menu #
####################################################


def menu_almacen():

    # Se podrá crear nuevos almacenes, ver los existentes, juntarlos o eliminarlos

    print(
        f'\n\t[1] -\tCrear nuevo almacen\n'
        f'\t[2] -\tVer almacenes\n'
        f'\t[3] - \tJuntar almacenes\n'
        f'\t[4] -\tEliminar almacen\n'
        f'\t[5] -\tAcceder a almacen\n'
        f'\t[0] -\tVolver al menu principal\n'
    )

    # Pedir la instrucción
    return pedir_num('\nAcceder a: ')


def menu_equipamiento():

    # Se podrá traer nuevo equipamiento, moverlo o tirarlo

    print(
        f'\n\t[1] - \tTraer nuevo equipamiento\n'
        f'\t[2] - \tMover equipamiento\n'
        f'\t[3] - \tTirar equipamiento\n'
        f'\t[0] - \tVolver al menu principal\n'
    )

    # Pedir la instrucción
    return pedir_num('\nAcceder a: ')


def menu_consumibles():

    # Los consumibles van por lotes, por lo que si tiramos un consumible de un lote A,
    # también se tiran los demás consumibles del lote A.

    print(
        f'\n\t[1] - \tTraer nuevo lote\n'
        f'\t[2] - \tTirar lote\n'
        f'\t[0] - \tVolver al menu principal\n'
    )

    # Pedir la instrucción
    return pedir_num('\nAcceder a: ')


def menu_sesiones():

    print(
        f'\n\t[1] - \tCrear nueva sesión\n'
        f'\t[2] - \tVer sesiones\n'
        f'\t[3] - \tFinalizar sesión\n'
        f'\t[0] - \tVolver al menu principal\n'
    )

    # Pedir la instrucción
    return pedir_num('\nAcceder a: ')