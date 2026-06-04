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
        media = self.calcular_media()
        return "Aprovado" if media >= 7 else "Recuperação"


class Turma:
    def __init__(self):
        self.estudantes = []

    def matricular(self, estudante):
        self.estudantes.append(estudante)

    def media_geral(self):
        if len(self.estudantes) == 0:
            return 0
        soma = sum(est.calcular_media() for est in self.estudantes)
        return soma / len(self.estudantes)

    def listar_estudantes(self):
        for est in self.estudantes:
            print(f"{est.nome} - Média: {est.calcular_media():.2f} - {est.situacao()}")


turma = Turma()
est1 = Estudante("Matheus", "2024001")
est1.adicionar_nota(8.5)
est1.adicionar_nota(9.0)

est2 = Estudante("João", "2024002")
est2.adicionar_nota(6.0)
est2.adicionar_nota(7.5)

turma.matricular(est1)
turma.matricular(est2)

turma.listar_estudantes()
