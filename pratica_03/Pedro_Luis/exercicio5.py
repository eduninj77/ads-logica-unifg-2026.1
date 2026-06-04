import os
os.system("clear" if os.name != "nt" else "cls")


def ler_notas():
    global n1, n2
    while True:
        try:
            n1 = float(input("Digite a primeira nota: "))
        except (ValueError, KeyboardInterrupt):
            print("Digite apenas números.")
            continue
        break
    while True:
        try:
            n2 = float(input("Digite a segunda nota: "))
        except (ValueError, KeyboardInterrupt):
            print("Digite apenas números.")
            continue
        break

def calcular_media(n1=0, n2=0):
    media = (n1 + n2) / 2

    return f"{media:.1f}"

def verificar_situacao(media):
    if media >= 7.0:
        return "APROVADO"
    elif 5.0 <= media <7.0:
        return "RECUPERAÇÃO"
    else:
        return "REPROVADO"

def exibir_resultado(nome, media, situacao):
    print("=" * 40)
    print("SITUAÇÃO".center(40))
    print("=" * 40)
    print(f"{nome} - Média: {media} - Situação: {situacao}")
    print("=" * 40)

ler_notas()
name = input("Digite o seu nome: ").title().replace(" De ", " de ").replace(" Da ", " da ").replace(" Do ", " do ")
exibir_resultado(name, calcular_media(n1 , n2), verificar_situacao(float((calcular_media(n1, n2)))))
