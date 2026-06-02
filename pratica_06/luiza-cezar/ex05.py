class Estudante:
    def __init__(self, nome: str, matricula: str):
        self.nome = nome
        self.matricula = matricula
        self.notas = []

    def adicionar_nota(self, nota: float):
        self.notas.append(float(nota))

    def calcular_media(self) -> float:
        if not self.notas:
            return 0.0
        return sum(self.notas) / len(self.notas)


def demo_independencia():
    a = Estudante("Diego", "2026004")
    b = Estudante("Eva", "2026005")
    a.adicionar_nota(10)
    b.adicionar_nota(5)
    print(a)
    print(b)
    return a, b


if __name__ == "__main__":
    a, b = demo_independencia()
    print(f"Média {a.nome}: {a.calcular_media():.2f}")
    print(f"Média {b.nome}: {b.calcular_media():.2f}")
