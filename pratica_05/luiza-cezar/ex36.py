# Exercício 36 - Questão objetiva ENADE

print("=" * 70)
print("EXERCÍCIO 36 - QUESTÃO OBJETIVA ENADE")
print("=" * 70)

print("\nQuestão:")
print("-" * 70)
print("""
Ao usar laços aninhados para percorrer uma matriz regular, é correto 
afirmar que:
""")

print("Opções:")
print("""
A) O laço interno normalmente percorre as linhas, e o externo 
   percorre as colunas.

B) Não é possível usar for em matrizes.

C) O laço externo pode percorrer as linhas, enquanto o laço interno 
   percorre os elementos de cada linha.

D) Matrizes só podem armazenar números inteiros.

E) O acesso matriz[i][j] sempre retorna uma linha inteira.
""")

print("-" * 70)
print("RESPOSTA CORRETA: C\n")

print("Explicação:")
print("-" * 70)
print("""
• A) INCORRETA
    É o inverso! O laço EXTERNO percorre as linhas, 
    o laço INTERNO percorre os elementos de cada linha.

• B) INCORRETA
    É totalmente possível usar for em matrizes. Exemplo:
    for linha in matriz:
        for elemento in linha:
            ...

• C) CORRETA
    Laço externo: for i in range(len(matriz))  # percorre linhas
    Laço interno: for j in range(len(matriz[i]))  # percorre colunas
    
    Ou:
    Laço externo: for linha in matriz  # cada linha
    Laço interno: for elemento in linha  # cada elemento

• D) INCORRETA
    Matrizes podem armazenar qualquer tipo de dado 
    (inteiros, floats, strings, etc.)

• E) INCORRETA
    matriz[i][j] retorna um ELEMENTO específico, 
    não uma linha inteira. matriz[i] retornaria a linha.
""")

# Verificação prática
print("Exemplo prático:\n")

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("for i in range(len(matriz)):           # Laço externo (linhas)")
print("    for j in range(len(matriz[i])):   # Laço interno (colunas)")
print("        print(matriz[i][j])")
print("\nSaída:")

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j], end=" ")
print()

print("\n" + "=" * 70)
