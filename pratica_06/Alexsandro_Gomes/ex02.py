class Estudante:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.notas = []

aluno = Estudante("Ana", "202601")
print(aluno.nome)
print(aluno.notas)