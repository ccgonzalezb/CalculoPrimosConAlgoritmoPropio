from PyQt5 import QtCore
from model import criba_tercio_optima


class Worker(QtCore.QThread):
    progreso = QtCore.pyqtSignal(int)
    resultado = QtCore.pyqtSignal(list)

    def __init__(self, limite):
        super().__init__()
        self.limite = limite

    def run(self):
        primos = criba_tercio_optima(self.limite, self.emit_progreso)
        self.resultado.emit(primos)

    def emit_progreso(self, valor):
        self.progreso.emit(valor)


class Controller:
    def __init__(self, ui):
        self.ui = ui
        self.ui.pushButton.clicked.connect(self.iniciar_calculo)
        self.worker = None

    def iniciar_calculo(self):
        self.ui.progressBar.setValue(0)
        self.ui.textBrowser.clear()

        try:
            limite = int(self.ui.lineEdit.text())
        except ValueError:
            self.ui.textBrowser.append("❌ Por favor ingresa un número válido.")
            return

        self.worker = Worker(limite)
        self.worker.progreso.connect(self.ui.progressBar.setValue)
        self.worker.resultado.connect(self.mostrar_resultado)
        self.worker.start()

    def mostrar_resultado(self, primos):
        # Guardar todos los primos en un archivo
        try:
            with open("primos.txt", "w", encoding="utf-8") as f:
                f.write(", ".join(map(str, primos)))
        except Exception as e:
            self.ui.textBrowser.append(f"❌ Error al guardar el archivo: {e}")
            return

        # Mostrar una buena cantidad en pantalla (por ejemplo, 2000)
        mostrar_max = 2000
        resumen = primos[:mostrar_max]
        self.ui.textBrowser.append(f"✅ Total de primos encontrados: {len(primos)}")
        self.ui.textBrowser.append(f"📋 Mostrando los primeros {mostrar_max} primos:")
        self.ui.textBrowser.append(", ".join(map(str, resumen)) + " ...")
        self.ui.textBrowser.append("📝 El archivo 'primos.txt' contiene la lista completa.")
