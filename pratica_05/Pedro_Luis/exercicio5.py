import os
os.system("clear" if os.name != "nt" else "cls")

notas = [
    [8.0, 7.5, 9.0],
    [5.0, 6.0, 5.5],
    [9.0, 8.5, 10.0],
    [6.5, 7.0, 6.0]
]


notas[1][0] = 6.5
notas[-1][-1] = 7.0
print(notas)
#A primeira posição mudada foi notas[1][0](segundo aluno), que a primeira nota de 5.0 foi para 6.5
#Já a segunda posição foi a notas[-1][-1](quarto aluno), que a terceira nota de 6.0 foi para 7.0