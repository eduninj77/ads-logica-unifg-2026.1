# Exercício 30 - Mapa de ocupação de laboratório

def exibir_mapa(matriz_lab):
    """Exibe o mapa do laboratório"""
    print("\nMapa atual:")
    for i, linha in enumerate(matriz_lab):
        print(f"Fileira {i}: ", end="")
        for j, status in enumerate(linha):
            print(f"[{status}] ", end="")
        print()

def contar_computadores(matriz_lab):
    """Conta computadores por status"""
    livres = 0
    ocupados = 0
    manutencao = 0
    
    for linha in matriz_lab:
        for status in linha:
            if status == "L":
                livres += 1
            elif status == "O":
                ocupados += 1
            elif status == "M":
                manutencao += 1
    
    return livres, ocupados, manutencao

def ocupar_computador(matriz_lab, linha, coluna):
    """Tenta ocupar um computador"""
    # Verificar limites
    if linha < 0 or linha >= len(matriz_lab) or coluna < 0 or coluna >= len(matriz_lab[0]):
        return False, "Posição fora dos limites"
    
    # Verificar status
    status_atual = matriz_lab[linha][coluna]
    
    if status_atual == "L":
        matriz_lab[linha][coluna] = "O"
        return True, "Computador ocupado com sucesso"
    elif status_atual == "O":
        return False, "Este computador já está ocupado"
    elif status_atual == "M":
        return False, "Este computador está em manutenção"
    
    return False, "Status desconhecido"

# Laboratório: 4 fileiras, 5 computadores por fileira
laboratorio = [
    ["L", "O", "L", "L", "O"],
    ["L", "L", "M", "O", "L"],
    ["O", "L", "L", "O", "L"],
    ["M", "O", "L", "L", "L"]
]

print("=" * 70)
print("EXERCÍCIO 30 - MAPA DE OCUPAÇÃO DE LABORATÓRIO")
print("=" * 70)

# Exibir estado inicial
exibir_mapa(laboratorio)

# Contar computadores
livres, ocupados, manutencao = contar_computadores(laboratorio)

print(f"\nEstatísticas (Estado inicial):")
print(f"Computadores livres: {livres}")
print(f"Computadores ocupados: {ocupados}")
print(f"Computadores em manutenção: {manutencao}")
print(f"Total: {livres + ocupados + manutencao}")

print("\n" + "-" * 70)

# Tentativa 1: Ocupar um computador livre
print("\nTentativa 1: Ocupar computador na fileira 0, posição 0")
sucesso, mensagem = ocupar_computador(laboratorio, 0, 0)
print(f"Resultado: {mensagem}")

# Tentativa 2: Ocupar um computador já ocupado
print("\nTentativa 2: Ocupar computador na fileira 0, posição 1")
sucesso, mensagem = ocupar_computador(laboratorio, 0, 1)
print(f"Resultado: {mensagem}")

# Tentativa 3: Ocupar um computador em manutenção
print("\nTentativa 3: Ocupar computador na fileira 1, posição 2")
sucesso, mensagem = ocupar_computador(laboratorio, 1, 2)
print(f"Resultado: {mensagem}")

# Tentativa 4: Posição fora dos limites
print("\nTentativa 4: Ocupar computador na fileira 5, posição 0")
sucesso, mensagem = ocupar_computador(laboratorio, 5, 0)
print(f"Resultado: {mensagem}")

print("\n" + "-" * 70)

# Exibir estado final
exibir_mapa(laboratorio)

# Contar computadores novamente
livres, ocupados, manutencao = contar_computadores(laboratorio)

print(f"\nEstatísticas (Estado final):")
print(f"Computadores livres: {livres}")
print(f"Computadores ocupados: {ocupados}")
print(f"Computadores em manutenção: {manutencao}")
print(f"Total: {livres + ocupados + manutencao}")

print("\n" + "=" * 70)
print("✓ Sistema de reserva de laboratório concluído!")
print("=" * 70)
