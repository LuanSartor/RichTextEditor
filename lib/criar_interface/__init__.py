import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtPrintSupport import *
from PyQt5.QtCore import *


class RTE(QMainWindow):
    def __init__(self):
        super(RTE, self).__init__()

        self.setWindowIcon(QIcon(r'lib/criar_interface/img/home.jpg'))
        self.setWindowTitle('RichTextEditor')

        self.editor = QTextEdit()
        self.fontSizeBox = QSpinBox()
        font = QFont('Arials', 24)
        self.editor.setFont(font)
        self.path = ""
        self.setCentralWidget(self.editor)
        self.editor.setFontPointSize(24)

        self.criarMenu()

        self.showMaximized()

    def criarMenu(self):

        mainMenu = self.menuBar()

        # cria e configura o menu file
        fileMenu = mainMenu.addMenu('File')

        newAction = QAction(QIcon(r'lib/criar_interface/img/new.jpg'), 'Novo Arquivo', self)
        fileMenu.addAction(newAction)

        openAction = QAction(QIcon(r'lib/criar_interface/img/open.jpg'), 'Abrir Arquivo', self)
        fileMenu.addAction(openAction)

        fileMenu.addSeparator()

        saveAction = QAction(QIcon(r'lib/criar_interface/img/save.jpg'), 'Salvar Arquivo', self)
        saveAction.setShortcut('ctrl+s')
        saveAction.triggered.connect(self.saveFile)
        fileMenu.addAction(saveAction)

        saveAsAction = QAction(QIcon(r'lib/criar_interface/img/save.jpg'), 'Salvar Como', self)
        saveAsAction.setShortcut('ctrl+shift+s')
        fileMenu.addAction(saveAsAction)

        fileMenu.addSeparator()

        closeAction = QAction(QIcon(r'lib/criar_interface/img/close.jpg'), 'Fechar Janela', self)
        closeAction.setShortcut('ctrl+e')
        closeAction.triggered.connect(self.closeWindow)
        fileMenu.addAction(closeAction)

        # cria e configura o menu edit
        editMenu = mainMenu.addMenu('Edit')

        undoBtn = QAction(QIcon('lib/criar_interface/img/undo.jpg'), 'undo', self)
        undoBtn.triggered.connect(self.editor.undo)
        undoBtn.setShortcut('ctrl+z')
        editMenu.addAction(undoBtn)

        redoBtn = QAction(QIcon('lib/criar_interface/img/redo.jpg'), 'redo', self)
        redoBtn.setShortcut('ctrl+shift+z')
        redoBtn.triggered.connect(self.editor.redo)
        editMenu.addAction(redoBtn)

        copyAction = QAction(QIcon(r'lib/criar_interface/img/copy.jpg'), 'Copiar', self)
        copyAction.setShortcut('ctrl+c')
        editMenu.addAction(copyAction)

        cutAction = QAction(QIcon(r'lib/criar_interface/img/cut.jpg'), 'Recortar', self)
        cutAction.setShortcut('ctrl+x')
        editMenu.addAction(cutAction)

        pasteAction = QAction(QIcon(r'lib/criar_interface/img/paste.jpg'), 'Colar', self)
        pasteAction.setShortcut('ctrl+v')
        editMenu.addAction(pasteAction)

        # cria e configura o menu view
        viewMenu = mainMenu.addMenu('View')

        fontAction = QAction(QIcon(r'lib/criar_interface/img/text.jpg'), 'Fonte', self)
        fontAction.setShortcut('ctrl+f')
        fontAction.triggered.connect(self.fontDialog)
        viewMenu.addAction(fontAction)

        rightAllign = QAction(QIcon(r'lib/criar_interface/img/right.jpg'), 'Right Allign', self)
        rightAllign.triggered.connect(lambda: self.editor.setAlignment(Qt.AlignRight))
        viewMenu.addAction(rightAllign)

        leftAllign = QAction(QIcon(r'lib/criar_interface/img/left.jpg'), 'left Allign', self)
        leftAllign.triggered.connect(lambda: self.editor.setAlignment(Qt.AlignLeft))
        viewMenu.addAction(leftAllign)

        centerAllign = QAction(QIcon(r'lib/criar_interface/img/center.jpg'), 'Center Allign', self)
        centerAllign.triggered.connect(lambda: self.editor.setAlignment(Qt.AlignCenter))
        viewMenu.addAction(centerAllign)

        # cria e configura o menu help
        helpMenu = mainMenu.addMenu('Help')


        # cria e configura a toolbar
        toolbar = self.addToolBar('ToolBar')
        toolbar.addAction(undoBtn)
        toolbar.addAction(redoBtn)


        toolbar.addAction(fontAction)

        toolbar.addAction(rightAllign)
        toolbar.addAction(leftAllign)
        toolbar.addAction(centerAllign)

        self.fontBox = QComboBox(self)
        self.fontBox.addItems(['Arial', "Courier New", 'Constantia', 'Gill Sans MT', 'Freestyle Script', 'c',
                               'Webdings', 'Wingdings 3'])
        self.fontBox.activated.connect(self.setFont)
        toolbar.addWidget(self.fontBox)

        self.fontSizeBox.setValue(24)
        self.fontSizeBox.valueChanged.connect(self.setFontSize)
        toolbar.addWidget(self.fontSizeBox)

        oneAction = QAction(QIcon(r'lib/criar_interface/img/cut.jpg'), 'One', self)
        twoAction = QAction(QIcon(r'lib/criar_interface/img/cut.jpg'), 'Two', self)
        toolbar.addActions(oneAction, twoAction)

    # funções do menu file
    def closeWindow(self):
        self.close()

    def fontDialog(self):
        font, ok = QFontDialog.getFont()

        if ok:
            self.textEdit.setFont(font)



    def setFontSize(self):
        value = self.fontSizeBox.value()
        self.editor.setFontPointSize(value)

    def setFont(self):
        font = self.fontBox.currentText()
        self.editor.setCurrentFont(QFont(font))

    def italicText(self):
        state = self.editor.fontItalic()
        self.editor.setFontItalic(not (state))

    def underlineText(self):
        state = self.editor.fontUnderline()
        self.editor.setFontUnderline(not (state))

    def boldText(self):
        if self.editor.fontWeight != QFont.Bold:
            self.editor.setFontWeight(QFont.Bold)
            return
        self.editor.setFontWeight(QFont.Normal)

    def saveFile(self):
        print(self.path)
        if self.path == '':
            self.file_saveas()
        text = self.editor.toPlainText()
        try:
            with open(self.path, 'w') as f:
                f.write(text)
                self.update_title()
        except Exception as e:
            print(e)

    def file_saveas(self):
        self.path, _ = QFileDialog.getSaveFileName(self, "Save file", "",
                                                   "text documents (*.txt );Text documents (*.txt);All files (*.*)")
        if self.path == '':
            return
        text = self.editor.toPlainText()
        try:
            with open(self.path, 'w') as f:
                f.write(text)
                self.update_title()
        except Exception as e:
            print(e)


def InitWindow():
    App = QApplication(sys.argv)
    rte = RTE()
    sys.exit(App.exec())
