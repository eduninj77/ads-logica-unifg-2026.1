class Estudante:
    def __init__(self, nome: str, matricula: str):
        self.nome = nome
        self.matricula = matricula
        self.notas = []

    def adicionar_nota(self, nota: float):
        """Adiciona nota validando que esteja entre 0 e 10."""
        n = float(nota)
        if n < 0 or n > 10:
            raise ValueError("Nota inválida: deve estar entre 0 e 10")
        self.notas.append(n)

    def calcular_media(self) -> float:
        if not self.notas:
            return 0.0
        return sum(self.notas) / len(self.notas)


if __name__ == "__main__":
    est = Estudante("Fábio", "2026006")
    try:
        est.adicionar_nota(float(input("Digite uma nota (0-10): ")))
    except ValueError as e:
        print("Erro:", e)
    print(est.notas)
