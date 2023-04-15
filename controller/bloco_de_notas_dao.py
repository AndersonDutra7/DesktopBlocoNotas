import sqlite3

from model.bloco_de_notas import Bloco_De_Notas


class DataBase:
    def __init__(self, nome='system.db2'):
        self.connection = None
        self.name = nome

    def connect(self):
        self.connection = sqlite3.connect(self.name)

    def close_connection(self):
        try:
            self.connection.close()
        except sqlite3.Error as e:
            print(e)

    def create_table_bloco_de_notas(self):
        self.connect()
        cursor = self.connection.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS BLOCO_DE_NOTAS(
            ID INTEGER SERIAL PRIMARY KEY,
            NOME_NOTA TEXT,
            DATA_NOTA TEXT,
            TEXTO_NOTA TEXT
            );
            """)
        self.close_connection()

    def criar_nota(self, bloco = Bloco_De_Notas):
        self.connect()
        cursor = self.connection.cursor()
        campos_bloco = ('ID', 'NOME_NOTA', 'DATA_NOTA', 'TEXTO_NOTA')

        valores_bloco = f" '{bloco.id}', '{bloco.nome_nota}', '{bloco.data_nota}', " \
                  f" '{bloco.texto_nota}' "

        try:
            cursor.execute(f""" INSERT INTO BLOCO_DE_NOTAS {campos_bloco} VALUES ({valores_bloco})""")
            self.connection.commit()
            return 'Ok'
        except sqlite3.Error as e:
            return str(e)
        finally:
            self.close_connection()

    def ler_nota(self):
        pass

    def editar_nota(self, nota = Bloco_De_Notas):
        self.connect()
        try:
            cursor = self.connection.cursor()
            cursor.execute(f""" UPDATE BANCO_DE_NOTAS SET
                 ID = '{nota.id}',
                 NOME_NOTA = '{nota.nome_nota}',
                 DATA_NOTA = '{nota.data_nota}'
                 TEXTO_NOTA = '{nota.texto_nota}'""")
            self.connection.commit()
            return 'Ok'
        except sqlite3.Error as e:
            return str(e)
        finally:
            self.close_connection()

    def excluir_nota(self):
        pass