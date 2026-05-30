nome_completo = "Maria Clara Souza"

partes = nome_completo.split()
print("Lista de partes:", partes)

nome_hifenizado = "-".join(partes)
print("Com hífen:", nome_hifenizado)

primeiro = partes[0]
ultimo = partes[-1]
print("Primeiro e último:", primeiro, ultimo)