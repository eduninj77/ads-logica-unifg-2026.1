contador = 0  # variável global

def incrementar():
    passo = 1  # variável local
    return contador + passo

print(incrementar())  # 1
# print(passo)  # NameError: passo não existe aqui