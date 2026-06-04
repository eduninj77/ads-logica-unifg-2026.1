def dividir(a, b):
    if b == 0:
        print("Erro: não é possível dividir por zero.")
        return None
    return a / b

resultado = dividir(10, 0)
if resultado is not None:
    print(resultado)