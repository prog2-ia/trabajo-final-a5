# Importar clases y funciones necesarias
import funciones

# Primera capa de menu
def menu_principal():


    print(
        f'\n\t1 -\tAlmacen\n'
        f'\t2 -\tEquipamiento\n'
        f'\t3 -\tConsumibles\n'
        f'\t0 -\tSalir programa\n'
    )

    # Pedir la instrucción
    return pedirNum('\nAcceder a: ')
    


if __name__ == '__main__':
    
    print('Aquí ira el flujo del código...')