import mysql.connector

def get_db_connection():
    config = {
        'user': 'admin',
        'password': '1234',
        'host': 'localhost',
        'database': 'resta'
    }
    return mysql.connector.connect(**config)
