# Para que el archivo main() no sea gigantesco,
# escribimos la mayoría de funciones aquí

def pedirNum(frase):

    print(frase, end='')

    numero = input()

    # Comprueba que sea un número
    if isinstance(numero, int) or isinstance(numero, float):

        return numero
    
    # Si el usuario no introduce un número, devolvemos -1
    # El 0 está reservado para salir de capas de menu
