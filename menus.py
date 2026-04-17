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
        f'\t[2] -\tVer y acceder a almacenes\n'
        f'\t[3] - \tJuntar almacenes\n'
        f'\t[4] -\tEliminar almacen\n'
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


####################################################
# A partir de aquí estaría la tercera capa de menu #
####################################################


def menu_traer_equipamiento():

    print(
        f'\n\t[1] - \tDefinir equipamiento genérico\n'
        f'\t[2] - \tDefinir centrifugadora\n'
        f'\t[3] - \tDefinir equipamiento de medida\n'
        f'\t[4] - \tDefinir equipamiento térmico\n'
        f'\t[5] - \tTraer equipamiento anteriormente definido\n'
        f'\t[0] - \tVolver atras\n'
    )

    # Pedir la instrucción
    return pedir_num('\nAcceder a: ')



def menu_traer_consumibles():


    print(
        f'\n\t[1] - \tDefinir nuevo lote\n'
        f'\t[2] - \tTraer lote anteriormente definido\n'
        f'\t[0] - \tVolver atras\n'
    )


    # Pedir la instrucción
    return pedir_num('\nAcceder a: ')


def menu_acceso_almacen():

    print(f'\n\t[1] - \tAcceder a un almacen\n'
          f'\t[2] - \tVer almacen\n'
          f'\t[0] - \tVolver atras\n'
    )

    return pedir_num('\nAcceder a: ')