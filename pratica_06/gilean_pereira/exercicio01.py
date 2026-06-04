class Estudante:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

aluno = Estudante("Mariana", "20260123")

print(f"Nome do estudante: {aluno.nome}")
print(f"Matrícula: {aluno.matricula}")