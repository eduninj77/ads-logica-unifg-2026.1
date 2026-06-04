##def dividir(a, b):
##  return a / b

##print(dividir(10, 0))


"""
Explique que erro acontece: O programa gera o erro ZeroDivisionError: division by zero.
Diga por que ele ocorre: Porque quando o código tentar realizar uma conta matematicamente
impossível os computadores não conseguem fazer uma divisão por zero.
Reescreva o programa para evitar esse problema: programa reescrito abaixo!
"""

def dividir(a, b):
    if b == 0:
        return "Não é possível dividir por 0!"
    return a / b


print(dividir(10, 0))
print(dividir(10, 2))

