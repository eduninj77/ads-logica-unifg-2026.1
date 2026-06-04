 Erro a) --
lista.sort() ordena no lugar e retorna None.
Não se deve atribuir o resultado a uma variável.

lista = [3, 1, 2]
lista.sort()
print(lista)

 Erro b) --
nomes tem índices 0 e 1 apenas.
nomes[5] causa IndexError.

nomes = ["Ana", "Bruno"]
if 5 < len(nomes):
    print(nomes[5])
else:
    print("Índice fora do intervalo.")

Desafio: erro c)
texto = "Python"
print(texto[10])  → IndexError: string index out of range
Correção: verificar len(texto) antes de acessar.