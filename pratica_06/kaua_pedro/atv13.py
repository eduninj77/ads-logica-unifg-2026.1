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

class Turma:
    def __init__(self):
        self.estudantes = []

    def matricular(self, estudante):
        self.estudantes.append(estudante)

    def media_geral(self):
        if len(self.estudantes) == 0:
            return 0
        total = sum(e.calcular_media() for e in self.estudantes)
        return total / len(self.estudantes)

    def relatorio(self):
        for e in self.estudantes:
            print(f"{e.nome} | Média: {e.calcular_media():.2f} | {e.situacao()}")

e1 = Estudante("Ana", "2024001")
e1.adicionar_nota(8.0)
e1.adicionar_nota(9.0)

e2 = Estudante("Bruno", "2024002")
e2.adicionar_nota(5.0)
e2.adicionar_nota(6.0)

e3 = Estudante("Carla", "2024003")
e3.adicionar_nota(10.0)
e3.adicionar_nota(9.5)

t = Turma()
t.matricular(e1)
t.matricular(e2)
t.matricular(e3)

t.relatorio()
print(f"\nMédia geral da turma: {t.media_geral():.2f}")
