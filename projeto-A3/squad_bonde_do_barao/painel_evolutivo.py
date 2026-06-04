def analise_horizontal(empresa):

    print("\n===== ANÁLISE HORIZONTAL =====")

    historico = empresa.historico

    for i in range(1, len(historico)):
        ano_anterior = historico[i - 1]
        ano_atual = historico[i]

        if ano_anterior.lucro == 0:
            print(
                f"{ano_anterior.ano} -> "
                f"{ano_atual.ano}: "
                f"não é possível calcular"
            )
            continue

        variacao = (
            (ano_atual.lucro / ano_anterior.lucro) - 1
        ) * 100

        if variacao > 0:
            status = "[CRESCIMENTO]"
        elif variacao < 0:
            status = "[QUEDA]"
        else:
            status = "[ESTÁVEL]"

        print(
            f"{ano_anterior.ano} -> "
            f"{ano_atual.ano} "
            f"{status} "
            f"{variacao:.2f}%"
        )