def calcular_media(n1 ,n2):
    return (n1+n2) / 2

nota1 = float(input("Digite sua primeira nota : "))
nota2 = float(input("Digite sua segunda nota : "))
print(f"A média do aluno é: {calcular_media(nota1, nota2):.1f}")