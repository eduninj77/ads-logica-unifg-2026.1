#  ERRADO — não verifica o valor de b antes de dividir
def dividir(a, b):
    return a / b          #  ZeroDivisionError quando b = 0

#  CORRETO — valida antes de operar
def dividir(a, b):
    if b == 0:            #  verifica o problema antes
        return "Erro: não é possível dividir por zero."
    return a / b          #  só divide se b for válido