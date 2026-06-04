class Estudante:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.notas = []

e = Estudante("Ana", "2024001")
print(e.notas)
