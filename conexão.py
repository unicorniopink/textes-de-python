import mysql.connector

def criar_conexão(host,user,password,database):
    return mysql.conector.connect(host=host, user=usuario, password=senha, database=banco)
def fechar_conexão(con):
    return con.close()
