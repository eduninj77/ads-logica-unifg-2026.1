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

e1 = Estudante("Ana", "2024001")
e1.adicionar_nota(8.0)
e1.adicionar_nota(9.0)

e2 = Estudante("Bruno", "2024002")
e2.adicionar_nota(5.0)
e2.adicionar_nota(6.0)

print(e1.nome, e1.notas)
print(e2.nome, e2.notas)
