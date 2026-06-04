from ex04 import Estudante
from ex10 import Turma


def matricular(turma: Turma, estudante: Estudante):
    """Adiciona um estudante (objeto Estudante) à turma."""
    turma.estudantes.append(estudante)


if __name__ == "__main__":
    turma = Turma()
    nome = input("Nome do estudante: ")
    matricula = input("Matrícula: ")
    est = Estudante(nome, matricula)
    matricular(turma, est)
    print("Matriculado:", turma.estudantes)
