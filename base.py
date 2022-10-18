import MySQLdb


def obter_conexao():
    conexao = MySQLdb.connect(user="root", passwd="#Serelepe123", db="escola")
    return conexao
