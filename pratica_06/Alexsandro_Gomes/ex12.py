class Estudante:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def calcular_media(self):
        return self.nota

class Turma:
    def __init__(self):
        self.estudantes = []

    def matricular(self, estudante):
        self.estudantes.append(estudante)

    def media_geral(self):
        if not self.estudantes:
            return 0
        soma_medias = sum(e.calcular_media() for e in self.estudantes)
        return soma_medias / len(self.estudantes)

t = Turma()
t.matricular(Estudante("Carlos", 8.0))
t.matricular(Estudante("Julia", 6.0))
print(t.media_geral())