def saudacao(nome):
    return f"Olá, {nome}"

for i in range(1, 4):
    nome = input("Digite um nome: ")
    print(saudacao(nome))
