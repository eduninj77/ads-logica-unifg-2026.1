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

e1 = Estudante("Ana", "2024001")
e2 = Estudante("Bruno", "2024002")

t = Turma()
t.matricular(e1)
t.matricular(e2)

print(len(t.estudantes))
