import math

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

    def get_tiempo_disponible(self):
        return self.disponible

    def get_tt(self):
        return self.tt

    def calcular_tiempos(self, tiempo_inicial, tiempo_cambio_contexto, quantum, tiempo_bloqueo, micro_tcc):
        self.ti = tiempo_inicial
        self.tcc = tiempo_cambio_contexto
        self.calcular_tvc(quantum, micro_tcc)
        self.calcular_tb(tiempo_bloqueo)
        self.calculat_tt()
        self.tf = self.ti + self.tt

    def calcular_tvc(self, quantum, tcc):
        self.tvc = (math.ceil(self.te / quantum) -1) * tcc

    def calcular_tb(self, tiempo_bloqueo):
        self.tb = tiempo_bloqueo * self.cantidad_bloqueo

    def calculat_tt(self):
        self.tt = self.tcc + self.te + self.tvc + self.tb

    def __str__(self):
        datos = "{disponible},{nombre},{tcc},{te},{tvc},{tb},{tt},{ti},{tf}".format(disponible=self.disponible, nombre=self.nombre, tcc=self.tcc, te=self.te, tvc=self.tvc, tb=self.tb, tt=self.tt, ti=self.ti, tf=self.tf)
        return datos