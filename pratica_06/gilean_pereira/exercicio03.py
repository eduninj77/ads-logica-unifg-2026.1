class Estudante:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.notas = []


    def adicionar_nota(self, nota):
        self.notas.append(nota)


aluno = Estudante("Mariana", "20260123")

aluno.adicionar_nota(8.5)
aluno.adicionar_nota(9.0)

print(f"Nome do estudante: {aluno.nome}")
print(f"Matrícula: {aluno.matricula}")
print(f"Notas após adições: {aluno.notas}")