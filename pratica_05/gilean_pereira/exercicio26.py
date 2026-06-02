#dados = [
#    [1, 2, 3],
#    [4, 5],
#    [6, 7, 8]
#]

 #for i in range(len(dados)):
 #   for j in range(3):
  #      print(dados[i][j])

# O erro IndexError: list index out of range.

# Porque o segundo laço tenta ler fixamente 3 elementos (range(3)) em todas as linhas. 
# Porém, a segunda linha (dados[1]) é irregular e só possui 2 elementos (índices 0 e 1). 
# Quando o código tenta acessar o índice 2 nessa linha, o programa quebra.

dados = [
    [1, 2, 3],
    [4, 5],
    [6, 7, 8]
]

for i in range(len(dados)):

    for j in range(len(dados[i])):
        print(dados[i][j])