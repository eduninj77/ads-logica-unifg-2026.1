total_percentual = 0.0
quantidade_alunos = 0

while True:
    nome = input("Digite o nome do estudante: ").strip()
    if not nome:
        print("Nome inválido. Tente novamente.")
        continue

    while True:
        try:
            acertos = int(input("Digite a quantidade de acertos (0 a 20): "))
            if 0 <= acertos <= 20:
                break
            print("Valor fora do intervalo. Informe um número entre 0 e 20.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro entre 0 e 20.")

    percentual = acertos / 20 * 100
    total_percentual += percentual
    quantidade_alunos += 1

    if percentual >= 90:
        classificacao = "Excelente"
    elif percentual >= 75:
        classificacao = "Satisfatório"
    elif percentual >= 50:
        classificacao = "Em atenção"
    else:
        classificacao = "Crítico"

    print(f"Aluno: {nome}")
    print(f"Acertos: {acertos}/20")
    print(f"Percentual de acertos: {percentual:.1f}%")
    print(f"Classificação: {classificacao}\n")

    continuar = input("Deseja cadastrar outro estudante? (s/n): ").strip().lower()
    if continuar != "s":
        break

if quantidade_alunos > 0:
    media_turma = total_percentual / quantidade_alunos
    print(f"Média percentual da turma: {media_turma:.1f}%")
else:
    print("Nenhum estudante cadastrado.")
