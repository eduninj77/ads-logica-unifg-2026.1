# Exercício 29 - Sistema simples de boletim

def calcular_media(notas):
    """Calcula a média de uma lista de notas"""
    if len(notas) == 0:
        return 0
    return sum(notas) / len(notas)

def definir_situacao(media):
    """Define a situação do estudante"""
    if media >= 7.0:
        return "Aprovado"
    elif media >= 5.0:
        return "Recuperação"
    else:
        return "Reprovado"

# Dados do sistema
nomes = ["Alice", "Bruno", "Carlos", "Diana", "Érica"]

notas = [
    [8.0, 7.5, 9.0, 8.5],
    [4.5, 5.0, 4.8, 5.5],
    [6.5, 6.0, 7.0, 6.8],
    [9.5, 9.0, 9.5, 9.8],
    [5.5, 6.5, 6.0, 5.8]
]

print("=" * 70)
print("EXERCÍCIO 29 - SISTEMA SIMPLES DE BOLETIM")
print("=" * 70)

print("\n1. BOLETIM INDIVIDUAL COM SITUAÇÃO\n")
print("-" * 70)

medias_estudantes = []
for i, nome in enumerate(nomes):
    media = calcular_media(notas[i])
    situacao = definir_situacao(media)
    medias_estudantes.append(media)
    print(f"{nome:10} - Média: {media:6.2f} - {situacao}")

print("\n" + "-" * 70)
print("\n2. MAIOR MÉDIA DA TURMA\n")

indice_maior = medias_estudantes.index(max(medias_estudantes))
maior_media = medias_estudantes[indice_maior]
print(f"Maior média: {nomes[indice_maior]} - {maior_media:.2f}")

print("\n" + "-" * 70)
print("\n3. MENOR MÉDIA DA TURMA\n")

indice_menor = medias_estudantes.index(min(medias_estudantes))
menor_media = medias_estudantes[indice_menor]
print(f"Menor média: {nomes[indice_menor]} - {menor_media:.2f}")

print("\n" + "-" * 70)
print("\n4. RESUMO ESTATÍSTICO\n")

total_aprovados = sum(1 for m in medias_estudantes if m >= 7.0)
total_recuperacao = sum(1 for m in medias_estudantes if 5.0 <= m < 7.0)
total_reprovados = sum(1 for m in medias_estudantes if m < 5.0)

print(f"Aprovados: {total_aprovados}")
print(f"Em Recuperação: {total_recuperacao}")
print(f"Reprovados: {total_reprovados}")

print("\n" + "=" * 70)
print("✓ Sistema de boletim concluído com sucesso!")
print("=" * 70)
