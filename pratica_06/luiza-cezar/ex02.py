class Estudante:
    """Estudante com lista de notas vazia no construtor."""

    def __init__(self, nome: str, matricula: str):
        self.nome = nome
        self.matricula = matricula
        self.notas = []  # atributo: lista de notas

    def __repr__(self):
        return f"Estudante(nome={self.nome!r}, matricula={self.matricula!r}, notas={self.notas})"


def criar_exemplo():
    e = Estudante("Ana", "2026001")
    print(e)
    return e


if __name__ == "__main__":
    criar_exemplo()
