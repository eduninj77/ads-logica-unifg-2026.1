import os
os.system("clear" if os.name != "nt" else "cls")

def somar(a, b):
    soma = a + b
    return soma

print(somar(2, 3))
print(somar(0, 3))
print(somar(-1, -3))