def dividir(numerador, divisor):
    if divisor != 0:
        return numerador / divisor
    return 0


def calcular_indices(dados):
    ativo_total = (
        dados.ativo_circulante +
        dados.ativo_nao_circulante
    )

    passivo_total = (
        dados.passivo_circulante +
        dados.passivo_nao_circulante
    )

    liquidez_corrente = dividir(
        dados.ativo_circulante,
        dados.passivo_circulante
    )

    liquidez_seca = dividir(
        dados.ativo_circulante - dados.estoque,
        dados.passivo_circulante
    )

    endividamento = dividir(
        passivo_total,
        ativo_total
    )

    margem_liquida = dividir(
        dados.lucro,
        dados.receita
    )

    roe = dividir(
        dados.lucro,
        dados.patrimonio_liquido
    )

    return {
        "ativo_total": ativo_total,
        "passivo_total": passivo_total,
        "liquidez_corrente": liquidez_corrente,
        "liquidez_seca": liquidez_seca,
        "endividamento": endividamento,
        "margem_liquida": margem_liquida,
        "roe": roe
    }