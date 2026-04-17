# main.py

from funciones import *
from menus import *

# Importar clases

from clases import Lote, Registro, Inventario, Equipo, EquipoMedida, EquipoTermico, Centrifugadora,\
    Consumible, ReactivoLiquido, ReactivoSolido


####################################################


if __name__ == '__main__':

    laboratorio = cargar_laboratorio()  # Diccionario con los almacenes y sesiones guardadas en listas

    #"lista_inventarios": [],   # Lista con las diferentes instancias de las clases
    #"lista_sesiones": []

    inventarios = laboratorio['lista_inventarios']
    sesiones = laboratorio['lista_sesiones']
    
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

                        case '5':   # Acceder a almacen
                            

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


    laboratorio_a_guardar = {
        "lista_inventarios": inventarios,
        "lista_sesiones": sesiones
    }

    guardar_laboratorio(laboratorio_a_guardar)