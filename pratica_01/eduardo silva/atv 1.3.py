# Solicita os dados ao usuário
total_fatias = int(input("Digite o total de fatias de pizza: "))
programadores = int(input("Digite o número de programadores: "))

# Calcula a divisão
fatias_por_pessoa = total_fatias // programadores
sobra = total_fatias % programadores

# Exibe o resultado
print(f"\nCada programador comerá {fatias_por_pessoa} fatias inteiras.")
print(f"Sobrarão {sobra} fatias na caixa.")