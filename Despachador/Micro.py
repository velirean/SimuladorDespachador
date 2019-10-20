class Micro:
    def __init__(self, num_id, tiempo_cambio_contexto, quantum, tiempo_bloqueo):
        self.id = num_id
        self.estaOcupado = False
        self.tt = 0
        self.proceso = [] # lista de procesos ejecutados
        self.quantum = quantum
        self.tb = tiempo_bloqueo
        self.tcc = tiempo_cambio_contexto

    def ejecutar_proceso(proceso):
        # Si el proceso no esta disponible, esperar
        # tt es el tiempo inicial antes de actualizar la lista
        # Si estaOcupado pasar tcc al proceso
        # llamar calcular_tiempos del proceso
        # Agrega el proceso a la lista y actualiza el tiempo total
        estaOcupado = True

    def esperar(tiempo):
        self.tt += tiempo
        estaOcupado = False

    def js_str():
        pass