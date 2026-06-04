from ex04 import Estudante
from ex10 import Turma


def relatorio(turma: Turma):
    """Imprime nome, média e situação de cada estudante da turma."""
    for e in turma.estudantes:
        nome = e.nome
        media = e.calcular_media()
        situacao = "Aprovado" if media >= 7 else "Reprovado"
        print(f"{nome}: média={media:.2f} - {situacao}")


if __name__ == "__main__":
    turma = Turma()
    # criar estudantes para demo
    a = Estudante("Iris", "2026009")
    b = Estudante("João", "2026010")
    a.adicionar_nota(7)
    a.adicionar_nota(8)
    b.adicionar_nota(5)
    turma.estudantes.extend([a, b])
    relatorio(turma)
