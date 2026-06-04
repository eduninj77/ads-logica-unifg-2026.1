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

    def situacao(self):
        media = self.calcular_media()
        if media >= 7:
            return "Aprovado"
        else:
            return "Recuperação"

aluno = Estudante("Carlos", "2026001")
aluno.adicionar_nota(8.5)
aluno.adicionar_nota(6.5)

print(f"Estudante: {aluno.nome}")
print(f"Média: {aluno.calcular_media():.1f}")
print(f"Situação: {aluno.situacao()}")