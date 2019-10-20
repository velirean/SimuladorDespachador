from cefpython3 import cefpython as cef
from bs4 import BeautifulSoup
from Despachador import PythonJS
import subprocess
import time

# Servidor local para compartir el folder src a la aplicacion
http_server = subprocess.Popen(["python", "-m", "http.server", "8080", "--bind", "127.0.0.1", "-d", "src"], creationflags=subprocess.CREATE_NO_WINDOW)
time.sleep(2)

# Carga el html para utilizarlo como interfaz grafica
with open("main.html", encoding="utf-8") as page:
    html_code = BeautifulSoup(page.read(), features="html.parser").decode('utf-8')

def main():
    # Crear lista de procesos para el despachador en una funcion


  

    settings = {
        "debug": False,
        "context_menu": {"enabled":False}
    }
    cef.Initialize(settings=settings)
    browser = cef.CreateBrowserSync(url=cef.GetDataUrl(html_code),
                                    window_title="Random Number Generator")
    browser.SetClientHandler(LifespanHandler())
    bindings = cef.JavascriptBindings()

    # Une las funciones de python a javascript

    bindings.SetFunction("py_despachador", PythonJS.py_html_despachador)

    browser.SetJavascriptBindings(bindings)
    cef.MessageLoop()
    del browser
    cef.Shutdown()

# Cierra el proceso del servidor http cuando se cierra
# el navegador
class LifespanHandler(object):
    def OnBeforeClose(self, browser):
        http_server.kill()

if __name__ == '__main__':
    main()
