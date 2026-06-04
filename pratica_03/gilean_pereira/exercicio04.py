def verificar_situacao(media):
    if (media >=7):
        return "aprovado"
    else:
        return "reprovado"
    

def calcular_media(n1, n2):
    media = (n1+n2)/2
    return media

nota1=float(input("Digite a primeira nota:"))
nota2=float(input("Digite a segunda nota:"))

media_final = calcular_media(nota1,nota2)
verificao = verificar_situacao(media_final)

print(f"sua media é {media_final:.1f}. Voce foi {verificao}")