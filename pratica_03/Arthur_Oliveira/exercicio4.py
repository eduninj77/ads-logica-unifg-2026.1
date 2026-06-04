def calcular_media(n1, n2):
    return (n1 + n2) / 2

def verificar_situacao(media):
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

nome = input("Digite o nome do aluno: ")
n1 = float(input("Digite a primeira nota: ").replace(",", "."))
n2 = float(input("Digite a segunda nota: ").replace(",", "."))

media = calcular_media(n1, n2)
situacao = verificar_situacao(media)

print(f"Aluno: {nome}")
print(f"Média: {media:.1f}")
print(f"Situação: {situacao}")