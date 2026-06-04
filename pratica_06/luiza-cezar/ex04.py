class Estudante:
    """Estudante com cálculo de média das notas."""

    def __init__(self, nome: str, matricula: str):
        self.nome = nome
        self.matricula = matricula
        self.notas = []

    def adicionar_nota(self, nota: float):
        self.notas.append(float(nota))

    def calcular_media(self) -> float:
        """Retorna a média das notas; 0 se não houver notas."""
        if not self.notas:
            return 0.0
        return sum(self.notas) / len(self.notas)

    def __repr__(self):
        return f"Estudante({self.nome}, média={self.calcular_media():.2f})"


if __name__ == "__main__":
    est = Estudante("Carla", "2026003")
    est.adicionar_nota(9)
    est.adicionar_nota(6)
    print(f"Média de {est.nome}:", est.calcular_media())
