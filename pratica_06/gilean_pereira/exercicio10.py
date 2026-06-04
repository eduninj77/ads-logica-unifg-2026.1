class Turma:
    def __init__(self):
        self.students = [] 

    def adicionar_estudante(self, estudante):
        self.students.append(estudante)

minha_turma = Turma()
minha_turma.adicionar_estudante("Ana")
minha_turma.adicionar_estudante("Bruno")

print(f"Lista de estudantes na turma: {minha_turma.students}")