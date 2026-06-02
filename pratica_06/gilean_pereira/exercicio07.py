class Estudante:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.notas = []


    def adicionar_nota(self, nota):
        if not (0 <= nota <= 10):
            raise ValueError("A nota deve estar entre 0 e 10.")
        self.notas.append(nota)


aluno = Estudante("Beatriz", "2026002")
aluno.adicionar_nota(9.5)
print(f"Notas do aluno: {aluno.notas}")


print("\nTentando adicionar nota inválida (11):")
try:
    aluno.adicionar_nota(11)
except ValueError as e:
    print(f"Erro capturado: {e}")