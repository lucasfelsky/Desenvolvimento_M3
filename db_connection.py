import mysql.connector
from mysql.connector import Error

def create_db_connection():
    
    connection = None
    try:
        connection = mysql.connector.connect(
            host="localhost",      
            user="root",           
            password="root",  
            database="banco"       
        )
        if connection.is_connected():
            print("Conexão com o banco de dados estabelecida com sucesso.")
        return connection
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None

def close_db_connection(connection):
    
    if connection and connection.is_connected():
        connection.close()
        print("Conexão com o banco de dados fechada.")