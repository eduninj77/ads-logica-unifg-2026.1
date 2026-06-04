import os
os.system("clear" if os.name != "nt" else "cls")

def ler_nome():
    global nome
    while True:    
        try:
            nome = input("Digite o seu nome: ").strip().title().replace(" De ", " de ").replace(" Da ", " da ").replace(" Do ", " do ")
            if not nome:
                print("Digite um nome!")
                continue
            break
        except KeyboardInterrupt:
            print("Não interrompa a operação no meio da execução!")
            continue

def ler_notas():
    global n1, n2
    while True:
        try:    
            n1 = float(input("Digite a primeira nota: "))
            if n1 > 10.0:
                print("Digite apenas de 0.0 a 10.0!")
                continue
            break
        except ValueError:
            print("Digite apenas números!")
            continue       
    while True:
        try:    
            n2 = float(input("Digite a segunda nota: "))
            if n2 > 10.0:
                print("Digite apenas de 0.0 a 10.0!")
                continue            
            break
        except ValueError:
            print("Digite apenas números!")
            continue      

def media(n1, n2):
    media = (n1 + n2) / 2
    return f"{media:.1f}" 

def situacao(media):
    if media >= 7.0:
        return "APROVADO"
    elif 5.0 <= media < 7.0:
        return "RECUPERAÇÃO"   
    else:
        return "REPROVADO"

def relatorio(nome, media, situacao):
    print("=" * 40)
    print("SITUAÇÃO".center(40))
    print("=" * 40)
    print(f"Aluno: {nome} - Média: {media} - Situação: {situacao}")

ler_nome()
ler_notas()
relatorio(nome,media(n1, n2),situacao(float(media(n1, n2))))