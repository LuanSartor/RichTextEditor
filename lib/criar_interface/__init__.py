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
        self.caixa_tamanho_fonte = QSpinBox()
        font = QFont('Arials', 16)
        self.editor.setFont(font)
        self.caminho = ""
        self.setCentralWidget(self.editor)
        self.editor.setFontPointSize(24)

        self.criar_menu()
        self.criar_barra_ferramentas()

        self.showMaximized()

    def criar_menu(self):

        menu_principal = self.menuBar()

        # cria e configura o menu file
        fileMenu = menu_principal.addMenu('File')

        novoAction = QAction(QIcon(r'lib/criar_interface/img/new.jpg'), 'Novo Arquivo', self)
        fileMenu.addAction(novoAction)

        abrirAction = QAction(QIcon(r'lib/criar_interface/img/open.jpg'), 'Abrir Arquivo', self)
        fileMenu.addAction(abrirAction)

        fileMenu.addSeparator()

        salvarAction = QAction(QIcon(r'lib/criar_interface/img/save.jpg'), 'Salvar Arquivo', self)
        salvarAction.setShortcut('ctrl+s')
        salvarAction.triggered.connect(self.salvar_arquivo)
        fileMenu.addAction(salvarAction)

        fileMenu.addSeparator()

        fecharAction = QAction(QIcon(r'lib/criar_interface/img/close.jpg'), 'Fechar Janela', self)
        fecharAction.setShortcut('ctrl+e')
        fecharAction.triggered.connect(self.fechar_janela)
        fileMenu.addAction(fecharAction)

        # cria e configura o menu edit
        editMenu = menu_principal.addMenu('Edit')

        self.desfazerAction = QAction(QIcon('lib/criar_interface/img/undo.jpg'), 'undo', self)
        self.desfazerAction.triggered.connect(self.editor.undo)
        self.desfazerAction.setShortcut('ctrl+z')
        editMenu.addAction(self.desfazerAction)

        self.refazerAction = QAction(QIcon('lib/criar_interface/img/redo.jpg'), 'redo', self)
        self.refazerAction.setShortcut('ctrl+shift+z')
        self.refazerAction.triggered.connect(self.editor.redo)
        editMenu.addAction(self.refazerAction)

        self.copiarAction = QAction(QIcon(r'lib/criar_interface/img/copy.jpg'), 'Copiar', self)
        self.copiarAction.setShortcut('ctrl+c')
        editMenu.addAction(self.copiarAction)

        self.recortarAction = QAction(QIcon(r'lib/criar_interface/img/cut.jpg'), 'Recortar', self)
        self.recortarAction.setShortcut('ctrl+x')
        editMenu.addAction(self.recortarAction)

        self.colarAction = QAction(QIcon(r'lib/criar_interface/img/paste.jpg'), 'Colar', self)
        self.colarAction.setShortcut('ctrl+v')
        editMenu.addAction(self.colarAction)

        editMenu.addSeparator()

        self.fonteAction = QAction(QIcon(r'lib/criar_interface/img/text.jpg'), 'Fonte', self)
        self.fonteAction.setShortcut('ctrl+f')
        self.fonteAction.triggered.connect(self.dialogo_fonte)
        editMenu.addAction(self.fonteAction)

        self.corAction = QAction(QIcon(r'lib/criar_interface/img/color.jpg'), 'Cor', self)
        self.corAction.triggered.connect(self.dialogoCor)
        editMenu.addAction(self.corAction)

        editMenu.addSeparator()

        self.alinhaDireitaAction = QAction(QIcon(r'lib/criar_interface/img/right.jpg'), 'Right Allign', self)
        self.alinhaDireitaAction.triggered.connect(lambda: self.editor.setAlignment(Qt.AlignRight))
        editMenu.addAction(self.alinhaDireitaAction)

        self.alinhaEsquerdaAction = QAction(QIcon(r'lib/criar_interface/img/left.jpg'), 'left Allign', self)
        self.alinhaEsquerdaAction.triggered.connect(lambda: self.editor.setAlignment(Qt.AlignLeft))
        editMenu.addAction(self.alinhaEsquerdaAction)

        self.alinhaCentroAction = QAction(QIcon(r'lib/criar_interface/img/center.jpg'), 'Center Allign', self)
        self.alinhaCentroAction.triggered.connect(lambda: self.editor.setAlignment(Qt.AlignCenter))
        editMenu.addAction(self.alinhaCentroAction)

        # cria e configura o menu view
        # viewMenu = menu_principal.addMenu('View')

    def criar_barra_ferramentas(self):
        # cria e configura a barra_ferramentas
        barra_ferramentas = self.addToolBar('Barra de Ferramentas')
        barra_ferramentas.addAction(self.desfazerAction)
        barra_ferramentas.addAction(self.refazerAction)

        barra_ferramentas.addSeparator()

        barra_ferramentas.addAction(self.copiarAction)
        barra_ferramentas.addAction(self.recortarAction)
        barra_ferramentas.addAction(self.colarAction)

        barra_ferramentas.addSeparator()

        barra_ferramentas.addAction(self.fonteAction)
        barra_ferramentas.addAction(self.corAction)

        self.caixaFonte = QComboBox(self)
        self.caixaFonte.addItems(['Arial', "Courier New", 'Constantia', 'Gill Sans MT', 'Freestyle Script', 'c',
                                  'Webdings', 'Wingdings 3'])
        self.caixaFonte.activated.connect(self.set_fonte)
        barra_ferramentas.addWidget(self.caixaFonte)

        self.caixaTamanhoFonte.setValue(24)
        self.caixaTamanhoFonte.valueChanged.connect(self.set_font_size)
        barra_ferramentas.addWidget(self.caixaTamanhoFonte)

        barra_ferramentas.addAction(self.alinhaDireitaAction)
        barra_ferramentas.addAction(self.alinhaEsquerdaAction)
        barra_ferramentas.addAction(self.alinhaCentroAction)

    # funções do menu file
    def salvar_arquivo(self):
        print(self.caminho)
        if self.caminho == '':
            self.salvar_arquivo_como()
        text = self.editor.toPlainText()
        try:
            with open(self.caminho, 'w') as f:
                f.write(text)
                self.update_title()
        except Exception as e:
            print(e)

    def salvar_arquivo_como(self):
        self.caminho, _ = QFileDialog.getSaveFileName(self, "Save file", "",
                                                      "text documents (*.txt );Text documents (*.txt);All files (*.*)")
        if self.caminho == '':
            return
        text = self.editor.toPlainText()
        try:
            with open(self.caminho, 'w') as f:
                f.write(text)
                self.update_title()
        except Exception as e:
            print(e)

    def fechar_janela(self):
        self.close()

    # funções do menu edit
    def dialogo_fonte(self):
        font, ok = QFontDialog.getFont()

        if ok:
            self.textEdit.set_fonte()

    def dialogo_cor(self):
        color = QColorDialog.getColor()
        self.editor.setTextColor(color)

    def set_tamanho_fonte(self):
        value = self.caixa_tamanho_fonte.value()
        self.editor.setFontPointSize(value)

    def set_fonte(self):
        fonte = self.caixaFonte.currentText()
        self.editor.setCurrentFont(QFont(fonte))

    def texto_italico(self):
        estado = self.editor.fontItalic()
        self.editor.setFontItalic(not estado)

    def texto_underline(self):
        estado = self.editor.fontUnderline()
        self.editor.setFontUnderline(not estado)

    def texto_negrito(self):
        if self.editor.fontWeight != QFont.Bold:
            self.editor.setFontWeight(QFont.Bold)
            return
        self.editor.setFontWeight(QFont.Normal)


def iniciar_janela():
    App = QApplication(sys.argv)
    rte = RTE()
    sys.exit(App.exec())
