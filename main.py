# Importar clases y funciones necesarias
from funciones import *

# Primera capa de menu
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



if __name__ == '__main__':
    
    print('Bienvenido al programa de gestión de laboratorio')

    # El flujo será constituido por bucles while

    instruccion = ''

    while instruccion != '0':


        instruccion = menu_principal()


        match instruccion:

            case '1':   # Almacen

                instruccion_almacen = ''

                while instruccion_almacen != '0':

                    instruccion_almacen = menu_almacen()

                    match instruccion_almacen:

                        # A partir de esta capa de abstracción ya estarán las funcionalidades

                        case '1':   # Crear nuevo almacen

                            pass

                        case '2':   # Ver almacenes

                            pass

                        case '3':   # Juntar almacenes

                            pass

                        case '4':   # Eliminar almacen

                            pass

                        case '0':   # Volver al menu principal

                            print('Volviendo al menu principal...')

                        case _:

                            print('Instrucción no válida, vuelva a intentarlo')




            case '2':   # Equipamiento

                instruccion_equipamiento = ''

                while instruccion_equipamiento != '0':

                    instruccion_equipamiento = menu_equipamiento()

                    match instruccion_equipamiento:

                        case '1':   # Traer nuevo equipamiento

                            pass

                        case '2':   # Mover equipamiento

                            pass

                        case '3':   # Tirar equipamiento

                            pass

                        case '0':   # Volver al menu principal

                            print('Volviendo al menu principal...')

                        case _:

                            print('Instrucción no válida, vuelva a intentarlo')




            case '3':   # Consumibles

                instruccion_consumibles = ''

                while instruccion_consumibles != '0':

                    instruccion_consumibles = menu_consumibles()

                    match instruccion_consumibles:

                        case '1':   # Traer nuevo lote

                            pass

                        case '2':   # Tirar lote

                            pass

                        case '0':   # Volver al menu principal

                            print('Volviendo al menu principal...')

                        case _:

                            print('Instrucción no válida, vuelva a intentarlo')



            case '4':   # Sesiones

                instruccion_sesiones = ''

                while instruccion_sesiones != '0':

                    instruccion_sesiones = menu_sesiones()

                    match instruccion_sesiones:

                        case '1':   # Crear nueva sesión

                            pass

                        case '2':   # Ver sesiones

                            pass

                        case '3':   # Finalizar sesión

                            pass

                        case '0':   # Volver al menu principal

                            print('Volviendo al menu principal...')

                        case _:

                            print('Instrucción no válida, vuelva a intentarlo')




            case '0':   # Salir

                print('Saliendo del programa...')

            case _:

                print('Instrucción no válida, vuelva a intentarlo')