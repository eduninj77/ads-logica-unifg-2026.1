# Problema: o loop deveria contar de 10 até 1, mas não atualizava o contador corretamente.
# Isso cria um loop infinito porque a variável de controle nunca diminui,
# então a condição do while permanece verdadeira para sempre.

contador = 10

while contador >= 1:
    print(contador)
    contador -= 1
