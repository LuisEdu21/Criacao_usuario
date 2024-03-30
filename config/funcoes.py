import requests
import psycopg2
import banco

#Banco

def Abrir_conexao():

    String_conexao = banco.conexao_postgresql()
    conn_postgresql = psycopg2.connect(String_conexao)

    return conn_postgresql

def Fecha_conexao(conn_postgresql, cursor_postgresql):

    cursor_postgresql.close()
    conn_postgresql.close()

    return

def usuario():
    url = "https://randomuser.me/api/"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)

    return

def run():

    conn_postgresql = Abrir_conexao()
    cursor_postgresql = conn_postgresql.cursor()

    # Execute uma consulta SQL para obter a versão do banco de dados
    cursor_postgresql.execute('SELECT version()')

    # Recupere o resultado da consulta
    versao = cursor_postgresql.fetchone()

    # Imprima a versão do banco de dados
    print('Versão do banco de dados:', versao[0])


    return

run()