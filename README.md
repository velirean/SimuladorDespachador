# SimuladorDespachador
Simulador simple de un despachador de procesos. Está hecho en python, pero utiliza Chromium Embedded Framework (CEF) como interfaz gráfica. 

## main.py
Se utiliza para empezar la aplicación. Realiza la unión de las funciones de Python para que se puedan utilizar desde JS. También crea un servidor http en otro proceso para servir el archivo JS con las funciones que modifican el DOM y los callbacks para Python También sirve los archivos de Bootstrap.

## main.html
Temporalmente tiene una tabla de relleno. Tiene el div con id "contenido" para mostrar la información de los micros y los procesos de cada uno. Se manipula su contenido con las funciones de `display.js`.

## display.js
Se encuentra en el directorio `src`. Tiene las funciones que manipulan el DOM y también los callbacks para Python (empiezan con *js_*). La función `crear_despachador()` tomará en cuenta los valores del usuario cuando se implemente el formulario correspondiente.

# Clases del paquete Despachador

## PythonJS
Contiene la lista de procesos como un atributo y en un futuro recibirá los parámetros del usuario para instanciar el Despachador. Las funciones que están disponibles para JS empiezan con *py_*, sólo funcionan si está la unión declarada en `main.py`.

## Despachador
Tiene la lista total de procesos a ejecutar e instancia los Micros que se indiquen. Elige a un Micro para que ejecute cada proceso en la lista basándose en el tiempo total de cada uno. Todavía no está implementada esta parte.

## Micro
Al recibir la instrucción de ejecutar un proceso, solamente actualiza su tiempo total y espera en caso de que no esté disponible el proceso que se le asignó. Le pasa los parámetros a la instancia de Proceso para que actualice sus atributos. Falta definir bien esa trancisión de datos.

## Proceso
Se encarga de definir los valores de sus atributos cuando Micro le pasa los datos necesarios. Falta implementar una función.
