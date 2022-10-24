import base
class Aluno():
	def __init__(self,nome_aluno ,cpf_aluno):
		self.nome_aluno = nome_aluno
		self.cpf_aluno = cpf_aluno
		while True:
			print("1 - Ver notas")
			print("2 - Ver recados")
			print("3 - Sair")
			opcoes_aluno = input("Selecione uma opção:")
			if opcoes_aluno == 1:
				self.ver_nota_aluno()
			if opcoes_aluno ==3:
				break
	def ver_nota_aluno (self):
		conexao = base.obter_conexao()
		cursor = conexao.cursor()
		comando = f'SELECT (disciplina , tipo_avaliacao , nota) FROM avaliacoes WHERE cpf_aluno = "{self.cpf_aluno}"'
		cursor.execute(comando)
		resultado = cursor.fetchall()
		print("=========================================")
		print("    Disciplina  /   Tipo   /    Nota    ")
		print("=========================================")
		for i in resultado:
			print(i)
			print("=========================================")
		input("Pressione qualquer tecla para continuar...")