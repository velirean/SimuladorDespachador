from Despachador import Proceso

class Micro:
    def __init__(self, num_id, tiempo_cambio_contexto, quantum, tiempo_bloqueo):
        self.id = num_id
        self.estaOcupado = False # El micro no esta ocupado al inicio
        self.tt = 0
        self.proceso = [] # lista de procesos ejecutados
        self.quantum = quantum
        self.tb = tiempo_bloqueo
        self.tcc = tiempo_cambio_contexto

    def ejecutar_proceso(self, proceso):
        # Si el proceso no esta disponible, esperar
        if self.tt < proceso.get_tiempo_disponible():
            tiempo_espera = proceso.get_tiempo_disponible() - self.tt
            self.esperar(tiempo_espera)

        # Si micro esta ocupado asignar tcc al proceso
        proceso_tcc = 0
        if self.estaOcupado:
            proceso_tcc = self.tcc

        # tt es el tiempo inicial antes de actualizar la lista
        proceso.calcular_tiempos(self.tt, proceso_tcc, self.quantum, self.tb, self.tcc)

        # Agrega el proceso a la lista y actualiza el tiempo total
        self.proceso.append(proceso)
        self.tt += proceso.get_tt()

        # Ahora el micro esta ocupado con este proceso
        self.estaOcupado = True

    def limpiar_micro(self):
        esperas_sobrantes = 0
        for p in reversed(self.proceso):
            if p.get_nombre() == "Espera":
                esperas_sobrantes += 1
            else:
                break
        for i in range(0, esperas_sobrantes):
            self.proceso.pop()

    def get_id(self):
        return self.id

    def get_tt(self):
        return self.tt

    def esperar(self, tiempo):
        # Esperar se maneja como un proceso
        proceso_espera = Proceso("Espera", 0, tiempo, 0)
        proceso_espera.calcular_tiempos(self.tt, 0, tiempo, 0, 0)
        self.proceso.append(proceso_espera)
        self.tt += tiempo
        self.estaOcupado = False

    def __str__(self):
        dato = ""

        for p in self.proceso:
            dato += str(p) + "#"

        dato = dato[:len(dato) -1]

        return dato