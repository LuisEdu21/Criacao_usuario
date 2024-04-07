import json
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

    return response.text

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

def Inserir_usuario(conn_postgresql, cursor_postgresql, sexo,name_first,name_last,city,state,country,email,date,age):

    sql = """INSERT INTO teste.cliente_teste
(name_first, name_last, city, state, country, email, data_nascimento, age)
VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', {})""".format(name_first,name_last,city,state,country,email,date,age)

    cursor_postgresql.execute(sql)
    conn_postgresql.commit()

    return

def run():

    conn_postgresql = Abrir_conexao()
    cursor_postgresql = conn_postgresql.cursor()

    criar_tabela(conn_postgresql=conn_postgresql,cursor_postgresql=cursor_postgresql)

    usuario = usuarios()
    usuario_json = json.loads(usuario)

    resultado = usuario_json['results']
    sexo = resultado[0]['gender']
    name = resultado[0]['name']
    name_first = name['first']
    name_last = name['last']
    location = resultado[0]['location']
    city = location['city']
    state = location['state']
    country = location['country']
    email = resultado[0]['email']
    dob = resultado[0]['dob']
    date = dob['date']
    age = dob['age']

    Inserir_usuario(conn_postgresql, cursor_postgresql, sexo,name_first,name_last,city,state,country,email,date,age)

    return

run()