import random

def notas():
    nota = random.randint(1,10)
    print(nota)
    return nota

def calcular(media):
    if media > 6:
        print('Aprovado!')
    else:
        print('Reprovado!')

nota87= notas()

media = calcular(nota87)
