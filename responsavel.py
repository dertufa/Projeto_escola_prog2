class Responsavel:
	def __init__(self, nome_responsavel_aluno, cpf_responsavel_aluno):
		self.nome_responsavel_aluno= nome_responsavel_aluno
		self.cpf_responsavel_aluno = cpf_responsavel_aluno
		while True:
			print("1 - Ver notas")
			print("2 - Ver recados")
			print("3 - Sair")
			opcoes_aluno = int(input("Selecione uma opção:"))
			if opcoes_aluno == 1:
				self.ver_nota_aluno()
			if opcoes_aluno == 2:
				self.ver_recados()
			if opcoes_aluno == 3:
				break

	def ver_nota_aluno(self):
		comando = f'SELECT disciplina ,tipo_avaliacao,nota FROM avaliacoes WHERE cpf_responsavel_aluno = "{self.cpf_responsavel_aluno}"'
		conexao = base.obter_conexao()
		cursor = conexao.cursor()
		cursor.execute(comando)
		resultado = cursor.fetchall()
		print("=========================================")
		print("    Disciplina  /   Tipo   /    Nota    ")
		print("=========================================")
		for i in resultado:
			print(i)
			print("=========================================")
		cursor.close()
		conexao.close()
		input("Pressione qualquer tecla para continuar...")