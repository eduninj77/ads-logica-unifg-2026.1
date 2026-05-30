total_fatias = int(input("Digite o número total de fatias: "))
programadores = int(input("Digite o número de programadores na equipe: "))

fatias_por_pessoa = total_fatias // programadores
sobra = total_fatias % programadores

print(f"\nCada programador comerá {fatias_por_pessoa} fatia(s).")
print(f"Sobram {sobra} fatia(s) na caixa.")
