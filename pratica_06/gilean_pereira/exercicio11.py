class Turma:
    def __init__(self):
        self.estudantes = []

    def adicionar_estudante(self, estudante):
        self.estudantes.append(estudante)


    def listar_estudantes(self):
        for est in self.estudantes:
            print(f"Nome: {est}")


minha_turma = Turma()
minha_turma.adicionar_estudante("Ana")
minha_turma.adicionar_estudante("Bruno")
minha_turma.adicionar_estudante("Carlos")

minha_turma.listar_estudantes()