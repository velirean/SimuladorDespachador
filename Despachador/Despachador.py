from Despachador import Micro
from operator import itemgetter

class Despachador:
    def __init__(self, quantum, tiempo_bloqueo, tiempo_cambio_contexto, cantidad_micros, lista_proceso):
        self.quantum = quantum
        self.tb = tiempo_bloqueo
        self.tcc = tiempo_cambio_contexto
        self.micro = []

        for i in range(0, cantidad_micros):
            self.micro.append({
                "id" : i + 1,
                "tt" : 0,
                "micro" : Micro(i + 1, self.tcc, self.quantum, self.tb)
            })
        # se considera que los procesos ya estan ordenados
        self.proceso = lista_proceso

        self.ejecutar_proceso()
    
    def ejecutar_proceso(self):
        for p in self.proceso:
            # seleccionar al micro correspondiente
            micro_actual = self.seleccionar_micro()
            
            # Cuando el micro seleccionado tiene que esperar se 
            # vuelve necesario que todos los micros esperen porque
            # uno podria tener un id mas bajo y estaria disponible
            # al aparecer el proceso. Esto maneja esa situacion.
            if micro_actual["micro"].get_tt() < p.get_tiempo_disponible():
                for m in self.micro:
                    # Solo a los micros en esa situacion
                    if m["micro"].get_tt() < p.get_tiempo_disponible():
                        tiempo_espera = p.get_tiempo_disponible() - m["micro"].get_tt()
                        m["micro"].esperar(tiempo_espera)
                        m["tt"] = m["micro"].get_tt()
                # Seleccionar de nuevo, debido a la actualizacion
                micro_actual = self.seleccionar_micro()

            micro_actual["micro"].ejecutar_proceso(p)
            micro_actual["tt"] = micro_actual["micro"].get_tt()

    def seleccionar_micro(self):
        # Para que el ordenamiento sea correcto el orden es inverso
        # Primero por id y despues por tiempo total de cada micro
        # y asi se obtiene el orden buscado: tiempo ascendente y 
        # despues por id descendente
        micro_ordenado = sorted(self.micro, key=itemgetter('id'))
        micro_ordenado = sorted(micro_ordenado, key=itemgetter('tt'))
        return micro_ordenado[0]
        

    def datos_js(self):
        # Regresa los datos de cada micro en formato para JS
        dato = {}

        for m in self.micro:
            dato.update({ str(m["micro"].get_id()) : str(m["micro"])})

        return dato
