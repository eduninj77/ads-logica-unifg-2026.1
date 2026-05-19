def ler_notas():
    n1 = float(input("Digite a 1ª nota: "))
    n2 = float(input("Digite a 2ª nota: "))
    return n1, n2
def calcular_media(n1, n2):
    return (n1 + n2) / 2
def verificar_situacao(media):
    if media >= 7:
        return "APROVADO"
    elif media >= 4:
        return "RECUPERAÇÃO"
    else:
        return "REPROVADO"
def exibir_resultado(nome, media, situacao):
    return f"Nome: {nome}\nMedia: {media:.1f}\nSituação: {situacao}"

def main():
    nome = input("Digite o nome do aluno: ")
    n1, n2 = ler_notas()
    media = calcular_media(n1, n2)
    situacao = verificar_situacao(media)
    print(exibir_resultado(nome, media, situacao))

if __name__ == "__main__":
    main()