tamanho_mb = float(input('Tamanho do arquivo (MB): '))
velocidade_mbps = float(input('Velocidade da internet (Mbps): '))

segundos = tamanho_mb / (velocidade_mbps / 8)
minutos = segundos // 60
segundos_restantes = segundos % 60

print(f'{minutos} minutos e {segundos_restantes} segundos')
