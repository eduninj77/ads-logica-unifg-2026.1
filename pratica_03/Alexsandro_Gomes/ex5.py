def ler_notas():
    nota1 = float(input("Digite sua primeira nota : "))
    nota2 = float(input("Digite sua segunda nota : "))
    return nota1, nota2

def calcular_media(n1, n2):
    return (n1 + n2) / 2

def verificar_situacao(media):
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

def exibir_resultado(nome, media, situacao):
    print("--- BOLETIM ---")
    print(f"Aluno: {nome} ")
    print(f"Média: {media:.1f}")
    print(f"Situação: {situacao}")

nome_aluno = input("Digite o nome do aluno: ")
n1, n2 = ler_notas()
media_final = calcular_media(n1, n2)
situacao_final = verificar_situacao(media_final)
exibir_resultado(nome_aluno , media_final, situacao_final)
