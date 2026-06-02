class Estudante:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def calcular_media(self):
        return self.nota

    def situacao(self):
        if self.calcular_media() >= 7:
            return "Aprovado"
        return "Recuperação"

class Turma:
    def __init__(self):
        self.estudantes = []

    def matricular(self, estudante):
        self.estudantes.append(estudante)

    def relatorio(self):
        for e in self.estudantes:
            print(f"Nome: {e.nome} | Média: {e.calcular_media()} | Situação: {e.situacao()}")

t = Turma()
t.matricular(Estudante("Carlos", 8.0))
t.matricular(Estudante("Julia", 6.0))
t.relatorio()