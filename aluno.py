import base
class Aluno():
	def __init__(self, nome_aluno, cpf_aluno):
		self.nome_aluno = nome_aluno
		self.cpf_aluno = cpf_aluno
		while True:
			print("1 - Ver notas")
			print("2 - Ver recados")
			print("3 - Sair")
			opcoes_aluno = int(input("Selecione uma opção:"))
			if opcoes_aluno == 1:
				self.ver_nota_aluno()
			if opcoes_aluno ==2:
				self.ver_recados()
			if opcoes_aluno == 3:
				break
			if opcoes_aluno > 3 or opcoes_aluno < 1:
				print("Opção Invalida")
	def ver_nota_aluno(self):
		comando = f'SELECT disciplina ,tipo_avaliacao,nota FROM avaliacoes WHERE cpf_aluno = "{self.cpf_aluno}"'
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

	def ver_recados(self):

		comando = f'SELECT nome_professor FROM recado WHERE cpf_receptor = "{self.cpf_aluno}"'
		conexao = base.obter_conexao()
		cursor = conexao.cursor()
		cursor.execute(comando)
		remetente_recado = cursor.fetchall()
		print("Remetente:",remetente_recado)
		cursor.close()
		conexao.close()

		comando = f'SELECT titulo_recado FROM recado WHERE cpf_receptor = "{self.cpf_aluno}"'
		conexao = base.obter_conexao()
		cursor = conexao.cursor()
		cursor.execute(comando)
		titulo_recado = cursor.fetchall()
		print("Titulo:", titulo_recado)
		cursor.close()
		conexao.close()

		comando = f'SELECT recado FROM recado WHERE cpf_receptor = "{self.cpf_aluno}"'
		conexao = base.obter_conexao()
		cursor = conexao.cursor()
		cursor.execute(comando)
		resultado = cursor.fetchall()
		cursor.close()
		conexao.close()
		input("Pressione qualquer tecla para continuar...")