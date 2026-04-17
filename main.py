# main.py

from funciones import *
from menus import *

# Importar clases

from clases import *


####################################################


if __name__ == '__main__':

    laboratorio = cargar_laboratorio()  # Diccionario con los almacenes y sesiones guardadas en listas

    #"lista_inventarios": [],   # Lista con las diferentes instancias de las clases
    #"lista_sesiones": []


    inventarios = laboratorio['lista_inventarios']
    sesiones = laboratorio['lista_sesiones']

    # Se guardaran los equipos y consumibles en listas para facilitar después de que se instancien
    # por primera vez


    equipos = laboratorio['equipos']
    lotes = laboratorio['lotes']

    

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


                            nuevo_almacen = crear_almacen(inventarios)
                            
                            if nuevo_almacen is not None:

                                inventarios.append(nuevo_almacen)


                        case '2':   # Acceder y ver almacenes

                            # Previamente se mostraran los almacenes disponibles

                            mostrar_almacenes(inventarios)

                            instruccion_acceso_almacen = ''

                            while instruccion_acceso_almacen != '0':

                                instruccion_acceso_almacen = acceso_almacen(inventarios)


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

                            instruccion_nuevo_equipamiento = ''

                            while instruccion_nuevo_equipamiento != '0':

                                instruccion_nuevo_equipamiento = menu_traer_equipamiento()

                                match instruccion_nuevo_equipamiento:

                                    case '1':   # Definir equipamiento genérico

                                        pass


                                    case '2':   # Definir centrifugadora

                                        pass


                                    case '3':   # Definir equipamiento de medida

                                        pass

                                    case '4':   # Definir equipamiento térmico

                                        pass


                                    case '5':   # Traer equipamiento anteriormente definido

                                        pass


                                    case '0':   # Volver al menu anterior

                                        print('Volviendo al menu anterior...')

                                    case _:

                                        print('Instrucción no válida, vuelva a intentarlo')


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

                            instruccion_nuevo_lote = ''

                            while instruccion_nuevo_lote != '0':

                                instruccion_nuevo_lote = menu_traer_consumibles()

                                match instruccion_nuevo_lote:

                                    case '1':   # Definir lote

                                        pass

                                    case '2':   # Traer lote anteriormente definido

                                        # Habrá que cambiar las fechas y código
                                        # solo se copiara los consumibles del lote

                                        pass

                                    case '0':  # Volver al menu anterior

                                        print('Volviendo al menu anterior...')

                                    case _:

                                        print('Instrucción no válida, vuelva a intentarlo')



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
        "lista_sesiones": sesiones,
        "equipos": equipos,
        "lotes": lotes
    }


    guardar_laboratorio(laboratorio_a_guardar)