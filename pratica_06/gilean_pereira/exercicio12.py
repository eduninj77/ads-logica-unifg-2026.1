class Estudante:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

class Turma:
    def __init__(self):
        self.estudantes = []

    def adicionar_estudante(self, estudante):
        self.estudantes.append(estudante)

    def listar_detalhes(self):
        for est in self.estudantes:
            print(f"Estudante: {est.nome} | Matrícula: {est.matricula}")

aluno1 = Estudante("Diana", "202601")
aluno2 = Estudante("Eduardo", "202602")

turma_ti = Turma()
turma_ti.adicionar_estudante(aluno1)
turma_ti.adicionar_estudante(aluno2)

turma_ti.listar_detalhes()