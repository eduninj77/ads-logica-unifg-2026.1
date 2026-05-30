def dividir(a, b):
    if b == 0:
        return "Erro: não é possível dividir por zero."
    return a / b

print(dividir(10, 0))   # Erro: não é possível dividir por zero.
print(dividir(10, 2))   