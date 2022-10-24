import base
class Professor():

	def __init__(self, nome_professor, senha_professor, disciplina_professor):
		self.nome_professor = nome_professor
		self.senha_professor = senha_professor
		self.disciplina_professor = disciplina_professor
		while True:
			Professor.meunu_professor(self)
			break

	def meunu_professor(self):
		while True:
			print("1 - Inserir as notas dos alunos")
			print("2 - Ver as notas dos alunos")
			print("3 - Enviar recado para um responsavel")
			print("4 - Sair")
			opcoes_professor = int(input("Selecione uma opção:"))
			if opcoes_professor == 1:
				Professor.inserir_nota(self)
			if opcoes_professor == 2:
				Professor.ver_nota_professor(self)
			if opcoes_professor == 4:
				break

	def ver_nota_professor(self):
		conexao = base.obter_conexao()
		cursor = conexao.cursor()
		comando = f'SELECT id_avaliacoes , nome_aluno , disciplina ,tipo_avaliacao, nota FROM avaliacoes WHERE disciplina = "{self.disciplina_professor}"'
		cursor.execute(comando)
		resultado = cursor.fetchall()  # Ler o banco de dados
		print("=======================================================")
		print("Indice   Aluno           Disciplina     Avaliação  Nota")
		print("=======================================================")

		for i in resultado:
			print(i)
			print("=========================================")
		cursor.close()
		conexao.close()
		input("Pressione qualquer tecla para continuar...")

	def inserir_nota(self):
		conexao = base.obter_conexao()
		cursor = conexao.cursor()
		comando = f'SELECT id_aluno , nome_aluno,  cpf_aluno FROM aluno'
		cursor.execute(comando)
		resultado = cursor.fetchall()
		print("=========================================")
		print("Índice / Aluno / CPF")
		print("=========================================")
		for i in resultado:
			print(i)
			print("=========================================")
		cursor.close()
		conexao.close()
		p_seleciona_aluno = int(input("Selecione o aluno pelo indice para inserir uma nota:"))

		conexao = base.obter_conexao()
		cursor = conexao.cursor()
		comando = f'SELECT nome_aluno FROM aluno WHERE id_aluno = "{p_seleciona_aluno}"'
		cursor.execute(comando)
		nome_aluno_inserir_nota = cursor.fetchall()
		cursor.close()
		conexao.close()


		print("1 - Prova")
		print("2 - Teste")
		print("3 - Trabalho")
		escolhe_tipo_avaliacao = int(input("Selecione o tipo da avaliação"))
		if escolhe_tipo_avaliacao ==1:
			tipo_avaliacao = "prova"
		elif escolhe_tipo_avaliacao ==2:
			tipo_avaliacao = "teste"
		elif escolhe_tipo_avaliacao ==3:
			tipo_avaliacao = "trabalho"

		p_nota_aluno = float(input("Insira a nota desse aluno:"))
		comando = f'INSERT INTO avaliacoes (nome_aluno, disciplina,tipo_avaliacao ,nota) VALUES ("{nome_aluno_inserir_nota}", "{self.disciplina_professor}","{tipo_avaliacao}","{p_nota_aluno}")'
		conexao = base.obter_conexao()
		cursor = conexao.cursor()
		cursor.execute(comando)
		conexao.commit()
		cursor.close()
		conexao.close()
		input("Nota inserida! pressione qualquer tecla para continuar...")
