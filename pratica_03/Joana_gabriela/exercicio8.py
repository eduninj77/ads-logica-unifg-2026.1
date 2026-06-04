#  ERRADO
def saudacao(nome)
    print("Ola,", nome)

#  CORRETO
def saudacao(nome):
    print("Ola,", nome)

    #O : não é opcional, ele é parte da sintaxe obrigatória do Python. Ele sinaliza ao interpretador que um bloco de código indentado vai começar logo abaixo.
Sem ele, o Python lê a linha e não sabe o que esperar a seguir, o código quebra antes mesmo de rodar, na fase de leitura.