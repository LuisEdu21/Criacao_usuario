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

def usuarios():
    url = "https://randomuser.me/api/"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)

    return

def tabela_existe(cursor_postgresql):
    
    sql = """
    SELECT EXISTS (
        SELECT 1
        FROM information_schema.tables 
        WHERE table_name = 'cliente_teste'
    );
    """
    cursor_postgresql.execute(sql)
    return cursor_postgresql.fetchone()[0]

def criar_tabela(conn_postgresql, cursor_postgresql):

    tabela = """
    CREATE TABLE teste.cliente_teste (
        id serial4 NOT NULL,
        name_first varchar NULL,
        name_last varchar NULL,
        city varchar NULL,
        state varchar NULL,
        country varchar NULL,
        email varchar NULL,
        data_nascimento timestamp NULL,
        age int NULL
    );
    """

    if tabela_existe(cursor_postgresql):
        return 'A tabela já existe'
    else:
        cursor_postgresql.execute(tabela)
        conn_postgresql.commit()
        return 'Tabela criada'

def run():

    conn_postgresql = Abrir_conexao()
    cursor_postgresql = conn_postgresql.cursor()

    criar_tabela(conn_postgresql=conn_postgresql,cursor_postgresql=cursor_postgresql)

    usuario = usuarios()

    return
