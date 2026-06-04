import os
os.system("clear" if os.name != "nt" else "cls")

def saudacao(nome=""):#Tem um erro de sintaxe aqui sem os dois pontos
    print("Ola,", nome)
#A função também não é chamada e muito menos é passado um paramêtro pra ela, o código é executado normalmente, mas não aparece nada no terminal.

nome = input("Digite o seu nome: ").title().replace(" De ", " de ").replace(" Da ", " da ").replace(" Do ", " do ")
saudacao(nome)