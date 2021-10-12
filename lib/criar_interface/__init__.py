from PyQt5.QtWidgets import *
from PyQt5 import QtGui
import sys


class Window(QMainWindow):
    def __init__(self, *classes):
        super().__init__()

        self.setWindowTitle('RichTextEditor')
        self.setGeometry(0, 0, 500, 300)

        self.show()

