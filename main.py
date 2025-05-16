import sys
from PyQt5 import QtWidgets
from view import Ui_MainWindow
from controller import Controller


def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    controlador = Controller(ui)
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
