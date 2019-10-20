class Proceso:
    def __init__(self, nombre_proceso, tiempo_disponible, tiempo_ejecucion, cantidad_bloqueo):
        self.disponible = tiempo_disponible
        self.nombre = nombre_proceso
        self.tcc = 0 # tiempo por cambio de contexto
        self.te = tiempo_ejecucion
        self.tvc = 0 # tiempo por vencimiento de quantum
        self.tb = 0 # tiempo por bloqueos
        self.tt = 0 # tiempo total
        self.ti = 0 # tiempo inicial
        self.tf = 0 # tiempo final
        self.cantidad_bloqueo = cantidad_bloqueo

    def get_tiempo_total():
        return self.tt

    def calcular_tiempos(tiempo_inicial, tiempo_cambio_contexto, quantum, tiempo_bloqueo):
        self.ti = tiempo_inicial
        self.tcc = tiempo_cambio_contexto
        calcular_tvc(quantum)
        calcular_tb(tiempo_bloqueo)
        calculat_tt()
        self.tf = self.ti + self.tt

    def calcular_tvc(quantum):
        pass

    def calcular_tb(tiempo_bloqueo):
        self.tb = tiempo_bloqueo * self.cantidad_bloqueo

    def calculat_tt():
        self.tt = self.tcc + self.te + self.tvc + self.tb

    