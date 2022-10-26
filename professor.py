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
				print("3 - Sair")
				opcoes_professor = int(input("Selecione uma opção:"))
				if opcoes_professor == 1:
					Professor.inserir_nota(self)
				if opcoes_professor == 2:
					Professor.ver_nota_professor(self)
				if opcoes_professor == 3:
					break
				if opcoes_professor >4 or opcoes_professor<1:
					print("Opção Invalida")

	def ver_nota_professor(self):
		conexao = base.obter_conexao()
		cursor = conexao.cursor()
		comando = f'SELECT * FROM avaliacoes WHERE disciplina = "{self.disciplina_professor}" '
		cursor.execute(comando)
		resultado = cursor.fetchall()  # Ler o banco de dados
		print("=======================================================")
		print("Aluno            Disciplina          Avaliação       Nota")
		print("=======================================================")

		for i in resultado:
			lista = list(i)
			print(lista[1], " ", lista[2], "   ", lista[3], "     ", lista[4])
			print("=====================================================")
		cursor.close()
		conexao.close()
		input("Pressione qualquer tecla para continuar...")
	def inserir_nota(self):
		conexao = base.obter_conexao()
		cursor = conexao.cursor()
		comando = f'SELECT * FROM aluno'
		cursor.execute(comando)
		resultado = cursor.fetchall()
		print("=========================================")
		print("Índice / Aluno   /        CPF")
		print("=========================================")
		for i in resultado:
			lista = list(i)
			print("  ", lista[0], " ", lista[1], "   ", lista[2])
			print("=========================================")
		cursor.close()
		conexao.close()
		p_seleciona_aluno = int(input("Selecione o aluno pelo indice para inserir uma nota:"))

		conexao = base.obter_conexao()
		cursor = conexao.cursor()
		comando = f'SELECT * FROM aluno WHERE id_aluno = "{p_seleciona_aluno}"'
		cursor.execute(comando)
		aluno_inserir_nota = cursor.fetchone()
		nome_aluno_inserir_nota = aluno_inserir_nota[1]
		cpf_aluno_inserir_nota = aluno_inserir_nota[2]
		cursor.close()
		conexao.close()


		print("1 - Prova")
		print("2 - Teste")
		print("3 - Trabalho")
		tipo_avaliacao =0
		escolhe_tipo_avaliacao = int(input("Selecione o tipo da avaliação:"))
		if escolhe_tipo_avaliacao ==1:
			tipo_avaliacao = "prova"
		elif escolhe_tipo_avaliacao ==2:
			tipo_avaliacao = "teste"
		elif escolhe_tipo_avaliacao ==3:
			tipo_avaliacao = "trabalho"
		while True:
			p_nota_aluno = float(input("Insira a nota desse aluno:"))
			if p_nota_aluno >10 or p_nota_aluno<0:
				print("Valor Invalido!!!")
			else:
				break
		comando = f'INSERT INTO avaliacoes (nome_aluno, disciplina,tipo_avaliacao ,nota, cpf_aluno) VALUES ("{nome_aluno_inserir_nota}", "{self.disciplina_professor}", "{tipo_avaliacao}" ,"{p_nota_aluno}","{cpf_aluno_inserir_nota}")'
		conexao = base.obter_conexao()
		cursor = conexao.cursor()
		cursor.execute(comando)
		conexao.commit()
		cursor.close()
		conexao.close()
		input("Nota inserida! pressione qualquer tecla para continuar...")
