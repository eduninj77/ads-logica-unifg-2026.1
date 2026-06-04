import os
os.system("clear" if os.name != "nt" else "cls")

n1 = 8
n2 = 6

def calcular_media(n1=0, n2=0):
    media = (n1 + n2) / 2

    return f"{media:.1f}"

def verificar_situacao(media):
    if media >= 7.0:
        return "APROVADO"
    else:
        return "REPROVADO"
    
print(f"A sua média foi {calcular_media(n1, n2)}, e você está {verificar_situacao(float(calcular_media(n1,n2)))}")