# ==========================================
# Exercício 10: Teste de mesa + caso de teste
# ==========================================
# Considere o código:
# 
# def calcular_total(preco, quantidade):
#     subtotal = preco * quantidade
#     desconto = subtotal * 0.1
#     total = subtotal - desconto
#     return total
#
# PARTE A: Teste de mesa com calcular_total(50, 2)
# PARTE B: Casos de teste (normais, limitrofe, extremo)

def calcular_total(preco, quantidade):
    """
    Calcula o total com 10% de desconto.
    
    Args:
        preco (float): Preço unitário do produto
        quantidade (int): Quantidade de produtos
        
    Returns:
        float: Total com desconto aplicado
    """
    subtotal = preco * quantidade
    desconto = subtotal * 0.1
    total = subtotal - desconto
    return total


# ========================================
# PARTE A: TESTE DE MESA
# ========================================
print("=" * 60)
print("PARTE A: TESTE DE MESA COM calcular_total(50, 2)")
print("=" * 60)
print("\nTABELA DE VALORES:")
print(f"{'Parâmetro':<20} {'Valor':<15}")
print("-" * 35)

preco = 50
quantidade = 2
subtotal = preco * quantidade
desconto = subtotal * 0.1
total = subtotal - desconto

print(f"{'Preço':<20} {preco:<15.2f}")
print(f"{'Quantidade':<20} {quantidade:<15}")
print(f"{'Subtotal':<20} {subtotal:<15.2f}")
print(f"{'Desconto (10%)':<20} {desconto:<15.2f}")
print(f"{'Total':<20} {total:<15.2f}")

resultado_funcao = calcular_total(50, 2)
print(f"\nResultado da função: R$ {resultado_funcao:.2f}")


# ========================================
# PARTE B: CASOS DE TESTE
# ========================================
print("\n" + "=" * 60)
print("PARTE B: CASOS DE TESTE")
print("=" * 60)

# Lista para armazenar os testes
testes = []

# 1º CASO NORMAL
testes.append({
    'nome': 'Caso Normal 1',
    'preco': 100,
    'quantidade': 3,
    'tipo': 'Normal'
})

# 2º CASO NORMAL
testes.append({
    'nome': 'Caso Normal 2',
    'preco': 25.50,
    'quantidade': 5,
    'tipo': 'Normal'
})

# CASO LIMITROFE (quantidade = 1)
testes.append({
    'nome': 'Caso Limitrofe',
    'preco': 50,
    'quantidade': 1,
    'tipo': 'Limitrofe'
})

# CASO EXTREMO (quantidade muito alta)
testes.append({
    'nome': 'Caso Extremo',
    'preco': 999.99,
    'quantidade': 1000,
    'tipo': 'Extremo'
})

# Executar os testes
print("\nRESULTADOS DOS TESTES:\n")
print(f"{'Caso':<25} {'Preço':<12} {'Qtd':<8} {'Total':<15} {'Tipo':<15}")
print("-" * 75)

for teste in testes:
    preco = teste['preco']
    quantidade = teste['quantidade']
    total = calcular_total(preco, quantidade)
    
    print(f"{teste['nome']:<25} "
          f"R${preco:<10.2f} "
          f"{quantidade:<8} "
          f"R${total:<13.2f} "
          f"{teste['tipo']:<15}")

# Testes adicionais para garantir a função funciona corretamente
print("\n" + "=" * 60)
print("VALIDAÇÃO ADICIONAL")
print("=" * 60)

print("\nTestando com valores diferentes:")
assert calcular_total(50, 2) == 90.0, "Teste 1 falhou"
assert calcular_total(100, 1) == 90.0, "Teste 2 falhou"
assert calcular_total(10, 10) == 90.0, "Teste 3 falhou"

print("✓ Todos os testes passaram com sucesso!")
