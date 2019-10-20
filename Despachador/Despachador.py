from Despachador import Micro

class Despachador:
    def __init__(self, quantum, tiempo_bloqueo, tiempo_cambio_contexto, cantidad_micros, lista_proceso):
        self.quantum = quantum
        self.tb = tiempo_bloqueo
        self.tcc = tiempo_cambio_contexto
        self.micro = [] # Puede ser un diccionario
        # se considera que los procesos ya estan ordenados
        self.proceso = lista_proceso

        # Falta inicializar los micros 
    
    def ejecutar_proceso():
        # seleccionar al micro correspondiente
        # llamar a su metodo ejecutar proceso
        pass