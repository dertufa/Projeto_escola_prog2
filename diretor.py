
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

			if self.opcoes_diretor == 3:
				break
			if self.opcoes_diretor > 3 or self.opcoes_diretor < 1:
				print("Opção Invalida")

	def cadastrar_aluno(self):
		nome_aluno_cadastro = input("Insira o nome do aluno:")
		cpf_cadastro_aluno = input("Insira o CPF do aluno:")
		nome_responsavel_cadastro = input("Insira o nome do responsável:")
		cpf_responsavel_cadastro = input("Insira o CPF do responsavel:")

		#cadastra as infromações na tabela aluno
		comando = f'INSERT INTO aluno (nome_aluno, cpf_aluno, nome_responsavel_aluno, cpf_responsavel_aluno) VALUES ("{nome_aluno_cadastro}", "{cpf_cadastro_aluno}", "{nome_responsavel_cadastro}","{cpf_responsavel_cadastro}")'
		conexao = base.obter_conexao()
		cursor = conexao.cursor()
		cursor.execute(comando)
		conexao.commit()
		cursor.close()
		conexao.close()
		input("Aluno Cadastrado com sucesso, pressione qualquer tecla para continuar...")

		#cadastra as informações na tabela responsavel
		comando = f'INSERT INTO responsavel (nome_responsavel,cpf_responsavel, aluno_responsavel) VALUES ("{nome_responsavel_cadastro}", "{cpf_responsavel_cadastro}", "{nome_aluno_cadastro}")'
		conexao = base.obter_conexao()
		cursor = conexao.cursor()
		cursor.execute(comando)
		conexao.commit()
		cursor.close()
		conexao.close()

	def ver_nota_diretor(self):
		conexao = base.obter_conexao()
		cursor = conexao.cursor()
		comando = f'SELECT id_aluno, nome_aluno , cpf_aluno  ,nome_responsavel_aluno FROM aluno'
		cursor.execute(comando)
		resultado = cursor.fetchall()
		print("=========================================")
		print("Índice / Aluno /     CPF     /    Responsável")
		print("=========================================")
		for i in resultado:
			lista = list(i)
			print("  ",lista[0]," " ,lista[1],"   " , lista[2],"   " ,lista[3])
			print("=========================================")
		cursor.close()
		conexao.close()

		cpf_consulta_diretor = input("Digite o CPF do aluno que você deseja ver a nota:")
		disciplina_consulta_diretor = input("Digite o nome da  disciplina que você deseja ver a nota ")
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
		comando = f'SELECT * FROM avaliacoes WHERE cpf_aluno ="{cpf_consulta_diretor}"'
		cursor.execute(comando)
		resultado = cursor.fetchall()
		print(resultado)
		cursor.close()
		conexao.close()
	
	def remover_aluno(self):

		conexao = base.obter_conexao()
		cursor = conexao.cursor()
		comando = f'SELECT (id_aluno, nome_aluno , cpf_aluno , nome_responsavel_aluno) FROM aluno'
		cursor.execute(comando)
		resultado = cursor.fetchall()
		print("=========================================")
		print("Índice / Aluno / CPF / Responsável")
		print("=========================================")
		for i in resultado:
			print(i)
			print("=========================================")
		cursor.close()
		conexao.close()
		diretor_deleta = input("Digite o indice do aluno a ser EXCLUIDO:")
		
		conexao = base.obter_conexao()
		cursor = conexao.cursor()
		comando = f'SELECT cpf_aluno FROM aluno WHERE id_aluno = "{diretor_deleta}"'
		cursor.execute(comando)
		aluno_deletado = cursor.fetchall()
		cursor.close()
		conexao.close()
		
		#Deleta o aluno da tabela aluno
		conexao = base.obter_conexao()
		cursor = conexao.cursor()
		comando = f'DELETE * FROM aluno WHERE cpf_aluno = "{aluno_deletado}"'
		cursor.execute(comando)
		conexao.commit()
		#falta colocar a parte de verificar se ele excluiu mesmo 
		cursor.close()
		conexao.close()






	'''
	def mandar_recado(self):
		conexao = base.obter_conexao()
		cursor = conexao.cursor()
		comando = f'SELECT id_aluno, nome_aluno , cpf_aluno , nome_responsavel_aluno FROM aluno'
		cursor.execute(comando)
		resultado = cursor.fetchall()
		print("=========================================")
		print("Índice / Aluno / CPF / Responsável")
		print("=========================================")
		for i in resultado:
			print(i)
			print("=========================================")
		cursor.close()
		conexao.close()
		diretor_recado = input("Digite o indice do aluno para enviar um recado:")
		print("1 - Aluno")
		print("2 - Responsavel")
		escolhe_recado = int(input("Quem ira receber o recado?:"))
		titulo_recado = input("Digite o titulo do recado:")
		texto_recado = input("Digite o recado(limite de 144 characteres):")

		if escolhe_recado ==1:
			conexao = base.obter_conexao()
			cursor = conexao.cursor()
			comando = f'SELECT nome_aluno  FROM aluno WHERE id_aluno = "{diretor_recado}"'
			cursor.execute(comando)
			nome_aluno_receptor = cursor.fetchall()
			cursor.close()
			conexao.close()

			conexao = base.obter_conexao()
			cursor = conexao.cursor()
			comando = f'SELECT cpf_aluno  FROM aluno WHERE id_aluno = "{diretor_recado}"'
			cursor.execute(comando)
			cpf_aluno_receptor = cursor.fetchall()
			cursor.close()
			conexao.close()

			comando = f'INSERT INTO recado (nome_aluno,nome_professor, titulo_recado, recado, cpf_receptor) VALUES ( "{nome_aluno_receptor}", "diretor", "{titulo_recado}","{texto_recado}","{cpf_aluno_receptor}")'
			conexao = base.obter_conexao()
			cursor = conexao.cursor()
			cursor.execute(comando)
			conexao.commit()
			cursor.close()
			conexao.close()

		if escolhe_recado ==2:
			conexao = base.obter_conexao()
			cursor = conexao.cursor()
			comando = f'SELECT nome_aluno  FROM aluno WHERE id_aluno = "{diretor_recado}"'
			cursor.execute(comando)
			nome_responsavel_receptor = cursor.fetchall()
			cursor.close()
			conexao.close()

			conexao = base.obter_conexao()
			cursor = conexao.cursor()
			comando = f'SELECT cpf_aluno  FROM aluno WHERE id_aluno = "{diretor_recado}"'
			cursor.execute(comando)
			cpf_responsavel_receptor = cursor.fetchall()
			cursor.close()
			conexao.close()


			comando = f'INSERT INTO recado (nome_aluno,nome_professor, titulo_recado, recado, cpf_receptor) VALUES ( "{nome_responsavel_receptor}", "diretor", "{titulo_recado}","{texto_recado}","{cpf_responsavel_receptor}")'
			conexao = base.obter_conexao()
			cursor = conexao.cursor()
			cursor.execute(comando)
			conexao.commit()
			cursor.close()
			conexao.close()
	'''