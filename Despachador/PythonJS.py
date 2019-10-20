from Despachador import Proceso, Despachador

class PythonJS:
    def __init__(self):
        self.quantum = 0
        self.tiempo_bloqueo = 0
        self.tiempo_cambio_contexto = 0
        self.cantidad_micros = 0
        self.proceso = [
            #    nombre, disp,   TE, n_bloqueo
            Proceso("B",    0,  300, 2),
            Proceso("D",    0,  100, 2),
            Proceso("F",    0,  500, 3),
            Proceso("H",    0,  700, 4),
            Proceso("J", 1500,  300, 2),
            Proceso("L", 1500, 3000, 5),
            Proceso("N", 1500,   50, 2),
            Proceso("O", 1500,  600, 3),
            Proceso("A", 3000,  400, 2),
            Proceso("C", 3000,   50, 2),
            Proceso("E", 3000, 1000, 5),
            Proceso("G", 3000,   10, 2),
            Proceso("I", 3000,  450, 3),
            Proceso("K", 4000,  100, 2),
            Proceso("M", 4000,   80, 2),
            Proceso("P", 4000,  800, 4),
            Proceso("Ñ", 8000,  500, 3) 
        ]
        self.despachador = None

    def crear_despachador(self, quantum, tiempo_bloqueo, tiempo_cambio_contexto, cantidad_micros):
        self.quantum = quantum
        self.tb = tiempo_bloqueo
        self.tcc = tiempo_cambio_contexto
        self.cantidad_micros = cantidad_micros

        self.despachador = Despachador(self.quantum, self.tb, self.tcc, self.cantidad_micros, self.proceso)

    def py_despachador(self, js_mostrar_info_micro):
        self.crear_despachador(3000, 15, 15, 2)
        info_micro = self.despachador.datos_js()

        for k, v in info_micro.items():
            js_mostrar_info_micro.Call(k, v)

