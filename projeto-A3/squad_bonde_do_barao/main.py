print("-=-=-=- ANALISADOR FINANCEIRO -=-=-=-")

def dividir(numerador, divisor):
    if divisor != 0:
        return numerador / divisor
    return 0

while True:
    try:
        nome_empresa = input("Digite o nome da empresa: ").strip()
        
        ativo_circulante = float(input("Digite o ativo circulante: "))
        ativo_nao_circulante = float(input("Digite o ativo não circulante: "))
        passivo_circulante = float(input("Digite o passivo circulante: "))
        passivo_nao_circulante = float(input("Digite o passivo não circulante: "))
        patrimonio_liquido = float(input("Digite o patrimonio liquido: "))
        receita = float(input("Digite a receita: "))
        estoque = float(input("Digite o estoque: "))
        lucro = float(input("Digite o lucro: "))

    except ValueError:
        print("Digite apenas números!")
        continue

    ativo_total = ativo_circulante + ativo_nao_circulante
    passivo_total = passivo_circulante + passivo_nao_circulante

    if ativo_total != (passivo_total + patrimonio_liquido):
        print("\nA soma do passivo total e do patrimonio liquido deve ser igual ao ativo total!")
        continue

    liquidez_corrente = dividir(ativo_circulante, passivo_circulante)
    liquidez_seca = dividir((ativo_circulante - estoque), passivo_circulante)
    endividamento = dividir(passivo_total, ativo_total)
    margem_liquida = dividir(lucro, receita)
    roe = dividir(lucro, patrimonio_liquido)

    print(f"\n-=-=-=- RELATÓRIO FINANCEIRO: {nome_empresa.upper()} -=-=-=-\n")

    print(f"Liquidez corrente: {liquidez_corrente:.2f} (R$ {ativo_circulante:.2f} / R$ {passivo_circulante:.2f})")
    if liquidez_corrente > 1:
        print("✅ BOM — consegue pagar dívidas de curto prazo")
    elif liquidez_corrente == 1:
        print("⚠️ ALERTA — no limite")
    else:
        print("❌ PERIGO — risco de não pagar dívidas")

    print(f"\nLiquidez seca: {liquidez_seca:.2f} (sem estoques)")
    if liquidez_seca > 1:
        print("✅ Muito boa")
    elif liquidez_seca == 1:
        print("⚠️ No limite")
    else:
        print("❌ Baixa — depende de vender estoque")

    print(f"\nEndividamento: {endividamento:.2f} ({endividamento*100:.2f}%)")
    if endividamento < 0.5:
        print("✅ Saudável")
    elif endividamento <= 0.8:
        print("⚠️ Atenção")
    else:
        print("❌ Alto risco — muita dívida")

    print(f"\nMargem líquida: {margem_liquida*100:.2f}%")
    if margem_liquida > 0:
        print("✅ Empresa lucrando")
    elif margem_liquida == 0:
        print("⚠️ Empate")
    else:
        print("❌ Prejuízo")

    print(f"\nROE: {roe*100:.2f}%")
    if roe > 0.20:
        print("🏆 Excelente retorno")
    elif roe > 0.10:
        print("✅ Bom retorno")
    elif roe > 0:
        print("⚠️ Retorno baixo")
    else:
        print("❌ Prejuízo")

    print("\n-=-=-=- RESUMO -=-=-=-")
    print(f"Ativos totais: R$ {ativo_total:.2f}")
    print(f"Dívidas totais: R$ {passivo_total:.2f}")

    if liquidez_corrente > 1 and margem_liquida > 0 and endividamento < 0.5:
        print("🏆 Empresa saudável e equilibrada")
    elif lucro < 0:
        print("⚠️ Empresa operando no prejuízo")
    else:
        print("⚠️ Empresa mediana / precisa de atenção")

    opcao = input("\nDeseja analisar outra empresa? (s/n): ").lower()
    if opcao != "s":
        print("Encerrando programa...")
        break