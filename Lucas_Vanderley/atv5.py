import random

def ler_notas():
  nota = random.randint(1,10)
  nota1 = random.randint(1,10)
  return nota,nota1
  
def calcular_media(n1, n2):
  return (n1 + n2) / 2
  

def verificar_situacao(media):
  if media < 7:
    return "Reprovado!"
  else:
    return "Aprovado!"
    

def exibir_resultado(nome, n1, n2, media, situacao):
    print("\n" + "="*30)
    print(f"RELATÓRIO DO ALUNO: {nome}")
    print("="*30)
    print(f"Nota 1:  {n1}")
    print(f"Nota 2:  {n2}")
    print(f"Média:   {media}")
    print(f"Situação: {situacao}")
    print("="*30)

nota_a, nota_b = ler_notas()

media = calcular_media(nota_a, nota_b)

verificar = verificar_situacao(media)

exibir_resultado("Lucas Vanderley", nota_a, nota_b, media, verificar)

