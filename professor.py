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
			print("4 - Voltar ao menu de login")
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
		comando = f'SELECT id_avaliacoes AND nome_aluno AND disciplina AND nota FROM avaliacoes WHERE disciplina = "{self.disciplina_professor}"'
		cursor.execute(comando)
		resultado = cursor.fetchall()  # Ler o banco de dados
		print("=========================================")
		print("Indice   Aluno           Disciplina  Nota")
		print("=========================================")

		for i in resultado:
			print(i)
			print("=========================================")
		cursor.close()
		conexao.close()


	def inserir_nota(self):
		conexao = base.obter_conexao()
		cursor = conexao.cursor()
		comando = f'SELECT * FROM aluno'
		cursor.execute(comando)
		resultado = cursor.fetchall()
		print("=========================================")
		print("Índice / Aluno / Responsável")
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

		p_nota_aluno = float(input("Insira a nota desse aluno:"))
		comando = f'INSERT INTO avaliacoes (nome_aluno, id_disciplina,nota, id_aluno) VALUES ("{nome_aluno_inserir_nota}", "{self.disciplina_professor}","{p_nota_aluno}","{p_seleciona_aluno}")'
		conexao = base.obter_conexao()
		cursor = conexao.cursor()
		cursor.execute(comando)
		conexao.commit()
		cursor.close()
		conexao.close()
