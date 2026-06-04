n1 = 8
n2 = 6
media = (n1 + n2) / 2

if media >= 7:
    print("Aprovado")
else:
    print("Reprovado")
    
nota1=float(input("digite sua primeria nota:"))
nota2=float(input("digite sua primeria nota:"))

def calculo_media(n1,n2):
 media = (n1 + n2) / 2
 return media

def calculo_situacao(media):
 if (media >= 7):
  return "aprovado"
 else:
  return "reprovado"
  
    
media_final = calculo_media (nota1,nota2)
situacao = calculo_situacao(media_final)

print (f"sua media é {media_final} e sua situação é {situacao}")