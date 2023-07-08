# importando módulos
import time
import re
import pandas as pd
from datetime import datetime
import pyodbc
from classes import *
from conexao import conecta
import warnings
warnings.filterwarnings('ignore')
# ///////////////////////////////// #


# Esta classe cria métodos para validar e cadastrar
class Validacao:

    def valida_string(self, char):
        """
            Esta função verifica se as strings estão válidas
        """
        while True:
            regex = "^([a-zA-Z]{2,}\s?([a-zA-Z]{1,})?)"
            if re.search(regex, char):
                break
            else:
                char = input("\033[1;34;40mDigite dados válidos\033[m  ")
                continue

        return char

    def valida_email(self, email):
        """
            Esta função verifica se o email esta válido
        """
        while True:
            regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
            if re.search(regex, email):
                break
            else:
                email = input("\033[1;34;40mDigite um email no formato válido 'teste@teste.com.br':\033[m ")

        return email

    def valida_data(self, data):
        """
            Esta função verifica se a data esta válida
        """
        while True:
            try:
                data = datetime.strptime(data, '%d/%m/%Y').date()
                break
            except:
                data = str(input('\033[1;34;40mDigite uma data na formato DD/MM/AAAA:\033[m '))

        return data

    def valida_placa(self, placa):
        """
            Esta função verifica se a placa esta válida
        """
        while True:
            regex = '^[a-zA-Z]{3}[0-9][A-Za-z0-9][0-9]{2}$'
            if re.search(regex, placa):
                break
            else:
                placa = input("\033[1;34;40mDigite uma placa no formato BRA1566/BRA2A18:\033[m  ")
                continue

        return placa

    def valida_cnh(self, cnh):
        """
            Esta função verifica se a cnh esta válida
        """
        while True:
            regex = '^[0-9]{11}$'
            if re.search(regex, cnh):
                break
            else:
                cnh = input("\033[1;34;40mDigite uma cnh com 11 digitos:\033[m ")
                continue

        return cnh

    def valida_linha(self, linha):
        """
            Esta função verifica se a linha do ônibus esta válida
        """
        while True:
            regex = '^[0-9]{3}$'

            if linha == '000':
                linha = input("\033[1;34;40mDigite uma linha válida:\033[m ")
                continue

            elif re.search(regex, linha):
                break

            else:
                linha = input("\033[1;34;40mDigite uma linha com 3 digitos:\033[m ")
                continue

        return linha

    def valida_credito(self, credito):
        """
            Esta função verifica se o crédito esta válido
        """
        while True:

            regex = '^[0-9]{0,5}$'
            if re.search(regex, credito):
                break
            else:
                credito = input("\033[1;34;40mDigite dados válidos R$\033[m  ")
                continue

        return float(credito)

    def valida_tipo(self, tipo):
        """
            Esta função verifica se o tipo esta válido
        """
        while True:

            if 'comum' == tipo:
                break
            elif 'estudante' == tipo:
                break
            elif 'vale transporte' == tipo:
                break
            elif 'idoso' == tipo:
                break
            else:
                tipo = input(
                    '\033[1;34;40mVoce deve inserir um tipo válido (comum, estudante, vale transporte ou idoso)\033[m ')
                continue

        return tipo

    def valida_ano(self, ano):
        """
            Esta função verifica se o ano esta válido
        """
        while True:
            try:
                ano = datetime.strptime(ano, '%Y').date().year
                break
            except:
                ano = str(input("\033[1;34;40mDigite um ano no formato '2022':\033[m "))

        return ano

    def valida_id(self, prop):
        """
            Esta função verifica se a id do propietário esta válido
        """
        while True:
            regex = '^[0-9]{0,}$'
            if re.search(regex, prop):
                break
            else:
                prop = input("\033[1;34;40mDigite apenas números:\033[m ")
                continue

        return prop

    def cadastrar_usuario(self):
        """
            Esta função cadastra um usuário
        """
        while True:
            nome = str(input('\033[1;34;40mDigite seu nome:\033[m '))
            nome = self.valida_string(nome).capitalize()
            sobrenome = str(input('\033[1;34;40mDigite seu sobrenome:\033[m '))
            sobrenome = self.valida_string(sobrenome).capitalize()
            email = str(input('\033[1;34;40mDigite seu email:\033[m '))
            email = self.valida_email(email)
            bairro = str(input('\033[1;34;40mDigite seu bairro:\033[m '))
            bairro = self.valida_string(bairro).capitalize()
            dt_nascimento = str(input('\033[1;34;40mDigite sua data de nascimento:\033[m '))
            dt_nascimento = self.valida_data(dt_nascimento)
            u = Usuario(nome, sobrenome, email, bairro, dt_nascimento)
            cnx = conecta()
            csr = cnx.cursor()
            try:

                sql = f""" INSERT INTO jaelson_matias.USUARIO (nome, sobrenome, email, bairro, data_nascimento)
                                        VALUES ('{u.nome}', '{u.sobrenome}', '{u.email}', '{u.bairro}', '{u.dt_nascimento}'); """
                csr.execute(sql)

            except pyodbc.DatabaseError as ex:
                print(ex)
                time.sleep(0.8)
                print('\033[1;34;40mErro na inserção\033[m\n')
                time.sleep(0.8)
                continue

            else:
                cnx.commit()
                print('\033[1;34;40mCadastrando...\033[m')
                time.sleep(0.8)
                print('\033[1;34;40mFinalizando cadastro...\033[m')
                time.sleep(0.8)
                print('\033[1;34;40mCadastro realizado com sucesso!!\033[m\n')
                cnx.close()
                break

    def cadastrar_motorista(self):
        """
            Esta função cadastra um motorista
        """
        while True:
            nome = str(input('\033[1;34;40mDigite seu nome:\033[m '))
            nome = self.valida_string(nome).capitalize()
            sobrenome = str(input('\033[1;34;40mDigite seu sobrenome:\033[m '))
            sobrenome = self.valida_string(sobrenome).capitalize()
            num_cnh = str(input('\033[1;34;40mDigite o número da cnh:\033[m '))
            num_cnh = self.valida_cnh(num_cnh)
            dt_nascimento = str(input('\033[1;34;40mDigite sua data de nascimento:\033[m '))
            dt_nascimento = self.valida_data(dt_nascimento)
            m = Motorista(nome, sobrenome, num_cnh, dt_nascimento)
            cnx = conecta()
            csr = cnx.cursor()
            try:

                sql = f""" INSERT INTO jaelson_matias.MOTORISTA (nome, sobrenome, num_cnh, data_nascimento)
                                        VALUES ('{m.nome}', '{m.sobrenome}', '{m.num_cnh}', '{m.dt_nascimento}'); """

                csr.execute(sql)

            except pyodbc.DatabaseError:
                time.sleep(0.8)
                print('\033[1;34;40mErro na inserção\033[m')
                time.sleep(0.8)
                continue

            else:
                cnx.commit()
                print('\033[1;34;40mCadastrando...\033[m')
                time.sleep(0.8)
                print('\033[1;34;40mFinalizando cadastro...\033[m')
                time.sleep(0.8)
                print('\033[1;34;40mCadastro realizado com sucesso!!\033[m\n')
                cnx.close()
                break

    def cadastrar_cartao(self):
        """
            Esta função cadastra um cartão
        """
        while True:
            id_prop = input('\033[1;34;40mDigite o ID:\033[m ')
            id_prop = self.valida_id(id_prop)
            cred = str(input('\033[1;34;40mDigite a quantidade de créditos R$:\033[m '))
            cred = self.valida_credito(cred)
            tipo = str(input('\033[1;34;40mO tipo do cartão deve ser comum, estudante, vale transporte ou idoso :\033[m '))
            tipo = self.valida_tipo(tipo)
            dt_ems = str(input('\033[1;34;40mData de emissão:\033[m '))
            dt_ems = self.valida_data(dt_ems)
            c = Cartao(id_prop, cred, tipo, dt_ems)
            cnx = conecta()
            csr = cnx.cursor()
            try:
                sql = f""" INSERT INTO jaelson_matias.CARTAO (id_proprietario, credito, tipo, data_emissao)
                                                VALUES ('{c.id_proprietario}', '{c.qtd_creditos}', '{c.tipo_cartao}', '{c.dt_emissao}'); """

                csr.execute(sql)

            except pyodbc.DatabaseError:
                time.sleep(0.8)
                print('\033[1;34;40mFalha ao cadastrar um cartão, verifique se o ID ou os dados estão válidos!!\033[m')
                time.sleep(0.8)
                continue
            else:
                cnx.commit()
                print('\033[1;34;40mCadastrando...\033[m')
                time.sleep(0.8)
                print('\033[1;34;40mFinalizando cadastro...\033[m')
                time.sleep(0.8)
                print('\033[1;34;40mCadastro realizado com sucesso!!\033[m\n')
                cnx.close()
                break

    def cadastrar_onibus(self):
        """
            Esta função cadastra um ônibus
        """
        while True:
            id_motorista = input('\033[1;34;40mDigite ID motorista:\033[m ')
            id_motorista = self.valida_id(id_motorista)
            placa = str(input('\033[1;34;40mDigite uma placa no formato BRA1566/BRA2A18:\033[m '))
            placa = self.valida_placa(placa).upper()
            linha = str(input('\033[1;34;40mDigite o numero da linha com 3 digitos:\033[m '))
            linha = self.valida_linha(linha)
            modelo = str(input('\033[1;34;40mDigite o modelo:\033[m '))
            modelo = self.valida_string(modelo).capitalize()
            ano = str(input('\033[1;34;40mDigite o ano:\033[m '))
            ano = self.valida_ano(ano)
            o = Onibus(id_motorista, placa, linha, modelo, ano)
            cnx = conecta()
            csr = cnx.cursor()
            try:
                sql = f""" INSERT INTO jaelson_matias.ONIBUS (id_motorista, placa, linha, modelo, ano)
                                                VALUES ('{o.id_motorista}', '{o.num_placa}', '{o.num_linha}', '{o.modelo}', '{o.ano}'); """

                csr.execute(sql)
            except pyodbc.DatabaseError:
                time.sleep(0.8)
                print('\033[1;34;40mFalha ao cadastrar um ônibus, verifique se o ID ou os dados estão válidos!!\033[m')
                time.sleep(0.8)
                continue

            else:
                cnx.commit()
                print('\033[1;34;40mCadastrando...\033[m')
                time.sleep(0.8)
                print('\033[1;34;40mFinalizando cadastro...\033[m')
                time.sleep(0.8)
                print('\033[1;34;40mCadastro realizado com sucesso!!\033[m\n')
                cnx.close()
                break

    def visualizar_usuario(self):
        """
            Esta função visualiza um cadastro de usuário
        """
        cnx = conecta()
        sql = f"SELECT id_usuario, nome, sobrenome, email, bairro, FORMAT(data_nascimento, 'dd/MM/yyyy') as dt_nasc FROM jaelson_matias.USUARIO;"
        df = pd.read_sql(sql, cnx)
        print(df)

    def visualizar_motorista(self):
        """
            Esta função visualiza um cadastro de motorista
        """
        cnx = conecta()
        sql = f"SELECT id_motorista, nome, sobrenome, num_cnh, FORMAT(data_nascimento, 'dd/MM/yyyy') as data_nascimento FROM jaelson_matias.MOTORISTA;"
        df = pd.read_sql(sql, cnx)
        print(df)

    def visualizar_cartao(self):
        """
            Esta função visualiza um cadastro de cartão
        """
        cnx = conecta()
        sql = f"SELECT id_cartao, id_proprietario, credito, tipo, FORMAT(data_emissao, 'dd/MM/yyyy') as data_emissao FROM jaelson_matias.CARTAO;"
        df = pd.read_sql(sql, cnx)
        print(df)

    def visualizar_onibus(self):
        """
            Esta função visualiza um cadastro de ônibus
        """
        cnx = conecta()
        sql = f"SELECT id_onibus, id_motorista, placa, linha, modelo, FORMAT(ano, 'yyyy') as ano FROM jaelson_matias.ONIBUS;"
        df = pd.read_sql(sql, cnx)
        print(df)
