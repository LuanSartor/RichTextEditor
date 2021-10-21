import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtPrintSupport import *
from PyQt5.QtCore import *


class RTE(QMainWindow):
    def __init__(self):
        super(RTE, self).__init__()

        self.setWindowIcon(QIcon(r'img/home.jpg'))
        self.setWindowTitle('Editor Rich Text')

        self.editor = QTextEdit()
        self.caixa_tamanho_fonte = QSpinBox()
        font = QFont('Arials', 12)
        self.editor.setFont(font)
        self.caminho = ""
        self.setCentralWidget(self.editor)
        self.editor.setFontPointSize(12)

        self.criar_menu()
        self.criar_barra_ferramentas()

        self.showMaximized()

    def criar_menu(self):

        menu_principal = self.menuBar()

        # cria e configura o menu file
        arquivo_menu = menu_principal.addMenu('Arquivo')

        novo_action = QAction(QIcon(r'img/new.jpg'), 'Novo Arquivo', self)
        novo_action.triggered.connect(self.novo_arquivo)
        arquivo_menu.addAction(novo_action)

        arquivo_menu.addSeparator()

        salvar_action = QAction(QIcon(r'img/save.jpg'), 'Salvar Arquivo', self)
        salvar_action.setShortcut('ctrl+s')
        salvar_action.triggered.connect(self.salvar_arquivo)
        arquivo_menu.addAction(salvar_action)

        save_pdf_action = QAction('Salvar como PDF', self)
        salvar_action.setShortcut('ctrl+shift+s')
        save_pdf_action.triggered.connect(self.salvar_pdf)
        arquivo_menu.addAction(save_pdf_action)

        arquivo_menu.addSeparator()

        fechar_action = QAction(QIcon(r'img/close.jpg'), 'Fechar Janela', self)
        fechar_action.setShortcut('ctrl+e')
        fechar_action.triggered.connect(self.fechar_janela)
        arquivo_menu.addAction(fechar_action)

        # cria e configura o menu edit
        editar_menu = menu_principal.addMenu('Editar')

        self.desfazer_action = QAction(QIcon('img/undo.jpg'), 'Desfazer', self)
        self.desfazer_action.triggered.connect(self.editor.undo)
        self.desfazer_action.setShortcut('ctrl+z')
        editar_menu.addAction(self.desfazer_action)

        self.refazer_action = QAction(QIcon('img/redo.jpg'), 'Refazer', self)
        self.refazer_action.setShortcut('ctrl+shift+z')
        self.refazer_action.triggered.connect(self.editor.redo)
        editar_menu.addAction(self.refazer_action)

        editar_menu.addSeparator()

        self.copiar_action = QAction(QIcon(r'img/copy.jpg'), 'Copiar', self)
        self.copiar_action.setShortcut('ctrl+c')
        self.copiar_action.triggered.connect(self.editor.copy)
        editar_menu.addAction(self.copiar_action)

        self.recortar_action = QAction(QIcon(r'img/cut.jpg'), 'Recortar', self)
        self.recortar_action.setShortcut('ctrl+x')
        self.recortar_action.triggered.connect(self.editor.cut)
        editar_menu.addAction(self.recortar_action)

        self.colar_action = QAction(QIcon(r'img/paste.jpg'), 'Colar', self)
        self.colar_action.setShortcut('ctrl+v')
        self.colar_action.triggered.connect(self.editor.paste)
        editar_menu.addAction(self.colar_action)

        editar_menu.addSeparator()

        self.fonte_action = QAction(QIcon(r'img/text.jpg'), 'Fonte', self)
        self.fonte_action.setShortcut('ctrl+f')
        self.fonte_action.triggered.connect(self.dialogo_fonte)
        editar_menu.addAction(self.fonte_action)

        self.cor_action = QAction(QIcon(r'img/color.jpg'), 'Cor', self)
        self.cor_action.triggered.connect(self.dialogo_cor)
        editar_menu.addAction(self.cor_action)

        editar_menu.addSeparator()

        self.alinhaDireita_action = QAction(QIcon(r'img/left.jpg'), 'Alinhamento a Esquerda', self)
        self.alinhaDireita_action.triggered.connect(lambda: self.editor.setAlignment(Qt.AlignLeft))
        editar_menu.addAction(self.alinhaDireita_action)

        self.alinhaCentro_action = QAction(QIcon(r'img/center.jpg'), 'Alinhamento ao Centro', self)
        self.alinhaCentro_action.triggered.connect(lambda: self.editor.setAlignment(Qt.AlignCenter))
        editar_menu.addAction(self.alinhaCentro_action)

        self.alinhaEsquerda_action = QAction(QIcon(r'img/right.jpg'), 'Alinhamento a Direita', self)
        self.alinhaEsquerda_action.triggered.connect(lambda: self.editor.setAlignment(Qt.AlignRight))
        editar_menu.addAction(self.alinhaEsquerda_action)

        # cria e configura o menu view
        # viewMenu = menu_principal.addMenu('View')

    def criar_barra_ferramentas(self):
        # cria e configura a barra_ferramentas

        barra_ferramentas = self.addToolBar('Barra de Ferramentas')
        barra_ferramentas.addAction(self.desfazer_action)
        barra_ferramentas.addAction(self.refazer_action)

        barra_ferramentas.addSeparator()

        barra_ferramentas.addAction(self.copiar_action)
        barra_ferramentas.addAction(self.recortar_action)
        barra_ferramentas.addAction(self.colar_action)

        barra_ferramentas.addSeparator()

        barra_ferramentas.addAction(self.fonte_action)
        barra_ferramentas.addAction(self.cor_action)

        self.caixaFonte = QComboBox(self)
        self.caixaFonte.addItems(['Arial', "Courier New", 'Constantia', 'Gill Sans MT', 'Freestyle Script', 'c',
                                  'Webdings', 'Wingdings 3'])
        self.caixaFonte.activated.connect(self.set_fonte)
        barra_ferramentas.addWidget(self.caixaFonte)

        self.caixa_tamanho_fonte.setValue(12)
        self.caixa_tamanho_fonte.valueChanged.connect(self.set_tamanho_fonte)
        barra_ferramentas.addWidget(self.caixa_tamanho_fonte)

        barra_ferramentas.addAction(self.alinhaDireita_action)
        barra_ferramentas.addAction(self.alinhaCentro_action)
        barra_ferramentas.addAction(self.alinhaEsquerda_action)

    # funções do menu file
    def novo_arquivo(self):
        self.editor.setText('')
        font = QFont('Arials', 12)
        self.editor.setFont(font)
        self.caminho = ""
        self.editor.setFontPointSize(12)

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

    def salvar_pdf(self):
        f_name, _ = QFileDialog.getSaveFileName(self, "Export PDF", None, "PDF files (.pdf );;All files()")
        print(f_name)

        if f_name != '':
            printer = QPrinter(QPrinter.HighResolution)
            printer.setOutputFormat(QPrinter.PdfFormat)
            printer.setOutputFileName(f_name)
            self.editor.document().print_(printer)

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

    def texto_sublinhado(self):
        estado = self.editor.fontUnderline()
        self.editor.setFontUnderline(not estado)

    def texto_negrito(self):
        if self.editor.fontWeight != QFont.Bold:
            self.editor.setFontWeight(QFont.Bold)
            return
        self.editor.setFontWeight(QFont.Normal)


App = QApplication(sys.argv)
rte = RTE()
sys.exit(App.exec())
