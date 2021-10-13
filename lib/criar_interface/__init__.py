from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5.QtGui import *
import sys


class Window(QMainWindow):
    def __init__(self, *classes):
        super().__init__()

        self.setWindowIcon(QtGui.QIcon(r'lib/criar_interface/img/home.jpg'))
        self.setWindowTitle('RichTextEditor')
        self.setGeometry(0, 0, 500, 300)

        self.createMenu()

        self.show()

    def createMenu(self):
        # cria o menu junto com suas opções
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('File')
        editMenu = mainMenu.addMenu('Edit')
        viewMenu = mainMenu.addMenu('View')
        helpMenu = mainMenu.addMenu('Help')


        # cria as ações do menu file
        newAction = QAction(QIcon(r'lib/criar_interface/img/new.jpg'), 'New File', self)
        fileMenu.addAction(newAction)

        openAction = QAction(QIcon(r'lib/criar_interface/img/open.jpg'), 'Open File', self)
        fileMenu.addAction(openAction)

        fileMenu.addSeparator()

        saveAction = QAction(QIcon(r'lib/criar_interface/img/save.jpg'), 'Save File', self)
        saveAction.setShortcut('ctrl+s')
        fileMenu.addAction(saveAction)

        fileMenu.addSeparator()

        closeAction = QAction(QIcon(r'lib/criar_interface/img/close.jpg'), 'Close Window', self)
        closeAction.setShortcut('ctrl+e')
        closeAction.triggered.connect(self.closeWindow)
        fileMenu.addAction(closeAction)

        # ações do menu edit
        copyAction = QAction(QIcon(r'lib/criar_interface/img/copy.jpg'), 'Copy', self)
        copyAction.setShortcut('ctrl+c')
        editMenu.addAction(copyAction)

        pasteAction = QAction(QIcon(r'lib/criar_interface/img/paste.jpg'), 'Paste', self)
        pasteAction.setShortcut('ctrl+v')
        editMenu.addAction(pasteAction)

    # funções do menu file
    def closeWindow(self):
        self.close()


def InitWindow():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
