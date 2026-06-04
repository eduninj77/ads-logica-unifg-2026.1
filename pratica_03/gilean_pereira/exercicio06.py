x= 10

def teste():
    y = 5
    return x + y

print(teste())


# variavel global é o x e a local é a y
# se usar a variavel y fora vai dar erro

a = 20 


def calcular():
    b = 30
    return a - b


print(calcular())