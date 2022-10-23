
import base



class Diretor:

	def __init__(self):
		while True:
			print("1 - Cadastrar Aluno")
			print("2 - Ver Nota de Aluno")
			print("3 - Sair")
			opcoes_diretor = int(input("Selecione uma opção:"))

			self.opcoes_diretor = opcoes_diretor
			if self.opcoes_diretor == 1:
				self.cadastrar_aluno()
			if self.opcoes_diretor == 2:
				self.ver_nota_diretor()
			if opcoes_diretor ==3:
				break

	def cadastrar_aluno(self):
		nome_aluno_cadastro = input("Insira o nome do aluno:")
		cpf_cadastro_aluno = input("Insira o CPF do aluno:")

		#cadastra as infromações na tabela aluno
		comando = f'INSERT INTO aluno (nome_aluno, cpf_aluno, nome_responsavel_aluno, cpf_responsavel_aluno) VALUES ("{nome_aluno_cadastro}", "{cpf_cadastro_aluno}", "{nome_responsavel_cadastro}","{cpf_responsavel_cadastro}")'
		conexao = base.obter_conexao()
		cursor = conexao.cursor()
		cursor.execute(comando)
		conexao.commit()
		cursor.close()
		conexao.close()
		input("Aluno Cadastrado com sucesso, pressione qualquer tecla para continuar...")

		nome_responsavel_cadastro = input("Insira o nome do responsável:")
		cpf_responsavel_cadastro = input("Insira o CPF do responsavel:")
		#cadastra as informações na tabela responsavel
		comando = f'INSERT INTO responsavel (nome_responsavel,cpf_responsavel, aluno_responsavel) VALUES ("{nome_responsavel_cadastro}", "{cpf_responsavel_cadastro}", "{nome_aluno_cadastro}")'
		conexao = base.obter_conexao()
		cursor = conexao.cursor()
		cursor.execute(comando)
		conexao.commit()
		cursor.close()
		conexao.close()
		input("Responsavel Cadastrado com sucesso, pressione qualquer tecla para continuar...")

	def ver_nota_diretor(self):
		conexao = base.obter_conexao()
		cursor = conexao.cursor()
		comando = f'SELECT * FROM aluno'
		cursor.execute(comando)
		resultado = cursor.fetchall()
		print("=========================================")
		print("Índice / Aluno / Responsável / CPF")
		print("=========================================")
		for i in resultado:
			print(i)
			print("=========================================")
		cpf_consulta_diretor = input("Digite o CPF do aluno que você deseja ver a nota:")
		disciplina_consulta_diretor = input("Digite o nome da  disciplina que você deseja ver a nota ")
		cursor.close()
		conexao.close()

		disciplina_consulta_diretor = disciplina_consulta_diretor.lower()

		conexao = base.obter_conexao()
		cursor = conexao.cursor()
		comando = f'SELECT nome_aluno FROM aluno WHERE id_aluno = "{cpf_consulta_diretor}"'
		cursor.execute(comando)
		nome_consulta_diretor = cursor.fetchall()
		cursor.close()
		conexao.close()

		conexao = base.obter_conexao()
		cursor = conexao.cursor()
		comando = f'SELECT * FROM avaliacoes WHERE cpf_aluno ="{cpf_consulta_diretor}" AND id_disciplina = "{disciplina_consulta_diretor}"'
		cursor.execute(comando)
		resultado = cursor.fetchall()
		print(resultado)
		cursor.close()
		conexao.close()

	#def adicionar_disciplinas(self):
	#	comando = f'INSERT INTO aluno (nome_aluno, responsavel_aluno, disciplinas_aluno) VALUES ("{aluno_cadastro}", "{responsavel_cadastro}", "{disciplinas_cadastro}")'
	#	conexao = base.obter_conexao()
	#	cursor = conexao.cursor()
	#	cursor.execute(comando)
	#	conexao.commit()
	#	cursor.close()
	#	conexao.close()