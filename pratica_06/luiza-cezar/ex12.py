from ex04 import Estudante
from ex10 import Turma


def media_geral(turma: Turma) -> float:
    """Calcula a média geral da turma (média das médias dos estudantes)."""
    if not turma.estudantes:
        return 0.0
    medias = [e.calcular_media() for e in turma.estudantes]
    return sum(medias) / len(medias)


if __name__ == "__main__":
    turma = Turma()
    # exemplo rápido: criar estudantes e matricular
    a = Estudante("Gina", "2026007")
    b = Estudante("Hugo", "2026008")
    a.adicionar_nota(8)
    a.adicionar_nota(9)
    b.adicionar_nota(6)
    turma.estudantes.extend([a, b])
    print(f"Média geral da turma: {media_geral(turma):.2f}")
