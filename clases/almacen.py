import copy

from funciones import *

from .items.consumible import Consumible
from .items.equipo import Equipo, importar_equipamiento

from .registro import Registro


# El almacen de nuestro laboratorio podrá tener varios
# invetarios, cada uno con un nombre y una lista de items

class Inventario():

    def __init__(self, codigo):
        self.__codigo = codigo
        self.items = []

        # Los items se guardaran en una tupla, el objeto item y la cantidad



    def __str__(self):

        frase_inicial = f'\n[{self.codigo}] con {len(self.items)} items\n\n'

        frase_items = ''

        for item in self.items:

            frase_items += f'\t- {str(item[0])}\n\t\t - Uds. disponibles: {item[1]}\n\n'

        return frase_inicial + frase_items

    @property
    def codigo(self):
        return self.__codigo



    def quitar_vacios(self):

        # Elimina los items con cantidad 0 del inventario

        for item in self.items:

            if item[1] == 0:

                self.items.remove(item)


    def limpieza_inventario(self):

        # Elimina items caducados o en mal estado
        items_eliminados = [] # Para mostrarlo en la auditoría

        for item in self.items:

            if isinstance(item[0], Consumible):

                if item[0].__lote.esta_caducado():

                    items_eliminados.append(item[0])
                    self.items.remove(item)


            elif isinstance(item[0], Equipo):

                if item[0].estado == False: # Defectuoso

                    items_eliminados.append(item[0])
                    self.items.remove(item)

        return items_eliminados
    

    # Se puede usar también para reducir las unidades, poniendo en la cantidad un número negativo
    # Por eso, se saneará la lista después para eliminar los items con cantidad 0
    def anadir_item_al_inventario(self, item_cantidad: tuple):

        terminado = False

        for indice, item in enumerate(self.items):

            # Comprueba si ya existía esa instancia para solo añadir la cantidad
            if item[0] == item_cantidad[0]:

                self.items[indice] = (item_cantidad[0], self.items[indice][1] + item_cantidad[1])
                terminado = True

        if not terminado:

            self.items.append(item_cantidad) # Se añade en caso de que no exista tal instancia en el inventario

        self.quitar_vacios() # Para eliminar los items con cantidad 0 después de reducir unidades






# Pasamos una lista de los objetos de un tipo de item en un inventario

def mostrar_items(inventario, tipo_item):

    print(f'\nItems de tipo {tipo_item.__name__} en el inventario [{inventario.codigo}]:\n')


    indice = 1
    for (instancia, cantidad) in inventario.items:

        if isinstance(instancia, tipo_item):

            print(f'[{indice}]\t - {str(instancia)}\n\t\t Uds. disponibles: {cantidad}\n\n')
            indice += 1

    return indice - 1 # Para saber el número de items mostrados, si es 0 no se ha mostrado ningún item del tipo pedido


                



# Pasamos una lista de inventarios
def mostrar_almacenes(inventarios):

    if len(inventarios) == 0:

        print('No hay almacenes disponibles.')
    
    else:

        print('\nAlmacenes disponibles:')

        for inventario in inventarios:

            print(f'[{inventario.codigo}] con {len(inventario.items)} items')





def crear_almacen(inventarios):

    print('El código de un almacen debe ser 2 letras mayúsculas seguidas de 3 dígitos. Introduce 0 para cancelar la operación.')

    # El while True crear un bucle infinito que solo romperá un return
    while True:

        codigo_input = input('Introduce el código del nuevo almacén: ')


        try:

            codigo = verificar_codigo_almacen(codigo_input)

            if codigo is None:

                print('Operación cancelada.')
                return None


            if codigo in [inventario.codigo for inventario in inventarios]:

                print('Ya existe un almacén con ese código. Operación cancelada.')
                return None
            

            print(f'Creando nuevo almacén con código [{codigo}]... ')
            return Inventario(codigo)
        

        except ValueError as e:

            print(f'\n{e}\n')
            # Imprime el mensaje hecho en la función verificar_codigo_almacen y vuelve a pedir el código



# El código de un almacen será 2 letras mayúsculas seguidas de 3 dígitos
# Devolvemos -1 cuando el usuario quiera cancelar la operación
def verificar_codigo_almacen(codigo):

    match codigo:

        case '0':

            return None
        
        case _:

            if len(codigo) == 5:

                if codigo[:2].isalpha() and codigo[:2].isupper() and codigo[2:].isdigit():

                    return codigo
                
            raise ValueError('Código no válido. El código debe ser 2 letras mayúsculas seguidas de 3 dígitos. Inténtalo de nuevo o introduce 0 para cancelar.')





def acceso_almacen(inventarios):

    while True:

        accedido = False

        # Menu de lo para acceder a un almacen concreto y ver su contenido
        print(f'\n\t[Código] - \tAcceder a un almacen\n'
            f'\t[0] - \tVolver atras\n'
        )

        # Tiene que tomar un código de almacen o 0 para volver atrás
        instruccion = input('\nAcceder a: ')

        for inventario in inventarios:

            if instruccion == inventario.codigo:

                print(inventario)
                accedido = True


        if instruccion == '0':

            print('Volviendo atrás...')
            return '0'
        
        
        if not accedido:

            print('Código no encontrado, vuelva a intentarlo.')





# Tengo que comentar esta función
def eliminar_almacen(inventarios):

    if inventarios: # Comprobar si hay inventarios disponibles para eliminar

        mostrar_almacenes(inventarios)

        while True:

            codigo_input = input('Introduce el código del almacén que quieres eliminar (0 para cancelar): ')

            if codigo_input == '0':

                print('Operación cancelada.')
                return None
            
            for inventario in inventarios:

                if codigo_input == inventario.codigo:

                    confirmacion = input(f'¿Estás seguro de que quieres eliminar el almacén [{inventario.codigo}] y todos sus items? Esta acción no se puede deshacer. (s para continuar): ')

                    if confirmacion.lower() == 's':

                        inventario_eliminado = copy.deepcopy(inventario) # Para mostrarlo en la auditoría

                        inventarios.remove(inventario)
                        print(f'Almacén [{inventario.codigo}] eliminado.')


                        return inventario_eliminado
                    
                    
                    else:

                        print('Operación cancelada.')
                        return None
            
            print('Código no encontrado, vuelva a intentarlo.')


    else:

        print('No hay almacenes para eliminar.')




def anadir_item(item_cantidad: tuple, inventarios: list):


    # item_cantidad viene de importar_equipamiento
    # importar equipamiento necesita de definir_equipamiento...etc.


    if item_cantidad is None:
        
        print('Operación cancelada...')
        return None


    if inventarios:

        mostrar_almacenes(inventarios)


        print(f'\n\t[Código] - \tAñadir al almacen...\n'
                f'\t[0] - \tCancelar operación\n'
            )


        while True:

            # Tiene que tomar un código de almacen o 0 para volver atrás
            codigo_input = input('\nAñadir a: ')


            for inventario in inventarios:

                if inventario.codigo == codigo_input:

                    inventario.anadir_item_al_inventario(item_cantidad)

                    print('\nItem importado de forma exitosa.\n')

                    return (item_cantidad, inventario.codigo) 
                    # Hacemos un return para triggear el mensaje de auditoría y para la función


            if codigo_input == '0':

                print('Cancelando operación...')
                return None
            
            else:

                print('Código no válido. Vuelva a intentarlo.')

    print('No hay almacenes disponibles. Crea un almacén antes de importar items.')
    return None



# Como los consumibles van por lotes, no se podrán mover de almacen, pero el equipamiento sí
def mover_equipamiento(inventarios):

    # Primero se comprueba que sea posible la operación
    if len(inventarios) < 2:

        print('No hay suficientes almacenes para mover equipamiento. Se necesitan al menos 2 almacenes.')
        return None
    

    # Hay que seleccionar el inventario del que se quiera mover el equipo

    mostrar_almacenes(inventarios)

    while True:

        # El usuario selecciona el inventario del que quiere mover el equipo
        codigo_input = input('Introduce el código del almacén que quieres eliminar (0 para cancelar): ')

        if codigo_input == '0':

            print('Operación cancelada.')
            return '0'
        
        for inventario in inventarios:

            if codigo_input == inventario.codigo:

                codigo_primero = codigo_input # Lo guardamos para después
                
                # Mostramos el equipamiento del inventario seleccionado
                longitud = mostrar_items(inventario, Equipo)

                if longitud == 0:

                    print('No hay equipamiento en este almacén. Operación cancelada.')
                    return '0'

                # El usuario selecciona el equipo que quiere mover

                while True:

                    equipo_input = pedir_int('Introduce el número del equipo que quieres mover (0/-1 para cancelar): ')

                    if equipo_input == 0 or equipo_input == '-1':

                        print('Operación cancelada.')
                        return '0'
                    
                    elif equipo_input > longitud:

                        print('Número no válido. Vuelva a intentarlo.')
                    
                    else:

                        equipo_seleccionado = None

                        indice = 1
                        for (instancia, cantidad) in inventario.items:

                            if isinstance(instancia, Equipo):

                                if indice == equipo_input:

                                    equipo_seleccionado = instancia
                                    cantidad_max = cantidad

                                
                                indice += 1
                        


                        cantidad = pedir_int_entre_valores(f'Introduce la cantidad a mover (1-{cantidad_max}, -1 para cancelar): ', 1, cantidad_max)



                        if cantidad == '-1':

                            print('Operación cancelada.')
                            return '0'
                        

                        equipo_seleccionado_cantidad = (equipo_seleccionado, cantidad)


                        # El usuario selecciona el inventario al que quiere mover el equipo

                        mostrar_almacenes(inventarios)


                        while True:


                            codigo_input_2 = input('Introduce el código del almacén al que quieres mover el equipo (0 para cancelar): ')



                            if codigo_input_2 == '0':

                                print('Operación cancelada.')
                                return '0'
                            
                            elif codigo_input_2 == codigo_primero:

                                print('No puedes mover un equipo a su mismo almacén. Vuelva a intentarlo.')
                            


                            else:

                                for inventario_2 in inventarios:

                                    if inventario_2.codigo == codigo_input_2:

                                        # Movemos el equipo de un inventario a otro

                                        # Quitar las unidades que quisieramos mover
                                        inventario.anadir_item_al_inventario((equipo_seleccionado_cantidad[0], -equipo_seleccionado_cantidad[1]))

                                        # La ponemos en positivo porque se añaden
                                        inventario_2.anadir_item_al_inventario((equipo_seleccionado_cantidad[0], equipo_seleccionado_cantidad[1]))

                                        print(f'Equipo movido de forma exitosa del almacén [{inventario.codigo}] al almacén [{inventario_2.codigo}].')

                                        return (equipo_seleccionado_cantidad, inventario.codigo, inventario_2.codigo) 
                                        # Hacemos un return para triggear el mensaje de auditoría y para la función