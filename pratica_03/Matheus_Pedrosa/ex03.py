def calcular_media(n1, n2):
    return (n1 + n2) / 2

num1 = float(input("Digite a primeira nota: "))
num2 = float(input("Digite a segunda nota: "))

media = calcular_media(num1, num2)

print(f"A média das notas é {media}")