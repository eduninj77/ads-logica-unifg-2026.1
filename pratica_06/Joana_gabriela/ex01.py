class Estudante:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

e1 = Estudante("Ana", "2024001")
e2 = Estudante("Bruno", "2024002")

print(e1.nome)
print(e1.matricula)
print(e2.nome)
print(e2.matricula)