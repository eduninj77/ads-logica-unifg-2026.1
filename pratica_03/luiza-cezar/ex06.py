# ==========================================
# Exercício 06: Escopo básico na prática
# ==========================================
# Analise o código e responda:
# 1. Qual variável é global?
# 2. Qual variável é local?
# 3. O que acontece se tentarmos usar y fora da função?
# 4. Crie um exemplo parecido.

# ANÁLISE DO CÓDIGO FORNECIDO:
# x = 10
# 
# def teste():
#     y = 5
#     return x + y
#
# print(teste())
# 
# RESPOSTA:
# 1. A variável x é GLOBAL (definida no escopo global)
# 2. A variável y é LOCAL (definida dentro da função teste())
# 3. Se tentarmos usar y fora da função, receberemos um NameError
#    porque y só existe dentro da função teste()

# Exemplo fornecido
x = 10

def teste():
    y = 5
    return x + y

print(f"Resultado da função teste(): {teste()}")
# Output: 15

# Demonstração do erro se tentarmos acessar y fora da função
# print(y)  # Isso causaria: NameError: name 'y' is not defined


# ========================================
# CRIANDO UM EXEMPLO PARECIDO
# ========================================

# Variável global
preco_unitario = 50.0

def calcular_preco_total(quantidade):
    """
    Calcula o preço total multiplicando a quantidade pelo preço unitário.
    
    preco_unitario é uma variável GLOBAL (acessível dentro da função)
    quantidade é um parâmetro (local à função)
    subtotal é uma variável LOCAL (definida dentro da função)
    """
    subtotal = preco_unitario * quantidade
    return subtotal

# Testando o exemplo
print("\nEXEMPLO PARECIDO:")
print(f"Preço unitário (global): {preco_unitario}")
quantidade_comprada = 3
total = calcular_preco_total(quantidade_comprada)
print(f"Quantidade comprada: {quantidade_comprada}")
print(f"Total: R$ {total:.2f}")

# Se descomentar a linha abaixo, receberá NameError:
# print(subtotal)  # NameError: name 'subtotal' is not defined
