total_fatias = int(input("Número total de fatias: "))
programadores = int(input("Número de programadores: "))

fatias_por_pessoa = total_fatias // programadores
sobra = total_fatias % programadores

print(f"Fatias por pessoa: {fatias_por_pessoa}")
print(f"Sobra na caixa: {sobra}")
