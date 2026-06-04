quantidade = int(input("Digite a quantidade de alunos da turma: "))

aprovados = 0
recuperacao = 0
reprovados = 0

for i in range(quantidade):
    media = float(input(f"Digite a média do aluno {i + 1}: "))
    if media >= 7.0:
        aprovados += 1
    elif media >= 4.0:
        recuperacao += 1
    else:
        reprovados += 1

print(f"Alunos aprovados: {aprovados}")
print(f"Alunos em recuperação: {recuperacao}")
print(f"Alunos reprovados: {reprovados}")
