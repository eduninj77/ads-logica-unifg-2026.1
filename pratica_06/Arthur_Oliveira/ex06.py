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

    def situacao(self):
        if self.calcular_media() >= 7:
            return "Aprovado"
        return "Recuperação"

e1 = Estudante("Ana",   "2024001")
e2 = Estudante("Bruno", "2024002")
e3 = Estudante("Carla", "2024003")

e1.adicionar_nota(8.0)
e1.adicionar_nota(7.5)
e1.adicionar_nota(9.0)

e2.adicionar_nota(5.0)
e2.adicionar_nota(6.0)
e2.adicionar_nota(4.5)

e3.adicionar_nota(7.0)
e3.adicionar_nota(7.0)
e3.adicionar_nota(7.0)

for estudante in [e1, e2, e3]:
    print(f"{estudante.nome} — Média: {estudante.calcular_media():.2f} — {estudante.situacao()}")