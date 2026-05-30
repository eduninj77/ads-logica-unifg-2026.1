# ====================================================
#  SISTEMA DE BOLETIM ESCOLAR
#=====================================================

nomes = ["Pedro", "Daniel", "Luckiã", "Alexandre"]

notas = [
    [7.0, 8.5, 9.0],  # Pedro
    [5.5, 6.0, 7.0],  # Daniel
    [9.0, 9.5, 10.0], # Luckiã
    [6.0, 7.5, 8.0]   # Alexandre
]

# Calculo das médias
medias = []
for i in range(len(nomes)):
    soma = 0
    for nota in notas[i]:
        soma += nota
    media = soma / len(notas[i])
    medias.append(media)

# Situação de cada estudante
def situacao(media):
    if media >= 7.0:
        return "Aprovado"
    elif media >= 5.0:
        return "Recuperação"
    else:
        return "Reprovado"
    
# --- Maior e menor média ---
maior_media = medias[0]
menor_media = medias[0]
aluno_maior = nomes[0]
aluno_menor = nomes[0]

for i in range(len(medias)):
    if medias[i] > maior_media:
        maior_media = medias[i]
        aluno_maior = nomes[i]
    if medias[i] < menor_media:
        menor_media = medias[i]
        aluno_menor = nomes[i]

# =====================================================
# RELATÓRIO FINAL
# =====================================================

print("=====================================================")
print("                            BOLETIM ESCOLAR")
print("=====================================================")
print(f"{'Aluno':<15} {'Média':<10} {'Situação':<15}")
print("------------------------------------------------------")

for i in range(len(nomes)):
    n = notas[i]
    print(f"{nomes[i]:<15} {medias[i]:<10.2f} {situacao(medias[i]):<15}")



print("======================================================")
print(f"🏆 Maior média: {aluno_maior} com {maior_media:.2f}")
print(f"Menor média: {aluno_menor} com {menor_media:.2f}")