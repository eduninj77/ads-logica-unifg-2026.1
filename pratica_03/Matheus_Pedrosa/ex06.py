x = 10

def teste():
    y = 5
    return x + y

print(teste())

# X é global porque está declarada fora da função e Y é 
# local pois só existe dentro da função e se tentar usar o Y fora da 
# função não funciona