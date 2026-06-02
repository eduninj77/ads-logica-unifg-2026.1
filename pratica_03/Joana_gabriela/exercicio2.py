def somar(a, b):
    return a + b

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

if b < 0:
    print(f"{a} - {abs(b)} = {somar(a, b)}")
else:
    print(f"{a} + {b} = {somar(a, b)}")