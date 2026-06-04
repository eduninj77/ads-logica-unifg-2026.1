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

    def situacao(self) -> str:
        """Retorna 'Aprovado' se média >= 7, caso contrário 'Reprovado'."""
        media = self.calcular_media()
        return "Aprovado" if media >= 7.0 else "Reprovado"


if __name__ == "__main__":
    est = Estudante(input("Nome: "), input("Matrícula: "))
    while True:
        s = input("Nota (ou Enter para sair): ")
        if s.strip() == "":
            break
        est.adicionar_nota(float(s))
    print(f"Média: {est.calcular_media():.2f} - Situação: {est.situacao()}")
