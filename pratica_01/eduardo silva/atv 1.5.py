# Solicita os dados ao usuário
tamanho_mb = float(input("Digite o tamanho do arquivo (MB): "))
velocidade_mbps = float(input("Digite a velocidade da internet (Mbps): "))

# Conversão de Mbps para MB/s (1 Byte = 8 bits)
velocidade_mbs = velocidade_mbps / 8

# Calcula o tempo total em segundos
tempo_segundos = tamanho_mb / velocidade_mbs

# Converte para minutos e segundos
minutos = int(tempo_segundos // 60)
segundos = int(tempo_segundos % 60)

# Exibe o resultado
print(f"{minutos} minutos e {segundos} segundos")