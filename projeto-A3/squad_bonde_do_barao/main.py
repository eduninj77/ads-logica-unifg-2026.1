from banco_poo import Empresa, DemonstracaoAnual
from motor_indices import calcular_indices
from painel_evolutivo import analise_horizontal

print("-=-=-=- ANALISADOR FINANCEIRO -=-=-=-")

nome_empresa = input("Digite o nome da empresa: ")

empresa = Empresa(nome_empresa)

for ano in [2023, 2024, 2025]:

    print(f"\n===== CADASTRO {ano} =====")

    while True:

        try:
            ativo_circulante = float(
                input("Ativo circulante: ")
            )

            ativo_nao_circulante = float(
                input("Ativo não circulante: ")
            )

            passivo_circulante = float(
                input("Passivo circulante: ")
            )

            passivo_nao_circulante = float(
                input("Passivo não circulante: ")
            )

            patrimonio_liquido = float(
                input("Patrimônio líquido: ")
            )

            receita = float(
                input("Receita: ")
            )

            estoque = float(
                input("Estoque: ")
            )

            lucro = float(
                input("Lucro: ")
            )

        except ValueError:
            print("Digite apenas números!")
            continue

        ativo_total = (
            ativo_circulante +
            ativo_nao_circulante
        )

        passivo_total = (
            passivo_circulante +
            passivo_nao_circulante
        )

        if ativo_total != (
            passivo_total +
            patrimonio_liquido
        ):
            print(
                "\nERRO: "
                "Ativo Total deve ser igual "
                "a Passivo Total + Patrimônio Líquido."
            )
            continue

        demonstracao = DemonstracaoAnual(
            ano,
            ativo_circulante,
            ativo_nao_circulante,
            passivo_circulante,
            passivo_nao_circulante,
            patrimonio_liquido,
            receita,
            estoque,
            lucro
        )

        empresa.adicionar_demonstracao(
            demonstracao
        )

        break

print(
    f"\n===== RELATÓRIO: "
    f"{empresa.nome.upper()} ====="
)

for demonstracao in empresa.historico:

    indices = calcular_indices(demonstracao)

    print(
        f"\nAno: {demonstracao.ano}"
    )

    print(
        f"Liquidez Corrente: "
        f"{indices['liquidez_corrente']:.2f}"
    )

    print(
        f"Liquidez Seca: "
        f"{indices['liquidez_seca']:.2f}"
    )

    print(
        f"Endividamento: "
        f"{indices['endividamento'] * 100:.2f}%"
    )

    print(
        f"Margem Líquida: "
        f"{indices['margem_liquida'] * 100:.2f}%"
    )

    print(
        f"ROE: "
        f"{indices['roe'] * 100:.2f}%"
    )

analise_horizontal(empresa)