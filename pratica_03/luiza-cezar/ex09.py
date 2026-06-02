# ==========================================
# Exercício 09: Depuração de erro de execução
# ==========================================
# Analise o código:
# 
# def dividir(a, b):
#     return a / b
#
# print(dividir(10, 0))
#
# QUESTÃO 1: Que erro acontece?
# ZeroDivisionError: division by zero
#
# QUESTÃO 2: Por que ele ocorre?
# Porque estamos tentando dividir um número por zero, o que é matematicamente
# indefinido. Python não permite essa operação e lança uma exceção.
#
# QUESTÃO 3: Reescrever para evitar o problema
# Usar um if para verificar se b == 0 antes de fazer a divisão

# VERSÃO 1: Tratamento simples com verificação
def dividir_v1(a, b):
    """
    Divide a por b com verificação para evitar divisão por zero.
    
    Args:
        a (float): Dividendo
        b (float): Divisor
        
    Returns:
        float: Resultado da divisão ou None se b for zero
    """
    if b == 0:
        print("Erro: Não é possível dividir por zero!")
        return None
    else:
        return a / b


# VERSÃO 2: Com mensagem amigável
def dividir_v2(a, b):
    """
    Divide a por b com mensagem amigável em caso de erro.
    
    Args:
        a (float): Dividendo
        b (float): Divisor
        
    Returns:
        float: Resultado da divisão
    """
    if b == 0:
        return "Erro: Divisão por zero não é permitida!"
    else:
        return a / b


# VERSÃO 3: Com tratamento de exceção (try/except)
def dividir_v3(a, b):
    """
    Divide a por b usando tratamento de exceção.
    
    Args:
        a (float): Dividendo
        b (float): Divisor
        
    Returns:
        float ou str: Resultado da divisão ou mensagem de erro
    """
    try:
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        return "Erro: Não é possível dividir por zero!"


# Programa principal
if __name__ == "__main__":
    print("=" * 50)
    print("TESTE DE DIVISÃO - TRATAMENTO DE ERROS")
    print("=" * 50)
    
    # Testando a versão 1
    print("\n--- VERSÃO 1: Verificação simples ---")
    resultado = dividir_v1(10, 2)
    if resultado is not None:
        print(f"dividir_v1(10, 2) = {resultado}")
    
    resultado = dividir_v1(10, 0)
    
    # Testando a versão 2
    print("\n--- VERSÃO 2: Mensagem amigável ---")
    print(f"dividir_v2(20, 4) = {dividir_v2(20, 4)}")
    print(f"dividir_v2(10, 0) = {dividir_v2(10, 0)}")
    
    # Testando a versão 3
    print("\n--- VERSÃO 3: Tratamento com try/except ---")
    print(f"dividir_v3(15, 3) = {dividir_v3(15, 3)}")
    print(f"dividir_v3(10, 0) = {dividir_v3(10, 0)}")
    
    # Teste interativo
    print("\n--- TESTE INTERATIVO ---")
    try:
        dividendo = float(input("Digite o dividendo: "))
        divisor = float(input("Digite o divisor: "))
        resultado = dividir_v2(dividendo, divisor)
        print(f"Resultado: {resultado}")
    except ValueError:
        print("Erro: Digite um número válido!")
