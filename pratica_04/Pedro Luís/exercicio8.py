import os
os.system("clear" if os.name != "nt" else "cls")

itens = ["mouse", "teclado", "mouse", "monitor", "mouse", "teclado"]

print(f"Existem {itens.count("mouse")} mouses nessa lista de itens")
print(f"Existem {itens.count("teclado")} teclados nesssa lista de itens")
print(f"Existe {itens.count("monitor")} monitor nessa lista de itens")