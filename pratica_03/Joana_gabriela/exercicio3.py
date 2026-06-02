def calcular_media(n1, n2):
    return (n1 + n2) / 2

nome = input("Digite o nome do aluno: ")
n1 = float(input("Digite a primeira nota: ").replace(",", "."))
n2 = float(input("Digite a segunda nota: ").replace(",", "."))

media = calcular_media(n1, n2)

print(f"Aluno: {nome}")
print(f"Média: {media:.1f}")