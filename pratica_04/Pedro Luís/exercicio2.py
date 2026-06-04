import os
os.system("clear" if os.name != "nt" else "cls")

nome_completo = "Maria Clara Souza"

nome_lista = nome_completo.split()

print(nome_lista)

nome_completof = "-".join(nome_lista)
print(nome_completof)
print(f"O primeiro nome é {nome_completof[:5]}, e o último é {nome_completof[12:]}")