def ler_notas():
    nome = input("Digite o nome do aluno: ")
    n1 = float(input("Digite a primeira nota: ").replace(",", "."))
    n2 = float(input("Digite a segunda nota: ").replace(",", "."))
    return nome, n1, n2

def calcular_media(n1, n2):
    return (n1 + n2) / 2

def verificar_situacao(media):
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

def exibir_resultado(nome, media, situacao):
    print("=" * 30)
    print(f"  BOLETIM ESCOLAR")
    print("=" * 30)
    print(f"  Aluno:    {nome}")
    print(f"  Média:    {media:.1f}")
    print(f"  Situação: {situacao}")
    print("=" * 30)

# Programa principal
nome, n1, n2 = ler_notas()
media = calcular_media(n1, n2)
situacao = verificar_situacao(media)
exibir_resultado(nome, media, situacao)