class Estudante:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.notas = []

    def adicionar_nota(self, nota):
        self.notas.append(nota)

    def calcular_media(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)


aluno1 = Estudante("Carlos", "2026001")
aluno2 = Estudante("Beatriz", "2026002")


aluno1.adicionar_nota(9.0)
aluno1.adicionar_nota(8.0)

aluno2.adicionar_nota(5.0)
aluno2.adicionar_nota(6.0)


print(f"Estudante 1: {aluno1.nome} | Notas: {aluno1.notas} | Média: {aluno1.calcular_media()}")
print(f"Estudante 2: {aluno2.nome} | Notas: {aluno2.notas} | Média: {aluno2.calcular_media()}")