class Estudante:
    """Classe simples que representa um estudante com nome e matrícula."""

    def __init__(self, nome: str, matricula: str):
        self.nome = nome
        self.matricula = matricula

    def __repr__(self):
        return f"Estudante(nome={self.nome!r}, matricula={self.matricula!r})"


def criar_estudante_por_input():
    """Função de exemplo que cria um Estudante a partir de input do usuário."""
    nome = input("Nome do estudante: ")
    matricula = input("Matrícula: ")
    return Estudante(nome, matricula)


if __name__ == "__main__":
    # Demonstração: cria um estudante usando input e exibe-o
    estudante = criar_estudante_por_input()
    print("Objeto criado:", estudante)
