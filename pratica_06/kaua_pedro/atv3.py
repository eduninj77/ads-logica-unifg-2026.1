class Estudante:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.notas = []

    def adicionar_nota(self, nota):
        self.notas.append(nota)

e = Estudante("Ana", "2024001")
e.adicionar_nota(8.0)
e.adicionar_nota(7.5)
e.adicionar_nota(9.0)
print(e.notas)
