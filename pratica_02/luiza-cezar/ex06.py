nota = float(input("Digite uma nota de 0 a 10: "))

while nota < 0 or nota > 10:
    print("Valor inválido. A nota precisa estar entre 0 e 10.")
    nota = float(input("Digite uma nota de 0 a 10: "))

print(f"Nota válida: {nota}")
