#import os
from base import obter_conexao
#import MySQLdb
from responsavel import Responsavel
from professor import Professor
from diretor import Diretor


while True:

	print("1 - Aluno")
	print("2 - Responsavel")
	print("3 - Professor")
	print("4 - Diretor")
	print("5 - Sair")
	escolhe_login = int(input("Selecione o tipo de login:"))

	if escolhe_login == 1:
		nome_login_aluno = input("Digite o seu nome ")
		nome_login_aluno = nome_login_aluno.lower()
		cpf_login_aluno = input("Digite o seu CPF")
		conexao = obter_conexao()
		cursor = conexao.cursor()


	if escolhe_login == 2:
		while True:
			nome_login_responsavel = input("Digite seu nome:")
			nome_login_responsavel = nome_login_responsavel.lower()
			cpf_login_reponsavel = input("Digite seu cpf:")

			conexao = obter_conexao()
			cursor = conexao.cursor()
			comando = 'SELECT nome_responsavel, cpf_responsavel FROM responsavel'
			cursor.execute(comando)
			resultado = cursor.fetchall()
			cursor.close()
			conexao.close()
			for i in range(len(resultado)):
				if nome_login_responsavel in resultado[i] and cpf_login_reponsavel in resultado[i]:
					r = Responsavel()

	if escolhe_login == 3:
		while True:
			print("Login Professor")
			nome_login_professor = input("Digite seu nome:")
			senha_login_professor = input("Digite sua senha:")
			conexao = obter_conexao()
			cursor = conexao.cursor()
			comando = 'SELECT nome_professor, senha_professor FROM professor'
			cursor.execute(comando)
			resultado = cursor.fetchall()
			cursor.close()
			conexao.close()
			for i in range(len(resultado)):
				if nome_login_professor in resultado[i] and senha_login_professor in resultado[i]:
					print("Login efetuado com sucesso")
					conexao = obter_conexao()
					cursor = conexao.cursor()
					comando = f'SELECT disciplina FROM professor WHERE nome_professor = "{nome_login_professor}"'
					cursor.execute(comando)
					disciplina = cursor.fetchall()
					cursor.close()
					conexao.close()
					p = Professor(nome_login_professor, senha_login_professor,disciplina)
				else:
					print("Login incorreto")
			break



	if escolhe_login == 4:
		while True:
			usuario_diretor = input("Digite seu usuario:")
			usuario_diretor = usuario_diretor.lower()
			senha_diretor = int(input("Digite sua senha:"))
			if usuario_diretor == "diretor" and senha_diretor == 123:
				d = Diretor()
			else:
				print("Login Invalido!")
			break
	if escolhe_login == 5:
		break

