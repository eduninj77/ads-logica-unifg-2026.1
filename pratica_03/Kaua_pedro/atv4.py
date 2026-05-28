
def n_total (n1, n2):
    return (n1+n2)/2



def verificar_situacao(media):
    if media >=7:
        return "aprovado"
    else:
        return "reprovado"

n1 = float(input("escreva sua nota 1 :"))
n2 = float(input("escreva sua nota 2 :"))    

media_final= n_total(n1,n2)

situacao = verificar_situacao(media_final)

print(f"media:{media_final:.1f} -situação: {situacao}")
    