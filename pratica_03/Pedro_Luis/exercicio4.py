import os
os.system("clear" if os.name != "nt" else "cls")

def verificar_situacao(media):
    if media >= 7:
        return "APROVADO"
    else:
        return "REPROVADO" 
    
def calcular_media(n1=0, n2=0):
    media = (n1+n2) / 2
    return f"{media:.1f}"
while True:
    try:
        nota = [float(input("Digite a primeira nota: ")), float(input("Digite a segunda nota: "))]
    except ValueError:
        print("Digite apenas números.")
        continue
    break

print("Você está " + verificar_situacao(float(calcular_media(nota[0], nota[1])))+ "." + f"Com média {calcular_media(nota[0], nota[1])}")