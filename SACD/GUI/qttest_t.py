import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication, QWidget, QPushButton, QToolTip, QAction, QMenu,
QComboBox, QDialog, QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
QMenuBar, QSpinBox, QTextEdit, QVBoxLayout)
from PyQt5.QtGui import QIcon, QFont

class App():

    def slot_method(self):
        print('llamada al metodo slot')

    def __init__(self):
        super().__init__()
        self.title = 'Laboratorio Secundario de Tiempo y Frecuencia'
        self.left = 30
        self.top = 50
        self.width = 600
        self.height = 400
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowIcon(QIcon("logocena.png"))

        QToolTip.setFont(QFont('SansSerif', 10))

        self.setToolTip('This is a buttom')

        btn = QPushButton('Buttom', self)
        btn.setToolTip('Esto es un boton')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        ############menu
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')
        viewMenu = menubar.addMenu('View')

        ###########despliegues
        #file menu
        impMenu = QMenu('Import', self)
        impAct = QAction('Import mail', self)
        impMenu.addAction(impAct)

        newAct = QAction('New', self)

        fileMenu.addAction(newAct)
        fileMenu.addMenu(impMenu)
        #view
        viewStatAct = QAction('View statusbar', self, checkable=True)
        viewStatAct.setStatusTip('View statusbar')
        viewStatAct.setChecked(True)
        viewStatAct.triggered.connect(self.toggleMenu)

        viewMenu.addAction(viewStatAct)

        ##Accion click al botton
        buttom = QPushButton("Click")
        buttom.clicked.connect(self.slot_metod)
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(button)

        self.Layout(mainLayout)
        self.setWindowTitle("B example - press")

        self.show()

    def toggleMenu(self, state):

        if state:
            self.statusbar.show()
        else:
            self.statusbar.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
