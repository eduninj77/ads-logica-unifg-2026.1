def calcular_media(n1, n2):
    """Recebe duas notas e retorna a média."""
    return (n1 + n2) / 2


def verificar_situacao(media):
    """Recebe a média e retorna a situação do aluno."""
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"


def exibir_resultado(n1, n2):
    """Orquestra o cálculo e exibe o resultado final."""
    media = calcular_media(n1, n2)
    situacao = verificar_situacao(media)
    print(f"Média: {media:.1f} → {situacao}")


