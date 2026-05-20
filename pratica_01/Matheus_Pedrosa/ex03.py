total_fatias = int(input('Número total de fatias: '))
programadores = int(input('Número de programadores na equipe: '))

fatias_por_pessoa = total_fatias // programadores
sobra = total_fatias % programadores

print(f'Cada pessoa receberá {fatias_por_pessoa} fatias.')
print(f'Sobrará(m) {sobra} fatia(s).')
