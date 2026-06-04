class Estudante:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

aluno = Estudante("Ana", "202601")
print(aluno.nome)
print(aluno.matricula)