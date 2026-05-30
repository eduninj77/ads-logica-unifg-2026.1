# (a) problemas com .sort()

# Código com erro
lista = [3, 1, 2]
resultado = lista.sort()
print(resultado)  #None
# Imprime None porque o método .sort ordena a lista no lugar (modifica a original) e não retorna nada.

# Correção - opcção 1: ordenar e usar a lista original
lista = [3, 1, 2]
lista.sort()
print(lista)

# Correção - opcção 2: usar sorted() que SIM retorna uma nova lista
lista = [3, 1, 2]
resultado = sorted(lista)
print(resultado)

# (b) problemas com índice inexistente

# Código com erro
nomes = ["Ana", "Bruno"]
print(nomes[5])   #IndexError: list index out of range
# Aconte o erro porque a lista tem apenas 2 elementos (índice 0 e 1). Tentar acessar o índice 5 ultrapassa os limites da lista, causando um IndexError.

# Correção - verificar se o índice existe antes de acessar
nomes = ["Ana", "Bruno"]
indice = 5

if indice < len(nomes):
    print(nomes[indice])
else:
    print(f"Índice {indice} não existe. A lista tem {len(nomes)} elementos.")

# Correção - versão com try/except
try:
    print(nomes[5])
except IndexError:
    print("Erro: índice fora do intervalo da lista.")

# ---- Desafio Terceiro exemplo de erro ----

# Código com erro
idade = 20
print("Minha idade é " + idade)  #TypeError: can only concatenate str to str
# Acontece o erro porque o operador + não mistura tipos diferentes. "texto" é string e 20 é int e o Python não converte automaticamente

# Correção - opcção 1: converter com str()
print("Minha idade é" + str(idade))