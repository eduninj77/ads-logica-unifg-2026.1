import os
os.system("clear" if os.name != "nt" else "cls")

def dividir(a, b):
    if b == 0 or a == 0:
        return "Não é possível dividir por zero"
    return a / b

print(dividir(10, 0))#O erro ocorre aqui, não é possível dividir um número por zero e o python acaba ocasionando uma excessão/erro de ZeroDivisionError, quando você tenta dividir algo por zero

