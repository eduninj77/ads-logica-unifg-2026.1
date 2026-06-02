class Estudante:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.notas = []

e1 = Estudante("Ana", "2024001")
e2 = Estudante("Bruno", "2024002")

print(e1.nome, e1.notas)
print(e2.nome, e2.notas)