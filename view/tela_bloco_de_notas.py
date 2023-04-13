import requests
import json
import sys

from PySide6 import QtWidgets
from PySide6.QtWidgets import (QMainWindow, QVBoxLayout, QComboBox, QLabel, QLineEdit, QWidget, QPushButton,
                               QMessageBox, QSizePolicy, QTableWidget, QAbstractItemView, QTableWidgetItem, QTextEdit)

from model.bloco_de_notas import Bloco_De_Notas
from controller.bloco_de_notas_dao import DataBase

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(400, 300)

        self.setWindowTitle('BLOCO DE NOTAS')

        self.lbl_id = QLabel('ID')
        self.txt_id = QLineEdit('1')
        self.lbl_nome_nota = QLabel('TITULO')
        self.txt_nome_nota = QTextEdit()
        self.lbl_data_nota = QLabel('NOTA')
        self.txt_data_nota = QTextEdit()
        self.lbl_texto_nota = QLabel('NOTAS CADASTRADAS')
        self.txt_texto_nota = QTextEdit()
        self.btn_salvar = QPushButton('Salvar')
        self.btn_remover = QPushButton('Remover')
        # self.tabela_clientes = QTableWidget()

        # self.tabela_clientes.setColumnCount(12)
        # self.tabela_clientes.setHorizontalHeaderLabels(['CPF', 'Nome', 'Telefone Fixo', 'Telefone Celular', 'Sexo'
        #                                                 , 'Cep', 'Logradouro', 'Número', 'Complemento', 'Bairro',
        #                                                 'Município', 'Estado'])
        # self.tabela_clientes.setSelectionMode(QAbstractItemView.NoSelection)
        # self.tabela_clientes.setEditTriggers(QAbstractItemView.NoEditTriggers)


        layout = QVBoxLayout()
        layout.addWidget(self.lbl_id)
        layout.addWidget(self.txt_id)
        layout.addWidget(self.lbl_nome_nota)
        layout.addWidget(self.txt_nome_nota)
        layout.addWidget(self.lbl_data_nota)
        layout.addWidget(self.txt_data_nota)
        layout.addWidget(self.lbl_texto_nota)
        layout.addWidget(self.txt_texto_nota)
        layout.addWidget(self.btn_salvar)
        layout.addWidget(self.btn_remover)

        self.container = QWidget()
        self.container.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.container.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.setCentralWidget(self.container)
        self.container.setLayout(layout)

        # self.btn_remover.setVisible(False)
        self.btn_salvar.clicked.connect(self.salvar_nota)
        # self.txt_cpf.editingFinished.connect(self.consultar_cliente)
        # self.txt_cep.editingFinished.connect(self.consultar_enderecos)
        # self.btn_remover.clicked.connect(self.remover_cliente)
        # self.btn_limpar.clicked.connect(self.limpar_campos)
        # self.tabela_clientes.cellDoubleClicked.connect(self.carrega_dados)
        # self.popula_tabela_clientes()

    def salvar_nota(self):
        db = DataBase()

        nota = Bloco_De_Notas(
            id = self.txt_id.isReadOnly(),
            nome_nota = self.txt_nome_nota.isReadOnly(),
            data_nota = self.txt_data_nota.isReadOnly(),
            texto_nota = self.txt_texto_nota.isReadOnly()
        )

        if self.btn_salvar.text() == 'Salvar':
            retorno = db.criar_nota(nota)

            if retorno == 'Ok':
                msg = QMessageBox()
                msg.setWindowTitle('Nota Criada')
                msg.setText('Nota Salva com Sucesso')
                msg.exec()
                    # self.limpar_campos()
            elif retorno == 'UNIQUE constraint failed: BLOCO_DE_NOTAS.ID':
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setWindowTitle('Erro ao Criar Nota!')
                msg.setText(f'O ID {self.txt_id.text()} já existe com o nome {self.txt_nome_nota.text()}')
                msg.exec()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setWindowTitle('Erro ao Criar Nota!')
                msg.setText('Erro ao Criar Nota, Verifique os Dados Inseridos')
                msg.exec()
        elif self.btn_salvar.text() == 'Atualizar':
            retorno = db.editar_nota(nota)
            if retorno == 'Ok':
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                    # msg.setWindowTitle('Erro ao Editar a Nota')
                msg.setText('Nota Atualizada')
                msg.exec()
                    # self.limpar_campos()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setWindowTitle('Erro ao Atualizar Nota! ')
                msg.setText('Erro ao Atualziar Nota, Verifique os Dados Inseridos')
                msg.exec()
        # self.popula_tabela_clientes()
            # self.txt_cpf.setReadOnly(False)