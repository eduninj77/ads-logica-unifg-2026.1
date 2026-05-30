# Código Monolítico
n1 = 8
n2 = 6
media = (n1 + n2) / 2

if media >= 7:
    print("Aprovado")
else:
    print("Reprovado")

# Código Modular
def calcular_media(n1, n2):
    return (n1 + n2) / 2

def verificar_situacao(media):
    if media >= 7:
        print("Aprovado")
    else:
        print("Reprovado")

# Programa principal
n1 = 8
n2 = 6
media = calcular_media(n1, n2)
verificar_situacao(media)