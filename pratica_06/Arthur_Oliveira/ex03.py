class Estudante:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.notas = []

    def adicionar_nota(self, nota):
        self.notas.append(nota)

e1 = Estudante("Ana", "2024001")
e2 = Estudante("Bruno", "2024002")

e1.adicionar_nota(8.0)
e1.adicionar_nota(7.5)
e1.adicionar_nota(9.0)

e2.adicionar_nota(5.0)
e2.adicionar_nota(6.5)
e2.adicionar_nota(4.0)

print(f"{e1.nome}: {e1.notas}")
print(f"{e2.nome}: {e2.notas}")