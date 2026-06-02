# ==========================================
# Exercício 01: Saudação modular
# ==========================================
# Crie uma função chamada saudacao(nome) que receba o nome 
# de uma pessoa e retorne uma mensagem de boas-vindas.

def saudacao(nome):
    """
    Retorna uma mensagem de boas-vindas personalizada.
    
    Args:
        nome (str): O nome da pessoa
        
    Returns:
        str: Mensagem de boas-vindas
    """
    return f"Bem-vindo(a), {nome}!"


# Programa principal
if __name__ == "__main__":
    # Chamando a função 3 vezes com nomes diferentes
    print(saudacao("Ana"))
    print(saudacao("João"))
    print(saudacao("Maria"))
