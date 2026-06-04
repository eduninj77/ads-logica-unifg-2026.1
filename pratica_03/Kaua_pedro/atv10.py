def obter_nome_aluno():
    return input("Digite o nome do aluno: ").strip()


def obter_notas():
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    return n1, n2


def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2


def determinar_situacao(media_final):
    if media_final >= 7.0:
        return "Aprovado"
    elif media_final >= 5.0:
        return "Recuperação"
    else:
        return "Reprovado"


def exibir_relatorio(nome, media, situacao):
    print("\n" + "="*30)
    print(f"{'RELATÓRIO FINAL':^30}")
    print("="*30)
    print(f"Aluno:    {nome}")
    print(f"Média:    {media:.1f}")
    print(f"Situação: {situacao}")
    print("="*30)


# Fluxo principal do programa
nome_aluno = obter_nome_aluno()
nota1, nota2 = obter_notas()

media = calcular_media(nota1, nota2)
situacao = determinar_situacao(media)

exibir_relatorio(nome_aluno, media, situacao)