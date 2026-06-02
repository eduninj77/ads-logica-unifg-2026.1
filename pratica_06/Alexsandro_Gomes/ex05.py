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

aluno1 = Estudante("Ana", "202601")
aluno2 = Estudante("Bruno", "202602")

aluno1.adicionar_nota(9.0)
aluno2.adicionar_nota(6.0)

print(aluno1.nome, aluno1.calcular_media())
print(aluno2.nome, aluno2.calcular_media())