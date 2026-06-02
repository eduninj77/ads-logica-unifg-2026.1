class Estudante:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.notas = []

    def adicionar_nota(self, nota):
        self.notas.append(nota)

    def calcular_media(self):
        if not self.notas:
            return 0
        return sum(self.notas) / len(self.notas)

aluno = Estudante("Ana", "202601")
aluno.adicionar_nota(8.0)
aluno.adicionar_nota(10.0)
print(aluno.calcular_media())