def calcular_media(n1, n2):
    media = (n1+n2)/2
    return media

n1=float(input("Digite a primeira nota:"))
n2=float(input("Digite a segunda nota:"))


print(f"sua media é {calcular_media(n1,n2):.1f}")