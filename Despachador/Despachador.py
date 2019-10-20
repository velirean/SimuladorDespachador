from Despachador import Micro

class Despachador:
    def __init__(self, quantum, tiempo_bloqueo, tiempo_cambio_contexto, cantidad_micros, lista_proceso):
        self.quantum = quantum
        self.tb = tiempo_bloqueo
        self.tcc = tiempo_cambio_contexto
        self.micro = []

        for i in range(0, cantidad_micros):
            self.micro.append(Micro(i + 1, self.tcc, self.quantum, self.tb))
        # se considera que los procesos ya estan ordenados
        self.proceso = lista_proceso

        self.ejecutar_proceso()
    
    def ejecutar_proceso(self):
        # seleccionar al micro correspondiente
        # llamar a su metodo ejecutar proceso
        for p in self.proceso:
            self.micro[0].ejecutar_proceso(p)
        

    def datos_js(self):
        # Regresa los datos de cada micro en formato para JS
        dato = {}

        for m in self.micro:
            dato.update({ str(m.get_id()) : str(m)})

        return dato
