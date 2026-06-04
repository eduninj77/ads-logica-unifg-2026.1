palavra = "algoritmo"
notas = [7.0, 8.5, 6.0, 9.0, 7.5]

print("Primeira letra:", palavra[0])
print("Quarta letra:", palavra[3])
print("Primeira nota:", notas[0])
print("Última nota::", notas[-1])

# ─── Desafio: por que o primeiro índice é 0? ───
# Em Python (e na maioria das linguagens), a indexação
# começa em 0 porque o índice representa a DISTÂNCIA
# até o primeiro elemento.
# O primeiro item está a 0 posições do início → índice 0
# O segundo item está a 1 posição do início  → índice 1
# E assim por diante.