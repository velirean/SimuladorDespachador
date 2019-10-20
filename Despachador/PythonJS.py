from Despachador import Proceso, Despachador

class PythonJS:
    def __init__(self):
        self.quantum = 3000
        self.tiempo_bloqueo = 15
        self.tiempo_cambio_contexto = 15
        self.cantidad_micros = 1
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
        self.despachador = Despachador(self.quantum, self.tiempo_bloqueo, self.tiempo_cambio_contexto, self.cantidad_micros, self.proceso)
        print(str(self.proceso[0]))

    def py_despachador(self, js_mostrar_info_micro):
        info = ""

        for p in self.proceso:
            info += str(p) + "#"

        info = info[:len(info) -1]

        js_mostrar_info_micro.Call(info)
