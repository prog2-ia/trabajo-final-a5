# main.py

from funciones import *
from menus import *

# Importar clases

from clases import *


####################################################


if __name__ == '__main__':

    # Comprobar que exista el archivo de escritura

    crear_auditoria()

    laboratorio = cargar_laboratorio()  # Diccionario con los almacenes y sesiones guardadas en listas

    #"lista_inventarios": [],   # Lista con las diferentes instancias de las clases
    #"lista_sesiones": []


    inventarios = laboratorio['lista_inventarios']
    sesiones = laboratorio['lista_sesiones']

    # Se guardaran los equipos y consumibles en listas para facilitar después de que se instancien
    # por primera vez


    equipos = laboratorio['equipos']
    lotes = laboratorio['lotes'] # lotes será un diccionario


    

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
                            
                            if isinstance(nuevo_almacen, Inventario):

                                inventarios.append(nuevo_almacen)
                                escribir_creado_almacen(nuevo_almacen.codigo)



                        case '2':   # Acceder y ver almacenes

                            # Previamente se mostraran los almacenes disponibles

                            mostrar_almacenes(inventarios)


                            instruccion_acceso_almacen = ''

                            while instruccion_acceso_almacen != '0':
                                # Subflujo para operar dentro de un almacén específico
                                instruccion_acceso_almacen = acceso_almacen(inventarios)


                        case '3':   # Juntar almacenes

                            conclusion_operacion = juntar_almacenes(inventarios)

                            if conclusion_operacion is None:

                                print('Operación cancelada.\n')

                            else:

                                nuevo_inventario = conclusion_operacion[0]
                                inventario_base = conclusion_operacion[1]
                                inventario_suma = conclusion_operacion[2]

                                inventarios = conclusion_operacion[3]

                                escribir_juntado_almacenes(nuevo_inventario, inventario_base, inventario_suma)



                        case '4':   # Eliminar almacen

                            conclusion_operacion = eliminar_almacen(inventarios)

                            if type(conclusion_operacion) == Inventario:

                                # Si la función devuelve un inventario, es que se ha borrado correctamente,
                                # solo que ha pasado una copia para mostrarla por auditoría

                                escribir_eliminado_almacen(conclusion_operacion)


                        case '5': # Limpiar almacenes

                            # La conclusión debería ser un diccionario con listas
                            conclusion_operacion = limpiar_inventarios(inventarios)

                            if isinstance(conclusion_operacion, dict):

                                escribir_limpieza_inventarios(conclusion_operacion)



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

                                # Variable para guardar el objeto definido antes de importarlo
                                item_definido = None
                                # Asignación según el tipo específico de equipamiento
                                match instruccion_nuevo_equipamiento:

                                    case '1':
                                        item_definido = definir_equipamiento(equipos)

                                    case '2':
                                        item_definido = definir_centrifugadora(equipos)

                                    case '3':
                                        item_definido = definir_equipo_medida(equipos)

                                    case '4':
                                        item_definido = definir_equipo_termico(equipos)

                                    case '5':
                                        item_definido = traer_equipamiento_definido(equipos) # Reutilizar catálogo

                                    case '0':
                                        print('Volviendo al menu anterior...')

                                    case _:
                                            print('Instrucción no válida, vuelva a intentarlo')

                                

                                # Si el objeto fue configurado con éxito, se procede a su importación fisica
                                if item_definido is not None:

                                    # 1. Lo importamos (esto devuelve la tupla para anadir_item)
                                    datos_importacion = importar_equipamiento(item_definido)


                                    if datos_importacion is not None:

                                        # 2. Lo añadimos al inventario
                                        conclusion_operacion = anadir_item(datos_importacion, inventarios)


                                        if isinstance(conclusion_operacion, tuple):


                                            escribir_importar_equipo(conclusion_operacion)

                                            # Si era un equipo nuevo (no de la opción 5), lo guardamos en la biblioteca
                                            if instruccion_nuevo_equipamiento != '5':

                                                anadir_equipo_definido(conclusion_operacion[0][0], equipos)


                        case '2':   # Mover equipamiento

                            conclusion_operacion = mover_equipamiento(inventarios)

                            if type(conclusion_operacion) == tuple:

                                escribir_mover_equipo(conclusion_operacion[0], conclusion_operacion[1], conclusion_operacion[2])


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


                            # anadir_lote -> Añade a un inventario los consumibles
                            # definir_lote_nuevo -> Se deciden que consumibles se ponen en el lote
                            # definir_lote -> Se pone la fecha de caducidad y el ID

                           
                                        
                            lote_datos = definir_lote(lotes)

                            if lote_datos is not None:

                                lista_consumibles = definir_lote_nuevo(lote_datos)

                                if lista_consumibles is not None:

                                    conclusion_operacion = anadir_lote(lista_consumibles, inventarios)

                                    if isinstance(conclusion_operacion, tuple):

                                        escribir_nuevo_lote_definido(conclusion_operacion)

                                        consumibles_tupla = conclusion_operacion[0]
                                        consumible_obj = consumibles_tupla[0][0]
                                        lote_obj = consumible_obj.lote

                                        lotes[lote_obj.id_lote] = consumibles_tupla

                                    else:

                                        print('Operación cancelada...\n')

                                else:

                                    print('Operación cancelada...\n')

                            else:

                                print('Operación cancelada...\n')



                        case '2':   # Traer lote anteriormente definido

                                        
                            # Habrá que cambiar las fechas y código
                            # solo se copiara los consumibles del lote

                            conclusion_operacion = anadir_lote(traer_lote_definido(lotes), inventarios)

                            if isinstance(conclusion_operacion, tuple):

                                    escribir_nuevo_lote_definido(conclusion_operacion)
                                        


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

                            conclusion_operacion, copia_seguridad = anadir_items_a_sesion(inventarios, sesiones)

                            if conclusion_operacion is None:

                                print('Operación cancelada.\n')

                                # Por si se cancela una sesión la cual tenía items ya añadidos
                                inventarios = copia_seguridad

                            else:

                                # Se añade la sesión a las sesiones para el pickle
                                sesiones.append(copy.deepcopy(conclusion_operacion))

                                escribir_sesion_empezada(conclusion_operacion)


                        case '2':   # Ver sesiones

                            ver_sesiones_abiertas(sesiones)

                        case '3':   # Finalizar sesión

                            conclusion_operacion = devolver_items_de_sesion(inventarios, sesiones)

                            if not conclusion_operacion is None:

                                sesion_cerrada = conclusion_operacion[0]
                                inventarios = conclusion_operacion[1]
                                sesiones = conclusion_operacion[2]

                                escribir_sesion_cerrada(sesion_cerrada)

                            else:

                                print('Operación cancelada.\n')

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