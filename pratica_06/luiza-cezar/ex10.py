class Turma:
    """Classe Turma para armazenar estudantes."""

    def __init__(self):
        self.estudantes = []  # lista de objetos Estudante

    def listar_estudantes(self):
        return list(self.estudantes)


if __name__ == "__main__":
    t = Turma()
    print("Turma criada. Número de estudantes:", len(t.estudantes))
