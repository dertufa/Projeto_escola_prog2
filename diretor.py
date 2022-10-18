
import base



class Diretor:

	def __init__(self):
		print("1 - Cadastrar Aluno")
		print("2 - Ver Nota de Aluno")
		opcoes_diretor = int(input("Selecione uma opção:"))

		self.opcoes_diretor = opcoes_diretor
		if self.opcoes_diretor == 1:
			self.cadastrar_aluno()
		if self.opcoes_diretor == 2:
			self.ver_nota_diretor()

	def cadastrar_aluno(self):
		aluno_cadastro = input("Insira o nome do aluno:")
		responsavel_cadastro = input("Insira o nome do responsável")
		cpf_cadastro_aluno = input("Insira o cpf do aluno")
		comando = f'INSERT INTO aluno (nome_aluno, responsavel_aluno, cpf_aluno) VALUES ("{aluno_cadastro}", "{responsavel_cadastro}", "{cpf_cadastro_aluno}")'
		conexao = base.obter_conexao()
		cursor = conexao.cursor()
		cursor.execute(comando)
		conexao.commit()
		cursor.close()
		conexao.close()



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