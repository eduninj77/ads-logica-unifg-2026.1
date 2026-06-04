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
e2 = Estudante("Bruno", "2024002")
e3 = Estudante("Carla", "2024003")

e1.adicionar_nota(8.0)
e1.adicionar_nota(7.5)
e1.adicionar_nota(9.0)

e2.adicionar_nota(5.0)
e2.adicionar_nota(6.5)
e2.adicionar_nota(4.0)

# e3 sem notas — testa lista vazia

print(f"{e1.nome} - Média: {e1.calcular_media():.2f}")
print(f"{e2.nome} - Média: {e2.calcular_media():.2f}")
print(f"{e3.nome} - Média: {e3.calcular_media():.2f}")