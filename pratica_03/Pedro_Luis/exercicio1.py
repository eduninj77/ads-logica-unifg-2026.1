import os
os.system("clear" if os.name != "nt" else "cls")

def saudação(palavra):
    return f"Bem-vindo(a), {palavra}!"

print(saudação("Pedro"))