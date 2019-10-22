from Despachador import Proceso, Despachador

class PythonJS:
    def __init__(self):
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

    def py_despachador(self, js_mostrar_info_micro, js_mostrar_mensaje, quantum, tiempo_bloqueo, tiempo_cambio_contexto, cantidad_micros):
        if self.are_positive_integers(quantum, tiempo_bloqueo, tiempo_cambio_contexto, cantidad_micros):
            quantum = int(quantum) 
            tiempo_bloqueo = int(tiempo_bloqueo)
            tiempo_cambio_contexto = int(tiempo_cambio_contexto)
            cantidad_micros = int(cantidad_micros)
            if cantidad_micros >= 1 and quantum >= 1:
                despachador = Despachador(quantum, tiempo_bloqueo, tiempo_cambio_contexto, cantidad_micros, self.proceso)
                info_micro = despachador.datos_js()

                for k, v in info_micro.items():
                    js_mostrar_info_micro.Call(k, v)
            else:
                js_mostrar_mensaje.Call("Debe haber al menos un micro y el quantum debe ser mayor a cero.")

        else:
            js_mostrar_mensaje.Call("Todos los valores deben ser enteros.")


    def are_positive_integers(self, *num):
        all_integers = True

        for n in num:
            all_integers = self.is_integer(n) and (int(n) >= 0)
            if not all_integers:
                break
        return all_integers

    def is_integer(self, number):
        try:
            number = int(number)
        except ValueError:
            return False
        else:
            return True
