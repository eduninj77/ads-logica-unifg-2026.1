class Estudante:
    def __init__(self, nome):
        self.nome = nome

class Turma:
    def __init__(self):
        self.estudantes = []

    def matricular(self, estudante):
        self.estudantes.append(estudante)

t = Turma()
aluno = Estudante("Carlos")
t.matricular(aluno)
print(t.estudantes[0].nome)