def calcular_total(preco, quantidade):
    subtotal = preco * quantidade
    desconto = subtotal * 0.1
    total = subtotal - desconto
    return total

print("Normal 1:", calcular_total(10, 5))
print("Normal 2:", calcular_total(100, 1))
print("Limítrofe:", calcular_total(20, 0))
print("Extremo:", calcular_total(1e6, 1000))
