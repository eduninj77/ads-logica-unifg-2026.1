# Exercício 14 - Situação acadêmica

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

def definir_situacao(media):
    """Define a situação do estudante baseado na média"""
    if media >= 7.0:
        return "Aprovado"
    else:
        return "Recuperação"

print("=" * 60)
print("EXERCÍCIO 14 - SITUAÇÃO ACADÊMICA")
print("=" * 60)

print("\nBoletim de notas com situação:\n")

for i, nome in enumerate(nomes):
    media = calcular_media(notas[i])
    situacao = definir_situacao(media)
    print(f"{nome} - Média: {media:.2f} - {situacao}")

print("\n" + "=" * 60)
print("✓ Critérios:")
print("  • Média >= 7.0: Aprovado")
print("  • Média < 7.0: Recuperação")
print("=" * 60)
