from datetime import date
from typing import Any, Optional, Dict, List

from .consumible import importar_consumible_generico
from .consumibles.reactivoSolido import importar_reactivo_solido
from .consumibles.reactivoLiquido import importar_reactivo_liquido

from funciones import *

class Lote():


    def __init__(self, id_lote: str, fecha_vencimiento: date):

        # El id es constante, así que solo habrá getter
        self.__id_lote = id_lote

        # Las fechas son constante, así que solo habrá getter
        self.__fecha_vencimiento = fecha_vencimiento




    # Como no se puede modificar el id ni la fecha, no habrá setter, solo getter
    
    @property   # Getter del id del lote
    def id_lote(self) -> str:
        return self.__id_lote
        

    @property   # Getter de la fecha de vencimiento del lote
    def fecha_vencimiento(self) -> date:
        return self.__fecha_vencimiento
        

    def esta_caducado(self) -> bool:
        # Compara de forma directa la fecha del sistema con la del lote
        return date.today() > self.fecha_vencimiento
    
    def __eq__(self, other: Any) -> bool:
        # Identicos si comparten id
        if isinstance(other, Lote):

            return self.id_lote == other.id_lote
        
        return False
    
    def __str__(self) -> str:

        return f'Lote: [{self.id_lote}] | Fecha vencimiento: {self.fecha_vencimiento}'
    

# Los IDs de los lotes tendrán forman 00-ABC
def comprobar_id_lote(id:str) -> bool:
    # Limpiar la entrada antes de validar
    id = id.strip()

    if len(id) != 6:

        return False
    
    return id[0:2].isdigit() and id[2] == '-' and id[3:6].isalpha()
    


# El usuario define un lote nuevo, aunque se seleccione un lote
# anteriormente definido, habría que cambiar la fecha y el ID
def definir_lote(lotes: Dict[str, Any]) -> Optional[Lote]:

    introducir_id = ''
    id_valido = False
    # Validación y registro del id único
    while not id_valido:

        entrada = input('(0 para cancelar | ID (00-ABC): ').strip().upper()

        if entrada == '0':
            return None
        
        if comprobar_id_lote(entrada):

            if entrada in lotes:

                print('Ya existe un lote con ese ID.\n')
                return None
            
            introducir_id = entrada
            id_valido = True

        else:

            print('Introduzca un ID válido.\n')
    # Entrada y validación de la fecha (no vencida)
    while True:

        fecha = pedir_fecha('(0) para cancelar | Fecha (DD/MM/AAAA): ')

        if fecha is None:
            return None

        if fecha < date.today():
            print('Fecha no válida. No puedes importar lotes caducados.\n')
            
        else:
            return Lote(introducir_id, fecha)
    '''
    id_comprobado = False

    # Pasamos la lista de los lotes anteriormente definidos
    # Hara falta para ver que no hayan IDs repetidos

    while not id_comprobado:   # Este bucle se parara con un return o si el id introducido es válido


        introducir_id = input('(0) para cancelar la operación | Introduzca el ID (00-ABC) del nuevo lote: ').upper()

        if introducir_id == '0':

            return None
        

        
        if comprobar_id_lote(introducir_id):


            # Comprobamos que no exista tal id en lotes anteriormente definidos
            for lote in lotes.keys():


                if lote == introducir_id:

                    print('Ya existe un lote con ese ID.\n')
                    return None
                
            
            id_comprobado = True
            

        if not id_comprobado:

            print('Introduzca un ID válido o (0) para cancelar la operación.\n')


    # A partir de aquí se pide la fecha
    while True:

        fecha_caducidad = pedir_fecha('(0) para cancelar la operación | Introduzca la fecha de caducidad (DD/MM/AAAA): ')
        if fecha_caducidad is None:
            return None
        if fecha_caducidad < date.today():
            print('Fecha no válida. No puedes importar lotes ya caducados.\n')
        else:
            return Lote(introducir_id, fecha_caducidad)
    return None
    
        while id_comprobado:


            fecha_caducidad = pedir_fecha('(0) para cancelar la operación | Introduzca la fecha de caducidad (DD/MM/AAAA): ')


            if fecha_caducidad is None:

                return None


            # Comprobar que sea válida.
            if fecha_caducidad < date.today():

                print('Fecha no válida. No puedes importar lotes ya caducados.\n')

            else:

                return Lote(introducir_id, fecha_caducidad)
                '''


# Ahora hay que añadir consumibles al lote definido
def definir_lote_nuevo(lote: Optional[Lote]) -> Optional[List[Any]]:

    if lote is None:

        return None


    instruccion = ''

    consumibles: List[Any] = [] # Esta lista se desempaquetara a la hora de añadirla
                     # a un inventario


    # Submenú dinámico para poblar el lote de reactivos o consumibles generales
    while not instruccion in ['4', '0']:

        instruccion = menu_consumibles()

        match instruccion:

            case '1': # Consumible genérico
                
                # Como las funciones trabaja mediante referencia de lista, no tiene return
                importar_consumible_generico(consumibles, lote)



            case '2': # Reactivo líquido

                importar_reactivo_liquido(consumibles, lote)



            case '3': # Reactivo solido

                importar_reactivo_solido(consumibles, lote)



            case '4':

                return consumibles


            case '0':

                return None
    return None


def traer_lote_definido(lotes: dict):

    if not lotes:

        print('No hay lotes anteriormente definidos.\n')
        return None
    # Muestra un inventario resumido de los lotes guardados en el histórico
    for lote in lotes:

        # Extraemos la lista del lote
        consumibles = lotes[lote]
        unidades_totales = 0

        # Desempaquetamos la tupla
        for consumible, unidades in consumibles:

            unidades_totales += unidades

        print(f'\t - {lote}: {len(consumibles)} consumibles, {unidades_totales} uds.')



    codigo_valido = False

    while not codigo_valido:

        # Se pide el código del lote que se quiera volver a importar
        lote_pedido = pedir_cadena_no_vacia('(0) para cancelar | Introduzca el código del lote que quieras importar: ')

        if lote_pedido is None:

            return None
        
        if not lote_pedido in lotes.keys():
            print('Introduzca un código válido.\n')

        else:
            codigo_valido = True
    

    

    print('\nHay que definir un nuevo código y fecha para el lote importado.\n')

    # Se trae un objeto de lote para poner a los consumibles
    lote_definido = definir_lote(lotes)

    if lote_definido is None:

        return None

    # Ahora a las instancias de consumible hay que cambiar el atributo lote

    consumibles_nuevos = []
    # Actualiza las referencias de cada consumible hacia la nueva instancia de Lote
    for consumible, unidades in lotes[lote_pedido]:

        consumible.lote = lote_definido

        consumibles_nuevos.append((consumible, unidades))

    return consumibles_nuevos





# Menu para que el usuario seleccione que consumible quiere añadir al lote
def menu_consumibles() -> str:
    menu = (
        "\n\t╔" + "═"*40 + "╗\n"
        "\t║" + " CARGANDO CONSUMIBLES AL LOTE ".center(40, "░") + "║\n"
        "\t╠" + "═"*40 + "╣\n"
        "\t║ [1] - Consumible genérico              ║\n"
        "\t║ [2] - Reactivo líquido                 ║\n"
        "\t║ [3] - Reactivo sólido                  ║\n"
        "\t║                                        ║\n"
        "\t║ [4] - Finalizar y guardar lote         ║\n"
        "\t║ [0] - Cancelar lote completo           ║\n"
        "\t╚" + "═"*40 + "╝"
    )
    print(menu)

    instruccion = input("\n\t Instrucción de carga: ").strip()
    if instruccion not in ['1', '2', '3', '4', '0']:
        print("\t⚠️ Opción no válida. Intente de nuevo.")
        return menu_consumibles() # Recursividad para forzar opción correcta
    return instruccion