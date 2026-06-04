# Exercício 35 - Questão objetiva ENADE

print("=" * 70)
print("EXERCÍCIO 35 - QUESTÃO OBJETIVA ENADE")
print("=" * 70)

print("\nQuestão:")
print("-" * 70)
print("""
Considere a matriz:

sala = [
    ["L", "O"],
    ["O", "L"]
]

Qual trecho conta corretamente os assentos livres?
""")

print("Opções:")
print("""
A) livres = sala.count("L")

B) livres = 0
   for linha in sala:
       for assento in linha:
           if assento == "L":
               livres += 1

C) livres = len(sala)

D) livres = 0
   for assento in sala:
       if assento == "L":
           livres += 1

E) livres = sala["L"]
""")

print("-" * 70)
print("RESPOSTA CORRETA: B\n")

print("Explicação:")
print("-" * 70)
print("""
• A) sala.count("L") - método count() não funciona em lista de listas
    Ele só contaria se a lista fosse 1D como ["L", "O", "L", "O"]

• B) Laços aninhados - CORRETO
    Percorre todas as linhas e depois todos os assentos de cada linha
    Verifica se é "L" e incrementa o contador

• C) len(sala) - retorna 2 (número de linhas), não de assentos livres

• D) sala não contém strings diretamente, contém listas
    O loop iteraria sobre as sublistas, não os elementos

• E) sala["L"] - não pode usar string como índice em lista
    Isso gera erro de tipo
""")

# Verificação prática
print("Verificação prática:\n")

sala = [
    ["L", "O"],
    ["O", "L"]
]

print("Método CORRETO (Opção B):")
livres = 0
for linha in sala:
    for assento in linha:
        if assento == "L":
            livres += 1

print(f"Assentos livres: {livres}")

print("\n" + "=" * 70)
