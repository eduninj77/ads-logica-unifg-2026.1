# ==========================================
# Exercício 08: Depuração de erro sintático
# ==========================================
# O código abaixo contém erro:
# 
# def saudacao(nome)
#     print("Ola,", nome)
#
# ERRO IDENTIFICADO:
# Falta o símbolo ':' (dois-pontos) ao final da linha da definição da função.
#
# EXPLICAÇÃO:
# Em Python, toda função deve ter a sintaxe:
# def nome_da_funcao(parametros):
#                               ↑
#                             DOIS-PONTOS OBRIGATÓRIO
# 
# Se o ':' não estiver presente, o Python não consegue fazer o parsing
# (análise sintática) do código, causando um erro de sintaxe que impede
# a execução do programa.

# CÓDIGO CORRIGIDO:
def saudacao(nome):
    """
    Exibe uma saudação para a pessoa cujo nome é passado.
    
    Args:
        nome (str): Nome da pessoa a ser saudada
    """
    print("Olá,", nome)


# Programa principal
if __name__ == "__main__":
    # Testando a função corrigida
    saudacao("Ana")
    saudacao("João")
    saudacao("Maria")
    
    print("\n--- EXPLICAÇÃO DO ERRO ---")
    print("O código original tinha a seguinte estrutura incorreta:")
    print("def saudacao(nome)")
    print("    print('Ola,', nome)")
    print("\nO ERRO: Falta dos dois-pontos (:) no final da linha 1")
    print("\nPor isso o Python exibe: SyntaxError: invalid syntax")
    print("O código não pode ser executado até que o erro seja corrigido.")
