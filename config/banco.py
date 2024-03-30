import os
from dotenv import load_dotenv

load_dotenv()

def conexao_postgresql():

    host = os.getenv('host_db_postgresql')
    name = os.getenv('name_db_postgresql')
    user = os.getenv('user_postgresql')
    password = os.getenv('password_postgresql')
    # sslmode = os.getenv('sslmode_postgresql')

    conn_string_postgresql = 'host={0} user={1} dbname={2} password={3}'.format(host,name,user,password)
    
    return conn_string_postgresql