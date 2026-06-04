def ler_notas():

  n1=float(input("Digite a primeira nota:"))
  n2=float(input("Digite a segunda nota:"))

  return n1,n2

def calcular_media(n1, n2):
    media = (n1+n2)/2
    return media

def verificar_situacao(media):
    if (media >=7):
        return "aprovado"
    else:
        return "reprovado"
    
def exibir_resultado(nome, media, situacao):
    print ("===Boletim===")
    print (f"aluno: {nome}")
    print (f"sua media : {media:.1f}")
    print (f"voce foi {situacao}")


nome_aluno = input("Digite o nome do aluno: ")
nota1,nota2 = ler_notas()
media_final = calcular_media(nota1, nota2)
situacao_final = verificar_situacao(media_final)

exibir_resultado(nome_aluno, media_final, situacao_final)