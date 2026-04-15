# Para que el archivo main() no sea gigantesco,
# escribimos la mayoría de funciones aquí


def pedir_num(frase):

    print(frase, end='')

    numero = input()

    # Comprueba que sea un número
    if numero.isdigit():

        return numero
    
        # Aunque se pida un número, se devuelve un str para evitar errores
    
    return '-1'
    
    # Si el usuario no introduce un número, devolvemos -1
    # El 0 está reservado para salir de capas de menu



def pedir_int(frase):

    numero = pedir_num(frase)

    if numero == '-1':

        return -1
    
    return int(numero)