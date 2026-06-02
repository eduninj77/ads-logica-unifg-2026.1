# ==========================================
# Exercício 02: Soma com parâmetros
# ==========================================
# Crie uma função chamada somar(a, b) que receba dois números 
# e retorne a soma.

def somar(a, b):
    """
    Retorna a soma de dois números.
    
    Args:
        a (int/float): Primeiro número
        b (int/float): Segundo número
        
    Returns:
        int/float: A soma de a e b
    """
    return a + b


# Programa principal
if __name__ == "__main__":
    # Teste 1: Números inteiros normais
    resultado1 = somar(5, 3)
    print(f"somar(5, 3) = {resultado1}")
    
    # Teste 2: Caso usando zero
    resultado2 = somar(10, 0)
    print(f"somar(10, 0) = {resultado2}")
    
    # Teste 3: Caso usando número negativo
    resultado3 = somar(15, -5)
    print(f"somar(15, -5) = {resultado3}")
    
    # Teste adicional: dois números negativos
    resultado4 = somar(-10, -5)
    print(f"somar(-10, -5) = {resultado4}")
