# SimuladorDespachador
Simulador simple de un despachador de procesos. Está hecho en python, pero utiliza Chromium Embedded Framework (CEF) como interfaz gráfica. 

## main.py
Se utiliza para empezar la aplicación. Realiza la unión de las funciones de Python para que se puedan utilizar desde JS. También crea un servidor http en otro proceso para servir el archivo JS con las funciones que modifican el DOM y los callbacks para Python También sirve los archivos de Bootstrap.

## main.html
Tiene el div con id "contenido" para mostrar la información de los micros y los procesos de cada uno. Se manipula su contenido con las funciones de `display.js`. El div con id "alerta" es para mostrar mensajes al usuario cuando una de las entradas no es válida, las validaciones se hacen con Python.|

## display.js
Se encuentra en el directorio `src`. Tiene las funciones que manipulan el DOM y también los callbacks para Python (empiezan con *js_*). La función `crear_despachador()` se ejecuta cuando se envía el formulario, así se puede mandar la configuración al despachador.

# Clases del paquete Despachador
A excepción de `PythonJS` y `Despachador`, se modificaron los `__str__` para que sean fáciles de pasar a JS al momento de generar el string con la información de cada Micro

## PythonJS
Contiene la lista de procesos como un atributo y recibe los parámetros del usuario para instanciar el Despachador. Las funciones que están disponibles para JS empiezan con *py_*, sólo funcionan si está la unión declarada en `main.py`.

## Despachador
Tiene la lista total de procesos a ejecutar e instancia los Micros que se indiquen. Elige a un Micro para que ejecute cada proceso en la lista de procesos a ejecutar. Tiene prioridad el Micro con menor tiempo total y con id más bajo. También hace que todos los Micro instanciados esperen cuando no hay procesos disponibles para ejecutar. 

## Micro
Al recibir la instrucción de ejecutar un proceso, solamente actualiza su tiempo total y espera en caso de que no esté disponible el proceso que se le asignó. Le pasa los parámetros a la instancia de Proceso para que actualice sus atributos.
Como futura mejora se debería mejorar el doble sort para encontrar el Micro a utilizar.

## Proceso
Se encarga de definir los valores de sus atributos cuando Micro le pasa los datos necesarios.
