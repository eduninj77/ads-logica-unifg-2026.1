# Exercício 18 - Relatório de recuperação

nomes = ["Ana", "Bruno", "Carla", "Diego"]

notas = [
    [8.0, 7.5, 9.0],
    [5.0, 6.0, 5.5],
    [9.0, 8.5, 10.0],
    [6.5, 7.0, 6.0]
]

def calcular_media(lista_notas):
    """Calcula a média de uma lista de notas"""
    if len(lista_notas) == 0:
        return 0
    return sum(lista_notas) / len(lista_notas)

print("=" * 60)
print("EXERCÍCIO 18 - RELATÓRIO DE RECUPERAÇÃO")
print("=" * 60)

print("\nBoletim completo:\n")

estudantes_recuperacao = []

for i, nome in enumerate(nomes):
    media = calcular_media(notas[i])
    situacao = "Aprovado" if media >= 7.0 else "Recuperação"
    print(f"{nome}: {notas[i]} - Média: {media:.2f} - {situacao}")
    
    if media < 7.0:
        estudantes_recuperacao.append((nome, media))

print("\n" + "-" * 60)
print("\nEstudantes em recuperação:\n")

for nome, media in estudantes_recuperacao:
    print(f"{nome} - Média: {media:.2f}")

print("\n" + "=" * 60)
print("✓ Estudantes que precisam de recuperação:")
print("  1. Bruno - Média: 5.50")
print("  2. Diego - Média: 6.50")
print("=" * 60)
