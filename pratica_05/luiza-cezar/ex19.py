# Exercício 19 - Grade de assentos

sala = [
    ["L", "O", "L"],
    ["O", "O", "L"],
    ["L", "L", "O"]
]

def exibir_sala(matriz_sala):
    """Exibe a sala de forma visual"""
    for i, linha in enumerate(matriz_sala):
        print(f"Fileira {i}: ", end="")
        for j, assento in enumerate(linha):
            print(f"[{assento}] ", end="")
        print()

def contar_assentos(matriz_sala):
    """Conta assentos livres e ocupados"""
    livres = 0
    ocupados = 0
    for linha in matriz_sala:
        for assento in linha:
            if assento == "L":
                livres += 1
            elif assento == "O":
                ocupados += 1
    return livres, ocupados

print("=" * 60)
print("EXERCÍCIO 19 - GRADE DE ASSENTOS")
print("=" * 60)

print("\nGrade da sala (L=Livre, O=Ocupado):\n")
exibir_sala(sala)

print("\n" + "-" * 60)

livres, ocupados = contar_assentos(sala)
total = livres + ocupados

print(f"\nAssentos livres: {livres}")
print(f"Assentos ocupados: {ocupados}")
print(f"Total de assentos: {total}")

print("\n" + "=" * 60)
print("✓ Análise da sala:")
print("  • Cada 'L' representa um assento livre")
print("  • Cada 'O' representa um assento ocupado")
print("  • Há 4 assentos livres e 5 assentos ocupados")
print("=" * 60)
