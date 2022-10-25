import MySQLdb

def obter_conexao():
    # conexao = mysql.connector.connect(user="root", passwd="#Serelepe123", db="escola")
    conexao = MySQLdb.connector.connect(user="root", passwd="#Serelepe123", db="escola")
    return conexao
