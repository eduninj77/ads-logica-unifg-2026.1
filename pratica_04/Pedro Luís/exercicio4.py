import os
os.system("clear" if os.name != "nt" else "cls")

palavra = "programacao"
valores = [10, 20, 30, 40, 50, 60]

print(palavra[:4])
print(palavra[3:8])
print(valores[:3])
print(valores[1:])

#Se você quer pegar o último índice, é apenas você digitar -1