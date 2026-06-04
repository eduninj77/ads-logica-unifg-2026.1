def calcular_media (nota1,nota2):
    return (nota1+nota2) / 2

def verificar_situacao(media):
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"
nota1 = 8 
nota2 = 6
media = calcular_media (nota1,nota2)
ResultadoFinal = verificar_situacao(media)

print(f"Sua média é {media} é voce foi {ResultadoFinal}")