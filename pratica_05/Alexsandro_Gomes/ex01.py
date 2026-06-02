matriz = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

for linha in matriz:
    for numero in linha:
        print(f"Valor: {numero}")

#1- A matriz tem 3 linhas
#2- tem 3 colunas cada linha
#3- 30
#4- 80
#5- 50 porque o primeiro colchete sempre escolhe a linha e o segundo a coluna. Como no Python tudo começa no zero, o índice [1] vai direto na segunda linha (que é [40, 50, 60]). o outro [1] entra nessa linha e pega o segundo número, que é o 50.