import datetime

class Registro():


    def __init__(self, cod, items):


        self.inicio = datetime.datetime.now()
        self.abierta = True


        self.items = items # Paquete con los objetos usados durante la sesión
        self.cod = cod # Código de la sesión, para identificarla en el registro


    def cerrar_sesion(self):

        # Hay que programarla de tal manera que los objetos de items
        # se devuelvan al inventario, y que se guarde el registro de la sesión

        self.fin = datetime.datetime.now()
        self.abierta = False