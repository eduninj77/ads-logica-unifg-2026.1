def calcular_total(preco, quantidade):
    subtotal = preco * quantidade
    desconto = subtotal * 0.1
    total = subtotal - desconto
    return total

calcular_total(50, 2)


#                                  preco,            quantidade,         subtotal,       desconto,      total (Retorno)
#Entrada (Parâmetros),               50,                  2,                 -,              -,                -
#subtotal = preco * quantidade,      50,                  2,                100,             -,                -
#desconto = subtotal * 0.1           50,                  2,                100,            10.0,              -
#total = subtotal - desconto,        50,                  2,                100,            10.0,            90.0


#Caso normal
print (calcular_total(10, 5))
print (calcular_total(100, 1))

#Caso Limítrofe
print (calcular_total(0, 5))

#Caso extremo
print (calcular_total(1000000, 1000))
