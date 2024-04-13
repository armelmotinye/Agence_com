import mysql.connector as mysql

def connection_db():
    return mysql.connect(
        user='root',
        host='localhost',
        password='',
        database='agence'
    )