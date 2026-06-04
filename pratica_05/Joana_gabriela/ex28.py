#1. Qual é o problema com soma?soma = 0 está fora do loop externo — ela nunca é reiniciada entre uma linha e outra, acumulando as notas de todas as linhas anteriores no cálculo de cada média:Linha 0: soma = 0 + 8 + 7 + 9 = 24  →  média = 24/3 = 8.0   ✅ (coincide)
#Linha 1: soma = 24 + 5 + 6 + 5 = 40 →  média = 40/3 = 13.3  💥 (errado!)
#Linha 2: soma = 40 + 9 + 10 + 8 = 67 → média = 67/3 = 22.3  💥 (errado!)

pythonnotas = [
    [8, 7, 9],
    [5, 6, 5],
    [9, 10, 8]
]

#2. Código corrigido:
for i in range(len(notas)):
    soma = 0                          # ← reinicia a cada nova linha
    for j in range(len(notas[i])):
        soma += notas[i][j]
    media = soma / len(notas[i])
    print(f"Linha {i} - Média: {media:.2f}")

#3. Por que a correção funciona? Movendo soma = 0 para dentro do loop externo, ela é zerada antes de cada linha — garantindo que cada média seja calculada só com as notas daquele aluno:
#Linha 0: soma = 0 → 0+8+7+9 = 24  → 24/3 = 8.00  ✅
#Linha 1: soma = 0 → 0+5+6+5 = 16  → 16/3 = 5.33  ✅
#Linha 2: soma = 0 → 0+9+10+8 = 27 → 27/3 = 9.00  ✅