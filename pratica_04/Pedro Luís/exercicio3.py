import os
os.system("clear" if os.name != "nt" else "cls")

palavra = "algoritmo"
notas = [7.0, 8.5, 6.0, 9.0, 7.5]

print(palavra[0])
print(palavra[3])
print(notas[0])
print(notas[-1])

##EXEMPLO TEÓRICO/PRÁTICO
#O primeiro índice para o computador sempre é zero,
#pois para ele é como se cada índice fosse a quantidade de passos que o computador deve dar para chegar em tal parte da string/"variável" dentro da lista,
#e ele começa do zero porque é como se ele precisasse de 0 passos para chegar naquela parte espécifica.