import os
os.system("clear" if os.name != "nt" else "cls")

vendas = [
    [20, 25, 18, 30],
    [15, 22, 20, 19],
    [30, 28, 35, 40]
]

total_p = []
total_s = [0, 0, 0, 0]
for i in vendas:
    total_p.append(sum(i))

for i in range(len(vendas)):
    for c in range(len(vendas[i])):
        if vendas[i][c] == vendas[i][0]:
            total_s[c] += vendas[i][c]
        if vendas[i][c] == vendas[i][1]:
            total_s[c] += vendas[i][c]
        if vendas[i][c] == vendas[i][2]:
            total_s[c] += vendas[i][c]
        if vendas[i][c] == vendas[i][3]:
            total_s[c] += vendas[i][c]

print(f"O total vendido por produto foi: {total_p}")
print(f"O total vendido por semana foi: {total_s}")
print(f"O produto com o maior total vendido foi o produto {total_p.index(max(total_p)) + 1}")
print(f"A semana com o maior total vendido foi a semana {total_s.index(max(total_s)) + 1}")
