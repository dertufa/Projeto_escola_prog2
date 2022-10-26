import base
class Responsavel:
	def __init__(self, nome_responsavel_aluno, cpf_responsavel_aluno):
		self.nome_responsavel_aluno= nome_responsavel_aluno
		self.cpf_responsavel_aluno = cpf_responsavel_aluno
		while True:
			print("1 - Ver notas")
			print("2 - Sair")
			opcoes_aluno = int(input("Selecione uma opção:"))
			if opcoes_aluno == 1:
				self.ver_nota_aluno()
			if opcoes_aluno == 2:
				break
			if opcoes_aluno > 2 or opcoes_aluno < 1:
				print("Opção Invalida")
	def ver_nota_aluno(self):
		comando = f'SELECT * FROM avaliacoes WHERE cpf_responsavel_aluno = "{self.cpf_responsavel_aluno}"'
		conexao = base.obter_conexao()
		cursor = conexao.cursor()
		cursor.execute(comando)
		resultado = cursor.fetchall()
		print("=========================================")
		print("    Disciplina  /   Tipo   /    Nota    ")
		print("=========================================")
		for i in resultado:
			lista = list(i)
			print("  ", lista[2], " ", lista[3], "   ", lista[4])
			print("=========================================")
		cursor.close()
		conexao.close()
		input("Pressione qualquer tecla para continuar...")

	#e se o mesmo responsavel tiver mais de um dependente cadastrado?