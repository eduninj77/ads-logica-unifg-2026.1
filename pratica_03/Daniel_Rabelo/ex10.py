# Caso de teste
def calcular_total(preco, quantidade):
    subtotal = preco * quantidade
    desconto = subtotal * 0.1
    total = subtotal - desconto
    return total

# Casos normais
# Caso 1 — compra simples
print(calcular_total(50, 2))    # Esperado: 90.0

# Caso 2 — outro produto comum
print(calcular_total(30, 3))    # Esperado: 81.0
                                # subtotal = 90, desconto = 9, total = 81

# Caso limítrofe
                                # Quantidade mínima possível: 1 unidade
print(calcular_total(50, 1))    # Esperado: 45.0
                                # subtotal = 50, desconto = 5, total = 45

# Caso extremo
# Preço zero — o que a função retorna?
print(calcular_total(0, 5))     # Esperado: 0.0
                                # subtotal = 0, desconto = 0, total = 0

def calcular_total(preco, quantidade):
    if preco < 0 or quantidade < 0:
        return "Erro: valores não podem ser negativos."
    subtotal = preco * quantidade
    desconto = subtotal * 0.1
    total = subtotal - desconto
    return total
