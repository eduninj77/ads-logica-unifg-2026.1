def verificar_situacao(media):
    if media >= 7:
        return "APROVADO"
    elif media >= 4:
        return "RECUPERAÇÃO"
    else:
        return "REPROVADO"
    
def calcular_media(n1, n2):
    return (n1 + n2) / 2


num1 = float(input("Digite a primeira nota: "))
num2 = float(input("Digite a segunda nota: "))

media = calcular_media(num1, num2)

print(f"Sua media é {media}:   {verificar_situacao(media)}")
