import os
os.system("clear" if os.name != "nt" else "cls")

#1. A variável x
#2. A variável y
#3. O pyhton não irá reconhecer y como variável existente no "código principal", ocasionando em um NameError
#4. Exemplo



def teste():
    global y
    y = 8
    x = 10
    return y/x

print(teste())