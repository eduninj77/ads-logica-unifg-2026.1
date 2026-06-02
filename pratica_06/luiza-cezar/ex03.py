class Estudante:
    """Estudante com método para adicionar notas."""

    def __init__(self, nome: str, matricula: str):
        self.nome = nome
        self.matricula = matricula
        self.notas = []

    def adicionar_nota(self, nota: float):
        """Adiciona uma nota à lista de notas (sem validação nesta etapa)."""
        self.notas.append(float(nota))

    def __repr__(self):
        return f"Estudante({self.nome}, {self.matricula}, notas={self.notas})"


def demo():
    est = Estudante("Bruno", "2026002")
    # exemplo de adicionar múltiplas notas
    est.adicionar_nota(7.5)
    est.adicionar_nota(8)
    print(est)
    return est


if __name__ == "__main__":
    # Permite inserir notas via input (opcional)
    est = Estudante(input("Nome: "), input("Matrícula: "))
    while True:
        s = input("Digite uma nota (ou Enter para sair): ")
        if s.strip() == "":
            break
        est.adicionar_nota(float(s))
    print("Estudante:", est)
