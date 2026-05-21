while True:
 def calcular_media(n1, n2):
    return (n1 + n2) / 2

 num = int(input("Digite seu primeiro valor: "))
 num1 = int(input("Digite seu segundo valor: "))

 if num > 10:
    print("Error!")
    break
 elif num1 > 10:
    print("Error!")
    break
 elif num < 0:
    print("Error!")
    break
 elif num1 < 0:
    print("Error!")
    break
 else:
    print("------")

 final = calcular_media(num,num1)
 print(final)
 break